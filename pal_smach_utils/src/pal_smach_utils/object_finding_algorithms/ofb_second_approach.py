#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from smach import StateMachine, Concurrence, CBState
from geometry_msgs.msg import Pose, Quaternion
from tf.transformations import quaternion_from_euler
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.object_finding_algorithms.detect_tables_of_zone_sm import DetectTablesOfZoneSM
from pal_smach_utils.speech.sound_action import SpeakActionFromPoolStateMachine
from pal_smach_utils.object_finding_algorithms.tell_move_and_recognize_sm import TellGoRecognizeSM
from pal_smach_utils.object_finding_algorithms.object_check_states import CheckObjectAndRemoveFromList, CheckRemaining
from pal_smach_utils.object_finding_algorithms.tsp_smach_state import TSPState
from pal_smach_utils.object_finding_algorithms.calc_sensing_locations_sm import CalculateSensingLocations

DIST_TO_TABLE = 0.3
DIST_BETWEEN_TABLES = 1.0  # Distance bewtween two table detections to considerate it two different tables
HC = True  # If True, Hill Climbing is used


class OFBSecondApproach(smach.StateMachine):
    '''
    Object finding state machine.
    Parameters:
        - target_object_key: string indicating the name of the input_key that has the name of the object you want to find
        - target_frame: the frame in what you want the output object's location.
    Keys:
        - in_room_name: Name of the room where the robot is and has to search objects.
        - out_object_found: Information about the found object
        - out_location_inside_room_name: name of the location where the object was found. I.E. the table.
    Notes:
        - If there are objects remaining in a location, it will go to that location again, rather than searching for objects
        in another room.
    '''

    def __init__(self, target_object_key=None, target_frame='/map'):
        input_keys = ['in_room_name']
        if target_object_key is not None:
            input_keys.append(target_object_key)

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                                    input_keys=input_keys,
                                    output_keys=['out_object_found', 'out_location_inside_room_name'])

        if target_object_key is None:
            target_object_key = 'in_target_object'
            self.userdata.in_target_object = ''  # No target object set! Before set to str(None), changed for SearchObjectWCSM
            going_to_pool = ["I'm going to look for objects.", "Maybe I find objects there. I'll have a look.",
                             "I think I know where objects can be."]
            object_not_found_pool = ["I can't see any object here.", "It seems that there aren't objects here.",
                                     "I haven't found any object here."]
        else:
            going_to_pool = ["I'm going to look if I find it.", "Maybe I find it there. I'll have a look.",
                             "I think I know where it can be.", "I think it can be there."]
            object_not_found_pool = ["I can't see it here.", "It seems that it isn't here.",
                                     "I haven't found it here."]

        object_found_pool = ["I can see the %s.", "Is that the %s? I think so!",
                             "The %s is just there.", "I found the %s.",
                             "Can't you see the %s? It's there!"]

        self.userdata.out_location_inside_room_name = 'tabletop'  # Always the same as it's not possible to know the name.
        self.userdata.objects_data = None  # To avoid errors the first time the check_if_remaining is called
        self.userdata.sensing_route = None  # Because at the very beginning there's no route
        self.userdata.tabletop_route = None  # Because at the very beginning there's no route
        self.userdata.out_object_found = None  # To avoid errors if there's an abort.

        with self:
            StateMachine.add('CHECK_IF_OBJECTS_REMAINING', CheckRemaining(),
                             remapping={'in_obj_list': 'objects_data'},
                             transitions={'empty': 'CHECK_IF_TABLE_ROUTE_EMPTY',
                                          'remaining': 'TELL_GO_RECOGNIZE'})

            @smach.cb_interface(input_keys=['in_route', 'in_table_poses', 'in_orientations'],
                                output_keys=['out_remaining_poses', 'out_remaining_orientations'],
                                outcomes=['remaining', 'empty'])
            def check_ttop_route_emptiness(userdata):
                if userdata.in_route:
                    # We get the remaining poses and orientations of the tabletop route
                    # and then we'll recalculate the route through that remaining nodes
                    remaining_poses = []
                    remaining_orientations = []
                    for index in userdata.in_route:  # Tabletop route has only the indices of the elements
                        remaining_poses.append(userdata.in_table_poses[index])
                        remaining_orientations.append(userdata.in_orientations[index])
                    userdata.out_remaining_poses = remaining_poses
                    userdata.out_remaining_orientations = remaining_orientations
                    return 'remaining'
                return 'empty'

            StateMachine.add('CHECK_IF_TABLE_ROUTE_EMPTY',
                             CBState(check_ttop_route_emptiness,
                                     input_keys=['in_route', 'in_table_poses', 'in_orientations'],
                                     output_keys=['out_remaining_poses', 'out_remaining_orientations'],
                                     outcomes=[succeeded, 'empty']),
                             remapping={'in_route': 'tabletop_route',
                                        'in_table_poses': 'tabletop_detect_poses',
                                        'in_orientations': 'tabletop_orientation_data',
                                        'out_remaining_poses': 'tabletop_detect_poses',
                                        'out_remaining_orientations': 'tabletop_orientation_data'},
                             transitions={'remaining': 'TABLETOPS_TSP_ROUTE',
                                          'empty': 'CHECK_IF_SENSING_ROUTE_EMPTY'})

            @smach.cb_interface(input_keys=['in_route'], output_keys=['out_remaining_nodes'],
                                outcomes=['remaining', 'empty'])
            def check_sensing_route_emptiness(userdata):
                if userdata.in_route:
                    # We get the remaining nodes of the route
                    # and then we'll recalculate the route through that remaining nodes
                    userdata.out_remaining_nodes = userdata.in_route  # The route itself has the nodes ordered.
                    return 'remaining'
                return 'empty'

            StateMachine.add('CHECK_IF_SENSING_ROUTE_EMPTY',
                             CBState(check_sensing_route_emptiness,
                                     input_keys=['in_route'],
                                     output_keys=['out_remaining_nodes'],
                                     outcomes=[succeeded, 'empty']),
                             remapping={'in_route': 'sensing_route',
                                        'out_remaining_nodes': 'sens_locations'},
                             transitions={'remaining': 'SENSING_LOCATIONS_TSP_ROUTE',
                                          'empty': 'CALCULATE_TTOP_SENSING_LOCATIONS'})

            StateMachine.add('CALCULATE_TTOP_SENSING_LOCATIONS', CalculateSensingLocations(),
                             remapping={'in_room_name': 'in_room_name', 'out_guards': 'sens_locations'},
                             transitions={succeeded: 'SENSING_LOCATIONS_TSP_ROUTE', 'no_corner_info': aborted})

            StateMachine.add('SENSING_LOCATIONS_TSP_ROUTE', TSPState(HC=HC),
                             remapping={'in_nodes': 'sens_locations', 'out_route': 'sensing_route'},
                             transitions={succeeded: 'GET_NEXT_SENSING_LOCATION'})

            @smach.cb_interface(input_keys=['in_sensing_route'], output_keys=['out_sensing_route', 'out_next_sensing_pose'],
                                outcomes=[succeeded, 'empty_route'])
            def get_next_loc_from_route(userdata):
                # Returns the next sensing location to go and removes it from the route
                if not userdata.in_sensing_route:  # The sensing route is empty...
                    return 'empty_route'
                next_pos = userdata.in_sensing_route[0]
                userdata.out_sensing_route = userdata.in_sensing_route[1:]
                pose = Pose()
                pose.position.x = next_pos[0]
                pose.position.y = next_pos[1]
                pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 1.57))  # FIXME is it possible to avoid a fixed orientation?
                userdata.out_next_sensing_pose = pose
                return succeeded

            StateMachine.add('GET_NEXT_SENSING_LOCATION',
                             CBState(get_next_loc_from_route,
                                     input_keys=['in_sensing_route'],
                                     output_keys=['out_sensing_route', 'out_next_sensing_pose'],
                                     outcomes=[succeeded, 'empty_route']),
                             remapping={'out_sensing_route': 'sensing_route',
                                        'in_sensing_route': 'sensing_route',
                                        'out_next_sensing_pose': 'next_sensing_pose'},
                             transitions={succeeded: 'MOVE_TO_SENSING_LOCATION',
                                          'empty_route': 'CALCULATE_TTOP_SENSING_LOCATIONS'})

            StateMachine.add('MOVE_TO_SENSING_LOCATION',
                             MoveActionState("/map", goal_key='next_sensing_pose'),
                             transitions={succeeded: 'DETECT_TABLETOPS_AND_ANNOUNCE',
                                          aborted: 'GET_NEXT_SENSING_LOCATION'})  # FIXME if aborted we get the next pose.

            tell_and_search = Concurrence(outcomes=[succeeded, aborted, preempted, 'no_tables'],
                                          default_outcome=aborted,
                                          output_keys=['tabletop_detect_poses', 'tabletop_orientation_data'],
                                          outcome_map={succeeded: {'ANNOUNCE_SEARCHING': succeeded,
                                                                   'DETECT_TABLETOPS_ZONE': succeeded},
                                                       'no_tables': {'DETECT_TABLETOPS_ZONE': 'no_tables'}})
            with tell_and_search:
                searching_tables_pool = ["I'm looking for places that can contain objects.",
                                         "I'm searching a place that can have objects.",
                                         "I'm searching the best place to find objects."]
                Concurrence.add('ANNOUNCE_SEARCHING',
                                SpeakActionFromPoolStateMachine(searching_tables_pool))

                Concurrence.add('DETECT_TABLETOPS_ZONE',
                                DetectTablesOfZoneSM(distance_treshold=DIST_BETWEEN_TABLES, dist_to_table=DIST_TO_TABLE),
                                remapping={'out_table_pose_list': 'tabletop_detect_poses',
                                           'out_table_orientation_list': 'tabletop_orientation_data'})

            StateMachine.add('DETECT_TABLETOPS_AND_ANNOUNCE', tell_and_search,
                             transitions={succeeded: 'TABLETOPS_TSP_ROUTE', 'no_tables': 'GET_NEXT_SENSING_LOCATION'},
                             remapping={'tabletop_orientation_data': 'tabletop_orientation_data',
                                        'tabletop_detect_poses': 'tabletop_detect_poses'})

            # @smach.cb_interface(input_keys=['in_tabletop_detect_data'], output_keys=['out_table_node_list'],
            #                     outcomes=[succeeded])
            # def check_ttop_data(userdata):
            #     #FIXME -> May be necessary to filter in some way the already visited tables...
            #     #tabletop_detect_data is a list of tuples (pos, orientation), so we get only the poses for the TSP
            #     userdata.out_table_node_list = reduce(lambda acc, x: acc + [x[0]], userdata.in_tabletop_detect_data, [])

            #     return succeeded

            # StateMachine.add('CHECK_TABLETOP_DATA',
            #                  CBState(check_ttop_data, input_keys=['in_tabletop_detect_data'],
            #                          output_keys=['out_object_detection_pose'],
            #                          outcomes=[succeeded]),
            #                  remapping={'in_tabletop_detect_data': 'tabletop_detect_data',
            #                             'out_table_node_list': 'table_node_list'},
            #                  transitions={succeeded: 'TELL_GO_RECOGNIZE'})

            StateMachine.add('TABLETOPS_TSP_ROUTE', TSPState(HC=HC, indices=True),
                             remapping={'in_nodes': 'tabletop_detect_poses',
                                        'out_route': 'tabletop_route'},
                             transitions={succeeded: 'GET_NEXT_TABLETOP_LOCATION'})

            @smach.cb_interface(input_keys=['in_table_route', 'in_orient_list', 'in_pose_list'],
                                output_keys=['out_table_route', 'out_object_detection_pose'],
                                outcomes=[succeeded, 'empty_route'])
            def get_next_loc_from_table_route(userdata):
                # Returns the next tabletop location to go and removes it from the route
                if not userdata.in_table_route:  # The route is empty, so we recalculate the sensing route and go again
                    return 'empty_route'

                node_index = userdata.in_table_route[0]
                print('node_index: %d, length in_table_route: %d' % (node_index, len(userdata.in_table_route)))
                next_pos = userdata.in_pose_list[node_index]

                # Only the index is removed from the list, to preserve the index order of the other elements
                userdata.out_table_route = userdata.in_table_route[1:]
                pose = Pose()
                pose.position.x = next_pos[0]
                pose.position.y = next_pos[1]
                pose.orientation = userdata.in_orient_list[node_index]
                userdata.out_object_detection_pose = pose
                return succeeded

            StateMachine.add('GET_NEXT_TABLETOP_LOCATION',
                             CBState(get_next_loc_from_table_route,
                                     input_keys=['in_table_route', 'in_orient_list', 'in_pose_list'],
                                     output_keys=['out_table_route', 'out_object_detection_pose'],
                                     outcomes=[succeeded, 'empty_route']),
                             remapping={'out_table_route': 'tabletop_route',
                                        'in_table_route': 'tabletop_route',
                                        'in_orient_list': 'tabletop_orientation_data',
                                        'in_pose_list': 'tabletop_detect_poses',
                                        'out_object_detection_pose': 'object_detection_pose'},
                             transitions={succeeded: 'TELL_GO_RECOGNIZE',
                                          'empty_route': 'SENSING_LOCATIONS_TSP_ROUTE'})

            StateMachine.add('TELL_GO_RECOGNIZE', TellGoRecognizeSM(msg_pool=going_to_pool, arg_key=None),
                             remapping={'out_objects_data': 'objects_data',
                                        'in_target_object': target_object_key,
                                        'in_location_pose_in_map': 'object_detection_pose'},
                             transitions={'move_failed': 'GET_NEXT_SENSING_LOCATION',
                                          'no_object_found': 'CHECK_IF_OBJECT_FOUND',
                                          succeeded: 'CHECK_IF_OBJECT_FOUND',
                                          aborted: aborted})  # FIXME aborted should abort everything?

            StateMachine.add('CHECK_IF_OBJECT_FOUND',
                             CheckObjectAndRemoveFromList(target_frame),
                             remapping={'out_object_found': 'out_object_found',
                                        'in_objects_data': 'objects_data',
                                        'out_objects_data': 'objects_data',
                                        'in_target_object': target_object_key},
                             transitions={succeeded: 'PREPARE_POOL_ARGS', aborted: 'TELL_NO_OBJECT_FOUND'})

            StateMachine.add('TELL_NO_OBJECT_FOUND',
                             SpeakActionFromPoolStateMachine(object_not_found_pool, arg_key=None),
                             remapping={},
                             transitions={succeeded: 'GET_NEXT_SENSING_LOCATION', aborted: 'GET_NEXT_SENSING_LOCATION'})

            @smach.cb_interface(input_keys=['in_first_object', 'in_location_name'], output_keys=['out_tell_arg'],
                                outcomes=[succeeded])
            def prepare_userdata(userdata):
                userdata.out_tell_arg = userdata.in_first_object.name
                return succeeded

            StateMachine.add('PREPARE_POOL_ARGS',
                             CBState(prepare_userdata,
                                     input_keys=['in_first_object', 'in_location_name'],
                                     output_keys=['out_tell_arg'], outcomes=[succeeded]),
                             remapping={'in_first_object': 'out_object_found',
                                        'out_tell_arg': 'tell_arg'},
                             transitions={succeeded: 'TELL_OBJECT_RECOGNIZED'})

            StateMachine.add('TELL_OBJECT_RECOGNIZED',
                             SpeakActionFromPoolStateMachine(object_found_pool, arg_key="tell_arg"),
                             remapping={'tell_arg': 'tell_arg'},
                             transitions={succeeded: succeeded, aborted: aborted})
