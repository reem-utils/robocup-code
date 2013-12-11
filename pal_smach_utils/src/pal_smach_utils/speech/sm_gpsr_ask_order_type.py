import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_smach_utils.utils.timeout_container import SleepState

from grammar_state import GrammarState
from sound_action import SpeakActionState

from pal_interaction_msgs.msg import asrresult


ONE_TOW_GRAMMAR = 'confirming_one_two'
TIMEOUT_one_two = None
one_two_KEY = 'action'
one_WORD = 'one'
two_WORD = 'two'
SLEEP_TILL_HEARD_AGAIN = 0.5


class SentenceConfirmationSM(smach.StateMachine):
    """
    This will ask you what type of sentence is going to say
    """

    def __init__(self, grammar_to_reset_when_finished=""):
        smach.StateMachine.__init__(self,
                                    ['one_word_heard',
                                     'two_word_heard',
                                     preempted, aborted],
                                    input_keys=['in_message_heard'])

        self._grammar_to_reset_when_finished = grammar_to_reset_when_finished

        with self:


            smach.StateMachine.add('DISABLE_ROOT_GRAMMAR',
                                   GrammarState(self._grammar_to_reset_when_finished, enabled=False),
                                   transitions={succeeded: 'ENABLE_GRAMMAR', aborted: aborted})

            smach.StateMachine.add('ENABLE_GRAMMAR',
                                   GrammarState(ONE_TOW_GRAMMAR, enabled=True),
                                   transitions={succeeded: 'HEAR_COMMAND'})

            def listen_command_cb(userdata, message):
                rospy.loginfo("The message listened is %s", message)

                one_or_two_in_tags = [tag for tag in message.tags if tag.key == one_two_KEY]
                if one_or_two_in_tags and one_or_two_in_tags[0].value == one_WORD:
                    return 'heard_one'
                elif one_or_two_in_tags and one_or_two_in_tags[0].value == two_WORD:
                    return 'heard_two'
                else:
                    return 'word_diff_from_one_two'

            smach.StateMachine.add('HEAR_COMMAND',
                                   TopicReaderState(topic_name='/usersaid',
                                                    msg_type=asrresult,
                                                    timeout=TIMEOUT_one_two,
                                                    outcomes=['heard_one',
                                                              'heard_two',
                                                              'word_diff_from_one_two',
                                                              preempted,
                                                              aborted],
                                                    callback=listen_command_cb),
                                   transitions={preempted: preempted,
                                                aborted: aborted,
                                                'heard_one': 'PRINT_one_MESSAGE',
                                                'heard_two': 'PRINT_two_MESSAGE',
                                                'word_diff_from_one_two': 'PRINT_DIDNT_HEAR_MESSAGE'},
                                   remapping={'message': 'o_userSaidData'})

            smach.StateMachine.add('PRINT_DIDNT_HEAR_MESSAGE',
                                   SpeakActionState(text="I beg your pardon, may you repeat what you just said ?"),
                                   transitions={succeeded: 'SLEEP_STATE'})

            smach.StateMachine.add('SLEEP_STATE',
                                   SleepState(SLEEP_TILL_HEARD_AGAIN),
                                   transitions={succeeded: 'HEAR_COMMAND',
                                                preempted: preempted})

            smach.StateMachine.add('PRINT_one_MESSAGE',
                                   SpeakActionState(text="One? Understood!"),
                                   transitions={succeeded: 'one_DISABLE_GRAMMAR'})

            smach.StateMachine.add('one_DISABLE_GRAMMAR',
                                   GrammarState(one_two_GRAMMAR, enabled=False),
                                   transitions={succeeded: 'one_ENABLE_ROOT_GRAMMAR', aborted: aborted})

            smach.StateMachine.add('one_ENABLE_ROOT_GRAMMAR',
                                   GrammarState(self._grammar_to_reset_when_finished, enabled=True),
                                   transitions={succeeded: 'one_word_heard'})

            smach.StateMachine.add('PRINT_two_MESSAGE',
                                   SpeakActionState(text="Two? Understood!"),
                                   transitions={succeeded: 'two_DISABLE_GRAMMAR'})

            smach.StateMachine.add('two_DISABLE_GRAMMAR',
                                   GrammarState(one_two_GRAMMAR, enabled=False),
                                   transitions={succeeded: 'two_ENABLE_ROOT_GRAMMAR', aborted: aborted})

            smach.StateMachine.add('two_ENABLE_ROOT_GRAMMAR',
                                   GrammarState(self._grammar_to_reset_when_finished, enabled=True),
                                   transitions={succeeded: 'two_word_heard'})
