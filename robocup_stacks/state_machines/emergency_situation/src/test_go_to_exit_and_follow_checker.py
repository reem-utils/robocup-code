#! /usr/bin/env python
# -.- coding: utf-8 -.-
import roslib
roslib.load_manifest("emergency_situation")
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from go_to_exit_and_follow_checker import GoExitAndFollowChecker


def main():
    rospy.init_node('test_go_to_exit_and_follow_checker')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:
        sm.userdata.room_name = "exit"
        smach.StateMachine.add("GO_EXIT_AND_FOLLOW_CHECKER", GoExitAndFollowChecker())

    sis = smach_ros.IntrospectionServer(
        'test_go_to_exit_and_follow_checker_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
