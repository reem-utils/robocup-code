#! /usr/bin/env python
# -.- coding: utf-8 -.-
import roslib
roslib.load_manifest("emergency_situation")
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from find_and_go_to_person import FindAndGoToPersonStateMachine


def main():
    rospy.init_node('test_go_to_person')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:
        sm.userdata.location_list=[]
        smach.StateMachine.add("GO_EXIT_AND_FOLLOW_CHECKER", FindAndGoToPersonStateMachine())

    sis = smach_ros.IntrospectionServer(
        'test_go_to_person', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
