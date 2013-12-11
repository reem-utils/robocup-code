# This is SM give
#! /usr/bin/env python

import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import actionlib

from smach_ros import SimpleActionState, ServiceState


from std_msgs.msg import *
from arm_navigation_msgs.msg import *
from actionlib_msgs import *
from actionlib_msgs.msg import GoalStatus

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from coord_translator.srv import *

try:
    from pr_msgs.msg import ObjectPoseList, ObjectPose 
except ImportError:
    from pr_msgs.msg import ObjectPoseList, ObjectPose

from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.utils.global_common import *
from pal_smach_utils.speech.grammar_state import GrammarState
from pal_smach_utils.utils.math_utils import *
from pal_smach_utils.speech.sound_action import SpeakActionState

from trajectory_msgs.msg import *
from control_msgs.msg import *



class GiveStateMachine(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
        input_keys=['object_location', 'object_name', 'pose_object'])
    
        with self:
            @smach.cb_interface(input_keys=['object_name'], output_keys=['object_location_3d'])
            def loc_response_cb(userdata, response):
                if response.exists:
                    #pose.orientation = Quaternion(
                        #*quaternion_from_euler(0, 0, response.coordinates.z))
                    userdata.object_location_3d = response.arm_coordinates
                    return succeeded
                else:
                    userdata.object_location_3d = None
                    return aborted

    	    def loc_request_cb(userdata, request):
        		req = ObjectTranslatorRequest()
        		req.objname = userdata.object_name
        		print "Asking coord_translator for " + req.objname
        		return req

            smach.StateMachine.add(
                'GETTING_3D_OBJECT_POSITION',
                ServiceState('object_translator', ObjectTranslator,
                    response_cb = loc_response_cb,
                    #request_key = 'object_name',
		            request_cb = loc_request_cb,
		            input_keys = ['object_name'],
                    output_keys = ['object_location_3d']),
                    transitions = {succeeded:'ANNOUNCE_APROXIMATION_TO_OBJ_LOCATION'})


            smach.StateMachine.add(
                'ANNOUNCE_APROXIMATION_TO_OBJ_LOCATION',
                SpeakActionState(text="Im getting near the object supposed location."),
                transitions = {succeeded:'approximate_arm_to_object_location'})  

  
            
            
            def arm_goal_cb(userdata, old_goal):
                print "Preparing MoveArmGoal() on SM_give"
                arm_goal = MoveArmGoal()
                
                objposlist  = ObjectPoseList()
                objposlist.object_list = [None]
                # Pose with arm in front of the robot
                objposlist.object_list[0] = ObjectPose()
                objposlist.object_list[0].pose.position.x = 0.30
                objposlist.object_list[0].pose.position.y = -0.30
                objposlist.object_list[0].pose.position.z = 1.13
                objposlist.object_list[0].pose.orientation.x = 0.5
                objposlist.object_list[0].pose.orientation.y = -0.5
                objposlist.object_list[0].pose.orientation.z = 0.5
                objposlist.object_list[0].pose.orientation.w = -0.5
                
                
                # Reading from the object_location
                #objposlist.object_list[0] = ObjectPose()
                #objposlist.object_list[0].pose.position = userdata.object_location_3d.position
                #rospy.loginfo("I'm attempting to move the arm to position:" + str(userdata.object_location_3d.position.x) + " " + str(userdata.object_location_3d.position.y) + " " + str(userdata.object_location_3d.position.z)  )
                #objposlist.object_list[0].pose.orientation = userdata.pose_object.object_list[0].pose.orientation
                #rospy.loginfo("I'm attempting to move the arm to orientation: " + str(userdata.pose_object.object_list[0].pose.orientation.x) + " " + str(userdata.pose_object.object_list[0].pose.orientation.y) + " " + str(userdata.pose_object.object_list[0].pose.orientation.z) + " " +  str(userdata.pose_object.object_list[0].pose.orientation.w))
                
                
                
                ######## Message formed from the example message: http://pastebin.com/zcrWcaih ###########
                
                arm_goal.planner_service_name = "ompl_planning/plan_kinematic_path"
                
                #Planning Scene diff: empty!
                
                #motion_plan_request
                arm_goal.motion_plan_request = MotionPlanRequest()
                # workspace_parameters, empty until we get to goal_constaints
                arm_goal.motion_plan_request.workspace_parameters = WorkspaceParameters()
                #arm_goal.motion_plan_request.workspace_parameters.workspace_region_pose.pose.position = objposlist.object_list[0].pose.position
                #arm_goal.motion_plan_request.workspace_parameters.workspace_region_pose.pose.orientation = objposlist.object_list[0].pose.orientation 			#userdata.object_data.object_list[0].pose.position
                
                
                arm_goal.motion_plan_request.goal_constraints.position_constraints =  [None] * 1
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0] = PositionConstraint()
                
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].header = Header()
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].header.stamp = rospy.Time().now()
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].header.frame_id = "/base_link" #FIXME: This is ALWAYS GONNA BE BASE_LINK??? #userdata.object_location.header.frame_id
                #userdata.object_data.header.frame_id#"torso_lift_link"

                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].link_name = "arm_right_7_link"
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].position.x = objposlist.object_list[0].pose.position.x
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].position.y = objposlist.object_list[0].pose.position.y
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].position.z = objposlist.object_list[0].pose.position.z
                
                
                # Not used O.o
                #		arm_goal.motion_plan_request.goal_constraints.absolute_position_tolerance.x = 0.1;
                #		arm_goal.motion_plan_request.goal_constraints.absolute_position_tolerance.y = 0.1;
                #		arm_goal.motion_plan_request.goal_constraints.absolute_position_tolerance.z = 0.1;
                  
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.type = 1 # 1 should be box
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions = [None] * 3
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions[0] = 0.040000000000000001
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions[1] = 0.040000000000000001
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions[2] = 0.040000000000000001
                
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_orientation.w = 1.0
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].weight = 1.0
                
                
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints = [None] * 1
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0] = OrientationConstraint()
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].header = Header()
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].header.stamp = rospy.Time().now()
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].header.frame_id = "/base_link" 
                #userdata.object_data.header.frame_id
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].link_name = "arm_right_7_link"
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].orientation.x = objposlist.object_list[0].pose.orientation.x
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].orientation.y = objposlist.object_list[0].pose.orientation.y
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].orientation.z = objposlist.object_list[0].pose.orientation.z
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].orientation.w = objposlist.object_list[0].pose.orientation.w 
                  
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].absolute_roll_tolerance = 0.02
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].absolute_pitch_tolerance = 0.02
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].absolute_yaw_tolerance = 0.02
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].weight = 1.0
                
                
                
                
                arm_goal.motion_plan_request.planner_id = ""
                arm_goal.motion_plan_request.group_name = "right_arm_torso"
                arm_goal.motion_plan_request.num_planning_attempts = 1
                arm_goal.motion_plan_request.allowed_planning_time = rospy.Duration(10)
                arm_goal.motion_plan_request.expected_path_duration = rospy.Duration(0)
                arm_goal.motion_plan_request.expected_path_dt = rospy.Duration(0)
                
                
                
                print "After this print the message is sent!"
                return arm_goal
            
            
            
            smach.StateMachine.add(
            'approximate_arm_to_object_location',
            SimpleActionState(
                '/move_right_arm_torso',
                MoveArmAction,
                goal_cb = arm_goal_cb,
                input_keys = ['object_location_3d', 'object_location', 'pose_object']),
            transitions = {succeeded: 'ANNOUNCE_DELIVER_OBJ'}) 



            smach.StateMachine.add(
                'ANNOUNCE_DELIVER_OBJ',
                SpeakActionState(text="Im delivering the object."),
                transitions = {succeeded:'deliver_object'})   
            
            
            
  
            
            
            def deliver_arm_goal_cb(userdata, old_goal):
                grasp_msg = FollowJointTrajectoryGoal()
                grasp_msg.trajectory = JointTrajectory()
                # grasp_msg.trajectory.header <- its empty because:
                # the timestamp is used to set a delay to the start of the movement
                # an empty value means to start as we receive the message.
                grasp_msg.trajectory.joint_names = [None]*1
                grasp_msg.trajectory.joint_names[0] = 'hand_right_joint'
                grasp_msg.trajectory.points = [None]*1
                grasp_msg.trajectory.points[0] = JointTrajectoryPoint()
                # grasp_msg.trajectory.points[0].positions goes from 0 to 1.something where 0 is fully open hand
                
                
                # Set hand to open  [0.0], [0.0], [0.0], [1, 0] open
                grasp_msg.trajectory.points[0].positions = [None]*1
                grasp_msg.trajectory.points[0].positions[0] = 0.0

                grasp_msg.trajectory.points[0].velocities = [None]*1
                grasp_msg.trajectory.points[0].velocities[0] = 0.0
                
                grasp_msg.trajectory.points[0].accelerations = [None]*1
                grasp_msg.trajectory.points[0].accelerations[0] = 0.0
                
                grasp_msg.trajectory.points[0].time_from_start = rospy.Duration(1)
                
		# You can find more movements in sm_grasp


                return grasp_msg
            
            def deliver_arm_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED:
                    rospy.loginfo("Succeeded: result of right_hand_controller: " + str(result.error_code) )
                    return succeeded
                else:
                    rospy.loginfo("Other than succeeded: result of right_hand_controller: " + str(result.error_code) )
                    return aborted
            
            smach.StateMachine.add(
            'deliver_object',
            SimpleActionState(
                '/right_hand_controller/follow_joint_trajectory',
                FollowJointTrajectoryAction,
                goal_cb = deliver_arm_goal_cb,
                result_cb = deliver_arm_result_cb,),
                transitions = {succeeded: 'Arm_to_safe_position', aborted: aborted})


            def arm_goal_cb(userdata, old_goal):
                print "Preparing MoveArmGoal() to move the arm to a safe arm position"
                arm_goal = MoveArmGoal()
                
                objposlist  = ObjectPoseList()
                objposlist.object_list = [None]
                # Pose with arm down
                objposlist.object_list[0] = ObjectPose()
                objposlist.object_list[0].pose.position.x = -0.14
                objposlist.object_list[0].pose.position.y = -0.27
                objposlist.object_list[0].pose.position.z = 0.8
                objposlist.object_list[0].pose.orientation.x = 0.78
                objposlist.object_list[0].pose.orientation.y = -0.615
                objposlist.object_list[0].pose.orientation.z = 0.081
                objposlist.object_list[0].pose.orientation.w = -0.075
                
                
                # Reading from the object_pose
                #objposlist.object_list[0] = ObjectPose()
                #objposlist.object_list[0].pose.position = userdata.object_data.object_list[0].pose.position
                #objposlist.object_list[0].pose.orientation = userdata.object_data.object_list[0].pose.orientation
                
                
                # Pose with arm down (taken from the robot) Error! reference from /map not /base_link
                #objposlist.object_list[0] = ObjectPose()
                #objposlist.object_list[0].pose.position.x = 0.130007
                #objposlist.object_list[0].pose.position.y = -0.198804
                #objposlist.object_list[0].pose.position.z = 0.900355
                
                #objposlist.object_list[0].pose.orientation.x = 0.87292
                #objposlist.object_list[0].pose.orientation.y = -0.244933
                #objposlist.object_list[0].pose.orientation.z = 0.127606
                #objposlist.object_list[0].pose.orientation.w = -0.402163
                
                
                
                
                ######## Message formed from the example message: http://pastebin.com/zcrWcaih ###########
                
                arm_goal.planner_service_name = "ompl_planning/plan_kinematic_path"
                
                #Planning Scene diff: empty!
                
                #motion_plan_request
                arm_goal.motion_plan_request = MotionPlanRequest()
                # workspace_parameters, empty until we get to goal_constaints
                arm_goal.motion_plan_request.workspace_parameters = WorkspaceParameters()
                #arm_goal.motion_plan_request.workspace_parameters.workspace_region_pose.pose.position = objposlist.object_list[0].pose.position
                #arm_goal.motion_plan_request.workspace_parameters.workspace_region_pose.pose.orientation = objposlist.object_list[0].pose.orientation 			#userdata.object_data.object_list[0].pose.position
                
                
                arm_goal.motion_plan_request.goal_constraints.position_constraints =  [None] * 1
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0] = PositionConstraint()
                
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].header = Header()
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].header.stamp = rospy.Time().now()
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].header.frame_id = "/base_link" #FIXME: This is ALWAYS GONNA BE BASE_LINK??? #userdata.object_location.header.frame_id
                #userdata.object_data.header.frame_id#"torso_lift_link"
                  
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].link_name = "arm_right_7_link"
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].position.x = objposlist.object_list[0].pose.position.x
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].position.y = objposlist.object_list[0].pose.position.y
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].position.z = objposlist.object_list[0].pose.position.z
                
                
                     
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.type = 1 # 1 should be box
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions = [None] * 3
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions[0] = 0.040000000000000001
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions[1] = 0.040000000000000001
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions[2] = 0.040000000000000001
                
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].constraint_region_orientation.w = 1.0
                arm_goal.motion_plan_request.goal_constraints.position_constraints[0].weight = 1.0
                
                
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints = [None] * 1
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0] = OrientationConstraint()
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].header = Header()
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].header.stamp = rospy.Time().now()
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].header.frame_id = "/base_link" 
                #userdata.object_data.header.frame_id
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].link_name = "arm_right_7_link"
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].orientation.x = objposlist.object_list[0].pose.orientation.x
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].orientation.y = objposlist.object_list[0].pose.orientation.y
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].orientation.z = objposlist.object_list[0].pose.orientation.z
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].orientation.w = objposlist.object_list[0].pose.orientation.w 
                  
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].absolute_roll_tolerance = 0.02
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].absolute_pitch_tolerance = 0.02
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].absolute_yaw_tolerance = 0.02
                arm_goal.motion_plan_request.goal_constraints.orientation_constraints[0].weight = 1.0
                
                
                
                
                arm_goal.motion_plan_request.planner_id = ""
                arm_goal.motion_plan_request.group_name = "right_arm_torso"
                arm_goal.motion_plan_request.num_planning_attempts = 1
                arm_goal.motion_plan_request.allowed_planning_time = rospy.Duration(10)
                arm_goal.motion_plan_request.expected_path_duration = rospy.Duration(0)
                arm_goal.motion_plan_request.expected_path_dt = rospy.Duration(0)
                
                
                
                
                
                
                print "After this print the message is sent!"
                return arm_goal
            
            
            
            smach.StateMachine.add(
            'Arm_to_safe_position',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb = arm_goal_cb,
		        #result_cb = arm_result_cb,
                input_keys = ['object_data']),
                transitions = {succeeded: succeeded, aborted: aborted}) 
            
            
# Having the pose of the operator
# Add state approximate arm to the operator

# Add "wait for release" state

# Add M6 deliver the object state

# -- here we left the object -- 

# vim: expandtab ts=4 sw=4
