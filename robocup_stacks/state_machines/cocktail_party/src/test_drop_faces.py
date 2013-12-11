#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.utils.drop_faces import DropAllFacesStateMachine


def main():
    """Unit test to test DropAllFacesStateMachine"""
    rospy.init_node('test_drop_faces')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:
        smach.StateMachine.add("TEST_DROP_FACES",
            DropAllFacesStateMachine()
            )

    sis = smach_ros.IntrospectionServer(
        'test_drop_faces_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
