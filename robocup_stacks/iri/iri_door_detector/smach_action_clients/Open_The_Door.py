#!/usr/bin/env python

import roslib; roslib.load_manifest('iri_door_detector')
import rospy
import smach
import smach_ros
import tf
import iri_door_detector.msg
from geometry_msgs.msg import Point, Pose, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from pr2_controllers_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from arm_navigation_msgs.msg import *
from smach_ros import SimpleActionState
from smach import CBState
from sensor_msgs.msg import JointState

def main():
    rospy.init_node('smach_example_state_machine')

    sm = smach.StateMachine(outcomes=['succeeded','aborted','preempted'])
    with sm:

	#---smach callbacks

	def init_left_arm_cb(userdata, goal):
		point = JointTrajectoryPoint()
		point.time_from_start = rospy.Duration.from_sec(2)
		point.positions = [ -0.5, 0.1, -0.1, 0.6109, 0.0, 0.0, 0.0 ]
		point.velocities = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
		joint_goal = JointTrajectoryGoal()
		joint_goal.trajectory.joint_names = ['arm_left_1_joint', 'arm_left_2_joint', 'arm_left_3_joint', 
						     'arm_left_4_joint', 'arm_left_5_joint', 'arm_left_6_joint', 
						     'arm_left_7_joint']
		joint_goal.trajectory.header.stamp = rospy.get_rostime()
		joint_goal.trajectory.points.append(point)
		return joint_goal

	def init_right_arm_torso_cb(userdata,goal):
		point = JointTrajectoryPoint()
		point.time_from_start = rospy.Duration.from_sec(2)
		point.positions = [ 0.0, 0.0, -0.5, 0.1, -0.1, 0.6109, 0.0, 0.0, 0.0 ]
		point.velocities = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
		joint_goal = JointTrajectoryGoal()
		joint_goal.trajectory.joint_names = ['torso_1_joint', 'torso_2_joint', 'arm_right_1_joint',
		                                     'arm_right_2_joint', 'arm_right_3_joint', 'arm_right_4_joint',
		                                     'arm_right_5_joint', 'arm_right_6_joint', 'arm_right_7_joint']
		joint_goal.trajectory.header.stamp = rospy.get_rostime()
		joint_goal.trajectory.points.append(point)
		return joint_goal

	def rise_left_arm_cb(userdata, goal):
		point = JointTrajectoryPoint()
		point.time_from_start = rospy.Duration.from_sec(2)
		point.positions = [ 0.8, 0.1, -0.2, 1.8, -1.5, -1.0, 0.0 ]
		point.velocities = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
		joint_goal = JointTrajectoryGoal()
		joint_goal.trajectory.joint_names = ['arm_left_1_joint', 'arm_left_2_joint', 'arm_left_3_joint', 
						     'arm_left_4_joint', 'arm_left_5_joint', 'arm_left_6_joint', 
						     'arm_left_7_joint']
		joint_goal.trajectory.header.stamp = rospy.get_rostime()
		joint_goal.trajectory.points.append(point)
		return joint_goal

	def rise_right_arm_torso_cb(userdata,goal):
		point = JointTrajectoryPoint()
		point.time_from_start = rospy.Duration.from_sec(2)
		point.positions = [ 0.0, 0.0, 0.8, 0.1, -0.2, 1.8, -1.5, -1.0, 0.0 ]
		point.velocities = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
		joint_goal = JointTrajectoryGoal()
		joint_goal.trajectory.joint_names = ['torso_1_joint', 'torso_2_joint', 'arm_right_1_joint',
		                                     'arm_right_2_joint', 'arm_right_3_joint', 'arm_right_4_joint',
		                                     'arm_right_5_joint', 'arm_right_6_joint', 'arm_right_7_joint']
		joint_goal.trajectory.header.stamp = rospy.get_rostime()
		joint_goal.trajectory.points.append(point)
		return joint_goal

	
	def tuck_left_arm_cb(userdata, goal):
		point = JointTrajectoryPoint()
		point.time_from_start = rospy.Duration.from_sec(2)
		point.positions = [ 0.3, 0.1, -1.0, 0.8, 0.0, 0.0, 0.0 ]
		point.velocities = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
		joint_goal = JointTrajectoryGoal()
		joint_goal.trajectory.joint_names = ['arm_left_1_joint', 'arm_left_2_joint', 'arm_left_3_joint', 
						     'arm_left_4_joint', 'arm_left_5_joint', 'arm_left_6_joint', 
						     'arm_left_7_joint']
		joint_goal.trajectory.header.stamp = rospy.get_rostime()
		joint_goal.trajectory.points.append(point)
		return joint_goal

	def tuck_right_arm_torso_cb(userdata,goal):
		point = JointTrajectoryPoint()
		point.time_from_start = rospy.Duration.from_sec(2)
		point.positions = [ 0.0, 0.0, 0.3, 0.1, -1.0, 0.8, 0.0, 0.0, 0.0 ]
		point.velocities = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
		joint_goal = JointTrajectoryGoal()
		joint_goal.trajectory.joint_names = ['torso_1_joint', 'torso_2_joint', 'arm_right_1_joint',
		                                     'arm_right_2_joint', 'arm_right_3_joint', 'arm_right_4_joint',
		                                     'arm_right_5_joint', 'arm_right_6_joint', 'arm_right_7_joint']
		joint_goal.trajectory.header.stamp = rospy.get_rostime()
		joint_goal.trajectory.points.append(point)
		return joint_goal


	def stretch_left_arm_cb(userdata, goal):
		point = JointTrajectoryPoint()
		point.time_from_start = rospy.Duration.from_sec(2)
		point.positions = [ 1.3, 0.1, 0.0, 0.6, 0.0, 0.0, 0.0 ]
		point.velocities = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
		joint_goal = JointTrajectoryGoal()
		joint_goal.trajectory.joint_names = ['arm_left_1_joint', 'arm_left_2_joint', 'arm_left_3_joint', 
						     'arm_left_4_joint', 'arm_left_5_joint', 'arm_left_6_joint', 
						     'arm_left_7_joint']
		joint_goal.trajectory.header.stamp = rospy.get_rostime()
		joint_goal.trajectory.points.append(point)
		return joint_goal

	def stretch_right_arm_torso_cb(userdata,goal):
		point = JointTrajectoryPoint()
		point.time_from_start = rospy.Duration.from_sec(2)
		point.positions = [ 0.0, 0.0, 1.3, 0.1, 0.0, 0.6, 0.0, 0.0, 0.0 ]
		point.velocities = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
		joint_goal = JointTrajectoryGoal()
		joint_goal.trajectory.joint_names = ['torso_1_joint', 'torso_2_joint', 'arm_right_1_joint',
		                                     'arm_right_2_joint', 'arm_right_3_joint', 'arm_right_4_joint',
		                                     'arm_right_5_joint', 'arm_right_6_joint', 'arm_right_7_joint']
		joint_goal.trajectory.header.stamp = rospy.get_rostime()
		joint_goal.trajectory.points.append(point)
		return joint_goal

	def find_a_door_goal_cb(userdata, goal):
		find_a_door_goal = iri_door_detector.msg.FindADoorGoal()
       		find_a_door_goal.start = 1
       		return find_a_door_goal

	@smach.cb_interface(
		outcomes=['succeeded_closed_left','succeeded_closed_right','succeeded_open_left','succeeded_open_right','succeeded_open','aborted','preempted'])

	def find_a_door_base_result_cb(userdata, status, result):
		#according to actionlib_msgs/GoalStatus.msg, SUCCEEDED = 3
		rospy.loginfo("status code %d" % status)
		rospy.loginfo("\n door state: %s" % result.state + "\n base poses: \n %s" % result.base_poses)
		if status == 3 and result.state == "fully_open": 
			return 'succeeded_open'
		elif status == 3 and result.state == "open_left": 
			return 'succeeded_open_left'
		elif status == 3 and result.state == "open_right": 
       			return 'succeeded_open_right'
		elif status == 3 and result.state == "closed_left":
			return 'succeeded_closed_left'
		elif status == 3 and result.state == "closed_right": 
       			return 'succeeded_closed_right'
		else:
			return 'aborted'

	@smach.cb_interface(
		outcomes=['succeeded_left', 'succeeded_right', 'aborted','preempted'])

	def find_a_door_arm_result_cb(userdata, status, result):
		#according to actionlib_msgs/GoalStatus.msg, SUCCEEDED = 3
		rospy.loginfo("status code %d" % status)
		rospy.loginfo("\n door state: %s" % result.state + "\n arm poses: \n %s" %  result.arm_poses.goal_constraints.position_constraints[0].header + "\n %s" % result.arm_poses.goal_constraints.position_constraints[0].position + "\n %s" % result.arm_poses.goal_constraints.orientation_constraints[0].orientation )		
		if (status == 3 and (result.state == "closed_right" or result.state == "open_right" or result.state == "fully_open")): 
       			return 'succeeded_right'
		if (status == 3 and (result.state == "closed_left" or result.state == "open_left")): 
       			return 'succeeded_left'
		if (status != 3):
			return 'aborted'

	def turn_handle_goal_cb(userdata, goal):
		goal.planner_service_name=userdata.planner_service_name
		goal.motion_plan_request=userdata.motion_plan_request
		goal.motion_plan_request.goal_constraints.position_constraints[0].position.z = userdata.motion_plan_request.goal_constraints.position_constraints[0].position.z -0.12
		#goal.motion_plan_request.goal_constraints.position_constraints[0].position.y = userdata.motion_plan_request.goal_constraints.position_constraints[0].position.y + 0.05
      		return goal

	@smach.cb_interface(input_keys=['position'],
		outcomes=['succeeded', 'aborted', 'preempted'])

	def joint_state_cb(userdata):

		# Local cb
		def joint_states_cb(joint_states, userdata):
			#userdata.position = dict(zip(joint_states.name, joint_states.position))['arm_left_1_joint']
			if joint_states.name:
				joint_sub.unregister()
 
		# Subscribe to joint state messages
		joint_sub = rospy.Subscriber("/joint_states", JointState, joint_states_cb, userdata)			

		position = joint_states.name
		rospy.loginfo("Joints are %s" % position)
				
		return 'succeeded'
			

	def push_door_left_goal_cb(userdata, goal):
		nav_goal = MoveBaseGoal()
        	nav_goal.target_pose.header.stamp    = rospy.Time.now()
        	nav_goal.target_pose.header.frame_id = "/base_link"
        	p = Point(0.7,-0.35,0.0)
        	q = tf.transformations.quaternion_from_euler(0, 0, -0.5)
        	nav_goal.target_pose.pose = Pose(position=p, orientation=Quaternion(*q))
		rospy.loginfo("\n push door goal: \n %s" % nav_goal.target_pose.pose)
       		return nav_goal

	def push_door_right_goal_cb(userdata, goal):
		nav_goal = MoveBaseGoal()
        	nav_goal.target_pose.header.stamp    = rospy.Time.now()
        	nav_goal.target_pose.header.frame_id = "/base_link"
        	p = Point(0.7,0.35,0.0)
        	q = tf.transformations.quaternion_from_euler(0, 0, 0.5)
        	nav_goal.target_pose.pose = Pose(position=p, orientation=Quaternion(*q))
		rospy.loginfo("\n push door goal: \n %s" % nav_goal.target_pose.pose)
       		return nav_goal

	def finish_push_door_right_goal_cb(userdata, goal):
		nav_goal = MoveBaseGoal()
        	nav_goal.target_pose.header.stamp    = rospy.Time.now()
        	nav_goal.target_pose.header.frame_id = "/base_link"
        	p = Point(1.2,-0.2,0.0)
        	q = tf.transformations.quaternion_from_euler(0, 0, 0)
        	nav_goal.target_pose.pose = Pose(position=p, orientation=Quaternion(*q))
       		return nav_goal

	def finish_push_door_left_goal_cb(userdata, goal):
		nav_goal = MoveBaseGoal()
        	nav_goal.target_pose.header.stamp    = rospy.Time.now()
        	nav_goal.target_pose.header.frame_id = "/base_link"
        	p = Point(1.2,0.2,0.0)
        	q = tf.transformations.quaternion_from_euler(0, 0, 0)
        	nav_goal.target_pose.pose = Pose(position=p, orientation=Quaternion(*q))
       		return nav_goal


	#---smach states

	#Tuck arm
	smach.StateMachine.add('SAFE_POSITION_LEFT_ARM', 
		SimpleActionState('left_arm_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = tuck_left_arm_cb),
				transitions={'succeeded':'SAFE_POSITION_RIGHT_ARM', 
			             	     'aborted':'SAFE_POSITION_LEFT_ARM'})
	#Tuck arm
	smach.StateMachine.add('SAFE_POSITION_RIGHT_ARM', 
		SimpleActionState('right_arm_torso_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = tuck_right_arm_torso_cb),
				transitions={'succeeded':'FIND_A_DOOR_BASE', 
				             'aborted':'SAFE_POSITION_LEFT_ARM'})

	#Find a door 
	smach.StateMachine.add('FIND_A_DOOR_BASE',
		SimpleActionState('/iri_door_detector/door_detector_actions/find_a_door',
                		iri_door_detector.msg.FindADoorAction,
                		goal_cb=find_a_door_goal_cb,
				result_slots=['base_poses',
					      'arm_poses',
					      'planner_service_name',
					      'state']),
		transitions={'succeeded':'BASE_POSES',
			     'aborted':'SAFE_POSITION_LEFT_ARM'},
                remapping={'base_poses':'user_data_base_poses',
			   'arm_poses':'user_data_arm_poses',
			   'planner_service_name':'user_data_planner_service_name',
                           'state':'user_data_state'})
	
	#Print goal for move_base
	smach.StateMachine.add('BASE_POSES',
		SimpleActionState('/iri_door_detector/door_detector_actions/find_a_door',
                		iri_door_detector.msg.FindADoorAction,
                		result_cb=find_a_door_base_result_cb),
		transitions={'succeeded_open':'MOVE_BASE_OPEN',
			     'succeeded_open_left':'LIFT_ARM_LEFT',
			     'succeeded_open_right':'LIFT_ARM_RIGHT',
			     'succeeded_closed_left':'RISE_ARM_LEFT',
			     'succeeded_closed_right':'RISE_ARM_RIGHT',
			     'aborted':'FIND_A_DOOR_BASE'})

	#Prepare left arm for door opening
	smach.StateMachine.add('RISE_ARM_LEFT', 
		SimpleActionState('left_arm_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = rise_left_arm_cb),
				transitions={'succeeded':'MOVE_BASE_CLOSED', 
			             	     'aborted':'SAFE_POSITION_LEFT_ARM'})
	#Prepare right arm for door opening
	smach.StateMachine.add('RISE_ARM_RIGHT', 
		SimpleActionState('right_arm_torso_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = rise_right_arm_torso_cb),
				transitions={'succeeded':'MOVE_BASE_CLOSED', 
				             'aborted':'SAFE_POSITION_LEFT_ARM'})

	#Move towards the door
	smach.StateMachine.add('MOVE_BASE_OPEN',
		SimpleActionState('move_base',
                		MoveBaseAction,
                		goal_slots=['target_pose']),
		transitions={'succeeded':'succeeded',
			     'aborted':'FIND_A_DOOR_BASE'},
		remapping={'target_pose':'user_data_base_poses'})

	#Move towards the door
	smach.StateMachine.add('MOVE_BASE_CLOSED',
		SimpleActionState('move_base',
                		MoveBaseAction,
                		goal_slots=['target_pose']),
		transitions={'succeeded':'FIND_A_DOOR_ARM',
			     'aborted':'FIND_A_DOOR_BASE'},
		remapping={'target_pose':'user_data_base_poses'})

	#Find a door 
	smach.StateMachine.add('FIND_A_DOOR_ARM',
		SimpleActionState('/iri_door_detector/door_detector_actions/find_a_door',
                		iri_door_detector.msg.FindADoorAction,
                		goal_cb=find_a_door_goal_cb,
				result_slots=['arm_poses',
					      'planner_service_name',
					      'state']),
		transitions={'succeeded':'ARM_POSES',
			     'aborted':'SAFE_POSITION_LEFT_ARM'},
                remapping={'arm_poses':'user_data_arm_poses',
			   'planner_service_name':'user_data_planner_service_name',
			   'state':'user_data_state'})

	#Print goal for move_arm
	smach.StateMachine.add('ARM_POSES',
		SimpleActionState('/iri_door_detector/door_detector_actions/find_a_door',
                		iri_door_detector.msg.FindADoorAction,
                		result_cb=find_a_door_arm_result_cb),
		transitions={'succeeded_left':'GRASP_HANDLE_LEFT',
			     'succeeded_right':'GRASP_HANDLE_RIGHT',
			     'aborted':'FIND_A_DOOR_ARM'})


	#Lift arm to prepare the robot for partially open door crossing 
	smach.StateMachine.add('LIFT_ARM_LEFT',
		SimpleActionState('move_left_arm',
                		MoveArmAction,
                		goal_slots=['planner_service_name',
					    'motion_plan_request']),
		transitions={'succeeded':'MOVE_BASE_OPEN',
			     'aborted':'SAFE_POSITION_LEFT_ARM'},
		remapping={'motion_plan_request':'user_data_arm_poses',
			   'planner_service_name':'user_data_planner_service_name'})

	#Lift arm to prepare the robot for partially open door crossing 
	smach.StateMachine.add('LIFT_ARM_RIGHT',
		SimpleActionState('move_right_arm_torso',
                		MoveArmAction,
                		goal_slots=['planner_service_name',
					    'motion_plan_request']),
		transitions={'succeeded':'MOVE_BASE_OPEN',
			     'aborted':'SAFE_POSITION_LEFT_ARM'},
		remapping={'motion_plan_request':'user_data_arm_poses',
			   'planner_service_name':'user_data_planner_service_name'})

	#Move the arm above the handle
	smach.StateMachine.add('GRASP_HANDLE_LEFT',
		SimpleActionState('move_left_arm',
                		MoveArmAction,
                		goal_slots=['planner_service_name',
					    'motion_plan_request']),
		transitions={'succeeded':'JOINT_STATE_LEFT_ARM',
			     'aborted':'FAIL_TURN_LEFT'},
		remapping={'motion_plan_request':'user_data_arm_poses',
			   'planner_service_name':'user_data_planner_service_name'})

	#Joint poses
	smach.StateMachine.add('JOINT_STATE_LEFT_ARM', 
				CBState(joint_state_cb),
		transitions={'succeeded':'TURN_HANDLE_LEFT',
			     'aborted':'FAIL_TURN_LEFT'})		

	#Move the arm above the handle
	smach.StateMachine.add('GRASP_HANDLE_RIGHT',
		SimpleActionState('move_right_arm_torso',
                		MoveArmAction,
                		goal_slots=['planner_service_name',
					    'motion_plan_request']),
		transitions={'succeeded':'TURN_HANDLE_RIGHT',
			     'aborted':'FAIL_TURN_RIGHT'},
		remapping={'motion_plan_request':'user_data_arm_poses',
			   'planner_service_name':'user_data_planner_service_name'})

	#Turn handle
	smach.StateMachine.add('TURN_HANDLE_RIGHT',
		SimpleActionState('move_right_arm_torso',
                		MoveArmAction,
                		goal_cb=turn_handle_goal_cb,
				input_keys=['planner_service_name',
					    'motion_plan_request']),
		transitions={'succeeded':'PUSH_DOOR_RIGHT',
			     'aborted':'FAIL_TURN_RIGHT'},
		remapping={'motion_plan_request':'user_data_arm_poses',
			   'planner_service_name':'user_data_planner_service_name'})

	#Turn handle
	smach.StateMachine.add('TURN_HANDLE_LEFT',
		SimpleActionState('move_left_arm',
                		MoveArmAction,
                		goal_cb=turn_handle_goal_cb,
				input_keys=['planner_service_name',
					    'motion_plan_request']),
		transitions={'succeeded':'PUSH_DOOR_LEFT',
			     'aborted':'FAIL_TURN_LEFT'},
		remapping={'motion_plan_request':'user_data_arm_poses',
			   'planner_service_name':'user_data_planner_service_name'})

	#Turn handle fail
	smach.StateMachine.add('FAIL_TURN_LEFT', 
		SimpleActionState('left_arm_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = rise_left_arm_cb),
		transitions={'succeeded':'FIND_A_DOOR_ARM', 
	             	     'aborted':'FAIL_TURN_LEFT'})

	#Turn handle fail
	smach.StateMachine.add('FAIL_TURN_RIGHT', 
		SimpleActionState('right_arm_torso_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = rise_right_arm_torso_cb),
		transitions={'succeeded':'FIND_A_DOOR_ARM', 
		             'aborted':'FAIL_TURN_RIGHT'})
	
	#Push the door
        smach.StateMachine.add('PUSH_DOOR_LEFT',
        	SimpleActionState('move_base',
        		        MoveBaseAction,
        			goal_cb=push_door_left_goal_cb),
        	transitions={'succeeded':'RELEASE_HANDLE_LEFT',
			     'aborted':'PUSH_DOOR_LEFT'})

	#Push the door
	smach.StateMachine.add('PUSH_DOOR_RIGHT',
        	SimpleActionState('move_base',
        		        MoveBaseAction,
        			goal_cb=push_door_right_goal_cb),
        	transitions={'succeeded':'RELEASE_HANDLE_RIGHT',
			     'aborted':'PUSH_DOOR_RIGHT'})

	#Release handle
	smach.StateMachine.add('RELEASE_HANDLE_LEFT', 
		SimpleActionState('left_arm_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = rise_left_arm_cb),
				transitions={'succeeded':'TUCK_LEFT_ARM', 
			             	     'aborted':'RELEASE_HANDLE_LEFT'})
	#Release handle
	smach.StateMachine.add('RELEASE_HANDLE_RIGHT', 
		SimpleActionState('right_arm_torso_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = rise_right_arm_torso_cb),
				transitions={'succeeded':'TUCK_RIGHT_ARM', 
				             'aborted':'RELEASE_HANDLE_RIGHT'})

	#Tuck arm
	smach.StateMachine.add('TUCK_LEFT_ARM', 
		SimpleActionState('left_arm_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = tuck_left_arm_cb),
				transitions={'succeeded':'STRETCH_RIGHT_ARM', 
			             	     'aborted':'TUCK_LEFT_ARM'})

	#Tuck arm
	smach.StateMachine.add('TUCK_RIGHT_ARM', 
		SimpleActionState('right_arm_torso_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = tuck_right_arm_torso_cb),
				transitions={'succeeded':'STRETCH_LEFT_ARM', 
				             'aborted':'TUCK_RIGHT_ARM'})
	
	#Prepare the other arm to finish door push
	smach.StateMachine.add('STRETCH_LEFT_ARM', 
		SimpleActionState('left_arm_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = stretch_left_arm_cb),
				transitions={'succeeded':'SHRINK_LEFT_ARM', 
			             	     'aborted':'STRETCH_LEFT_ARM'})

	#Prepare the other arm to finish door push
	smach.StateMachine.add('STRETCH_RIGHT_ARM', 
		SimpleActionState('right_arm_torso_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = stretch_right_arm_torso_cb),
				transitions={'succeeded':'SHRINK_RIGHT_ARM', 
				             'aborted':'STRETCH_RIGHT_ARM'})

	#Shrink arm
	smach.StateMachine.add('SHRINK_LEFT_ARM', 
		SimpleActionState('left_arm_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = tuck_left_arm_cb),
				transitions={'succeeded':'FINISH_PUSH_DOOR_RIGHT', 
			             	     'aborted':'SHRINK_LEFT_ARM'})

	#Shrink arm
	smach.StateMachine.add('SHRINK_RIGHT_ARM', 
		SimpleActionState('right_arm_torso_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = tuck_right_arm_torso_cb),
				transitions={'succeeded':'FINISH_PUSH_DOOR_LEFT', 
				             'aborted':'SHRINK_RIGHT_ARM'})

	#Push the door
        smach.StateMachine.add('FINISH_PUSH_DOOR_LEFT',
        	SimpleActionState('move_base',
        		        MoveBaseAction,
        			goal_cb=finish_push_door_left_goal_cb),
        	transitions={'succeeded':'REST_LEFT_ARM',
			     'aborted':'FINISH_PUSH_DOOR_LEFT'})

	#Push the door
        smach.StateMachine.add('FINISH_PUSH_DOOR_RIGHT',
        	SimpleActionState('move_base',
        		        MoveBaseAction,
        			goal_cb=finish_push_door_right_goal_cb),
        	transitions={'succeeded':'REST_LEFT_ARM',
			     'aborted':'FINISH_PUSH_DOOR_RIGHT'})

	#Return to safe position
	smach.StateMachine.add('REST_LEFT_ARM', 
		SimpleActionState('left_arm_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = init_left_arm_cb),
				transitions={'succeeded':'REST_RIGHT_ARM', 
			             	     'aborted':'REST_LEFT_ARM'})
	#Return to safe position
	smach.StateMachine.add('REST_RIGHT_ARM', 
		SimpleActionState('right_arm_torso_controller/joint_trajectory_action',
				JointTrajectoryAction,
				goal_cb = init_right_arm_torso_cb),
				transitions={'succeeded':'succeeded', 
				             'aborted':'REST_RIGHT_ARM'})


    # Create and start the introspection server
    sis = smach_ros.IntrospectionServer('open_the_door', sm, '/SM_ROOT')
    sis.start()	

    # Execute SMACH plan
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

