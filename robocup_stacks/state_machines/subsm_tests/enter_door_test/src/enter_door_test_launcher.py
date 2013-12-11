#! /usr/bin/env python

import roslib; roslib.load_manifest('enter_door_test')
import rospy
import smach
import smach_ros
import actionlib

from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.door_interaction.enter_door import *


def main():
    rospy.init_node('sm_enter_door_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add(
            'SM_enter_door',
            EnterDoorStateMachine(),
            transitions={succeeded: succeeded, aborted: aborted})

         # NOT USING ANYTHING  MORE

    sis = smach_ros.IntrospectionServer(
        'sm_enter_door_test_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
