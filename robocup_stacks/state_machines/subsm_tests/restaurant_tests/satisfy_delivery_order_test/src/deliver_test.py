#! /usr/bin/env python
# -.- coding: utf-8 -.-


import roslib
roslib.load_manifest('satisfy_delivery_order_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.navigation.satisfy_delivery_order import SatisfyDeliveryOrder
from pal_smach_utils.utils.stop_till_press_enter_and_read_key_board import StopTillPressEnterAndReadKeyBoard
from pal_smach_utils.grasping.deliver_object import DeliverObject
from pal_smach_utils.grasping.initialise_and_close_grasp import InitGraspPipelineSM, CloseGraspPipelineSM

OBJECT_NAME_A = 'coke'
LOCATION_NAME2 = 'table three'


class HeadDummyState(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['message1','message2'])

    def execute(self, userdata):

        userdata.message1 = OBJECT_NAME_A
        userdata.message2 = LOCATION_NAME2

        print "DUMMY SATE ENDED"
        return succeeded



def main():
    rospy.init_node('sm_deliver_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Let's deliver something"
        smach.StateMachine.add('INTRO',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'DUMMY_STATE_GENERATE_OBJECT_NAME_AND_LOCATION'})


        smach.StateMachine.add('DUMMY_STATE_GENERATE_OBJECT_NAME_AND_LOCATION',
                               HeadDummyState(),
                               transitions={succeeded: 'START_GRASP_PROTOCOL',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'message1': 'object_name',
                                          'message2': 'delivery_location'})

        smach.StateMachine.add("START_GRASP_PROTOCOL",
                                   InitGraspPipelineSM(),
                                   transitions={succeeded: "DELIVER_OBJECT",
                                                aborted: aborted,
                                                preempted: aborted})
        smach.StateMachine.add('DELIVER_OBJECT',
                                   DeliverObject(),
                                   transitions={'object_delivered_succesfully': 'STOP_GRASP_PROTOCOL',
                                                preempted: preempted,
                                                'didnt_deliver_object': 'COULDNT_DELIVER_OBJECT'},
                                   remapping={'in_delivery_location_name': 'delivery_location',
                                              'in_object_name': 'object_name'})

        smach.StateMachine.add('COULDNT_DELIVER_OBJECT',
                                   DeliverObject(),
                                   transitions={'object_delivered_succesfully': 'STOP_GRASP_PROTOCOL',
                                                preempted: preempted,
                                                'didnt_deliver_object': aborted},
                                   remapping={'in_delivery_location_name': 'object_name'})

        smach.StateMachine.add("STOP_GRASP_PROTOCOL",
                                   CloseGraspPipelineSM(),
                                   transitions={succeeded: succeeded,
                                                aborted: aborted,
                                                preempted: preempted})

        smach.StateMachine.add('BYE',
                               SpeakActionState("It was a pleasure to serve you."))

    sis = smach_ros.IntrospectionServer(
        'restaurant_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
