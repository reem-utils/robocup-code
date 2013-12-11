import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import dynamic_reconfigure.client
from smach_ros import ServiceState

from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Pose, Point, Quaternion
from coord_translator.srv import LocationTranslator

from move_action import MoveActionState
from pal_smach_utils.speech.sound_action import SpeakActionState, SpeakActionFromPoolStateMachine
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted


class AnnounceAndMoveStateMachine(smach.Concurrence):

    def __init__(self, announcement):
        smach.Concurrence.__init__(self, outcomes=[succeeded, aborted],
                                   default_outcome=aborted,
                                   input_keys=['room_name', 'room_location'],
                                   outcome_map={succeeded: {'ANNOUNCE_MOVEMENT': succeeded,
                                                            'MOVE_TO_ROOM': succeeded}})

        # Concurrence container to speak and move simultanously
        with self:
            if type(announcement) is str:  # We have an only string, we can use a simple speakActionState.
                def announce_movement_cb(userdata):
                    return announcement % userdata.room_name

                smach.Concurrence.add('ANNOUNCE_MOVEMENT',
                                      SpeakActionState(text_cb=announce_movement_cb, input_keys=['room_name']))
            else:  # We have a list (or it should, it'll fail if not) so we use a SpeakActionFromPoolSM
                smach.Concurrence.add('ANNOUNCE_MOVEMENT',
                                      SpeakActionFromPoolStateMachine(announcement, arg_key='room_name'),
                                      remapping={'room_name': 'room_name'})

            smach.Concurrence.add('MOVE_TO_ROOM',
                                  MoveActionState("/map", goal_key='room_location'))


class MoveToRoomStateMachine(smach.StateMachine):

    """
    The name of the target room is expected to be in a input key named `room_name'.

    The announcement argument in the constructor is the text to be announced while going to the room.
        If it's a string, a SpeakActionState is used. If it's a list of strings, a SpeakActionFromPoolStateMachine is used.
        All the strings (either the single string or all the strings inside the list) must have a %s to be replaced for the room's name.
        If the announcement argument equals None no speak action is used and the robot simply moves to the room.
    The ignore_orientation parameter performs a dynamic reconfigure to ignore the orientation at the goal, if set to True
    """
    def __init__(self, announcement="%s, here I go!", ignore_orientation=False):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                                    input_keys=['room_name'], output_keys=['room_location'])

        with self:

            @smach.cb_interface(input_keys=['room_name'], output_keys=['room_location'])
            def loc_response_cb(userdata, response):
                if response.exists:
                    pose = Pose()
                    pose.position = Point(response.coordinates.x,
                                          response.coordinates.y, 0)
                    pose.orientation = Quaternion(
                        *quaternion_from_euler(0, 0, response.coordinates.z))
                    userdata.room_location = pose
                    return succeeded
                else:
                    userdata.room_location = None
                    return aborted

            transition = 'TELL_AND_MOVE_TO_ROOM' if (announcement is not None) else 'MOVE_TO_ROOM_NO_SPEAK'
            smach.StateMachine.add('TRANSLATE_ROOM_NAME',
                                   ServiceState('loc_translator', LocationTranslator,
                                                response_cb=loc_response_cb,
                                                request_key='room_name',
                                                output_keys=['room_location'],
                                                input_keys=['room_name']),
                                   transitions={succeeded: 'CHANGE_ROTATION_TOLERANCE' if ignore_orientation else transition,
                                                aborted: 'ANNOUNCE_UNKNOWN'})

            def tolerance_up(userdata):
                node_to_reconfigure = "/move_base/PalLocalPlanner"
                client = dynamic_reconfigure.client.Client(node_to_reconfigure)
                original_config = client.get_configuration()
                userdata.original_config = original_config.yaw_goal_tolerance
                new_params = {'yaw_goal_tolerance': 3.1416}
                client.update_configuration(new_params)
                return succeeded

            smach.StateMachine.add('CHANGE_ROTATION_TOLERANCE', smach.CBState(tolerance_up,
                                                                              outcomes=['succeeded'],
                                                                              output_keys=['original_config']),
                                   transitions={succeeded: transition})

            if (announcement is not None):
                smach.StateMachine.add('TELL_AND_MOVE_TO_ROOM', AnnounceAndMoveStateMachine(announcement),
                                       remapping={'room_name': 'room_name',
                                                  'room_location': 'room_location'},
                                       transitions={succeeded: 'RESET_TOLERANCE' if ignore_orientation else succeeded,
                                                    aborted: 'TELL_CANT_REACH'})
            else:
                smach.StateMachine.add('MOVE_TO_ROOM_NO_SPEAK',
                                       MoveActionState("/map", goal_key='room_location'),
                                       transitions={succeeded: 'RESEsT_TOLERANCE' if ignore_orientation else succeeded,
                                                    aborted: 'TELL_CANT_REACH'})

            def announce_unknown_cb(userdata):
                return "I am sorry, I don't know where %s is located" % \
                    userdata.room_name

            smach.StateMachine.add('ANNOUNCE_UNKNOWN',
                                   SpeakActionState(text_cb=announce_unknown_cb, input_keys=['room_name']),
                                   transitions={succeeded: aborted})

            cant_reach_pool = ["I can't reach the %s.", "There is no path to the %s.", "The %s is unreachable."]
            smach.StateMachine.add('TELL_CANT_REACH', SpeakActionFromPoolStateMachine(cant_reach_pool, arg_key='location_name'),
                                   transitions={succeeded: aborted},  # FIXME It may be better a 'no_path' outcome?
                                   remapping={'location_name': 'room_name'})

            def tolerance_original(userdata):
                node_to_reconfigure = "/move_base/PalLocalPlanner"
                client = dynamic_reconfigure.client.Client(node_to_reconfigure)
                new_params = {'yaw_goal_tolerance': userdata.original_config}
                client.update_configuration(new_params)
                return succeeded

            smach.StateMachine.add('RESET_TOLERANCE', smach.CBState(tolerance_original,
                                                                    outcomes=['succeeded'],
                                                                    input_keys=['original_config']),
                                   transitions={succeeded: succeeded})

# vim: expandtab ts=4 sw=4
