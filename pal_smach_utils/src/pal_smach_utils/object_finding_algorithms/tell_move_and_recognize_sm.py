#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')

from smach import StateMachine, Concurrence
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.speech.sound_action import SpeakActionFromPoolStateMachine
#from pal_smach_utils.grasping.search_object_with_confidence_moped import SearchObjectWithConfidenceStateMachine  # Moped
from pal_smach_utils.grasping.search_object_with_confidence import SearchObjectWithConfidenceStateMachine  # TABLETOP, WAS BLORT BEFORE


class TellGoRecognizeSM(Concurrence):

    '''
    Says a message extracted from the msg_pool argument while goes to a location and looks for objects.
    Constructor parameters:
        arg_key is the name of the userdata key containing the argument to pass to the SpeakActionFromPoolStateMachine.
        You need to add a remap with the same value as the arg_key and put there the argument for the speech action.
        arg_key has to be None if the speak state don't need a parameter.
        In the other case, the easiest way of using this state is ignoring the arg_key parameter and remapping the userdata
            variable containing the argument for the speak action to the input_key 'tell_argument' of this state.
    Userdata:
        - in_location_pose_in_map: Location pose in /map coordinate frame where the robot has to go.
        - in_target_object: Name of a target object to search for.
                            If a specific object is not being searched (ie it doesn't mind what object is found),
                            the key MUST be filled with an empty string ( '' ).
        - out_objects_data: ObjectPoseList of recognized data.
        - tell_argument: Argument for the speak state. For example, it may be used to tell the name of the location.
                         For more information, look the SpeakActionFromPoolStateMachine explanation.
    Outcomes:
        Appart from the common ones:
        - move_failed: Is outcomed when the move action fails.

    Notes:
        - The out_objects_data's value is None if the move fails.

    Example of use:
        StateMachine.add('TELL_GO_RECOGNIZE', TellGoRecognizeSM(msg_pool=going_to_pool, arg_key='location_name),
                         remapping={'location_name': 'location_room_name',
                                    'out_objects_data': 'objects_data',
                                    'in_target_object': target_object_key,
                                    'in_location_pose_in_map': 'location_pose_in_map'},
                         transitions={succeeded: succeeded, aborted: aborted, 'move_failed': 'TELL_CANT_REACH'}
        (or simply ignoring the arg_key and doing the remapping like this:
            remapping={'tell_argument': 'location_room_name', ...})
    '''

    def __init__(self, msg_pool, arg_key='tell_argument'):
        input_keys = ['in_location_pose_in_map', 'in_target_object']
        if arg_key:
            input_keys.append(arg_key)
        Concurrence.__init__(self, outcomes=[succeeded, aborted, 'move_failed', 'no_object_found'],
                             default_outcome=aborted,
                             input_keys=input_keys,
                             output_keys=['out_objects_data'],
                             outcome_map={succeeded: {'TELL_GOING_TO_SEARCH': succeeded,
                                                      'MOVE_AND_RECOGNIZE': succeeded},
                                          'no_object_found': {'MOVE_AND_RECOGNIZE': 'no_object_found'},
                                          'move_failed': {'MOVE_AND_RECOGNIZE': 'move_failed'}})

        if type(msg_pool) is str:
            msg_pool = [msg_pool]

        if arg_key is None:
            arg_key = 'tell_argument'
            self.userdata.tell_argument = None  # No argument set!

        # Concurrence container to speak and search simultanously
        with self:
            Concurrence.add('TELL_GOING_TO_SEARCH', SpeakActionFromPoolStateMachine(msg_pool, arg_key=arg_key),
                            remapping={arg_key: arg_key})
            Concurrence.add('MOVE_AND_RECOGNIZE', GoAndRecognizeSM(),
                            remapping={'in_target_object': 'in_target_object',
                                       'in_location_pose_in_map': 'in_location_pose_in_map',
                                       'out_objects_data': 'out_objects_data'})


class GoAndRecognizeSM(StateMachine):

    '''
    State machine that goes to a location and recognizes objects.
    Userdata:
        - in_location_pose_in_map: Location pose in /map coordinate frame where the robot has to go.
        - in_target_object: Name of a target object to search for.
                            If a specific object is not being searched (ie it doesn't mind what object is found),
                            the key MUST be filled with an empty string ( '' ).
        - out_objects_data: ObjectPoseList of recognized data.
    Outcomes:
        Appart from the common ones:
        - move_failed: Is outcomed when the MOVE_TO_SEARCHING_LOCATION fails.
    Notes:
        - The out_objects_data's value is None if the move fails.
    '''

    def __init__(self):
        StateMachine.__init__(self, outcomes=[succeeded, aborted, preempted, 'move_failed', 'no_object_found'],
                              input_keys=['in_location_pose_in_map', 'in_target_object'],
                              output_keys=['out_objects_data'])

        self.userdata.out_objects_data = None  # If the move action fails, this output key is not filled and shows an error.

        # SM that moves to searching location and searches objects
        with self:
            StateMachine.add('MOVE_TO_SEARCHING_LOCATION',
                             MoveActionState("/map", goal_key='in_location_pose_in_map'),
                             transitions={succeeded: 'RECOGNIZE_OBJECTS', aborted: 'move_failed'})

            StateMachine.add('RECOGNIZE_OBJECTS', SearchObjectWithConfidenceStateMachine(),
                             remapping={'object_found': 'out_objects_data',
                                        'object_to_search_for': 'in_target_object'},
                             transitions={succeeded: succeeded, aborted: 'RETRY_RECOGNIZE_OBJECTS'})

            StateMachine.add('RETRY_RECOGNIZE_OBJECTS', SearchObjectWithConfidenceStateMachine(),
                             remapping={'object_found': 'out_objects_data',
                                        'object_to_search_for': 'in_target_object'},
                             transitions={succeeded: succeeded, aborted: 'no_object_found'})
