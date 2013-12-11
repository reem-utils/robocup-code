#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from smach import StateMachine, CBState
from smach_ros import ServiceState
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionFromPoolStateMachine
from next_location_provider.srv import NextProbableLocation
from pal_smach_utils.object_finding_algorithms.object_check_states import CheckObjectAndRemoveFromList, CheckRemaining
from pal_smach_utils.object_finding_algorithms.tell_move_and_recognize_sm import TellGoRecognizeSM


class OFBFirstApproach(smach.StateMachine):

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

        cant_reach_pool = ["I can't reach the %s.", "There is no path to the %s.", "The %s is unreachable."]

        self.userdata.objects_data = None  # To avoid errors the first time the check_if_remaining is called

        with self:
            def check_room_name(userdata):
                self.userdata.o_room_name = self.userdata.i_room_name.replace(' ', '_')
                return succeeded

            StateMachine.add('CHECK_ROOM_NAME',
                             CBState(check_room_name,
                                     input_keys=['in_room_name'],
                                     output_keys=['out_room_name'], outcomes=[succeeded]),
                             remapping={'i_room_name': 'in_room_name',
                                        'o_room_name': 'in_room_name'},
                             transitions={succeeded: 'CHECK_IF_OBJECTS_REMAINING'})

            StateMachine.add('CHECK_IF_OBJECTS_REMAINING', CheckRemaining(),
                             remapping={'in_obj_list': 'objects_data'},
                             transitions={'empty': 'GET_NEXT_PROB_LOCATION',
                                          'remaining': 'TELL_GO_RECOGNIZE'})  # FIXME transition to 'CHECK_IF_OBJECT_FOUND' to check it works.

            @smach.cb_interface(output_keys=['out_location_name', 'out_location_pose'])
            def next_prob_location_cb(userdata, response):
                userdata.out_location_name = response.location
                userdata.out_location_pose = response.loc_position
                return succeeded

            StateMachine.add('GET_NEXT_PROB_LOCATION',
                             ServiceState('get_next_probable_location',
                                          NextProbableLocation,
                                          request_slots=['room'],
                                          response_cb=next_prob_location_cb,
                                          output_keys=['out_location_name', 'out_location_pose'],
                                          input_keys=['room']),
                             transitions={succeeded: 'TELL_GO_RECOGNIZE', aborted: aborted},  # FIXME aborted?
                             remapping={'out_location_name': 'out_location_inside_room_name',
                                        'out_location_pose': 'location_pose_in_map',
                                        'room': 'in_room_name'})

            StateMachine.add('TELL_GO_RECOGNIZE', TellGoRecognizeSM(msg_pool=going_to_pool, arg_key='location_name'),
                             remapping={'location_name': 'out_location_inside_room_name',
                                        'out_objects_data': 'objects_data',
                                        'in_target_object': target_object_key,
                                        'in_location_pose_in_map': 'location_pose_in_map'},
                             transitions={'move_failed': 'TELL_CANT_REACH',
                                          'no_object_found': 'CHECK_IF_OBJECT_FOUND',
                                          succeeded: 'CHECK_IF_OBJECT_FOUND',
                                          aborted: aborted})  # FIXME aborted should abort everything?

            StateMachine.add('TELL_CANT_REACH', SpeakActionFromPoolStateMachine(cant_reach_pool, arg_key='location_name'),
                             transitions={succeeded: 'GET_NEXT_PROB_LOCATION'},  # FIXME aborted to GET_NEXT or again to the move?
                             remapping={'location_name': 'out_location_inside_room_name'})

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
                             transitions={succeeded: 'GET_NEXT_PROB_LOCATION', aborted: aborted})

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
                                        'in_location_name': 'out_location_inside_room_name',
                                        'out_tell_arg': 'tell_arg'},
                             transitions={succeeded: 'TELL_OBJECT_RECOGNIZED'})

            StateMachine.add('TELL_OBJECT_RECOGNIZED',
                             SpeakActionFromPoolStateMachine(object_found_pool, arg_key="tell_arg"),
                             remapping={'tell_arg': 'tell_arg'},
                             transitions={succeeded: succeeded, aborted: aborted})
