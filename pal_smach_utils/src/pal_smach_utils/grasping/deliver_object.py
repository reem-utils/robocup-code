#! /usr/bin/env python
# -.- coding: utf-8 -.-
# vim: expandtab ts=4 sw=4

import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.speech.sound_action import SpeakActionState
from release_object_sm import ReleaseObjectSM
#from sm_grasp_from_tray import GraspFromTrayStateMachine

OBJECT_DELIVERED_FRASE = "I've delivered this to the "
DIDNT_FIND_DELIVERY_LOCATION_FRASE = "I couldn't find the "
ALTERNATIVE_LOCATION_FRASE = " so I'll leave this where I found it in the first place. "


class DeliverObject(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    ['object_delivered_succesfully',
                                     'didnt_deliver_object_total',
                                     preempted,
                                     aborted],
                                    input_keys=['in_delivery_location_name', 'in_object_name'])

        with self:

            smach.StateMachine.add('MOVE_TO_OBJECT',
                                   MoveToRoomStateMachine(),
                                   transitions={succeeded: 'RELEASE_OBJECT',
                                                preempted: preempted,
                                                aborted: 'DIDNT_DELIVER_OBJECT'},
                                   remapping={'room_name': 'in_delivery_location_name'})

            smach.StateMachine.add('RELEASE_OBJECT',
                                   ReleaseObjectSM(),
                                   transitions={'object_delivered_succesfully': 'object_delivered_succesfully',
                                                'didnt_deliver_object': 'DIDNT_DELIVER_OBJECT',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'object_name': 'in_object_name'})

            def say_text_cb(userdata):
                text_say = DIDNT_FIND_DELIVERY_LOCATION_FRASE + userdata.in_delivery_location_name + ALTERNATIVE_LOCATION_FRASE
                return text_say
            smach.StateMachine.add('DIDNT_DELIVER_OBJECT',
                                   SpeakActionState(text_cb=say_text_cb, input_keys=['in_delivery_location_name']),
                                   transitions={succeeded: 'didnt_deliver_object_total'})
