#! /usr/bin/env python

import roslib; roslib.load_manifest('look_at_door_test')
import rospy
import smach
import smach_ros
import actionlib

from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.door_interaction.look_at_handle import *


def main():
    rospy.init_node('sm_look_at_door_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add(
            'SM_look_at_door',
            LookAtHandleStateMachine(),
            transitions={succeeded: succeeded, aborted: aborted})

         # NOT USING ANYTHING  MORE

    sis = smach_ros.IntrospectionServer(
        'sm_look_at_door_test_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
