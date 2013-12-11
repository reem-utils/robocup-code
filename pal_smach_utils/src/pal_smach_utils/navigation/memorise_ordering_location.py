#! /usr/bin/env python
# -.- coding: utf-8 -.-
'''
MEMORISE_ORDERING_LOCATION.PY
'''
import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.speech.sm_hear_voice_commands_and_pois import SM_MemorisePois

MEMORISED_ORDERING_LOCATION_FRASE = "So here is where I will take the delivery orders? Nice place."
ORDERING_LOCATION_NAME = "ordering_location"
ORDERING_ORIENTATION_NAME = "front"


class InitOrderingLocationName(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded],
                             output_keys=['ordering_name_out',
                                          'ordering_orientation_out'])

    def execute(self, userdata):

        userdata.ordering_name_out = ORDERING_LOCATION_NAME
        userdata.ordering_orientation_out = ORDERING_ORIENTATION_NAME

        return succeeded


class MemoriseOrderingLocation(smach.StateMachine):

    '''
    Memorised the current position as the ordering location.
    '''

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted])

        with self:

            smach.StateMachine.add('INIT_ORDERING_LOCATION_NAME',
                                   InitOrderingLocationName(),
                                   transitions={succeeded: 'SM_FO_MEMORISE_POI'},
                                   remapping={'ordering_name_out': 'ordering_name',
                                              'ordering_orientation_out': 'ordering_orientation'})

            smach.StateMachine.add('SM_FO_MEMORISE_POI',
                                   SM_MemorisePois(),
                                   transitions={succeeded: 'DONE_MEMORISING_ORDERING_LOCATION',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'FO_POI_name': 'ordering_name',
                                              'FO_orientation_side': 'ordering_orientation'})

            smach.StateMachine.add('DONE_MEMORISING_ORDERING_LOCATION',
                                   SpeakActionState(MEMORISED_ORDERING_LOCATION_FRASE),
                                   transitions={succeeded: succeeded})

# vim: expandtab ts=4 sw=4
