#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib; roslib.load_manifest('cloth_hanging')
import rospy
import smach
import smach_ros

from smach_ros import SimpleActionState
from smach_ros import ServiceState
from smach import CBState

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
from pal_smach_utils.grasping.sm_reem_grasp_cloth import SMReemClothGraspStateMachine
from pal_smach_utils.grasping.st_reem_hand import OpenReemHand, CloseReemHand
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.play_sound_sm import PlaySoundOnceState, StopSoundState
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


@smach.cb_interface(input_keys=['grasp_point'],
                    output_keys=['grasp_pose_st', 'target_frame'],
                    outcomes=['done'])
def build_grasp_pose_from_point_cb(ud):
    p                 = PoseStamped()
    p.pose            = build_pose(ud.grasp_point.x, ud.grasp_point.y, ud.grasp_point.z, 0, 1, 0, 0)
    p.header.frame_id = '/head_mount_xtion_rgb_optical_frame'
    p.header.stamp = rospy.Time.now()
    pub = rospy.Publisher('/debug/grasp_point', PoseStamped, None, False, True)
    rospy.sleep(1) # wait for subscribers
    pub.publish(p)
    ud.grasp_pose_st = p

    ud.target_frame = '/base_link'

    return 'done'

def grasping_point_goal_cb(userdata, goal):
    goal = GetGraspingPointGoal()
    goal.pointcloud = userdata.pcl_RGB
    return goal


class TransformPoseStamped(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded','preempted','aborted'],
                    input_keys=['sm_grasp_pose','sm_target_frame'],
                    output_keys=['target_pose'])
        self.service_topic = '/skills/bow_detector/iri_transform_pose/transform_pose'

    def execute(self, userdata):
        rospy.logdebug('Executing state TransformPoseStamped')
        rospy.wait_for_service(self.service_topic)
        try:
            get_target_pose = rospy.ServiceProxy(self.service_topic, TransformPose)
            resp = get_target_pose(userdata.sm_grasp_pose, userdata.sm_target_frame)

            userdata.target_pose = resp.target_pose_st
            return 'succeeded'

        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
            return 'aborted'


class SMGraspStateMachine(smach.StateMachine):
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
            # desactivate controllers
            smach.StateMachine.add(
                        'DeactivateControllersInit',
                        StopRobotControllers(head=True, left=True, right=True),
                        transitions={succeeded: 'MOVE_TO_NO_COLLISION_POSE', preempted: preempted, aborted: aborted})

            # move arms to cool pose
            filename = MOTION_FOLDER_PATH + "interact_head_up.xml"
            cool_motion_goal = MotionManagerGoal()
            cool_motion_goal.plan = False
            cool_motion_goal.filename = filename
            cool_motion_goal.checkSafety = False
            cool_motion_goal.repeat = False
            cool_motion_action = SimpleActionState('/motion_manager', MotionManagerAction,
                                           goal=cool_motion_goal)
            smach.StateMachine.add('MOVE_TO_NO_COLLISION_POSE', cool_motion_action,
                                   transitions={succeeded: 'GetPCL',
                                                preempted: preempted,
                                                aborted: succeeded})
            
            
            smach.StateMachine.add('GetPCL', GetPCL('/head_mount_xtion/depth_registered/points'),
                    transitions={'success':'GetGraspingPointAction',
                            'fail':aborted},
                    remapping={'pcl_RGB':'pcl_RGB'})

            smach.StateMachine.add('GetGraspingPointAction',
                    SimpleActionState('/skills/bow_detector/bow_object_detector/get_grasping_point',
                            GetGraspingPointAction,
                            #goal_slots=['pcl_RGB'],
                            goal_cb=grasping_point_goal_cb,
                            input_keys=['pcl_RGB'],
                            result_slots=['grasping_point']),
                            #server_wait_timeout=rospy.Duration(10.0)),
                    transitions={'succeeded':'ConvertGraspPoint',
                            'preempted':preempted,
                            'aborted':aborted},
                    remapping={'grasping_point':'sm_grasp_point'})


            # prepare pose
            smach.StateMachine.add('ConvertGraspPoint',
                                CBState(build_grasp_pose_from_point_cb),
                    transitions={'done':'TransformPoseStamped'},
                    remapping={'grasp_point' : 'sm_grasp_point',
                            'grasp_pose_st' : 'sm_grasp_pose',
                            'target_frame' : 'sm_target_frame'})


            # transform pose ¿needed?
            smach.StateMachine.add('TransformPoseStamped',
                        TransformPoseStamped(),
                    transitions={'succeeded':'ActivateControllers',
                            'preempted':preempted,
                            'aborted':aborted},
                    remapping={'target_pose':'target_pose_stamped'})

            # activate controllers
            smach.StateMachine.add(
                        'ActivateControllers',
                        StartRobotControllers(head=False, left=False, right=True),
                        transitions={succeeded: 'ReemGraspStateMachine', preempted: preempted, aborted: aborted})
            # grasp
            smach.StateMachine.add(
                        'ReemGraspStateMachine',
                        SMReemClothGraspStateMachine(),
                        transitions={'succeeded': 'DeactivateControllers', 'preempted': preempted, 'aborted': aborted})

            # desactivate controllers
            smach.StateMachine.add(
                        'DeactivateControllers',
                        StopRobotControllers(head=False, left=False, right=True),
                        transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})


class SMExplanationInitStateMachine(smach.StateMachine):
    def __init__(self, retry=False):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:
            description_text1=""
            description_text2=""
            description_text3=""
            if not retry:
                description_text1 = "I will grasp your cloth."
                description_text2 = "Ugg. . .  It is an ugly polo. . .  let me help you choose a cool shirt next time."
                description_text3 = "Using my Kinect camera I will analyze the cloth. . . I will select a good grasping point in the collar."
            else:
                description_text1 = "I can't reach the cloth. Could you move it closer?"
                description_text2 = "Ok, I will try to grasp it again."
                description_text3 = "Using my Kinect camera I will analyze the cloth. . . I will select a good grasping point in the collar."
            
            smach.StateMachine.add(
                        'DESCRIPTION_SPEECH1',
                        SpeakActionState(description_text1),
                        transitions={succeeded: 'SLEEP_STATE1', 
                                     preempted: preempted, 
                                     aborted: aborted})
            
            smach.StateMachine.add('SLEEP_STATE1',
                                   SleepState(2),
                                   transitions={succeeded: 'DESCRIPTION_SPEECH2',
                                                preempted: preempted})
                                                
            smach.StateMachine.add(
                        'DESCRIPTION_SPEECH2',
                        SpeakActionState(description_text2),
                        transitions={succeeded: 'SLEEP_STATE2', 
                                     preempted: preempted, 
                                     aborted: aborted})
                                                
            smach.StateMachine.add('SLEEP_STATE2',
                                   SleepState(2),
                                   transitions={succeeded: 'DESCRIPTION_SPEECH3',
                                                preempted: preempted})
                                                
            smach.StateMachine.add(
                        'DESCRIPTION_SPEECH3',
                        SpeakActionState(description_text3),
                        transitions={succeeded: 'succeeded', 
                                     preempted: preempted, 
                                     aborted: aborted})
            
            # WARNING ignoring it
            #filename = MOTION_FOLDER_PATH + "../music/cantina.mp3"
            ## filename = ""
            #self.userdata.sound_file_path = filename
            #smach.StateMachine.add(
                        #'MUSIC_START',
                        #PlaySoundOnceState(),
                        #transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})
            

class SMConcurrentGraspExplanationInit(smach.Concurrence):
    def __init__(self, retry = False):
        smach.Concurrence.__init__(self, outcomes = [succeeded, aborted,preempted],
                 default_outcome = succeeded,
                 outcome_map = {'succeeded':{'CLOTH_GRASPING':'succeeded'},
                                'preempted':{'CLOTH_GRASPING':'preempted'},
                                'aborted':{'CLOTH_GRASPING':'aborted'}})
                                
        with self:
            smach.Concurrence.add('EXPLANATION', 
                                  SMExplanationInitStateMachine(retry))
            smach.Concurrence.add('CLOTH_GRASPING',
                                   SMGraspStateMachine())

class SMClothHangingGraspAndExplanationPartStateMachine(smach.StateMachine):
    def __init__(self, retry = False):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:
            # desactivate controllers
            smach.StateMachine.add(
                        'ClothAndExplanationInit',
                        SMConcurrentGraspExplanationInit(retry),
                        transitions={succeeded: 'succeeded', preempted: preempted, aborted: aborted})
            
            # WARNING ignoring it
            #smach.StateMachine.add('STOP_SOUND',
                        #StopSoundState(),
                        #transitions={succeeded: succeeded,
                                    #preempted: preempted,
                                    #aborted: aborted},
                        #remapping={'sound_file_path': 'sound_file_path'})
    
                  
