#! /usr/bin/env python
# -.- coding: utf-8 -.-
import roslib
roslib.load_manifest("emergency_situation")
import smach
import rospy
import smach_ros

from locate_a_person import FindAPersonStateMachine
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted


def main():
    rospy.init_node('test_find_a_person')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:

        sm.userdata.location_list = []  # rospy.get_param("/mmap/poi/submap_0")

        smach.StateMachine.add(
            "TEST_FIND_A_PERSON",
            FindAPersonStateMachine())
        #input_keys=["location_list"]

    sis = smach_ros.IntrospectionServer(
        'test_find_a_person_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
