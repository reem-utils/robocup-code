#! /usr/bin/env python

import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import copy
import smach
import actionlib
from smach_ros import SimpleActionState, ServiceState
from actionlib_msgs.msg import GoalStatus

from pal_smach_utils.utils.global_common import *

# open/close hand state
from pal_smach_utils.grasping.st_reem_hand import OpenReemHand, CloseReemHand

# utils
from arm_and_hand_goals import get_arm_goal

# msgs
from geometry_msgs.msg import PoseStamped, Pose
from arm_navigation_msgs.msg import MoveArmAction, MoveArmActionResult


# move arm
def arm_result_cb(userdata, result_status, result):
    if result_status != GoalStatus.SUCCEEDED:  # SUCCEEDED = 3
        rospy.loginfo("MoveArmActionResult result wasn't succeeded, was: " + str(result_status) +
            "\nmessage: \n" + str(result))
        return aborted
    else:
        return succeeded

def arm_grasp_goal_cb(userdata, old_goal):
    userdata.target_pose_stamped.pose.orientation = Quaternion(0, 0, 0 ,1)
    rospy.loginfo("Modifying grasp pose.")
    goal_for_pregrasping = copy.deepcopy(userdata.target_pose_stamped)
    goal_for_pregrasping.pose.position.x -= 0.14
    arm_goal = get_arm_goal(goal_for_pregrasping.pose, frame_id="/base_link")

    # Do a interpolated movement!
    #arm_goal.motion_plan_request.planner_id = "interpolated_ik"
    #arm_goal.planner_service_name = "generic_interpolated_ik_right_arm_torso/GetInterpolatedIkMotionPlan"
    rospy.loginfo("Sending arm goal:\n" + str(arm_goal))
    return arm_goal

def arm_pre_grasp_goal_cb(userdata, old_goal):
    userdata.target_pose_stamped.pose.orientation = Quaternion(0, 0, 0 ,1)
    rospy.loginfo("Modifying pre grasp pose.")
    goal_for_pregrasping = copy.deepcopy(userdata.target_pose_stamped)
    goal_for_pregrasping.pose.position.x -= 0.3
    arm_goal = get_arm_goal(goal_for_pregrasping.pose, frame_id="/base_link")
    rospy.loginfo("Sending arm goal:\n" + str(arm_goal))
    return arm_goal

def get_pose_for_arm_down(userdata, old_goal):
    # FIXME: Check if it is correct
    relax_pose = PoseStamped()
    relax_pose.pose.position = Point(0.130007, -0.198804, 0.900355)
    relax_pose.pose.orientation = Quaternion(0.87292, -0.244933, 0.127606, -0.402163)
    arm_goal = get_arm_goal(relax_pose.pose, frame_id="/base_link")
    return arm_goal

def arm_post_grasp_goal_cb(userdata, old_goal):
    userdata.target_pose_stamped.pose.orientation = Quaternion(0, 0, 0 ,1)
    goal_for_pregrasping = copy.deepcopy(userdata.target_pose_stamped)
    goal_for_pregrasping.pose.position.x -= 0.22
    arm_goal = get_arm_goal(goal_for_pregrasping.pose, frame_id="/base_link")
    rospy.loginfo("Sending arm goal:\n" + str(arm_goal))
    return arm_goal


class SMReemClothGraspStateMachine(smach.StateMachine):
    """
    Given an object and it's location it opens the hand,
    moves the arm to the object to a pre-grasping position,
    then to a grasping position, closes the hand, and
    moves the arm back to a travel position.

    Required parameters:
    No parameters

    Optional parameters:
    No optional parameters.


    @input_keys: 'target_pose_stamped', 'object_data'
        'target_pose_stamped' is a pose_stamped with target object position
        with the position and orientation transformed from
        the original frame_id to base_link
    No output keys.
    No io_keys.

    If the input_keys aren't fullfilled this state aborts.
    """
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=['target_pose_stamped'])

        with self:

            # pre-grasp pose
            smach.StateMachine.add(
                'MOVE_TO_PRE_GRASP_POSE',
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal_cb=arm_pre_grasp_goal_cb,
                    result_cb=arm_result_cb,
                    input_keys=['target_pose_stamped']),
                transitions={succeeded: 'GRASP_OPEN_HAND', aborted: aborted})

            # open hand
            smach.StateMachine.add(
                'GRASP_OPEN_HAND',
                OpenReemHand(),
                transitions={succeeded: 'MOVE_TO_GRASP_POSE', aborted: aborted})

            # grasp position
            # grasp
            smach.StateMachine.add(
                'MOVE_TO_GRASP_POSE',
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal_cb=arm_grasp_goal_cb,
                    result_cb=arm_result_cb,
                    input_keys=['target_pose_stamped']),
                transitions={succeeded: 'GRASP_CLOSE_HAND', aborted: aborted})

            # close hand
            smach.StateMachine.add(
                'GRASP_CLOSE_HAND',
                CloseReemHand(),
                transitions={succeeded: 'MOVE_TO_POST_GRASP_POSE', aborted: aborted})

            # post position
            smach.StateMachine.add(
                'MOVE_TO_POST_GRASP_POSE',
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal_cb=arm_post_grasp_goal_cb,
                    result_cb=arm_result_cb,
                    input_keys=['target_pose_stamped']),
                transitions={succeeded: succeeded, aborted: aborted})

            # down position
            #smach.StateMachine.add(
                #'MOVE_TO_RELAX_POSE',
                #SimpleActionState(
                    #'move_right_arm_torso',
                    #MoveArmAction,
                    #goal_cb=get_pose_for_arm_down,
                    #result_cb=arm_result_cb,
                    #input_keys=['target_pose_stamped']),
                #transitions={succeeded: succeeded, aborted: aborted})
