#! /usr/bin/env python
# -.- coding: utf-8 -.-


import roslib
roslib.load_manifest('listen_delivery_order_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.speech.listen_delivery_order import ListenDeliveryOrder
from pal_smach_utils.utils.stop_till_press_enter_and_read_key_board import StopTillPressEnterAndReadKeyBoard

DEBUGGING = True


def main():
    rospy.init_node('sm_listen_delivery_order_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Hello, my name is REEM! What do you want me to do today?"
        smach.StateMachine.add('INTRO',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'LISTEN_DELIVERY_ORDER'})

        smach.StateMachine.add('LISTEN_DELIVERY_ORDER',
                               ListenDeliveryOrder(),
                               transitions={succeeded: 'PAUSE_STATEMACHINE',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'delivery_order_list_out': 'delivery_order_list'})

        smach.StateMachine.add('PAUSE_STATEMACHINE',
                               StopTillPressEnterAndReadKeyBoard(debugging=DEBUGGING),
                               transitions={succeeded: 'BYE',
                                            preempted: preempted,
                                            aborted: aborted},
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
