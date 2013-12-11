#!/usr/bin/env python

import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import smach_ros
import threading
import time

from smach_ros import SimpleActionState
from actionlib_msgs.msg import GoalStatus

# Action msgs
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint, JointTrajectory


def grasp_hand_result_cb(userdata, status, result):
    if status == GoalStatus.SUCCEEDED:
        return 'succeeded'
    else:  # TODO: See if this is important, Hilario says maybe it's a problem of gazebo
        rospy.loginfo("Other than succeeded: result of right_hand_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code))
        if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
            rospy.loginfo("Continuing even with this error as it's not really aborted...")
            return 'succeeded'
        else:
            return 'aborted'

def get_hand_goal(goal_positions):
    grasp_msg = FollowJointTrajectoryGoal()

    point1 = JointTrajectoryPoint(
        positions=goal_positions,
        velocities=[0.0, 0.0, 0.0],
        time_from_start = rospy.Duration(1))

    grasp_msg.trajectory = JointTrajectory(
        joint_names = ['hand_right_thumb_joint', 'hand_right_index_1_joint', 'hand_right_middle_1_joint'],
        points = [point1])

    return grasp_msg



#*********
# open hand
def get_open_positions():
    #positions=[1.0, 0.2, 0.2]  # cant close too much or the object to grasp flies away
    positions=[1.6, 0.0, 0.0]
    return positions


def grasp_open_hand_goal_cb2(userdata, old_goal):
    hand_goal = get_hand_goal([0.0, 0.0, 0.0])
    rospy.loginfo("Sending hand goal:\n" + str(hand_goal))
    return hand_goal


def grasp_open_hand_goal_cb(userdata, old_goal):
    hand_goal = get_hand_goal(get_open_positions())
    rospy.loginfo("Sending hand goal:\n" + str(hand_goal))
    return hand_goal

class OpenReemHand(SimpleActionState):
    """
    Custom smach for openning REEM hand
    """
    def __init__(self, follow_joint_trajectory_topic = '/right_hand_controller/follow_joint_trajectory'):
        SimpleActionState.__init__(self, follow_joint_trajectory_topic,
                                    FollowJointTrajectoryAction,
                                    goal_cb=grasp_open_hand_goal_cb,
                                    result_cb=grasp_hand_result_cb)


class OpenReemHand2(SimpleActionState):
    """
    Custom smach for openning REEM hand
    """
    def __init__(self, follow_joint_trajectory_topic = '/right_hand_controller/follow_joint_trajectory'):
        SimpleActionState.__init__(self, follow_joint_trajectory_topic,
                                    FollowJointTrajectoryAction,
                                    goal_cb=grasp_open_hand_goal_cb2,
                                    result_cb=grasp_hand_result_cb)



#*********
# close hand
def get_close_positions():
    #positions=[1.0, 0.2, 0.2]  # cant close too much or the object to grasp flies away
    #positions=[1.6,1.57,1.57]
    positions=[1.6,2.8,2.8]
    return positions

def grasp_close_hand_goal_cb(userdata, old_goal):
    hand_goal = get_hand_goal(get_close_positions())
    rospy.loginfo("Sending hand goal:\n" + str(hand_goal))
    return hand_goal

class CloseReemHand(SimpleActionState):
    """
    Custom smach for closing REEM hand
    """
    def __init__(self, follow_joint_trajectory_topic = '/right_hand_controller/follow_joint_trajectory'):
        SimpleActionState.__init__(self, follow_joint_trajectory_topic,
                                    FollowJointTrajectoryAction,
                                    goal_cb=grasp_close_hand_goal_cb,
                                    result_cb=grasp_hand_result_cb)


