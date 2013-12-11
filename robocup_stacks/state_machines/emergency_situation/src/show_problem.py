#! /usr/bin/env python
# vim: expandtab ts=4 sw=4

import roslib
roslib.load_manifest('emergency_situation')
import rospy
import smach

from pal_smach_utils.speech.grammar_state import GrammarState
from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.speech.listen_general_command import RecogCommand,PrintUserData

YES_NO_GRAMMAR = 'robocup/yes_no'

class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded'], output_keys = ['room_name'])

    def execute(self, userdata):
        userdata.room_name = "kitchen"
        return 'succeeded' 

class ShowTheProblemStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, ['succeeded', 'preempted', 'aborted'])

        with self:

            smach.StateMachine.add(
                'INFORM_THE_PERSON',
                SpeakActionState("Excuse me. There is an emergency situation. Please follow me."),
                transitions = {'succeeded': 'dummy_state', 'aborted': 'INFORM_THE_PERSON'})

            smach.StateMachine.add(
                'dummy_state',
                DummyStateMachine(),
                transitions = {'succeeded':'MOVE_TO_KITCHEN'})

            smach.StateMachine.add(
                'MOVE_TO_KITCHEN',
                MoveToRoomStateMachine(),
                transitions = {'succeeded': 'CONFIRM_DANGER', 'aborted': 'MOVE_TO_KITCHEN'})

            smach.StateMachine.add(
                'CONFIRM_DANGER',
                SpeakActionState("is this a real danger?"),
                transitions = {'succeeded': 'DANGER_ANSWER', 'aborted': 'CONFIRM_DANGER'})

            smach.StateMachine.add(
                'DANGER_ANSWER',
                RecogCommand(YES_NO_GRAMMAR,'action','yes'),
                transitions = {'succeeded':'succeeded' , 'aborted':'aborted'})


# vim: expandtab ts=4 sw=4
