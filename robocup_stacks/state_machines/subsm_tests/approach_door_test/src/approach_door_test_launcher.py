#! /usr/bin/env python

import roslib; roslib.load_manifest('approach_door_test')
import rospy
import smach
import smach_ros
import actionlib

from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.door_interaction.approach_door import *


def main():
    rospy.init_node('sm_approach_door_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add(
            'SM_approach_door',
            ApproachDoorStateMachine(),
            transitions={succeeded: succeeded, aborted: aborted})

         # NOT USING ANYTHING  MORE

    sis = smach_ros.IntrospectionServer(
        'sm_approach_door_test_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
