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
#from pal_smach_utils.grasping.sm_search_and_grasp import *
from pal_smach_utils.grasping.arm_and_hand_goals import *


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


#  THIS STATE MACHINE
#               NEEDS THE HAND OPENED                      * yeah I can test if its open here too I know.
#                       IF NOT
#               IT WILL CRASH THE HAND
#     TO THE DESIRED GRASPING OBJECT


class ArmMovementToObjectStateMachine(smach.StateMachine):
    """
    Given an object and it's position moves the arm
    to it's position first stopping on a pregrasp
    position.

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
    If the input_keys aren't fullfilled this state aborts.
    """
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=['transformed_object_data', 'object_data'])

        with self:

            smach.StateMachine.add(
            'Check_if_object_specified',
            Check_if_object_specified(),
            transitions={succeeded: 'N2_APPROACH_PREGRASPING_POSITION', aborted: aborted})

            ### refresh collision map here! To implement when it works!

            # smach.StateMachine.add(
            #     'REFRESH_COLLISION_MAP',
            #     ServiceState('/refresh_collision_map/refresh', Empty),
            #     transitions = {succeeded:'WAIT_FOR_COLLISION_MAP_UPDATE'})

            # smach.StateMachine.add(
            #     'WAIT_FOR_COLLISION_MAP_UPDATE',
            #     WaitForCollisionMapUpdate(),
            #     transitions = {succeeded: 'N2_APPROACH_PREGRASPING_POSITION'})

            def arm_goal_cb(userdata, old_goal):
                #TODO: Move the arm to a position -19cm from the object in some more intelligent way, maybe just play with the orientation of the hand
                userdata.transformed_object_data.pose.orientation = Quaternion(0.5, -0.5, 0.5, -0.5)  # euler equivalent: (-1.57079632679, -0.0, -1.57079632679)
                #"yaw -pi/2, pitch 0, roll  -pi/2 +pi/8: -1.57079632679,  0, -1.57079632679 +0.785398/2"
                #userdata.transformed_object_data.pose.orientation = Quaternion(*quaternion_from_euler(-1.57079632679 -0.785398 , -0.0, -1.57079632679 +0.785398/2))
                #userdata.transformed_object_data.pose.orientation = Quaternion(-0.587937785162, 0.392847503208, -0.39284750321, 0.587937785165)
                rospy.loginfo("Now we will substract 18cm to X to reach the pre-grasping position and we will change the orientation to a good known one")
                goal_for_pregrasping = copy.deepcopy(userdata.transformed_object_data.pose)
                rospy.loginfo("thsi is goal_for_pregrasping: " + str(goal_for_pregrasping))
                goal_for_pregrasping.position.x -= 0.18
                goal_for_pregrasping.position.y -= 0.05
                rospy.loginfo("Now we send the goal:\n" + str(goal_for_pregrasping))
                arm_goal = get_arm_goal(goal_for_pregrasping, frame_id="/base_link")
                return arm_goal

            ## !!! callback used on all MoveArmActions
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

            smach.StateMachine.add(
            'N2_APPROACH_PREGRASPING_POSITION',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                result_cb=arm_result_cb,
                input_keys=['object_data', 'transformed_object_data']),
                transitions={succeeded: 'N2_APPROACH_FINAL_GRASPING_POSITION', aborted: 'N2_APPROACH_PREGRASPING_POSITION'})

           ### reset collision map here so we can really approach to the object

            # smach.StateMachine.add(
            #     'RESET_COLLISION_MAP',
            #     ServiceState('refresh_collision_map_reset/refresh_reset', Empty),
            #     transitions = {succeeded:'N2_APPROACH_FINAL_GRASPING_POSITION'})

            def arm_goal_cb(userdata, old_goal):
                #TODO: Move the arm to a position -14cm from the object in some more intelligent way, maybe just play with the orientation of the hand
                userdata.transformed_object_data.pose.orientation = Quaternion(0.5, -0.5, 0.5, -0.5)
                #userdata.transformed_object_data.pose.orientation = Quaternion(*quaternion_from_euler(-1.57079632679 -0.785398 , -0.0, -1.57079632679 +0.785398/2))
                #userdata.transformed_object_data.pose.orientation = Quaternion(-0.587937785162, 0.392847503208, -0.39284750321, 0.587937785165)

                rospy.loginfo("Now we will substract 14cm to X to reach the pre-grasping position and we will change the orientation to a good known one")
                goal_for_pregrasping = copy.deepcopy(userdata.transformed_object_data.pose)
                goal_for_pregrasping.position.x -= 0.12  # Testing 1cm less, was 14cm
                goal_for_pregrasping.position.y -= 0.01
                rospy.loginfo("Now we send the goal:\n" + str(goal_for_pregrasping))
                arm_goal = get_arm_goal(goal_for_pregrasping, frame_id="/base_link")
                return arm_goal

            smach.StateMachine.add(
            'N2_APPROACH_FINAL_GRASPING_POSITION',
            SimpleActionState(
                'move_right_arm_torso',  # WE MUST CHANGE THIS LAST MOVEMENT TO USE HILARIOuS INTERPOLATED MOVEMENT WHEN ITS OK TO USE
                MoveArmAction,
                goal_cb=arm_goal_cb,
                result_cb=arm_result_cb,
                input_keys=['object_data', 'transformed_object_data']),
                transitions={succeeded: succeeded, aborted: 'N2_APPROACH_FINAL_GRASPING_POSITION'})
