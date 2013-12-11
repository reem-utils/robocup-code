#! /usr/bin/env python
# -.- coding: utf-8 -.-


import roslib
roslib.load_manifest('listen_and_satisfy_delivery_order_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.navigation.listen_and_satisfy_delivery_order import ListenAndSatisfyDeliveryOrderSM


def main():
    rospy.init_node('sm_listen_and_satisfy_delivery_order_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Hello, my name is REEM! What do you want me to do today?"
        smach.StateMachine.add('INTRO',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'LISTEN_AND_SATISFY_DELIVERY_ORDER'})

        smach.StateMachine.add('LISTEN_AND_SATISFY_DELIVERY_ORDER',
                               ListenAndSatisfyDeliveryOrderSM(),
                               transitions={succeeded: 'BYE',
                                            preempted: preempted,
                                            aborted: aborted})

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
