#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.utils.gesture_recognition import GestureRecognition


def main():
    """Unit test to GestureRecognition. The kinect should be connected and the
    gestureRecognitionStart.sh should be previously executed."""

    rospy.init_node('test_gesture_recognition')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:
        smach.StateMachine.add("TEST_GESTURE_RECOGNITION",
            GestureRecognition(),
            transitions={succeeded: "TEST_GESTURE_RECOGNITION", aborted: "TEST_GESTURE_RECOGNITION"}
            )

    sis = smach_ros.IntrospectionServer(
        'test_gesture_recognition_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
