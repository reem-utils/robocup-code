#! /usr/bin/env python
# -.- coding: utf-8 -.-
'''
SATISFY_DELIVERY_ORDER.PY
'''


import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.grasping.fetch_object import FetchObject
from pal_smach_utils.grasping.deliver_object import DeliverObject
from pal_smach_utils.utils.read_and_process_object_delivery_list import ReadAndPorcessObjectDeliveryList
#from pal_smach_utils.grasping.initialise_and_close_grasp import InitGraspPipelineSM, CloseGraspPipelineSM
from pal_smach_utils.grasping.faulty_deliver_object import FaultyDeliverObject


class SatisfyDeliveryOrder(smach.StateMachine):

    '''
    This SM That takes in a list of vectors, where for each object there is
    a location where to take that object.
    It basicaly take object 1 to location A, 2 to B and so on.
    Finishes when it has delivered all the objects in the list that are also in
    its POI memory banks. If a non memorised previously object is in the list
    it will just let you know that she doesnt have it memorised.

    @Input_keys: in_delivery_order_list-->  List of vector elements of two positions.
                                            Firstone is the object, secondone is the
                                            delivery location for that object.

    Behaviour:
    #. If it cant fetch the object, it will just skip to the nextone in the list.
    #.If it has the object but then it cant deliver it, it will deliver the object
    in the location where she fetched it.
    #. If it cant return the object to its original place, then the statemachine aborts.
    should be improved in some way like, trying to put it else where or just drop the
    object to the floor.
    '''

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted],
                                    input_keys=['in_delivery_order_list'])

        self.userdata.list_marker = 0

        with self:

            smach.StateMachine.add('READ_LIST_TO_KNOW_WHAT_TO_DO_NEXT',
                                   ReadAndPorcessObjectDeliveryList(),
                                   transitions={'fetch_and_deliver': 'FETCH_OBJECT',
                                                'finished_list': succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_list': 'in_delivery_order_list',
                                              'in_list_marker': 'list_marker',
                                              'object_name_out': 'object_name',
                                              'delivery_location_out': 'delivery_location',
                                              'list_marker_out': 'list_marker'})

            smach.StateMachine.add('FETCH_OBJECT',
                                   FetchObject(),
                                   transitions={'object_fetched_succesfully': 'DELIVER_OBJECT',
                                                'didnt_fetch_object': 'READ_LIST_TO_KNOW_WHAT_TO_DO_NEXT',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_fetch_object_name': 'object_name'})

            smach.StateMachine.add('DELIVER_OBJECT',
                                   DeliverObject(),
                                   transitions={'object_delivered_succesfully': 'READ_LIST_TO_KNOW_WHAT_TO_DO_NEXT',
                                                preempted: preempted,
                                                'didnt_deliver_object_total': 'COULDNT_DELIVER_OBJECT'},
                                   remapping={'in_delivery_location_name': 'delivery_location',
                                              'in_object_name': 'object_name'})

            #Here we come either because we couldnt get to the position or we couldnt leave the object.
            # TODO, we should improve it to return reem to the normal position.
            smach.StateMachine.add('COULDNT_DELIVER_OBJECT',
                                   FaultyDeliverObject(),
                                   transitions={succeeded: 'READ_LIST_TO_KNOW_WHAT_TO_DO_NEXT',
                                                preempted: preempted,
                                                aborted: aborted})
