#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib; roslib.load_manifest('cloth_hanging')
import rospy
import smach
import smach_ros

from smach_ros import SimpleActionState
from smach_ros import ServiceState
from smach import CBState
from smach import Concurrence

import os

# generic libraries
import roslib.packages
from actionlib import *

# generic msgs
from actionlib.msg import *
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Empty

# pal & reem_at_iri imports
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from sb04_sonar.srv import SetStatus,SetStatusRequest
from pal_vision_msgs.srv import FaceTrackingStop, FaceTrackingStart
from pal_smach_utils.grasping.sm_reem_grasp_cloth import SMReemClothGraspStateMachine
from pal_smach_utils.grasping.st_reem_hand import OpenReemHand, CloseReemHand
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.speech.listen_general_command import RecogCommand
from pal_smach_utils.utils.timeout_container import SleepState

from pal_smach_utils.utils.robot_controllers_activation import StopRobotControllers,StartRobotControllers

from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction

# iri imports
from iri_common_smach.st_get_pcl import GetPCL
from iri_common_smach.homogeneous_product import homogeneous_product_pose_transform

from iri_common_smach.utils_msg import build_pose
from iri_common_smach.utils_msg import build_pose_stamped_msg
from iri_bow_object_detector.msg import *
from iri_wam_common_msgs.msg import *
from estirabot_msgs.srv import TransformPose

#import ipdb


#MOTION_FOLDER_PATH = roslib.packages.get_pkg_dir('cloth_hanging') + '/moves/'
robot = os.environ.get('PAL_ROBOT')
ros_master_uri = os.environ.get('ROS_MASTER_URI')
remotelly_executing = (ros_master_uri.rfind('localhost') == -1)
MOTION_FOLDER_PATH = ''

if remotelly_executing:
    MOTION_FOLDER_PATH = "/mnt_flash/robocup2013/reem_at_iri/state_machines/cloth_hanging/moves/"
else:
    MOTION_FOLDER_PATH = roslib.packages.get_pkg_dir('cloth_hanging') + '/moves/'



class SMClothHangingIntroPartStateMachine(smach.StateMachine):
    """
    Grabs a pointcloud and detects the neck of a cloth,
    then if it is found, a grasping action is executed
    in that point.

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

            # SALUDO
            intro_text = "Hello, my name is REEM! It seems that the cloth is bothering you, would you like me to hang it for you?"
            smach.StateMachine.add('INTRO',
                                   SpeakActionState(intro_text),
                                   transitions={succeeded: 'SLEEP_STATE1'})
            
            smach.StateMachine.add('SLEEP_STATE1',
                                   SleepState(6),
                                   transitions={succeeded: 'INTRO2',
                                                preempted: preempted})
            
            #smach.StateMachine.add('ENABLE_REEM_ALIVE',
                                        #ServiceState('/alive_engine/start', Empty),
                                        #transitions={succeeded: 'ENABLE_FACE_TRACKING'})
                                        
            #smach.StateMachine.add('ENABLE_FACE_TRACKING',
                                   #ServiceState('/personServer/faceTracking/start', FaceTrackingStart),
                                   #transitions={succeeded: 'HANG_CLOTHES_COMMAND',
                                                #preempted: 'HANG_CLOTHES_COMMAND',
                                                #failed: 'HANG_CLOTHES_COMMAND'})
            
            ### 2. Follow me command
            #HANG_CLOTHES_GRAMMAR_NAME = 'robocup/cloth_hanging'
            #smach.StateMachine.add('HANG_CLOTHES_COMMAND',
                                    #RecogCommand(HANG_CLOTHES_GRAMMAR_NAME, 'action', 'hang', False),
                                    #transitions={succeeded: 'INTRO',
                                                 #aborted: 'HANG_CLOTHES_COMMAND'})
            
            intro_text2 = "As you wish. Place the cloth in front of me, please."
            smach.StateMachine.add('INTRO2',
                                   SpeakActionState(intro_text2),
                                   transitions={succeeded: 'DISABLE_SONAR_SENSORS'})

            #smach.StateMachine.add('DISABLE_FACE_TRACKING',
                                   #ServiceState('/personServer/faceTracking/stop', FaceTrackingStop),
                                   #transitions={succeeded: 'DISABLE_SONAR_SENSORS'})

            smach.StateMachine.add('DISABLE_SONAR_SENSORS',
                                   ServiceState('/sb04/sonars/SetStatus', SetStatus, request=SetStatusRequest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0])),
                                   transitions={succeeded: 'succeeded',
                                                aborted: 'succeeded'})
                                                
            #smach.StateMachine.add('DISABLE_REEM_ALIVE',
                                        #ServiceState('/alive_engine/stop', Empty),
                                        #transitions={succeeded: succeeded})

                                        
            
