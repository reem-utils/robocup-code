#! /usr/bin/env python

import roslib; roslib.load_manifest('general_purpose')
import rospy
import smach
import smach_ros
import actionlib
from smach_ros import SimpleActionState

from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.recognize_face import RecognizeFaceStateMachine
from pal_smach_utils.utils.find_and_recognize_people import FindAndRecognizePeopleStateMachine

def main():
    rospy.init_node('general_purpose_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        # ...

        sis = smach_ros.IntrospectionServer(
        'general_purpose_introspection', sm, '/SM_ROOT')
        sis.start()

        sm.execute()

        rospy.spin()
        sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
