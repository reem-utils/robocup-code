#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib; roslib.load_manifest('cloth_hanging')
import rospy
import smach
import smach_ros

from pprint import pprint

from smach_ros import SimpleActionState
from smach_ros import ServiceState
from smach import CBState

# generic libraries
import roslib.packages
from actionlib import *

# generic msgs
from actionlib.msg import *
from geometry_msgs.msg import PoseStamped

# pal & reem_at_iri imports
from pal_smach_utils.grasping.sm_reem_grasp_cloth import SMReemClothGraspStateMachine
from pal_smach_utils.grasping.st_reem_hand import OpenReemHand, CloseReemHand
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine

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


# TODO add to map
#HANGER_NAME = "hanger"
HANGER_NAME = "charger"

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


def main():
    rospy.init_node('sm_pick_up_cloths')
    
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['FINISH_OK','FAILED_VISION','FAILED_MOVE_ARM','FAILED_MOVE_BASE'])

    # Open the container
    with sm:
        # Add states to the container
        #smach.StateMachine.add('GetPCL', GetPCL('/camera/rgb/points'),
        
        # TODO SALUDO
        
        # TODO RETRYING
        
        smach.StateMachine.add('GetPCL', GetPCL('/head_mount_xtion/depth_registered/points'),
                transitions={'success':'GetGraspingPointAction', 
                        'fail':'FAILED_VISION'},
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
                        'preempted':'FAILED_VISION',
                        'aborted':'FAILED_VISION'},
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
                transitions={'succeeded':'ReemGraspStateMachine', 
                        'preempted':'FAILED_VISION',
                        'aborted':'FAILED_VISION'},
                remapping={'target_pose':'target_pose_stamped'})
        
        # grasp
        smach.StateMachine.add(
                    'ReemGraspStateMachine',
                    SMReemClothGraspStateMachine(),
                    transitions={'succeeded': 'MOVE_TO_COOL_POSE', 'preempted': 'FAILED_MOVE_ARM', 'aborted': 'GetPCL'})
        
        # move arms to cool pose
        filename = MOTION_FOLDER_PATH + "cool_cloth_pose.xml"
        cool_motion_goal = MotionManagerGoal()
        cool_motion_goal.plan = True
        cool_motion_goal.filename = filename
        cool_motion_goal.checkSafety = True
        cool_motion_goal.repeat = False
        cool_motion_action = SimpleActionState('/motion_manager', MotionManagerAction,
                                       goal=cool_motion_goal)
        smach.StateMachine.add('MOVE_TO_COOL_POSE', cool_motion_action,
                               transitions={'succeeded': 'MOVE_TO_HANGER',
                                            'preempted': 'FAILED_MOVE_ARM',
                                            'aborted': 'FAILED_MOVE_ARM'})
        
        # move to hanger
        sm.userdata.hanger = HANGER_NAME
        smach.StateMachine.add('MOVE_TO_HANGER',
                               MoveToRoomStateMachine(announcement=None),
                               transitions={'succeeded': 'MOVE_TO_HANG_POSE',
                                            'preempted': 'FAILED_MOVE_BASE',
                                            'aborted': 'FAILED_MOVE_BASE'},
                               remapping={'room_name': 'hanger'})
        
        # move arm
        filename = MOTION_FOLDER_PATH + "hang.xml"
        hang_motion_goal = MotionManagerGoal()
        hang_motion_goal.plan = True
        hang_motion_goal.filename = filename
        hang_motion_goal.checkSafety = True
        hang_motion_goal.repeat = False
        hang_motion_action = SimpleActionState('/motion_manager', MotionManagerAction,
                                       goal=hang_motion_goal)
        smach.StateMachine.add('MOVE_TO_HANG_POSE', hang_motion_action,
                               transitions={'succeeded': 'RELEASE_OBJECT_FROM_HAND',
                                            'preempted': 'FAILED_MOVE_ARM',
                                            'aborted': 'FAILED_MOVE_ARM'})
        
        # release
        smach.StateMachine.add(
                'RELEASE_OBJECT_FROM_HAND',
                OpenReemHand(),
                transitions={'succeeded': 'CLOSE_HAND', 'preempted': 'FAILED_MOVE_ARM', 'aborted': 'FAILED_MOVE_ARM'})
                
        # close gripper
        smach.StateMachine.add(
                'CLOSE_HAND',
                CloseReemHand(),
                transitions={'succeeded': 'MOVE_TO_FINISH_POSE', 'preempted': 'FAILED_MOVE_ARM', 'aborted': 'FAILED_MOVE_ARM'})
                        
        #move arm home
        filename = MOTION_FOLDER_PATH + "final.xml"
        finish_motion_goal = MotionManagerGoal()
        finish_motion_goal.plan = True
        finish_motion_goal.filename = filename
        finish_motion_goal.checkSafety = True
        finish_motion_goal.repeat = False
        finish_motion_action = SimpleActionState('/motion_manager', MotionManagerAction,
                                       goal=finish_motion_goal)
        smach.StateMachine.add('MOVE_TO_FINISH_POSE', finish_motion_action,
                               transitions={'succeeded': 'FINISH_OK',
                                            'preempted': 'FAILED_MOVE_ARM',
                                            'aborted': 'FAILED_MOVE_ARM'})
        
        # finish
        

    # Execute SMACH plan
    outcome = sm.execute()



if __name__ == '__main__':
    main()
