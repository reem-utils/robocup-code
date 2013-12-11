#! /usr/bin/env python
# vim: expandtab ts=4 sw=4
### FOLLOW_ME.PY ###
import roslib
roslib.load_manifest('follow_me')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.learn_person import LearnPerson

from pal_smach_utils.speech.sound_action import SpeakActionState

from pal_smach_utils.speech.listen_general_command import RecogCommand
from pal_smach_utils.navigation.follow_and_stop import FollowAndStop

FOLLOW_GRAMMAR_NAME = 'robocup/followme'

START_FOLLOW_FRASE = "Ok, I'll follow you wherever you want. Please come a bit closer if you are too far, then Please stay still while I learn how you are."
LEARNED_PERSON_FRASE = "Let's go buttercup."


#Main
class FollowMe(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:

            intro_text = "Hello, my name is REEM! What do you want me to do today?"
            smach.StateMachine.add('INTRO',
                                   SpeakActionState(intro_text),
                                   transitions={succeeded: 'FOLLOW_ME_COMMAND'})

            ### 2. Follow me command
            smach.StateMachine.add('FOLLOW_ME_COMMAND',
                                   RecogCommand(FOLLOW_GRAMMAR_NAME, 'action', 'follow_me'),
                                   transitions={succeeded: 'START_FOLLOWING_COME_CLOSER',
                                                aborted: 'FOLLOW_ME_COMMAND'})

            start_text = START_FOLLOW_FRASE
            smach.StateMachine.add('START_FOLLOWING_COME_CLOSER',
                                   SpeakActionState(start_text),
                                   transitions={succeeded: 'SM_LEARN_PERSON'})

            smach.StateMachine.add('SM_LEARN_PERSON',
                                   LearnPerson(),
                                   transitions={succeeded: 'FOLLOW_ME',
                                                aborted: aborted},
                                   remapping={'PT_Id_of_person': 'out_targetId',
                                              'LP_all_person_data': 'out_personTrackingData'})

            learned_text = LEARNED_PERSON_FRASE
            smach.StateMachine.add('START_FOLLOWING_COME_CLOSER',
                                   SpeakActionState(learned_text),
                                   transitions={succeeded: 'SM_LEARN_PERSON'})

            smach.StateMachine.add('FOLLOW_ME',
                                   FollowAndStop(),
                                   remapping={'in_targetId': 'out_targetId',
                                              'in_personTrackingData': 'out_personTrackingData'},
                                   transitions={succeeded: succeeded})
