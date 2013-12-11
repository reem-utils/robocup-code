#! /usr/bin/env python
# -.- coding: utf-8 -.-
import roslib
roslib.load_manifest("emergency_situation")
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from call_fire_department import CallFireDepartmentState


def main():
    rospy.init_node('test_call_fire_department')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:

        sm.userdata.location_list = [[5.4, 5.6], [3, 5], [9, 9]]
        sm.userdata.location_of_fire = [2, 2]

        smach.StateMachine.add("TEST_CALL_FIRE_DEPARTMENT",
            CallFireDepartmentState())

    sis = smach_ros.IntrospectionServer(
        'test_call_fire_department_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
