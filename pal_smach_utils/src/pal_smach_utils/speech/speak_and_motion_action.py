import roslib
roslib.load_manifest('pal_smach_utils')
import smach
from smach_ros import SimpleActionState
from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction
from pal_smach_utils.speech.sound_action import SpeakActionState


class SpeakAndMotionActionConcurrentSM(smach.Concurrence):

    ''' StateMachine that does a motion action and says something.

      Parameters of the constructor:
        - filename: must be the full filename of the xml containing the movements.
        - text: The text that the robot has to say while doing the motion action.
    '''

    def __init__(self, filename, text, checksafety=True, plan=True, wait_before_speaking=0):
        smach.Concurrence.__init__(self, outcomes=['succeeded', 'aborted'],
                                   default_outcome='aborted',
                                   outcome_map={'succeeded': {'MOTION_ACTION': 'succeeded',
                                                              'SPEAK_ACTION': 'succeeded'}})

        with self:
            motion_goal = MotionManagerGoal()
            motion_goal.plan = plan
            motion_goal.filename = filename
            motion_goal.checkSafety = checksafety
            motion_goal.repeat = False
            smach.Concurrence.add('MOTION_ACTION', SimpleActionState('/motion_manager', MotionManagerAction,
                                                                     goal=motion_goal))

            smach.Concurrence.add('SPEAK_ACTION', SpeakActionState(text=text, wait_before_speaking=wait_before_speaking))
