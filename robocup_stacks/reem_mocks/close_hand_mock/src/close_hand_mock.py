#! /usr/bin/env python

import roslib; roslib.load_manifest('close_hand_mock')
import rospy
import actionlib
import actionlib_msgs


from trajectory_msgs.msg import *
from control_msgs.msg import *

class ArmNavigationMockServer:

    def __init__(self, name):
        print 'Inside __init__'
        self.server = actionlib.SimpleActionServer(name, FollowJointTrajectoryAction, self._execute, False)
        print 'Starting __init__ Server'
        self.server.start()

    def _execute(self, goal):
        Res = FollowJointTrajectoryResult()
        Res.error_code = 0 # SUCCESSFUL
        self.server.set_succeeded(result=Res)    

if __name__ == '__main__':
    rospy.init_node('close_hand_mock')
    print '-----Creating Close_Hand_Mock_Server-------'
    right_hand_server = ArmNavigationMockServer('/right_hand_controller/follow_joint_trajectory')
    left_hand_server = ArmNavigationMockServer('left_hand_controller/follow_joint_trajectory')
    print 'Waiting for goals'
    rospy.spin()
