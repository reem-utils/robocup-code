import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.topic_reader import TopicReaderState
from grammar_state import GrammarState
from pal_smach_utils.speech.sound_action import SpeakActionState

from pal_interaction_msgs.msg import asrresult

class Process_data(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['in_listened'], output_keys=['out_listened'])

    def execute(self, userdata):
            userdata.out_listened = userdata.in_listened.text
            return succeeded



class ListenOrders(smach.StateMachine):

    def __init__(self, GRAMMAR_NAME, timeout=30):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
            output_keys=['o_userSaidData_text'])

        with self:
            smach.StateMachine.add(
                    'ENABLE_GRAMMAR',
                    GrammarState(GRAMMAR_NAME, enabled=True),
                    transitions={succeeded: 'HEAR_COMMAND'})

            smach.StateMachine.add(
                    'HEAR_COMMAND',
                    TopicReaderState(topic_name='usersaid', msg_type=asrresult, timeout=timeout),
                    transitions={aborted: 'PRINT_BAD_MESSAGE', succeeded: 'PROC_DATA', preempted: preempted},
                    remapping={'message': 'o_userSaidData'})

            smach.StateMachine.add(
                    'PROC_DATA',
                    Process_data(),
                    transitions={aborted: 'PRINT_BAD_MESSAGE', succeeded: 'PRINT_GOOD_MESSAGE', preempted: preempted},
                    remapping={'in_listened': 'o_userSaidData', 'out_listened': 'o_userSaidData_text'})
                    

            smach.StateMachine.add(
                    'PRINT_BAD_MESSAGE',
                    SpeakActionState(text="I can't understand you. Can you repeat the command?"),
                    transitions={succeeded: 'HEAR_COMMAND'}
                    )

            smach.StateMachine.add(
                    'PRINT_GOOD_MESSAGE',
                    SpeakActionState(text="Understood!"),
                    transitions={succeeded: 'DISABLE_GRAMMAR'}
                    )

            smach.StateMachine.add(
                    'DISABLE_GRAMMAR',
                    GrammarState(GRAMMAR_NAME, enabled=False),
                    transitions={succeeded: succeeded, aborted: aborted})
