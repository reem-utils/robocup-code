#! /usr/bin/env python
# -.- coding: utf-8 -.-
'''
RETURN_TO_ORDERING_LOCATION.PY
'''


import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from move_to_room import MoveToRoomStateMachine
from memorise_ordering_location import InitOrderingLocationName

ORDERING_FRASE = "Wow, that was easy, wasn't it?"
ORDERING_LOCATION_NAME = "ordering_location"


class ReturnToOrderingLocation(smach.StateMachine):

    '''
    Makes the Reem return to a previously memorised location called ordering_location.
    '''

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted])

        with self:

            smach.StateMachine.add('RETURNING_TO_ORDERING_LOCATION',
                                   SpeakActionState(ORDERING_FRASE),
                                   transitions={succeeded: 'INIT_ORDERING_LOCATION_NAME'})

            smach.StateMachine.add('INIT_ORDERING_LOCATION_NAME',
                                   InitOrderingLocationName(),
                                   transitions={succeeded: 'MOVE_TO_OBJECT'},
                                   remapping={'ordering_name_out': 'ordering_name'})

            smach.StateMachine.add('MOVE_TO_OBJECT',
                                   MoveToRoomStateMachine(),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'room_name': 'ordering_name'})

# vim: expandtab ts=4 sw=4
