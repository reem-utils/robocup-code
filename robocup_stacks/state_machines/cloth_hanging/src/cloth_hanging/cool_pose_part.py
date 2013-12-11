#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib; roslib.load_manifest('cloth_hanging')
import os
import rospy
import smach
import smach_ros

from smach_ros import SimpleActionState

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

# generic libraries
import roslib.packages

from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction


#MOTION_FOLDER_PATH = roslib.packages.get_pkg_dir('cloth_hanging') + '/moves/'
robot = os.environ.get('PAL_ROBOT')
ros_master_uri = os.environ.get('ROS_MASTER_URI')
remotelly_executing = (ros_master_uri.rfind('localhost') == -1)
MOTION_FOLDER_PATH = ''

if remotelly_executing:
    MOTION_FOLDER_PATH = "/mnt_flash/robocup2013/reem_at_iri/state_machines/cloth_hanging/moves/"
else:
    MOTION_FOLDER_PATH = roslib.packages.get_pkg_dir('cloth_hanging') + '/moves/'

class SMClothHangingCoolPosePartStateMachine(smach.StateMachine):
    """
    Suppousing that a piece of cloth is grasped,
    a sequence of fixed movements is executed to
    move to a natural position that is fine for
    grasping.

    Required parameters:
    No parameters

    Optional parameters:
    No optional parameters.

    No imput keys.
    No output keys.
    No io_keys.

    """
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:

            # move arms to cool pose
            filename = MOTION_FOLDER_PATH + "cool_cloth_pose.xml"
            cool_motion_goal = MotionManagerGoal()
            cool_motion_goal.plan = False
            cool_motion_goal.filename = filename
            cool_motion_goal.checkSafety = False
            cool_motion_goal.repeat = False
            cool_motion_action = SimpleActionState('/motion_manager', MotionManagerAction,
                                           goal=cool_motion_goal)
            smach.StateMachine.add('MOVE_TO_COOL_POSE', cool_motion_action,
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted})





