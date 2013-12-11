#! /usr/bin/env python
# vim: expandtab ts=4 sw=4
### FOLOW_OPERATOR.PY ###

import rospy
import smach

from pal_smach_utils.utils.timeout_container import SleepState

from pal_smach_utils.speech.listen_general_command import PrintUserData
from pal_smach_utils.speech.sm_hear_voice_commands_and_pois import SM_MemorisePois
from pal_smach_utils.speech.grammar_state import GrammarState
from pal_smach_utils.speech.listen_poi_name import ListenPoiName
from pal_smach_utils.speech.did_you_say_yes_or_no_sm import HearingConfirmationSM


from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

#TODO Put this in the common, but for some reason I couldnt manage :(
POI_GRAMMAR_NAME = 'robocup/poi_grammar'

personsId_not_found = 'personsId_not_found'
memorise_poi = 'memorise_poi'
stop_mapping = 'stop_mapping'
no_plausible_person_found = 'no_plausible_person_found'
lost_person = 'lost_person'

#These are all the vocabs that in the POI_GRAMMAR
STOPWAIT_VOCAB = rospy.get_param('params_follow_me/stopwait_vocab', 'stopwait')
POI_GRAMMAR_VOCAB = rospy.get_param('params_follow_me/poi_grammar_vocab', ['POI1', 'POI2', 'POI3', 'POI4', STOPWAIT_VOCAB])


class ListenCommandForRestaurant(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])
        with self:

            smach.StateMachine.add('START_SPEECHRECOG_POI_GRAMMAR',
                                   GrammarState(POI_GRAMMAR_NAME, enabled=True),
                                   transitions={succeeded: 'SLEEP_STATE'})

            smach.StateMachine.add('SLEEP_STATE',
                                   SleepState(0.5),
                                   transitions={succeeded: 'LISTEN_POI',
                                                preempted: preempted})
            """
            smach.StateMachine.add('LISTEN_POI',
                                   ListenPoiName(),
                                   transitions={preempted: 'STOP_CONFIRMATION',
                                                succeeded: 'POI_CONFIRMATION',
                                                aborted: 'SLEEP_STATE'},
                                   remapping={'poi_name': 'poi_name',
                                              'what_you_heard_out': 'what_you_heard_out'})
            """
            smach.StateMachine.add('LISTEN_POI',
                                   ListenPoiName(),
                                   transitions={preempted: 'STOP_CONFIRMATION',
                                                succeeded: 'POI_CONFIRMATION',
                                                aborted: 'SLEEP_STATE'},
                                   remapping={'poi_name': 'poi_name',
                                              'orientation_side': 'orientation_side',
                                              'what_you_heard_out': 'what_you_heard_out'})

            smach.StateMachine.add('POI_CONFIRMATION',
                                   HearingConfirmationSM(grammar_to_reset_when_finished=POI_GRAMMAR_NAME),
                                   transitions={'correct_word_heard': 'PRINT_POI',
                                                'wrong_word_heard': 'SLEEP_STATE',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_message_heard': 'what_you_heard_out'})

            smach.StateMachine.add('STOP_CONFIRMATION',
                                   HearingConfirmationSM(grammar_to_reset_when_finished=POI_GRAMMAR_NAME),
                                   transitions={'correct_word_heard': 'DISABLE_GRAMMAR_WITH_POI',
                                                'wrong_word_heard': 'SLEEP_STATE',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_message_heard': 'what_you_heard_out'})

            smach.StateMachine.add('PRINT_POI',
                                   PrintUserData("I'm printing NOW in the Follow Operator :::"),
                                   transitions={succeeded: 'SM_FO_MEMORISE_POI',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'userSaidData': 'poi_name'})

            smach.StateMachine.add('SM_FO_MEMORISE_POI',
                                   SM_MemorisePois(),
                                   transitions={succeeded: 'SLEEP_STATE',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'FO_POI_name': 'poi_name',
                                              'FO_orientation_side': 'orientation_side'})

            smach.StateMachine.add('DISABLE_GRAMMAR_WITH_POI',
                                   GrammarState(POI_GRAMMAR_NAME, enabled=False),
                                   transitions={succeeded: succeeded})
