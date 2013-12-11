#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib; roslib.load_manifest('cloth_hanging')
import os
import rospy
import smach
import smach_ros

from smach_ros import SimpleActionState
from smach_ros import ServiceState

# generic libraries
import roslib.packages
from actionlib import *

# generic msgs
from actionlib.msg import *

# pal & reem_at_iri imports
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.grasping.st_reem_hand import OpenReemHand2, OpenReemHand, CloseReemHand
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

class SMClothHangingHangPartStateMachine(smach.StateMachine):
    """
    Suppousing that a piece of cloth is grasped and
     the robot is positioned in front of the hanger,
    hang the cloth in a hanger.

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

            # move arm
            filename = MOTION_FOLDER_PATH + "hang.xml"
            hang_motion_goal = MotionManagerGoal()
            hang_motion_goal.plan = False
            hang_motion_goal.filename = filename
            hang_motion_goal.checkSafety = False 
            hang_motion_goal.repeat = False
            hang_motion_action = SimpleActionState('/motion_manager', MotionManagerAction,
                                           goal=hang_motion_goal)
            smach.StateMachine.add('MOVE_TO_HANG_POSE', hang_motion_action,
                                   transitions={succeeded: 'RELEASE_OBJECT_FROM_HAND1', 
                                                preempted: preempted, 
                                                aborted: aborted})
            
            # release
            smach.StateMachine.add(
                    'RELEASE_OBJECT_FROM_HAND1',
                    OpenReemHand(),
                    transitions={succeeded: 'MOVE_TO_FINISH_POSE', preempted: preempted, aborted: aborted})
            
            smach.StateMachine.add(
                    'RELEASE_OBJECT_FROM_HAND2',
                    OpenReemHand2(),
                    transitions={succeeded: 'MOVE_TO_FINISH_POSE', preempted: preempted, aborted: aborted})
            
            #move arm home
            filename = MOTION_FOLDER_PATH + "final.xml"
            finish_motion_goal = MotionManagerGoal()
            finish_motion_goal.plan = False
            finish_motion_goal.filename = filename
            finish_motion_goal.checkSafety = False
            finish_motion_goal.repeat = False
            finish_motion_action = SimpleActionState('/motion_manager', MotionManagerAction,
                                           goal=finish_motion_goal)
            smach.StateMachine.add('MOVE_TO_FINISH_POSE', finish_motion_action,
                                   transitions={succeeded: 'RELEASE_OBJECT_FROM_HAND3', 
                                                preempted: preempted, 
                                                aborted: aborted})

            # close gripper
            #smach.StateMachine.add(
            #        'CLOSE_HAND',
            #        CloseReemHand(),
            #        transitions={succeeded: 'MOVE_TO_FINISH_POSE', preempted: preempted, aborted: aborted})
            
            smach.StateMachine.add(
                    'RELEASE_OBJECT_FROM_HAND3',
                    OpenReemHand2(),
                    transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})
            
                            



