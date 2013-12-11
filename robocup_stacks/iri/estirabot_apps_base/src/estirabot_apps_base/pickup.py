#!/usr/bin/env python

import roslib; roslib.load_manifest('estirabot_apps')
import rospy
import smach
import smach_ros

from object_manipulation_msgs.msg import Grasp, PickupGoal

# Build a PickupGoal message from a given pose
def build_simple_pickup_goal(grasp_joint_state, pre_grasp_joint_state, fingers_config):
    # Adjust finger config un param server
    rospy.set_param('/estirabot/skills/grasp/fingers_configuration', fingers_config)

    g = Grasp()
    g.grasp_posture     = grasp_joint_state
    g.pre_grasp_posture = pre_grasp_joint_state

    r = PickupGoal()
    r.desired_grasps.append(g)

    return r
