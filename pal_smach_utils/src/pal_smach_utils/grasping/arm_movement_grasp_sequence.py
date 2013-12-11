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
from control_msgs.msg import *
from trajectory_msgs.msg import *

from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
#from pal_smach_utils.grasping.sm_search_and_grasp import *
from pal_smach_utils.grasping.arm_and_hand_goals import *
from pal_smach_utils.grasping.arm_movement_to_object import *
from pal_smach_utils.grasping.arm_movement_to_travel import *
#from pr2_controllers_msgs.msg import *


class Check_if_object_specified(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys=['transformed_object_data', 'object_data'])

    def execute(self, userdata):
        if userdata.object_data != None and userdata.transformed_object_data != None:
            rospy.loginfo("This state machine will try to grasp " + str(userdata.transformed_object_data))  # whats the list of graspables?
            return succeeded
        else:
            rospy.loginfo("No object to grasp specified in the userdata key object_data or transformed_object_data")
            return aborted


class ArmMovementGraspSequenceStateMachine(smach.StateMachine):
    """
    Given an object and it's location it opens the hand,
    moves the arm to the object to a pre-grasping position,
    then to a grasping position, closes the hand, and
    moves the arm back to a travel position.

    Required parameters:
    No parameters

    Optional parameters:
    No optional parameters.


    @input_keys: 'transformed_object_data', 'object_data'
        'transformed_object_data' must contain an ObjectPose message
        with the position and orientation transformed from
        the original frame_id to base_link
        'object_data' must contain the original ObjectPoseList message
        of the object recognition part
    No output keys.
    No io_keys.

    If the input_keys aren't fullfilled this state aborts.
    """
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=['transformed_object_data', 'object_data'])

        with self:

            smach.StateMachine.add(
            'Check_if_object_specified',
            Check_if_object_specified(),
            transitions={succeeded: 'M4_grasp_object_open_hand', aborted: aborted})

            def grasp_arm_goal_cb(userdata, old_goal):
                grasp_msg = get_open_hand()
                return grasp_msg

            def grasp_arm_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED:
                    #rospy.loginfo("Succeeded: result of right_hand_controller: " + str(result.error_code) )
                    return succeeded
                else:  # TODO: See if this is important, Hilario says maybe it's a problem of gazebo
                    rospy.loginfo("Other than succeded: result of right_hand_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code))
                    if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
                        rospy.loginfo("Continuing even with this error as it's not really aborted...")
                        return succeeded
                    else:
                        return aborted

            smach.StateMachine.add(
            'M4_grasp_object_open_hand',
            SimpleActionState(
                '/right_hand_controller/follow_joint_trajectory',
                FollowJointTrajectoryAction,
                goal_cb=grasp_arm_goal_cb,
                result_cb=grasp_arm_result_cb,
                input_keys=['object_data']),
                transitions={succeeded: 'Move_arm_to_object', aborted: 'M4_grasp_object_open_hand'})

            smach.StateMachine.add(
                    'Move_arm_to_object',
                    ArmMovementToObjectStateMachine(),
                    transitions={succeeded: 'M4_grasp_object_close_hand', aborted: aborted})

            def grasp_arm_goal_cb(userdata, old_goal):
                grasp_msg = get_close_hand()
                return grasp_msg

            def grasp_arm_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED:
                    #rospy.loginfo("Succeeded: result of right_hand_controller: " + str(result.error_code) )
                    return succeeded
                else:  # TODO: See if this is important, Hilario says maybe it's a problem of gazebo
                    rospy.loginfo("Other than succeded: result of right_hand_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code))
                    if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
                        rospy.loginfo("Continuing even with this error as it's not really aborted...")
                        return succeeded
                    else:
                        return aborted

            smach.StateMachine.add(
            'M4_grasp_object_close_hand',
            SimpleActionState(
                '/right_hand_controller/follow_joint_trajectory',
                FollowJointTrajectoryAction,
                goal_cb=grasp_arm_goal_cb,
                result_cb=grasp_arm_result_cb,
                input_keys=['object_data']),
                transitions={succeeded: 'Move_arm_to_travel_position', aborted: 'M4_grasp_object_close_hand'})

            smach.StateMachine.add(
                    'Move_arm_to_travel_position',
                    ArmMovementToTravelStateMachine(),
                    transitions={succeeded: succeeded, aborted: aborted})
