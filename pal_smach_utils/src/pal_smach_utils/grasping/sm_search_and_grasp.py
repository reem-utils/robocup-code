#! /usr/bin/env python

import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import copy
import smach
import actionlib
from smach_ros import SimpleActionState, ServiceState

from std_msgs.msg import *
from arm_navigation_msgs.msg import *
from actionlib_msgs import *
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# try:
#     from pr_msgs.msg import ObjectPoseList, ObjectPose
#     from pr_msgs.srv import *
#     from iri_moped_handler.srv import *
# except ImportError:
#     from object_recognition_mock.msg import ObjectPoseList, ObjectPose
#     from object_recognition_mock.srv import *

from blort_ros.msg import ObjectPoseList, ObjectPose
from blort_ros.srv import *

from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped
from object_manipulation_msgs.msg import *
#from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *

from pal_smach_utils.utils.math_utils import *
from pal_smach_utils.grasping.arm_and_hand_goals import *
from pal_smach_utils.grasping.head_goals import *
from pal_smach_utils.grasping.search_objects_behaviour import *
from pal_smach_utils.grasping.arm_movement_grasp_sequence import *
from pal_smach_utils.grasping.sm_grasp import *
from trajectory_msgs.msg import *
from control_msgs.msg import *
from std_srvs.srv import *
#from pr2_controllers_msgs import *


class DummySearchObjectStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded])

    def execute(self, userdata):
        print "\n=====\nDummy state that simulates we did a search for the object...\n====="
        rospy.sleep(0.5)  # in seconds
        return succeeded


class WaitForCollisionMapUpdate(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded])

    def execute(self, userdata):
        print "\n=====\nWaiting for collision map update 10s\n====="
        rospy.sleep(10)  # in seconds
        return succeeded


class DummyApproachToObjectStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded])

    def execute(self, userdata):
        print "\n=====\nDummy state that simulates we approached the Reem to the object...\n====="
        rospy.sleep(0.5)  # in seconds
        return succeeded


class CheckObject(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys=['object_data'])

    def execute(self, userdata):
        rospy.loginfo("look_for_objects returned an structure of objects: ")
        if len(userdata.object_data.object_list) != 0:
            rospy.loginfo("Object is: " + userdata.object_data.object_list[0].name +
             "\nIn position: " + str(userdata.object_data.object_list[0].pose.position) +
             "\nWith orientation: " + str(userdata.object_data.object_list[0].pose.orientation))
            return succeeded
        else:
            rospy.loginfo("The structure is empty, we'll search again.")
            return aborted


class TransformObjectReferenceFrame(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], input_keys=['object_data', 'transformed_object_data'], output_keys=['transformed_object_data'])

    def execute(self, userdata):
        rospy.loginfo("Transforming pose of object from the kinect frame to the base_link frame.")
        rospy.loginfo("Asking tf to transform from " + userdata.object_data.header.frame_id + " to /base_link the pose:\n " + str(userdata.object_data.object_list[0].pose))
        object_in_base_link = transform_pose(userdata.object_data.object_list[0].pose,  userdata.object_data.header.frame_id, "/base_link")
        rospy.loginfo("tf returns the pose transformed:\n" + str(object_in_base_link))
        userdata.transformed_object_data = copy.deepcopy(userdata.object_data.object_list[0])
        userdata.transformed_object_data.pose = object_in_base_link
        return succeeded


class Check_if_object_specified(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys=['object_to_search_for'])

    def execute(self, userdata):
        if userdata.object_to_search_for != None:
            rospy.loginfo("This state machine will try to grasp " + userdata.object_to_search_for)  # whats the list of graspables?
            return succeeded
        else:
            rospy.loginfo("No object to search specified in the userdata key object_to_search_for")
            return aborted


class SearchAndGraspStateMachine(smach.StateMachine):
    """
    Given an object to grasp (TODO: may accept "None")
    it starts the pipeline of grasping:
    1) Search for the object. (We suppose we are near it).
    2) Get closer if needed.
    3) Grasp it.
    4) Put arm in travel position.

    Required parameters:
    No parameters.

    Optional parameters:
    No optional parameters.


    @input_keys: 'object_to_search_for'
        'object_to_search_for' string with the object
        we are going to search and grasp.
    No output keys.
    No io_keys.

    This is the main program for grasping. TODO: refactorize it.
    """
    # Defined here: https://docs.google.com/drawings/d/1L3muMd6uwvDVhdYN4e5OfHX3sCSxmeCC_EdFhfTQ5cQ/edit
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=['object_to_search_for'])

        with self:

            smach.StateMachine.add(
            'Check_if_object_specified',
            Check_if_object_specified(),
            transitions={succeeded: 'SEARCH_OBJECTS_STATE_MACHINE', aborted: aborted})

            # smach.StateMachine.add(
            # 'dummy_approach_to_object',
            # DummyApproachToObjectStateMachine(),
            # transitions = {succeeded: 'HEAD_MOVE_DOWN_AND_RIGHT'})

            smach.StateMachine.add(
            'SEARCH_OBJECTS_STATE_MACHINE',
            SearchObjectsStateMachine(),
            remapping={'object_found_in_base_link_ref_frame': 'transformed_object_data',
                        'object_found': 'object_data'},
            transitions={succeeded: 'GraspStateMachine'})
            
            smach.StateMachine.add(
             'GraspStateMachine',
             GraspStateMachine(),
             transitions={succeeded: succeeded, aborted: aborted})
            

#             smach.StateMachine.add(
#             'Arm_Movement_Grasp_Sequence',
#             ArmMovementGraspSequenceStateMachine(),
#             transitions={succeeded: 'HEAD_MOVE_FRONT', aborted: aborted})

#             def head_goal_cb(userdata, old_goal):
#                 head_msg = get_head_look_front()
#                 return head_msg
# 
#             def head_result_cb(userdata, status, result):
#                 if status == GoalStatus.SUCCEEDED:
#                     #rospy.loginfo("Succeeded: result of right_hand_controller: " + str(result.error_code) )
#                     return succeeded
#                 else:  # TODO: See if this is important, Hilario says maybe it's a problem of gazebo
#                     rospy.loginfo("Other than succeded: result of head_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code))
#                     if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
#                         rospy.loginfo("Continuing even with this error as it's not really aborted...")
#                         return succeeded
#                     else:
#                         return aborted
# 
#             smach.StateMachine.add(
#             'HEAD_MOVE_FRONT',
#             SimpleActionState(
#                 # '/head_controller/follow_joint_trajectory', for simulaiton
#                 '/head_traj_controller/follow_joint_trajectory',
#                 FollowJointTrajectoryAction,
#                 goal_cb=head_goal_cb,
#                 result_cb=head_result_cb,
#                 input_keys=['object_data']),
#                 transitions={succeeded: succeeded, aborted: 'HEAD_MOVE_FRONT'})


          #   def arm_goal_cb(userdata, old_goal):
          #       #TODO: Move the arm to a position -19cm from the object in some more intelligent way, maybe just play with the orientation of the hand
          #       userdata.transformed_object_data.pose.orientation = Quaternion (0.5, -0.5, 0.5, -0.5) # euler equivalent: (-1.57079632679, -0.0, -1.57079632679)
          #       #"yaw -pi/2, pitch 0, roll  -pi/2 +pi/8: -1.57079632679,  0, -1.57079632679 +0.785398/2"
          #       #userdata.transformed_object_data.pose.orientation = Quaternion(*quaternion_from_euler(-1.57079632679 -0.785398 , -0.0, -1.57079632679 +0.785398/2))
          #       #userdata.transformed_object_data.pose.orientation = Quaternion(-0.587937785162, 0.392847503208, -0.39284750321, 0.587937785165)
          #       rospy.loginfo("Now we will substract 19cm to X to reach the pre-grasping position and we will change the orientation to a good known one")
          #       goal_for_pregrasping = copy.deepcopy(userdata.transformed_object_data.pose)
          #       goal_for_pregrasping.position.x -= 0.19
          #       goal_for_pregrasping.position.y -= 0.05
          #       goal_for_pregrasping.position.z += 0.10
          #       rospy.loginfo("Now we send the goal:\n" + str(goal_for_pregrasping))
          #       arm_goal = get_arm_goal(goal_for_pregrasping, frame_id="/base_link")
          #       return arm_goal



          #   ## !!! callback used on all MoveArmActions
          #   def arm_result_cb(userdata, result_status, result):
          #       if result_status != GoalStatus.SUCCEEDED: # SUCCEEDED = 3 http://www.ros.org/doc/api/move_arm_msgs/html/msg/MoveArmActionResult.html
          #           rospy.loginfo("MoveArmActionResult result wasn't succeeded, was: " + str(result_status) +
          #               "\nmessage: \n" + str(result))
          #           # if result.error_code.val == 1: # SUCCESS
          #           #     rospy.loginfo("But we got SUCCESS as the result, so the planner will replan by itself.")
          #           #     return succeeded

          #           return aborted
          #       else:
          #           return succeeded


          #   smach.StateMachine.add(
          #   'N2_APPROACH_PREGRASPING_POSITION',
          #   SimpleActionState(
          #       'move_right_arm_torso',
          #       MoveArmAction,
          #       goal_cb = arm_goal_cb,
          #       result_cb = arm_result_cb,
          #       input_keys = ['object_data', 'transformed_object_data']),
          #   transitions = {succeeded: 'RESET_COLLISION_MAP', aborted: 'N2_APPROACH_PREGRASPING_POSITION'})


          #  ### reset collision map here so we can really approach to the object

          #   smach.StateMachine.add(
          #       'RESET_COLLISION_MAP',
          #       ServiceState('refresh_collision_map_reset/refresh_reset', Empty),
          #       transitions = {succeeded:'N2_APPROACH_FINAL_GRASPING_POSITION'})


          #   def arm_goal_cb(userdata, old_goal):
          #       #TODO: Move the arm to a position -14cm from the object in some more intelligent way, maybe just play with the orientation of the hand
          #       userdata.transformed_object_data.pose.orientation = Quaternion (0.5, -0.5, 0.5, -0.5)
          #       #userdata.transformed_object_data.pose.orientation = Quaternion(*quaternion_from_euler(-1.57079632679 -0.785398 , -0.0, -1.57079632679 +0.785398/2))
          #       #userdata.transformed_object_data.pose.orientation = Quaternion(-0.587937785162, 0.392847503208, -0.39284750321, 0.587937785165)

          #       rospy.loginfo("Now we will substract 14cm to X to reach the pre-grasping position and we will change the orientation to a good known one")
          #       goal_for_pregrasping = copy.deepcopy(userdata.transformed_object_data.pose)
          #       goal_for_pregrasping.position.x -= 0.13 # Testing 1cm less, was 14cm
          #       goal_for_pregrasping.position.y -= 0.01
          #       rospy.loginfo("Now we send the goal:\n" + str(goal_for_pregrasping))
          #       arm_goal = get_arm_goal(goal_for_pregrasping, frame_id="/base_link")
          #       return arm_goal


          #   smach.StateMachine.add(
          #   'N2_APPROACH_FINAL_GRASPING_POSITION',
          #   SimpleActionState(
          #       'move_right_arm_torso',
          #       MoveArmAction,
          #       goal_cb = arm_goal_cb,
          #       result_cb = arm_result_cb,
          #       input_keys = ['object_data', 'transformed_object_data']),
          #   transitions = {succeeded: 'M4_grasp_object_close_hand', aborted: 'N2_APPROACH_FINAL_GRASPING_POSITION'})


          #   def grasp_arm_goal_cb(userdata, old_goal):
          #       grasp_msg = get_close_hand()
          #       return grasp_msg

          #   def grasp_arm_result_cb(userdata, status, result):
          #       if status == GoalStatus.SUCCEEDED:
          #           #rospy.loginfo("Succeeded: result of right_hand_controller: " + str(result.error_code) )
          #           return succeeded
          #       else: #TODO: See if this is important, Hilario says maybe it's a problem of gazebo
          #           rospy.loginfo("Other than succeded: result of right_hand_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code) )
          #           if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
          #               rospy.loginfo("Continuing even with this error as it's not really aborted...")
          #               return succeeded
          #           else:
          #               return aborted


          #   smach.StateMachine.add(
          #   'M4_grasp_object_close_hand',
          #   SimpleActionState(
          #       '/right_hand_controller/follow_joint_trajectory',
          #       FollowJointTrajectoryAction,
          #       goal_cb = grasp_arm_goal_cb,
          #       result_cb = grasp_arm_result_cb,
          #       input_keys = ['object_data']),
          #   transitions = {succeeded: 'LIFT_UP_HAND_WITH_OBJECT', aborted: 'M4_grasp_object_close_hand'})




          #   ### in the future here we need to add the grasped object to the self collision map



          #   def arm_goal_cb(userdata, old_goal):
          #       #TODO: Maybe move it more intelligently up?
          #       rospy.loginfo("Now we will add 10cm to Z to lift up the object (and substract 10cm to X)")
          #       goal_for_lifting = copy.deepcopy(userdata.transformed_object_data.pose)
          #       goal_for_lifting.position.z += 0.10
          #       goal_for_lifting.position.x -= 0.10
          #       rospy.loginfo("Now we send the goal:\n" + str(goal_for_lifting))
          #       arm_goal = get_arm_goal(goal_for_lifting, frame_id="/base_link")
          #       return arm_goal


          #   smach.StateMachine.add(
          #   'LIFT_UP_HAND_WITH_OBJECT',
          #   SimpleActionState(
          #       'move_right_arm_torso',
          #       MoveArmAction,
          #       goal_cb = arm_goal_cb,
          #       result_cb = arm_result_cb,
          #       input_keys = ['object_data', 'transformed_object_data']),
          #   transitions = {succeeded: 'REFRESH_COLLISION_MAP_FOR_TRAVELLING_POS', aborted: 'LIFT_UP_HAND_WITH_OBJECT'})



          #   # FIXME: WE NEED A SECURE POSITION WHERE WE DON'T SEE OUR OWN HAND (with the object) to move the robot to travelling position






          #   # def arm_goal_cb(userdata, old_goal):
          #   #     rospy.loginfo("Moving arm to the intermediate pose to known travel position")
          #   #     intermediate_grasping_pose = get_pose_intermediate_position()
          #   #     arm_goal = get_arm_goal(intermediate_grasping_pose.pose, frame_id="/base_link")
          #   #     return arm_goal



          #   # ## !!! callback used on all MoveArmActions
          #   # def arm_result_cb(userdata, result_status, result):
          #   #     if result_status != GoalStatus.SUCCEEDED: # SUCCEEDED = 3 http://www.ros.org/doc/api/move_arm_msgs/html/msg/MoveArmActionResult.html
          #   #         rospy.loginfo("MoveArmActionResult result wasn't succeeded, was: " + str(result_status) +
          #   #             "\nmessage: \n" + str(result))
          #   #         # if result.error_code.val == 1: # SUCCESS
          #   #         #     rospy.loginfo("But we got SUCCESS as the result, so the planner will replan by itself.")
          #   #         #     return succeeded

          #   #         return aborted
          #   #     else:
          #   #         return succeeded


          #   # smach.StateMachine.add(
          #   # 'N2_APPROACH_INTERMEDIATE_TO_TRAVELLING_POSITION',
          #   # SimpleActionState(
          #   #     'move_right_arm_torso',
          #   #     MoveArmAction,
          #   #     goal_cb = arm_goal_cb,
          #   #     result_cb = arm_result_cb,
          #   #     input_keys = ['object_data', 'transformed_object_data']),
          #   # transitions = {succeeded: 'Arm_to_safe_travelling_position', aborted: 'N2_APPROACH_INTERMEDIATE_TO_TRAVELLING_POSITION'})



          #   #### we need a new collision map here

          #   smach.StateMachine.add(
          #       'REFRESH_COLLISION_MAP_FOR_TRAVELLING_POS',
          #       ServiceState('/refresh_collision_map/refresh', Empty),
          #       transitions = {succeeded:'WAIT_FOR_COLLISION_MAP_UPDATE_FOR_TRAVELLING_POS'})

          #   smach.StateMachine.add(
          #       'WAIT_FOR_COLLISION_MAP_UPDATE_FOR_TRAVELLING_POS',
          #       WaitForCollisionMapUpdate(),
          #       transitions = {succeeded: 'Arm_to_safe_travelling_position'})


          #   def arm_goal_cb(userdata, old_goal):
          #       #arm_goal = get_arm_goal_for_arm_down()
          #       arm_goal_pose = get_pose_for_arm_down()
          #       arm_goal = get_arm_goal(arm_goal_pose.pose)
          #       return arm_goal


          #   smach.StateMachine.add(
          #   'Arm_to_safe_travelling_position',
          #   SimpleActionState(
          #       'move_right_arm_torso',
          #       MoveArmAction,
          #       goal_cb = arm_goal_cb,
            # result_cb = arm_result_cb,
          #       input_keys = ['object_data']),
          #   transitions = {succeeded: 'HEAD_MOVE_FRONT', aborted: 'Arm_to_safe_travelling_position'})




