#! /usr/bin/env python

import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import copy
import smach
from smach_ros import SimpleActionState, ServiceState
import actionlib

from std_msgs.msg import *
from arm_navigation_msgs.msg import *
from actionlib_msgs import *
from actionlib_msgs.msg import GoalStatus


from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.grasping.arm_and_hand_goals import *


class ArmMovementToTravelStateMachine(smach.StateMachine):
    """
    Moves the arm to travel position. (Supposedly with a
    grasped object).

    Required parameters:
    No parameters.

    Optional parameters:
    No optional parameters


    @input_keys: 'transformed_object_data', 'object_data'
        'transformed_object_data' must contain an ObjectPose message
        with the position and orientation transformed from
        the original frame_id to base_link
        'object_data' must contain the original ObjectPoseList message
        of the object recognition part
    No output keys.
    No io_keys.

    The hand MUST BE OPEN as we suppose it to be open to graps.
    The input_keys should be fullfilled to pass the info over to
    next states. It's not checked (as it should be checked in
    previous states).
    """
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=['transformed_object_data', 'object_data'])

        with self:

            def arm_result_cb(userdata, result_status, result):
                if result_status != GoalStatus.SUCCEEDED:  # SUCCEEDED = 3 http://www.ros.org/doc/api/move_arm_msgs/html/msg/MoveArmActionResult.html
                    rospy.loginfo("MoveArmActionResult result wasn't succeeded, was: " + str(result_status) +
                        "\nmessage: \n" + str(result))
                    # if result.error_code.val == 1: # SUCCESS
                    #     rospy.loginfo("But we got SUCCESS as the result, so the planner will replan by itself.")
                    #     return succeeded

                    return aborted
                else:
                    return succeeded

            def arm_goal_cb(userdata, old_goal):
                #TODO: Maybe move it more intelligently up?
                rospy.loginfo("Now we will add 10cm to Z to lift up the object (and substract 10cm to X)")
                goal_for_lifting = copy.deepcopy(userdata.transformed_object_data.pose)
                goal_for_lifting.position.z += 0.10
                goal_for_lifting.position.x -= 0.10
                rospy.loginfo("Now we send the goal:\n" + str(goal_for_lifting))
                arm_goal = get_arm_goal(goal_for_lifting, frame_id="/base_link")
                return arm_goal

            smach.StateMachine.add(
            'LIFT_UP_HAND_WITH_OBJECT',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                result_cb=arm_result_cb,
                input_keys=['object_data', 'transformed_object_data']),
                transitions={succeeded: 'Arm_to_safe_travelling_position', aborted: 'LIFT_UP_HAND_WITH_OBJECT'})

            # smach.StateMachine.add(
         #        'REFRESH_COLLISION_MAP_FOR_TRAVELLING_POS',
         #        ServiceState('/refresh_collision_map/refresh', Empty),
         #        transitions = {succeeded:'WAIT_FOR_COLLISION_MAP_UPDATE_FOR_TRAVELLING_POS'})

         #    smach.StateMachine.add(
         #        'WAIT_FOR_COLLISION_MAP_UPDATE_FOR_TRAVELLING_POS',
         #        WaitForCollisionMapUpdate(),
         #        transitions = {succeeded: 'Arm_to_safe_travelling_position'})

            def arm_goal_cb(userdata, old_goal):
                #arm_goal = get_arm_goal_for_arm_down()
                arm_goal_pose = get_pose_for_arm_down()
                arm_goal = get_arm_goal(arm_goal_pose.pose)
                return arm_goal

            smach.StateMachine.add(
            'Arm_to_safe_travelling_position',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                result_cb=arm_result_cb,
                input_keys=['object_data']),
                transitions={succeeded: succeeded, aborted: 'Arm_to_safe_travelling_position'})
