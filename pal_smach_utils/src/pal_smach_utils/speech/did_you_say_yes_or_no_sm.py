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

YES_NO_GRAMMAR = 'confirming'
TIMEOUT_YES_NO = None
YES_NO_KEY = 'action'
YES_WORD = 'yes'
NO_WORD = 'no'
SLEEP_TILL_HEARD_AGAIN = 0.5


class HearingConfirmationSM(smach.StateMachine):
    """
    This will ask you if you said what's in in_message_heard and
    hear yes or no. Afterward it will return the result yes or no.
    """

    def __init__(self, grammar_to_reset_when_finished=""):
        smach.StateMachine.__init__(self,
                                    ['correct_word_heard',
                                     'wrong_word_heard',
                                     preempted, aborted],
                                    input_keys=['in_message_heard'])

        self._grammar_to_reset_when_finished = grammar_to_reset_when_finished

        with self:

            def confirm_object(userdata):
                text_to_say = "Excuse me, did you say " + str(userdata.in_message_heard) + " ?"
                return text_to_say

            smach.StateMachine.add('CONFIRM_ORDER',
                                   SpeakActionState(text_cb=confirm_object, input_keys=['in_message_heard']),
                                   transitions={succeeded: 'DISABLE_ROOT_GRAMMAR'})

            smach.StateMachine.add('DISABLE_ROOT_GRAMMAR',
                                   GrammarState(self._grammar_to_reset_when_finished, enabled=False),
                                   transitions={succeeded: 'ENABLE_GRAMMAR', aborted: aborted})

            smach.StateMachine.add('ENABLE_GRAMMAR',
                                   GrammarState(YES_NO_GRAMMAR, enabled=True),
                                   transitions={succeeded: 'SLEEP_FOR_GRAMMAR_INSTALL'})

            smach.StateMachine.add('SLEEP_FOR_GRAMMAR_INSTALL',
                                   SleepState(0.5),
                                   transitions={succeeded: 'HEAR_COMMAND',
                                                preempted: preempted})

            def listen_command_cb(userdata, message):
                rospy.loginfo("The message listened is %s", message)

                yes_or_no_in_tags = [tag for tag in message.tags if tag.key == YES_NO_KEY]
                if yes_or_no_in_tags and yes_or_no_in_tags[0].value == YES_WORD:
                    return 'heard_yes'
                elif yes_or_no_in_tags and yes_or_no_in_tags[0].value == NO_WORD:
                    return 'heard_no'
                else:
                    return 'word_diff_from_yes_no'

            smach.StateMachine.add('HEAR_COMMAND',
                                   TopicReaderState(topic_name='/usersaid',
                                                    msg_type=asrresult,
                                                    timeout=TIMEOUT_YES_NO,
                                                    outcomes=['heard_yes',
                                                              'heard_no',
                                                              'word_diff_from_yes_no',
                                                              preempted,
                                                              aborted],
                                                    callback=listen_command_cb),
                                   transitions={preempted: preempted,
                                                aborted: aborted,
                                                'heard_yes': 'PRINT_YES_MESSAGE',
                                                'heard_no': 'PRINT_NO_MESSAGE',
                                                'word_diff_from_yes_no': 'PRINT_DIDNT_HEAR_MESSAGE'},
                                   remapping={'message': 'o_userSaidData'})

            smach.StateMachine.add('PRINT_DIDNT_HEAR_MESSAGE',
                                   SpeakActionState(text="I beg your pardon, may you repeat what you just said ?"),
                                   transitions={succeeded: 'SLEEP_STATE'})

            smach.StateMachine.add('SLEEP_STATE',
                                   SleepState(SLEEP_TILL_HEARD_AGAIN),
                                   transitions={succeeded: 'HEAR_COMMAND',
                                                preempted: preempted})

            smach.StateMachine.add('PRINT_YES_MESSAGE',
                                   SpeakActionState(text="Yes ? Understood!"),
                                   transitions={succeeded: 'YES_DISABLE_GRAMMAR'})

            smach.StateMachine.add('YES_DISABLE_GRAMMAR',
                                   GrammarState(YES_NO_GRAMMAR, enabled=False),
                                   transitions={succeeded: 'YES_ENABLE_ROOT_GRAMMAR', aborted: aborted})

            smach.StateMachine.add('YES_ENABLE_ROOT_GRAMMAR',
                                   GrammarState(self._grammar_to_reset_when_finished, enabled=True),
                                   transitions={succeeded: 'correct_word_heard'})

            smach.StateMachine.add('PRINT_NO_MESSAGE',
                                   SpeakActionState(text="No ? Then I must have misheard you."),
                                   transitions={succeeded: 'NO_DISABLE_GRAMMAR'})

            smach.StateMachine.add('NO_DISABLE_GRAMMAR',
                                   GrammarState(YES_NO_GRAMMAR, enabled=False),
                                   transitions={succeeded: 'NO_ENABLE_ROOT_GRAMMAR', aborted: aborted})

            smach.StateMachine.add('NO_ENABLE_ROOT_GRAMMAR',
                                   GrammarState(self._grammar_to_reset_when_finished, enabled=True),
                                   transitions={succeeded: 'wrong_word_heard'})
