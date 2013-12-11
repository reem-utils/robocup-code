#! /usr/bin/env python
# vim: expandtab ts=4 sw=4
### FOLOW_OPERATOR.PY ###

import rospy
import smach

from pal_smach_utils.utils.timeout_container import SleepState

from pal_smach_utils.speech.grammar_state import GrammarState

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from pal_smach_utils.utils.topic_reader import TopicReaderState

from pal_interaction_msgs.msg import asrresult

from pal_smach_utils.speech.sound_action import SpeakActionState

from smach import CBState

import rosbag
from roslib import packages

from nav_msgs.msg import Odometry

from pal_smach_utils.utils.debug import debugPrint

from pal_smach_utils.speech.did_you_say_yes_or_no_sm import HearingConfirmationSM

LISTEN_COMMAND_TIMEOUT = 1.5

SLEEP_TIME_BETWEEN_LISTEN_AND_RECORD_ODOMETRY_ITERATIONS = 2.0

ELEVATOR_DISTANCE_TO_HUMAN = 0.65
follow_grammar_name_index = 0
follow_grammar_names = ["robocup/elevator_out"]  # ['robocup/elevator_in', 'robocup/elevator_out']
follow_grammar_values = ["getout"]  # ['getin', 'getout']
follow_tts_texts = ["I get out of the elevator"]  # ["Ok. I follow you to the elevator.", "I get out of the elevator."]
follow_confirm_messages = ["that you want me to get out of the elevator"]  # ["that you want to get into the elevator", "that you want me to get out of the elevator"]
missunterstood_text = "Sorry, i didn't understand you. Can you repeat please?"

bag = rosbag.Bag(packages.get_pkg_dir('common') + '/config/getin_odometry.bag', 'w')


class RecordOdometry(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:
            def read_odometry_cb(userdata, message):
                # if the value of the grammar is getout, we already heard a getin command
                # and we can record the odometry till we hear the getout command
                value = follow_grammar_values[follow_grammar_name_index]
                if value == 'getout':
                    try:
                        global bag
                        debugPrint("Writing odometry message to the bag...", 3)
                        bag.write('/base_odometry/odom', message)
                    finally:
                        debugPrint("Odometry data saved in bag", 3)

                return succeeded

            smach.StateMachine.add('READ_ODOMETRY_TOPIC',
                                   TopicReaderState(topic_name='/base_odometry/odom', msg_type=Odometry, timeout=1.5,
                                   outcomes=[succeeded, preempted, aborted], callback=read_odometry_cb))


def executeCommand():
    value = follow_grammar_values[follow_grammar_name_index]
    if value == 'getin':
        debugPrint("Get into the elevator command received", 2)

        #we try to set the parameter till it doesn't throw any error
        while True:
            try:
                rospy.set_param("/params_learn_and_follow_operator_test/distance_to_human", ELEVATOR_DISTANCE_TO_HUMAN)
                break
            except Exception as ex:
                debugPrint(str(ex), 0)
                debugPrint("There was an error while trying to set the parameter. Trying again...", 0)

    elif value == 'getout':
        debugPrint("Get out of the elevator command received", 2)
    return


class ListenCommand(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted, 'listen_command', 'command_received'], output_keys=["out_message_heard"])

        with self:
            def listen_command_cb(userdata, message):
                debugPrint("The message listened is " + str(message), 3)

                grammar_tags = [tag for tag in message.tags if tag.key == 'action']
                if grammar_tags and grammar_tags[0].value == follow_grammar_values[follow_grammar_name_index]:
                    userdata.out_message_heard = follow_confirm_messages[follow_grammar_name_index]
                    return 'command_received'
                return 'listen_command'

            smach.StateMachine.add('LISTEN',
                                   TopicReaderState(
                                       topic_name='/usersaid',
                                       msg_type=asrresult,
                                       timeout=LISTEN_COMMAND_TIMEOUT,
                                       outcomes=[succeeded, preempted, aborted, 'listen_command', 'command_received'],
                                       output_keys=["out_message_heard"],
                                       callback=listen_command_cb))


class ListenCommandForFollowMe(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])
        with self:

            @smach.cb_interface(outcomes=[succeeded])
            def initializeCommandVariables(userdata):
                global follow_grammar_name_index
                follow_grammar_name_index = 0
                try:
                    global bag
                    bag = rosbag.Bag(packages.get_pkg_dir('common') + '/config/getin_odometry.bag', 'w')
                finally:
                    debugPrint("Odometry bag opened", 3)
                return succeeded

            smach.StateMachine.add('INITIALIZE_LISTEN_COMMAND_VARIABLES',
                                   CBState(initializeCommandVariables),
                                   transitions={succeeded: 'START_SPEECHRECOG_FOLLOW_GRAMMAR'})

            smach.StateMachine.add('START_SPEECHRECOG_FOLLOW_GRAMMAR',
                                   GrammarState(follow_grammar_names[follow_grammar_name_index], enabled=True),
                                   transitions={succeeded: 'SLEEP_STATE'})

            smach.StateMachine.add('SLEEP_STATE',
                                   SleepState(SLEEP_TIME_BETWEEN_LISTEN_AND_RECORD_ODOMETRY_ITERATIONS),
                                   transitions={succeeded: 'RECORD_ODOMETRY',
                                                preempted: 'RECORD_ODOMETRY'})

            smach.StateMachine.add('RECORD_ODOMETRY',
                                   RecordOdometry(),
                                   transitions={succeeded: 'LISTEN_COMMAND',
                                                preempted: 'LISTEN_COMMAND',
                                                aborted: 'LISTEN_COMMAND'})

            smach.StateMachine.add('LISTEN_COMMAND',
                                   ListenCommand(),
                                   transitions={'listen_command': 'SLEEP_STATE',
                                                'command_received': 'CONFIRM_COMMAND',
                                                aborted: 'SLEEP_STATE'},
                                   remapping={'out_message_heard': 'out_message_heard'})

            smach.StateMachine.add('CONFIRM_COMMAND',
                                   HearingConfirmationSM(),
                                   transitions={"correct_word_heard": "EXECUTE_COMMAND_AND_TTS_SAY_FOLLOW_GRAMMAR_TEXT",
                                                "wrong_word_heard": "START_SPEECHRECOG_FOLLOW_GRAMMAR"},
                                   remapping={'in_message_heard': 'out_message_heard'})

            def executeCommandAndGetNextTtsText(userdata):
                executeCommand()
                return follow_tts_texts[follow_grammar_name_index]

            smach.StateMachine.add('EXECUTE_COMMAND_AND_TTS_SAY_FOLLOW_GRAMMAR_TEXT',
                                   SpeakActionState(text_cb=executeCommandAndGetNextTtsText),
                                   transitions={succeeded: 'DISABLE_GRAMMAR'})

            smach.StateMachine.add('DISABLE_GRAMMAR',
                                   GrammarState(follow_grammar_names[follow_grammar_name_index], enabled=False),
                                   transitions={succeeded: 'CHANGE_TO_NEXT_GRAMMAR',
                                                preempted: "DISABLE_GRAMMAR_OUT",
                                                aborted: "DISABLE_GRAMMAR_OUT"})

            @smach.cb_interface(outcomes=['start_speech_again', succeeded, "out_grammar"])
            def setNextGrammarCallback(userdata):
                global follow_grammar_name_index
                follow_grammar_name_index += 1
                debugPrint("Changing to the next grammar and set of commands", 2)
                if follow_grammar_name_index == len(follow_grammar_names):
                    debugPrint("We have reached the last grammar and set of commands. Exitting from the test...", 2)
                    global bag
                    try:
                        bag.close()
                    finally:
                        debugPrint("Odometry bag closed.", 2)
                    return succeeded
                if follow_grammar_name_index == 1:
                    return "out_grammar"
                return 'start_speech_again'

            smach.StateMachine.add('CHANGE_TO_NEXT_GRAMMAR',
                                   CBState(setNextGrammarCallback),
                                   transitions={'start_speech_again': 'START_SPEECHRECOG_FOLLOW_GRAMMAR',
                                                "out_grammar": "START_SPEECHRECOG_FOLLOW_GRAMMAR_OUT",
                                                succeeded: succeeded})

            #FIXME
            smach.StateMachine.add('START_SPEECHRECOG_FOLLOW_GRAMMAR_OUT',
                                   GrammarState(follow_grammar_names[0], enabled=True),
                                   transitions={succeeded: 'SLEEP_STATE'})

            #FIXME
            smach.StateMachine.add('DISABLE_GRAMMAR_OUT',
                                   GrammarState(follow_grammar_names[0], enabled=False),
                                   transitions={succeeded: 'CHANGE_TO_NEXT_GRAMMAR',
                                                preempted: "CHANGE_TO_NEXT_GRAMMAR",
                                                aborted: "CHANGE_TO_NEXT_GRAMMAR"})
