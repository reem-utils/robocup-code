#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted, unknown_face
from pal_smach_utils.utils.recognize_face import RecognizeFaceStateMachine


def main():
    """Unit test for RecognizeFaceStateMachine. The robot will ask the person to
    look at his face, and try recognize the person."""

    rospy.init_node('test_recognize_face')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted, unknown_face])
    with sm:
        smach.StateMachine.add("TEST_RECOGNIZE_FACE",
            RecognizeFaceStateMachine()
            #transitions={succeeded: succeeded}
            )

    sis = smach_ros.IntrospectionServer(
        'test_recognize_face_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
