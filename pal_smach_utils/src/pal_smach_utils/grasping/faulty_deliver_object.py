#! /usr/bin/env python
# -.- coding: utf-8 -.-
# vim: expandtab ts=4 sw=4

import roslib
roslib.load_manifest('pal_smach_utils')
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from st_reem_hand import OpenReemHand
from pal_smach_utils.utils.count_down_sm import CountDownSM

NUMBER_COUNT = 2


class FaultyDeliverObject(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded,
                                     preempted,
                                     aborted])

        with self:

            intro_text = "I'm quite in a hurry, so I will leave it here on the count of two."
            smach.StateMachine.add('FAULTY_DELIVERY_MESSAGE',
                                   SpeakActionState(intro_text),
                                   transitions={succeeded: 'COUNT_DOWN'})

            smach.StateMachine.add('COUNT_DOWN',
                                   CountDownSM(counting_number=NUMBER_COUNT),
                                   transitions={succeeded: 'OPEN_HAND',
                                                aborted: aborted})

            smach.StateMachine.add('OPEN_HAND',
                                   OpenReemHand(),
                                   transitions={succeeded: succeeded,
                                                aborted: aborted})
