import rospy
import smach
import random
from smach_ros import SimpleActionState


from text_to_speech.msg import SoundAction, SoundGoal

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted

# Constants
TTS_ACTION_NAME = '/sound'


class SpeakActionState(SimpleActionState):

    def __init__(self, text=None, text_cb=None, wait_before_speaking=0, **kwargs):
        """
        @param text: the text to speak out aloud (if `text_cb' is None)
        @param text_cb: a callback returning the text to speak out
               (if `text' is None)
        @param wait_before_speaking: how long to wait before speaking;
               it may be a number (in seconds) or a rospy.Duration
        @param **kwargs: input_keys, output_keys, etc.
        """

        if not text and not text_cb:
            raise ValueError("Neither `text' nor `text_cb' where set!")
        elif text and text_cb:
            raise ValueError("You've set both `text' and `text_cb'!")

        if not isinstance(wait_before_speaking, rospy.Duration):
            wait_before_speaking = rospy.Duration(wait_before_speaking)

        def generic_goal_cb(userdata, old_goal):
            tts_goal = SoundGoal()
            tts_goal.wait_before_speaking = wait_before_speaking
            tts_goal.text = text if text else text_cb(userdata)
            print "Speaking:", tts_goal.text
            return tts_goal

        SimpleActionState.__init__(self,
                                   TTS_ACTION_NAME, SoundAction,
                                   goal_cb=generic_goal_cb, **kwargs)


class SpeakActionFromPoolStateMachine(smach.StateMachine):
    """SpeakActionFromPoolStateMachine.

    Use this State Machine to the robot speak a random string from a list.

    """

    def __init__(self, message_pool, arg_key=None):  # arg_key is a string with the name of the input key with the argument that the state machine will recieve
        """Constructor for SpeakActionFromPoolStateMachine

        @type message_pool: list of strings
        @param message_pool: A list containing some tts.

        @type arg_key: input_key on userdata.
        @param arg_key: Is a string with the name of the input key with the argument that the state machine will recieve

        """
        input_keys = []
        if arg_key is not None:
            input_keys.append(arg_key)

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=input_keys, output_keys=[])

        if arg_key is None:
            arg_key = 'in_arg'
            self.userdata.in_arg = None  # No argument set!

        with self:
            smach.StateMachine.add('SELECT_MESSAGE', self.ChooseMessageFromPool(message_pool),
                                   remapping={'in_arg': arg_key,
                                              'out_message_to_say': 'message_to_say'},
                                   transitions={succeeded: 'TELL_SELECTED_MESSAGE'})

            smach.StateMachine.add('TELL_SELECTED_MESSAGE', SpeakActionState(text_cb=lambda userdata: userdata.message_to_say,
                                   input_keys=['message_to_say']),
                                   transitions={aborted: aborted,
                                                succeeded: succeeded})

    class ChooseMessageFromPool(smach.State):
        def __init__(self, pool):
            smach.State.__init__(self, outcomes=[succeeded], input_keys=['in_arg'], output_keys=['out_message_to_say'])
            self.pool = pool
            self.last_message = None

        def execute(self, userdata):
            message = random.choice(self.pool)
            if len(self.pool) > 1:
                i = 0
                while self.last_message == message and i < 10:
                    message = random.choice(self.pool)
                    i = i + 1

            if (userdata.in_arg is not None) and ('%s' in message):
                    userdata.out_message_to_say = message % userdata.in_arg
            else:
                userdata.out_message_to_say = message

            self.last_message = message
            return succeeded

# vim: expandtab ts=4 sw=4
