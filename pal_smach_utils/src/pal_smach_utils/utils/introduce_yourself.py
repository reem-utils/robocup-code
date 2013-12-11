import smach
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.speech.sound_action import SpeakActionState
from rospy.rostime import Duration


class IntroduceYourselfStateMachine(smach.StateMachine):
    """
    Reem tells his name and nothing else. 
    """

    def __init__(self, announce_unknown_face=True):
        smach.StateMachine.__init__(self,
            outcomes=[succeeded, preempted, aborted]
            )

        with self:
            introduction = "Hi! My name is Reem. Pleased to meet you!"
            smach.StateMachine.add('INTRODUCE_YOURSELF_TTS', SpeakActionState(text=introduction, wait_before_speaking=Duration(0.10)),
                               transitions={'succeeded': succeeded,
                                            'aborted': aborted})
