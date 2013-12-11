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

from pal_smach_utils.utils.debug import debugPrint

STOP_GRAMMAR_NAME = rospy.get_param('/restaurant/stop_grammar_name')

LISTEN_COMMAND_TIMEOUT = 3.0


class ListenCommandForFollowMeAgain(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])
        with self:

            smach.StateMachine.add('ENABLE_FOLLOW_ME_STOP_GRAMMAR',
                                   GrammarState(STOP_GRAMMAR_NAME, enabled=True),
                                   transitions={succeeded: 'LISTEN_FOLLOW_ME_STOP_COMMAND'})

            smach.StateMachine.add('SLEEP_STATE_BEFORE_LISTEN_AGAIN',
                                   SleepState(2.0/10.0),
                                   transitions={succeeded: 'LISTEN_FOLLOW_ME_STOP_COMMAND',
                                                preempted: 'LISTEN_FOLLOW_ME_STOP_COMMAND'})

            def listenFollowMeStartCommandCallback(userdata, message):
                debugPrint("The message listened is " + str(message), 3)
                grammar_tags = [tag for tag in message.tags if tag.key == 'action']
                if grammar_tags and (grammar_tags[0].value == "stopwait" or grammar_tags[0].value == "stop"):
                    return succeeded
                return aborted

            smach.StateMachine.add('LISTEN_FOLLOW_ME_STOP_COMMAND',
                                   TopicReaderState(topic_name='/usersaid', msg_type=asrresult, timeout=LISTEN_COMMAND_TIMEOUT,
                                   outcomes=[succeeded, preempted, aborted], callback=listenFollowMeStartCommandCallback),
                                   transitions={succeeded: "DISABLE_FOLLOW_ME_STOP_GRAMMAR",
                                                preempted: "SLEEP_STATE_BEFORE_LISTEN_AGAIN",
                                                aborted: "SLEEP_STATE_BEFORE_LISTEN_AGAIN"})

            smach.StateMachine.add('DISABLE_FOLLOW_ME_STOP_GRAMMAR',
                                   GrammarState(STOP_GRAMMAR_NAME, enabled=False),
                                   transitions={succeeded: succeeded})
