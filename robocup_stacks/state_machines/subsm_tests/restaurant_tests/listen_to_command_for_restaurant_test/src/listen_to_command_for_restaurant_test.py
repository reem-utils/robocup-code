#! /usr/bin/env python
# -.- coding: utf-8 -.-


import roslib
roslib.load_manifest('listen_to_command_for_restaurant_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.navigation.listen_command_for_restaurant import ListenCommandForRestaurant


def main():
    rospy.init_node('sm_listen_to_command_for_restaurant_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Hello sweety. Shall we proceed with the listen commands for restaurant test?"
        smach.StateMachine.add('INTRO',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'LISTEN_DELIVERY_ORDER'})

        smach.StateMachine.add('LISTEN_DELIVERY_ORDER',
                               ListenCommandForRestaurant(),
                               transitions={succeeded: 'BYE',
                                            preempted: preempted,
                                            aborted: aborted})

        smach.StateMachine.add('BYE',
                               SpeakActionState("We should repeat this another time. It was fun !"))

    sis = smach_ros.IntrospectionServer(
        'restaurant_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
