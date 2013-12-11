#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
import pal_smach_utils.object_finding_algorithms.ofb_utils as ofb_utils

from smach import StateMachine, Concurrence, CBState
from geometry_msgs.msg import Pose, Quaternion
from tf.transformations import quaternion_from_euler
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted, transform_pose
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.object_finding_algorithms.detect_furniture_of_zone_sm import DetectFurnitureOfZoneSM
from pal_smach_utils.speech.sound_action import SpeakActionFromPoolStateMachine
from pal_smach_utils.object_finding_algorithms.tell_move_and_recognize_sm import TellGoRecognizeSM
from pal_smach_utils.object_finding_algorithms.object_check_states import CheckObjectAndRemoveFromList, CheckRemaining
from pal_smach_utils.object_finding_algorithms.tsp_smach_state import TSPState
from pal_smach_utils.object_finding_algorithms.calc_sensing_locations_sm import CalculateSensingLocations

DIST_TO_FURNITURE = 0.3
DIST_BETWEEN_FURNITURE = 1.0  # Distance bewtween two furniture detections to considerate it two different furniture
HC = False  # If True, Hill Climbing is used
FURN_PROB_PARAM = '/mmap/furniture_probability/'  # Name of the parameter where the probabilities of each furniture are.
TSP_route = False


class OFBThirdApproach(smach.StateMachine):
    '''
    Object finding state machine.
    Parameters:
        - target_object_key: string indicating the name of the input_key that has the name of the object you want to find
        - target_frame: the frame in what you want the output object's location.
        - tsp_route: Specifies whether the route to the different located furniture should be calcualted with a TSP or with
                     the probabilities of the furniture_probabilities.yaml.
    Keys:
        - in_room_name: Name of the room where the robot is and has to search objects.
        - out_object_found: Information about the found object
        -   : name of the location where the object was found. I.E. the shelf.
    Notes:
        - If there are objects remaining in a location, it will go to that location again, rather than searching for objects
        in another room.
    '''

    def __init__(self, target_object_key=None, target_frame='/map', tsp_route=TSP_route):
        input_keys = ['in_room_name']
        if target_object_key is not None:
            input_keys.append(target_object_key)

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                                    input_keys=input_keys,
                                    output_keys=['out_object_found', 'out_location_inside_room_name'])

        if target_object_key is None:
            target_object_key = 'in_target_object'
            self.userdata.in_target_object = ''  # No target object set! Before set to str(None), changed for SearchObjectWCSM
            going_to_pool = ["I'm going to the %s to look for objects.", "Maybe I find objects on the %s. I'll have a look.",
                             "Why don't I search objects on the %s?", "I think there can be objects on the %s."]
            object_not_found_pool = ["I can't see any object on the %s.", "It seems that there aren't objects on the %s.",
                                     "I haven't found any object on the %s."]
        else:
            going_to_pool = ["I'm going to the %s to look if it's there.", "Maybe I find it on the %s. I'll have a look.",
                             "Why don't I search it on the %s?", "I think it can be on the %s."]
            object_not_found_pool = ["I can't see it on the %s.", "It seems that it isn't on the %s.",
                                     "I haven't found it on the %s."]

        object_found_pool = ["I can see the %s on the %s.", "Is that the %s on the %s? I think so!",
                             "The %s is just there on the %s.", "I found the %s on the %s.",
                             "Can't you see the %s? Is there, on the %s!"]

        self.userdata.objects_data = None  # To avoid errors the first time the check_if_remaining is called
        self.userdata.sensing_route = None  # Because at the very beginning there's no route
        self.userdata.furniture_route = None  # Because at the very beginning there's no route
        self.userdata.out_object_found = None  # To avoid errors if there's an abort.

        with self:
            StateMachine.add('CHECK_IF_OBJECTS_REMAINING', CheckRemaining(),
                             remapping={'in_obj_list': 'objects_data'},
                             transitions={'empty': 'CHECK_IF_FURNITURE_ROUTE_EMPTY',
                                          'remaining': 'TELL_GO_RECOGNIZE'})

            @smach.cb_interface(input_keys=['in_route', 'in_furniture_poses', 'in_orientations', 'in_furniture_name_list'],
                                output_keys=['out_remaining_poses', 'out_remaining_orientations', 'out_remaining_names'],
                                outcomes=['remaining', 'empty'])
            def check_furniture_route_emptiness(userdata):
                if userdata.in_route:
                    # We get the remaining poses and orientations of the furniture route
                    # and then we'll recalculate the route through that remaining nodes
                    remaining_poses = []
                    remaining_orientations = []
                    remaining_names = []
                    for index in userdata.in_route:  # furniture route has only the indices of the elements
                        remaining_poses.append(userdata.in_furniture_poses[index])
                        remaining_orientations.append(userdata.in_orientations[index])
                        remaining_names.append(userdata.in_furniture_name_list[index])
                    userdata.out_remaining_poses = remaining_poses
                    userdata.out_remaining_orientations = remaining_orientations
                    userdata.out_remaining_names = remaining_names
                    return 'remaining'
                return 'empty'

            StateMachine.add('CHECK_IF_FURNITURE_ROUTE_EMPTY',
                             CBState(check_furniture_route_emptiness,
                                     input_keys=['in_route', 'in_furniture_poses', 'in_orientations', 'in_furniture_name_list'],
                                     output_keys=['out_remaining_poses', 'out_remaining_orientations', 'out_remaining_names'],
                                     outcomes=[succeeded, 'empty']),
                             remapping={'in_route': 'furniture_route',
                                        'in_furniture_poses': 'furniture_detect_poses',
                                        'in_orientations': 'furniture_orientation_data',
                                        'out_remaining_poses': 'furniture_detect_poses',
                                        'out_remaining_orientations': 'furniture_orientation_data',
                                        'in_furniture_name_list': 'furniture_name_list',
                                        'out_remaining_names': 'furniture_name_list'},
                             transitions={'remaining': 'FURNITURE_TSP_ROUTE',
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
                                          'empty': 'CALCULATE_FURNITURE_SENSING_LOCATIONS'})

            StateMachine.add('CALCULATE_FURNITURE_SENSING_LOCATIONS', CalculateSensingLocations(),
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
                                          'empty_route': 'CALCULATE_FURNITURE_SENSING_LOCATIONS'})

            StateMachine.add('MOVE_TO_SENSING_LOCATION',
                             MoveActionState("/map", goal_key='next_sensing_pose'),
                             transitions={succeeded: 'DETECT_FURNITURE_AND_ANNOUNCE',
                                          aborted: 'GET_NEXT_SENSING_LOCATION'})  # FIXME if aborted we get the next pose.

            tell_and_search = Concurrence(outcomes=[succeeded, aborted, preempted, 'no_furniture'],
                                          default_outcome=aborted,
                                          output_keys=['furniture_detect_poses',
                                                       'furniture_orientation_data', 'furniture_name_list'],
                                          outcome_map={succeeded: {'ANNOUNCE_SEARCHING': succeeded,
                                                                   'DETECT_FURNITURE_ZONE': succeeded},
                                                       'no_furniture': {'DETECT_FURNITURE_ZONE': 'no_furniture'}})
            with tell_and_search:
                searching_furniture_pool = ["I'm looking for places that can contain objects.",
                                            "I'm searching a place that can have objects.",
                                            "I'm searching the best place to find objects."]
                Concurrence.add('ANNOUNCE_SEARCHING',
                                SpeakActionFromPoolStateMachine(searching_furniture_pool))

                Concurrence.add('DETECT_FURNITURE_ZONE',
                                DetectFurnitureOfZoneSM(distance_treshold=DIST_BETWEEN_FURNITURE, dist_to_furniture=DIST_TO_FURNITURE),
                                remapping={'out_furniture_pose_list': 'furniture_detect_poses',
                                           'out_furniture_orientation_list': 'furniture_orientation_data',
                                           'out_furniture_name_list': 'furniture_name_list'})

            transition_route = 'FURNITURE_TSP_ROUTE' if tsp_route else 'FURNITURE_PROBABILITY_ROUTE'
            StateMachine.add('DETECT_FURNITURE_AND_ANNOUNCE', tell_and_search,
                             transitions={succeeded: transition_route, 'no_furniture': 'GET_NEXT_SENSING_LOCATION'},
                             remapping={'furniture_detect_poses': 'furniture_detect_poses',
                                        'furniture_name_list': 'furniture_name_list',
                                        'furniture_orientation_data': 'furniture_orientation_data'})


            #FIXME filter poses and everything by probability or something like that?
            # @smach.cb_interface(input_keys=['in_furniture_detect_data'], output_keys=['out_furniture_node_list'],
            #                     outcomes=[succeeded])
            # def check_furniture_data(userdata):
            #     #FIXME -> May be necessary to filter in some way the already visited furniture...
            #     #furniture_detect_data is a list of tuples (pos, orientation), so we get only the poses for the TSP
            #     userdata.out_furniture_node_list = reduce(lambda acc, x: acc + [x[0]], userdata.in_furniture_detect_data, [])

            #     return succeeded

            # StateMachine.add('CHECK_FURNITURE_DATA',
            #                  CBState(check_furniture_data, input_keys=['in_furniture_detect_data'],
            #                          output_keys=['out_object_detection_pose'],
            #                          outcomes=[succeeded]),
            #                  remapping={'in_furniture_detect_data': 'furniture_detect_data',
            #                             'out_furniture_node_list': 'furniture_node_list'},
            #                  transitions={succeeded: 'TELL_GO_RECOGNIZE'})

            StateMachine.add('FURNITURE_TSP_ROUTE', TSPState(HC=HC, indices=True),
                             remapping={'in_nodes': 'furniture_detect_poses',
                                        'out_route': 'furniture_route'},
                             transitions={succeeded: 'GET_NEXT_FURNITURE_LOCATION'})

            @smach.cb_interface(input_keys=['in_nodes', 'in_furniture_name_list'],
                                output_keys=['out_route', 'out_furniture_name_list'],
                                outcomes=[succeeded])
            def create_probability_route(userdata):
                furn_prob_map = rospy.get_param(FURN_PROB_PARAM)
                n = len(userdata.in_nodes)
                route = range(n)
                # Get a list of tuples (probability, index_of_name)
                prob_index = zip(reduce(lambda acc, x: acc + [furn_prob_map[x]], userdata.in_furniture_name_list, []), route)
                prob_index.sort(key=lambda x: x[0], reverse=True)  # Sort by probability

                robot_pose = Pose()
                robot_pose.position.x = 0
                robot_pose.position.y = 0
                robot_pose.position.z = 0
                # Get robot's pose in /map coordinates
                robot_pose = transform_pose(robot_pose, '/base_link', '/map', timeout=3)
                actual = (robot_pose.position.x, robot_pose.position.y)

                route[0] = prob_index[0][1]
                for i in xrange(1, n):
                    route[i] = prob_index[i][1]
                    if prob_index[i][0] == 0:  # If probability is 0 we don't look at it.
                        del route[i]
                        del userdata.in_furniture_name_list[i]
                    elif prob_index[i][0] == prob_index[i-1][0]:  # If two things have the same probability, get the closer one
                        di_r = ofb_utils.euclidean_distance(userdata.in_nodes[route[i]], actual)
                        di1_r = ofb_utils.euclidean_distance(userdata.in_nodes[route[i-1]], actual)
                        if di_r < di1_r:   # The index at i is nearer than the one at i-1
                            route[i] = route[i-1]
                            route[i-1] = prob_index[i][1]
                userdata.out_route = route
                userdata.out_furniture_list = userdata.in_furniture_name_list
                return succeeded

            StateMachine.add('FURNITURE_PROBABILITY_ROUTE',
                             CBState(create_probability_route,
                                     input_keys=['in_nodes', 'in_furniture_name_list'],
                                     output_keys=['out_route', 'out_furniture_name_list'],
                                     outcomes=[succeeded]),
                             remapping={'in_nodes': 'furniture_detect_poses',
                                        'in_furniture_name_list': 'furniture_name_list',
                                        'out_furniture_name_list': 'furniture_name_list'
                                        'out_route': 'furniture_route'},
                             transitions={succeeded: 'GET_NEXT_FURNITURE_LOCATION'})

            @smach.cb_interface(input_keys=['in_furniture_route', 'in_orient_list', 'in_pose_list', 'in_furniture_name_list'],
                                output_keys=['out_furniture_route', 'out_object_detection_pose', 'out_furniture_name'],
                                outcomes=[succeeded, 'empty_route'])
            def get_next_loc_from_furniture_route(userdata):
                # Returns the next furniture location to go and removes it from the route
                if not userdata.in_furniture_route:  # The route is empty, so we recalculate the sensing route and go again
                    return 'empty_route'

                node_index = userdata.in_furniture_route[0]
                print('node_index: %d, length in_furniture_route: %d' % (node_index, len(userdata.in_furniture_route)))
                next_pos = userdata.in_pose_list[node_index]

                # Only the index is removed from the list, to preserve the index order of the other elements
                userdata.out_furniture_route = userdata.in_furniture_route[1:]
                pose = Pose()
                pose.position.x = next_pos[0]
                pose.position.y = next_pos[1]
                pose.orientation = userdata.in_orient_list[node_index]
                userdata.out_object_detection_pose = pose
                userdata.out_furniture_name = userdata.in_furniture_name_list[node_index]
                return succeeded

            StateMachine.add('GET_NEXT_FURNITURE_LOCATION',
                             CBState(get_next_loc_from_furniture_route,
                                     input_keys=['in_furniture_route', 'in_orient_list', 'in_pose_list'],
                                     output_keys=['out_furniture_route', 'out_object_detection_pose', 'out_furniture_name'],
                                     outcomes=[succeeded, 'empty_route']),
                             remapping={'out_furniture_route': 'furniture_route',
                                        'in_furniture_route': 'furniture_route',
                                        'in_orient_list': 'furniture_orientation_data',
                                        'in_pose_list': 'furniture_detect_poses',
                                        'in_furniture_name_list': 'furniture_name_list',
                                        'out_object_detection_pose': 'object_detection_pose',
                                        'out_furniture_name': 'out_location_inside_room_name'},
                             transitions={succeeded: 'TELL_GO_RECOGNIZE',
                                          'empty_route': 'SENSING_LOCATIONS_TSP_ROUTE'})

            StateMachine.add('TELL_GO_RECOGNIZE', TellGoRecognizeSM(msg_pool=going_to_pool, arg_key='location_name'),
                             remapping={'location_name': 'out_location_inside_room_name',
                                        'out_objects_data': 'objects_data',
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
                             SpeakActionFromPoolStateMachine(object_not_found_pool, arg_key='location_name'),
                             remapping={'location_name': 'out_location_inside_room_name'},
                             transitions={succeeded: 'GET_NEXT_SENSING_LOCATION', aborted: 'GET_NEXT_SENSING_LOCATION'})

            @smach.cb_interface(input_keys=['in_first_object', 'in_location_name'], output_keys=['out_tell_arg'],
                                outcomes=[succeeded])
            def prepare_userdata(userdata):
                userdata.out_tell_arg = (userdata.in_first_object.name, userdata.in_location_name)
                return succeeded

            StateMachine.add('PREPARE_POOL_ARGS',
                             CBState(prepare_userdata,
                                     input_keys=['in_first_object', 'in_location_name'],
                                     output_keys=['out_tell_arg'], outcomes=[succeeded]),
                             remapping={'in_first_object': 'out_object_found',
                                        'out_tell_arg': 'tell_arg',
                                        'in_location_name': 'out_location_inside_room_name'},
                             transitions={succeeded: 'TELL_OBJECT_RECOGNIZED'})

            StateMachine.add('TELL_OBJECT_RECOGNIZED',
                             SpeakActionFromPoolStateMachine(object_found_pool, arg_key="tell_arg"),
                             remapping={'tell_arg': 'tell_arg'},
                             transitions={succeeded: succeeded, aborted: aborted})
