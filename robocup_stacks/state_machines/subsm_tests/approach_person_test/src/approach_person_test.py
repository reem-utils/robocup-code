#! /usr/bin/env python

import roslib
roslib.load_manifest('approach_person_test')
import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.go_to_closest_person import ApproachPerson


def main():
    rospy.init_node('sm_approach_person_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:
        smach.StateMachine.add(
            'SM_approach_person',
            ApproachPerson(),
            transitions={succeeded: succeeded, aborted: aborted, preempted: preempted})

    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
