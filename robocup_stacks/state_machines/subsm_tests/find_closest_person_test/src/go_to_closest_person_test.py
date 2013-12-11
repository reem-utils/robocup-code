#!/usr/bin/env python

import roslib
roslib.load_manifest('find_closest_person_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.navigation.go_to_closest_person import GoToClosestPerson
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted


def main():
    rospy.init_node('find_and_go_to_closest_person_sm')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    # Open the container
    with sm:
        smach.StateMachine.add('GO_TO_CLOSEST_PERSON',
                            GoToClosestPerson(),
                            transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})

    sis = smach_ros.IntrospectionServer('find_and_go_to_closest_person_sm', sm, '/FIND_PERSON')
    sis.start()

    # Execute SMACH plan
    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
