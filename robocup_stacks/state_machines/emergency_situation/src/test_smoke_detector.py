#! /usr/bin/env python
# -.- coding: utf-8 -.-
import roslib
roslib.load_manifest("emergency_situation")
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from detect_fire import DetectFireOrSmokeStateMachine


def main():
    rospy.init_node('test_smoke')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:
        smach.StateMachine.add('TEST_SMOKE_DETECTION',
            DetectFireOrSmokeStateMachine()
            )

    sis = smach_ros.IntrospectionServer(
        'test_smoke', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
