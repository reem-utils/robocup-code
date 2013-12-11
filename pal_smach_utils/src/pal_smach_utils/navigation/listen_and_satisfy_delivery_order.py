#! /usr/bin/env python
# -.- coding: utf-8 -.-
'''
LISTEN_AND_SATISFY_DELIVERY_ORDER.PY
'''


import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.speech.listen_delivery_order import ListenDeliveryOrder
from satisfy_delivery_order import SatisfyDeliveryOrder
from return_to_ordering_location import ReturnToOrderingLocation
from pal_smach_utils.utils.fases_set_up_restaurant import DeliverRestaurantFaseSetUp
from pal_smach_utils.grasping.initialise_and_close_grasp import CloseGraspPipelineSM

INTRO_FRASE = "Can I get you something?"
FINISH_FRASE = "I've finished my job boss, may I have a break?"


class ListenAndSatisfyDeliveryOrderSM(smach.StateMachine):

    '''
    This SM listens to a delivery order of three objects to deliver
    in a maximum of two diferent locations. All the 5 locations must be
    memorised as POIS before using this SM, otherwise it will just give
    an error message telling you that it didnt find the locations that werent
    memorised.
    '''

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted])

        with self:

            smach.StateMachine.add('DELIVER_ORDER_SET_UP',
                                   DeliverRestaurantFaseSetUp(),
                                   transitions={succeeded: 'PREPARED_TO_TAKE_ORDERS',
                                                preempted: preempted,
                                                aborted: aborted})

            smach.StateMachine.add('PREPARED_TO_TAKE_ORDERS',
                                   SpeakActionState(INTRO_FRASE),
                                   transitions={succeeded: 'LISTEN_DELIVERY_ORDER',
                                                preempted: preempted,
                                                aborted: aborted})

            smach.StateMachine.add('LISTEN_DELIVERY_ORDER',
                                   ListenDeliveryOrder(),
                                   transitions={succeeded: 'SATISFY_DELIVERY_ORDER',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'delivery_order_list_out': 'delivery_order_list'})

            smach.StateMachine.add('SATISFY_DELIVERY_ORDER',
                                   SatisfyDeliveryOrder(),
                                   transitions={succeeded: 'RETURN_TO_ORDERING_LOCATION',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_delivery_order_list': 'delivery_order_list'})

            smach.StateMachine.add('RETURN_TO_ORDERING_LOCATION',
                                   ReturnToOrderingLocation(),
                                   transitions={succeeded: 'FINISHED_ORDERS',
                                                preempted: preempted,
                                                aborted: aborted})

            smach.StateMachine.add('FINISHED_ORDERS',
                                   SpeakActionState(FINISH_FRASE),
                                   transitions={succeeded: "STOP_GRASP_PROTOCOL",
                                                preempted: preempted,
                                                aborted: aborted})

            smach.StateMachine.add("STOP_GRASP_PROTOCOL",
                                   CloseGraspPipelineSM(),
                                   transitions={succeeded: succeeded,
                                                aborted: aborted,
                                                preempted: preempted})

# vim: expandtab ts=4 sw=4
