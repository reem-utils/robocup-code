#! /usr/bin/env python

import roslib; roslib.load_manifest('start_deployer_controllers')
import rospy
import smach
import actionlib

import smach_ros
from std_msgs import *

from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.robot_controllers_activation import StopRobotControllers, StartRobotControllers


def main():
    rospy.init_node('sm_robot_controllers_activation')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:


        smach.StateMachine.add(
                    'START_CONTROLLERS',
                    StartRobotControllers(),
                    transitions = {succeeded: 'STOP_CONTROLLERS'})

        smach.StateMachine.add(
                    'STOP_CONTROLLERS',
                    StopRobotControllers(),
                    transitions = {succeeded: succeeded, aborted: aborted})


    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()

