#! /usr/bin/env python

import roslib; roslib.load_manifest('pal_smach_utils')
import roslib
import rospy
import smach
#import smach_ros
import actionlib
#from actionlib_msgs.msg import GoalStatus
from smach_ros import SimpleActionState, ServiceState

from std_msgs.msg import *
from arm_navigation_msgs.msg import *
from actionlib_msgs import *
from actionlib_msgs.msg import GoalStatus

#from motion_planning_msgs import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

try:
    from pr_msgs.msg import ObjectPoseList, ObjectPose
    from pr_msgs.srv import *
    from iri_moped_handler.srv import *
except ImportError:
    from object_recognition_mock.msg import ObjectPoseList, ObjectPose
    from object_recognition_mock.srv import *

from tf.transformations import quaternion_from_euler

from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped

# Future use of grasping
#from tabletop_object_detector.msg import TabletopDetectionResult
#from tabletop_collision_map_processing.srv import *

from object_manipulation_msgs.msg import *

from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.math_utils import *

from trajectory_msgs.msg import *
from control_msgs.msg import *


from std_srvs.srv import *




class CheckObject(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted],input_keys=['object_data'])

    def execute(self, userdata):
        if len(userdata.object_data.object_list) != 0:
            obj_name = userdata.object_data.object_list[0].name
            print "Object is: " + userdata.object_data.object_list[0].name
            print "In position: "
            print userdata.object_data.object_list[0].pose.position
            print "With orientation:"
            print userdata.object_data.object_list[0].pose.orientation
            return succeeded
        else:
            print "\nNo object!! Can't set a goal.\n"
            return aborted



    
    
class GraspTestStateMachine(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])
    
        with self:
            
            def moped_enable_cb(userdata, response):
                if response.correct != None:
                    rospy.loginfo("ENABLE_CLOSE_OBJECT_SEARCH response: " + str(response.correct))
                    return succeeded
                else:
                    return aborted
            
            smach.StateMachine.add(
                'ENABLE_CLOSE_OBJECT_SEARCH',
                ServiceState('/iri_moped_handler/enable', enable,
                    response_cb = moped_enable_cb,
                    #request_key = 'object_name',
                    request = True),
                transitions = {succeeded:'look_for_objects'})
            
            smach.StateMachine.add(
                'look_for_objects',
                TopicReaderState(
                                 topic_name='/iri_moped_handler/outputOPL',
                                 msg_type=ObjectPoseList,
                                 timeout=10),
                remapping= {'message' : 'object_data'},
                transitions = {succeeded: 'CHECK_IF_OBJECT_FOUND', aborted: 'look_for_objects'})
            

            
            smach.StateMachine.add(
            'CHECK_IF_OBJECT_FOUND',
            CheckObject(),
            transitions = {succeeded: 'DISABLE_CLOSE_OBJECT_SEARCH', aborted: 'look_for_objects'})
            



            def moped_disable_cb(userdata, response):
                if response.correct != None:
                    rospy.loginfo("DISABLE_CLOSE_OBJECT_SEARCH response: " + str(response.correct))
                    rospy.sleep(3.0)
                    return succeeded
                else:
                    return aborted


            smach.StateMachine.add(
                'DISABLE_CLOSE_OBJECT_SEARCH',
                ServiceState('/iri_moped_handler/enable', enable,
                    response_cb = moped_disable_cb,
                    #request_key = 'object_name',
                    request = False),
                transitions = {succeeded: 'REFRESH_COLLISION_MAP'})
                
            smach.StateMachine.add(
                'REFRESH_COLLISION_MAP',
                ServiceState('/refresh_collision_map/refresh', Empty),
                transitions = {succeeded:'N2_APPROACH_PREGRASPING_POSITION'})
                
            def arm_goal_cb(userdata, old_goal):
                print "Pre-grasping position callback:"
                print "Object position on original frame: " + userdata.object_data.header.frame_id + " is " 
                print userdata.object_data.object_list[0].pose
                goal_in_base_link = transform_pose (userdata.object_data.object_list[0].pose, "/kinect_depth_optical_frame" , "/base_link") #TODO: change orinigal frame by userdata.object_data.header.frame_id
                goal_in_base_link.orientation = Quaternion (0.5, -0.5, 0.5, -0.5)
                print "Object position on frame /base_link: %s" % goal_in_base_link
                print "Modifying position to be -19cm in x to pre-grasp (hand=14cm)."
                goal_in_base_link.position.x -= 0.19
                print "New position: %s" % goal_in_base_link
                arm_goal = get_arm_goal(goal_in_base_link, frame_id="/base_link") 
                return arm_goal
            
            
            
            smach.StateMachine.add(
            'N2_APPROACH_PREGRASPING_POSITION',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb = arm_goal_cb,
		        #result_cb = arm_result_cb,
                input_keys = ['object_data']),
            transitions = {succeeded: 'N2_APPROACH_FINAL_GRASPING_POSITION', aborted: aborted})     
                
           


            
            
            def arm_goal_cb(userdata, old_goal):
                print "Grasping position callback"
                print "Object position on original frame: " + userdata.object_data.header.frame_id + " is " 
                print userdata.object_data.object_list[0].pose
                goal_in_base_link = transform_pose (userdata.object_data.object_list[0].pose, "/kinect_depth_optical_frame" , "/base_link") #TODO: change orinigal frame by userdata.object_data.header.frame_id
                goal_in_base_link.orientation = Quaternion (0.5, -0.5, 0.5, -0.5)
                print "Object position on frame /base_link: %s" % goal_in_base_link
                print "Approaching to object in -14cm in x to grasp."
                goal_in_base_link.position.x -= 0.14
                print "New position: %s" % goal_in_base_link
                arm_goal = get_arm_goal(goal_in_base_link, frame_id="/base_link") 
                return arm_goal
            
            
            
            smach.StateMachine.add(
            'N2_APPROACH_FINAL_GRASPING_POSITION',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb = arm_goal_cb,
		        #result_cb = arm_result_cb,
                input_keys = ['object_data']),
            transitions = {succeeded: 'M4_grasp_object_close_hand', aborted: aborted}) 
            






            
            def grasp_arm_goal_cb(userdata, old_goal):
                grasp_msg = get_close_hand()
                return grasp_msg
            
            def grasp_arm_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED:
                    rospy.loginfo("Succeeded: result of right_hand_controller: " + str(result.error_code) )
                    return succeeded
                else:
                    rospy.loginfo("Other than succeded: result of right_hand_controller: " + str(result.error_code) )
                    return aborted

            
            smach.StateMachine.add(
            'M4_grasp_object_close_hand',
            SimpleActionState(
                '/right_hand_controller/follow_joint_trajectory',
                FollowJointTrajectoryAction,
                goal_cb = grasp_arm_goal_cb,
                result_cb = grasp_arm_result_cb,
                input_keys = ['object_data']),
            transitions = {succeeded: 'Arm_to_safe_travelling_position', aborted: aborted}) 


            def arm_goal_cb(userdata, old_goal):
                arm_goal = get_arm_goal_for_arm_down()
                return arm_goal

            
            smach.StateMachine.add(
            'Arm_to_safe_travelling_position',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb = arm_goal_cb,
		        #result_cb = arm_result_cb,
                input_keys = ['object_data']),
            transitions = {succeeded: 'Release_object_open_hand', aborted: aborted}) 
            
            def grasp_arm_goal_cb(userdata, old_goal):
                grasp_msg = get_open_hand()
                return grasp_msg
            
            def grasp_arm_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED:
                    rospy.loginfo("Succeeded: result of right_hand_controller: " + str(result.error_code) )
                    return succeeded
                else:
                    rospy.loginfo("Other than succeded: result of right_hand_controller: " + str(result.error_code) )
                    return aborted

            
            smach.StateMachine.add(
            'Release_object_open_hand',
            SimpleActionState(
                '/right_hand_controller/follow_joint_trajectory',
                FollowJointTrajectoryAction,
                goal_cb = grasp_arm_goal_cb,
                result_cb = grasp_arm_result_cb,
                input_keys = ['object_data']),
            transitions = {succeeded: succeeded, aborted: aborted}) 

# vim: expandtab ts=4 sw=4
