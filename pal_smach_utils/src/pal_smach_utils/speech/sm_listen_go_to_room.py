#! /usr/bin/env python

import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from sound_action import SpeakActionState, SpeakActionFromPoolStateMachine
from grammar_state import GrammarState
from pal_interaction_msgs.msg import asrresult


class ListenGoToRoomStateMachine(smach.StateMachine):

    '''The question argument indicates the text that should be said to the referee.'''

    def __init__(self, question="Where should I go?", grammar_name='robocup/room'):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
            output_keys=['room_location', 'room_name'])

        with self:

            smach.StateMachine.add(
                'REQUEST_LOCATION',
                SpeakActionState(text=question),
                transitions={succeeded: 'ENABLE_GRAMMAR'})

            smach.StateMachine.add(
                'ENABLE_GRAMMAR',
                GrammarState(grammar_name, enabled=True),
                transitions={succeeded: 'LISTEN_TO_REFEREE'})

            def room_name_cb(userdata, message):
                goto_tags = [tag for tag in message.tags if tag.key == 'location']
                if goto_tags:
                    userdata.room_name = goto_tags[0].value
                    return succeeded
                return aborted

            smach.StateMachine.add(
                'LISTEN_TO_REFEREE',
                TopicReaderState(
                    topic_name='usersaid',
                    msg_type=asrresult,
                    timeout=20,
                    callback=room_name_cb,
                    output_keys=['room_name']),
                transitions={aborted: 'ASK_TO_REPEAT', succeeded: 'DISABLE_GRAMMAR'})

            repeat_pool = ["Pardon?", "Can you repeat the name, please?",
                           "I'm sorry I didn't understand you. Can you repeat that?",
                           "I didn't get it. Can you please repeat?"]
            smach.StateMachine.add('ASK_TO_REPEAT',
                                   SpeakActionFromPoolStateMachine(repeat_pool),
                                   transitions={succeeded: 'LISTEN_TO_REFEREE'})

            smach.StateMachine.add(
                'DISABLE_GRAMMAR',
                GrammarState('robocup/room', enabled=False),
                transitions={succeeded: 'MOVE_TO_REQUESTED_ROOM'})

            smach.StateMachine.add(
                'MOVE_TO_REQUESTED_ROOM',
                MoveToRoomStateMachine(),
                transitions={aborted: 'ENABLE_GRAMMAR'})
            # inputs: 'room_name', outputs: 'room_location'

# vim: expandtab ts=4 sw=4
