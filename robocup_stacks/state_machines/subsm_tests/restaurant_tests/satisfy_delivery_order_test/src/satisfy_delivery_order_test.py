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
from pal_smach_utils.grasping.initialise_and_close_grasp import InitGraspPipelineSM

DEBUGGING = True
OBJECT_NAME_A = 'coke'
#OBJECT_NAME_A = 'coconut'
OBJECT_NAME_B = 'juice'
OBJECT_NAME_C = 'cookies'
LOCATION_NAME1 = 'table 1'
LOCATION_NAME2 = 'table 3'


class HeadDummyState(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['message1'])

    def execute(self, userdata):

        order_list = []
        order_list.append([OBJECT_NAME_A, LOCATION_NAME1])
        order_list.append([OBJECT_NAME_B, LOCATION_NAME1])
        order_list.append([OBJECT_NAME_C, LOCATION_NAME2])
        userdata.message1 = order_list

        print "DUMMY SATE ENDED"
        return succeeded



def main():
    rospy.init_node('sm_satisfy_delivery_order')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Let's satisfy restaurant orders?"
        smach.StateMachine.add('INTRO',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'DUMMY_STATE_GENERATE_LIST'})

        smach.StateMachine.add('DUMMY_STATE_GENERATE_LIST',
                               HeadDummyState(),
                               transitions={succeeded: 'START_GRASP_PROTOCOL',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'message1': 'delivery_order_list'})

        smach.StateMachine.add("START_GRASP_PROTOCOL",
                               InitGraspPipelineSM(),
                               transitions={succeeded: "SATISFY_DELIVERY_ORDER",
                                            aborted: aborted,
                                            preempted: aborted})

        smach.StateMachine.add('SATISFY_DELIVERY_ORDER',
                               SatisfyDeliveryOrder(),
                               transitions={succeeded: 'PAUSE_STATEMACHINE',
                                            preempted: preempted,
                                            aborted: 'PAUSE_STATEMACHINE'},
                               remapping={'in_delivery_order_list': 'delivery_order_list'})

        smach.StateMachine.add('PAUSE_STATEMACHINE',
                               StopTillPressEnterAndReadKeyBoard(debugging=DEBUGGING),
                               transitions={succeeded: 'INTRO',
                                            preempted: preempted,
                                            aborted: 'BYE'},
                               remapping={'keyboard_input_out': 'keyboard_input'})

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
