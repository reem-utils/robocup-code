import roslib
roslib.load_manifest('who_is_who')
import smach

from text_to_speech.msg import *
from geometry_msgs.msg import Point, Quaternion

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted, unknown_face
from tf.transformations import quaternion_from_euler

from pal_smach_utils import *
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.recognize_face import RecognizeFaceStateMachine
from pal_smach_utils.utils.global_common import get_position_from_param, get_orientation_from_param


class RecognizeAndMoveToCallerStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
            output_keys=['caller_name'])

        with self:
            # FIXME: look for raised arm waving!

            def move_to_caller_goal_cb(userdata, nav_goal):
                # FIXME: (see above)
                nav_goal.target_pose.pose.position = get_position_from_param(
                    'who_is_who/caller_position', Point(0.2, 0.2, 0))
                nav_goal.target_pose.pose.orientation = get_orientation_from_param(
                    'who_is_who/caller_orientation',
                    Quaternion(*quaternion_from_euler(0, 0, 0.785)))
                return nav_goal

            smach.StateMachine.add(
                'MOVE_TO_CALLER',
                MoveActionState(
                    goal_cb=move_to_caller_goal_cb,
                    #input_keys = ['message']
                    ),
                transitions={succeeded: 'ANNOUNCE_CALLER'})

            smach.StateMachine.add(
                'ANNOUNCE_CALLER',
                SpeakActionState("You were looking for me? Here I am!"),
                transitions={succeeded: 'SM_RECOGNIZE_FACE'})

            # PRE: face recognition only knows the 3 people from the test,
            #      so we don't need to check the name

            smach.StateMachine.add(
                'SM_RECOGNIZE_FACE',
                RecognizeFaceStateMachine(learn=False),
                transitions={unknown_face: 'SM_RECOGNIZE_FACE'},
                remapping={'person_name': 'caller_name'})

# vim: expandtab ts=4 sw=4
