#!/usr/bin/env python
import roslib; roslib.load_manifest('pal_smach_utils')
import sys
import rospy
import actionlib
from std_srvs.srv import Empty, EmptyResponse
from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction

def hand_initialize(name):
    rospy.wait_for_service(name)
    try:
        hand_init = rospy.ServiceProxy(name, Empty)
        resp1 = hand_init()
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":

    rospy.init_node('calibrator')
    client = actionlib.SimpleActionClient('/motion_manager', MotionManagerAction)
    client.wait_for_server()
    goal = MotionManagerGoal()
    goal.filename = '/mnt_flash/etc/control/robot/reemh3/motion/start_reem.xml'
    goal.checkSafety = True
    goal.repeat = False
    goal.priority = 0 
    goal.queueTimeout = 0 
    client.send_goal(goal)
    client.wait_for_result()

    hand_initialize ('/rightHandDeviceInitializerStart')
    hand_initialize ('/leftHandDeviceInitializerStart')
