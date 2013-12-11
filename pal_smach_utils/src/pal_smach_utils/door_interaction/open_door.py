#! /usr/bin/env python

import roslib;roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import copy
import actionlib
from smach_ros import SimpleActionState, ServiceState
from std_msgs.msg import *
from geometry_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion
from arm_navigation_msgs.msg import *
from tf.transformations import quaternion_from_euler
from actionlib_msgs.msg import GoalStatus

from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.utils.global_common import *
#from pal_smach_utils.door_interaction.get_door_handle_position import *
from pal_smach_utils.grasping.arm_and_hand_goals import *
from door_detector_pal.msg import *



class dummy_state(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted])

    def execute(self, userdata):
        return succeeded

class TransformOrientationReferenceFrame(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys=['door_detection_data', 'door_detection_data_in_base_link'], output_keys=['door_detection_data_in_base_link'])

    def execute(self, userdata):
        rospy.loginfo("Transforming pose of door orientation from /head_mount_xtion_rgb_optical_frame to base_link frame.")
        pose_door = Pose()
        userdata.door_detection_data_in_base_link = copy.deepcopy(userdata.door_detection_data)  # to allocate message
        if userdata.door_detection_data.handle_side == "left" or userdata.door_detection_data.handle_side == "right":  # closed door
            pose_door = userdata.door_detection_data.door_handle.pose
            pose_in_base_link = transform_pose(pose_door, src_frame="/head_mount_xtion_rgb_optical_frame", dst_frame="/base_link", timeout=30)
            userdata.door_detection_data_in_base_link.door_handle.pose = pose_in_base_link
        else:  # open door
            pose_door = userdata.door_detection_data.door_position.pose
            pose_in_base_link = transform_pose(pose_door, src_frame="/head_mount_xtion_rgb_optical_frame", dst_frame="/base_link", timeout=30)
            userdata.door_detection_data_in_base_link.door_position.pose = pose_in_base_link

        rospy.loginfo("tf returns the pose transformed:\n" + str(pose_in_base_link))
        if userdata.door_detection_data.handle_side == "left" or userdata.door_detection_data.handle_side == "right":
            if(pose_in_base_link == userdata.door_detection_data.door_handle.pose):
                return aborted
            return succeeded
        else:
            if(pose_in_base_link == userdata.door_detection_data.door_position.pose):
                return aborted
            return succeeded


class OpenDoorStateMachine(smach.StateMachine):
    """
    Opens the door.

    Required parameters:
    No parameters.

    Optional parameters:
    No optional parameters.


    No input keys.
    No output keys.
    No io_keys.

    The robot should be positioned in front of the door, then it opens it.
    """

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:


            def door_goal_cb(userdata, old_goal):
                door_goal = DoorDetectorGoal()
                door_goal.votation = 9  # number of voting

                return door_goal

            def door_result_cb(userdata, result_status, result):
                if result_status != GoalStatus.SUCCEEDED:  # SUCCEEDED = 3 http://www.ros.org/doc/api/move_arm_msgs/html/msg/MoveArmActionResult.html
                    rospy.loginfo("Result wasn't succeeded, was: " + str(result_status) +
                        "\nmessage: \n" + str(result))
                    return aborted
                else:
                    # Do awesome stuff with the door data
                    rospy.loginfo("Result from  /door_detector_action_server was: \n" + str(result))
                    userdata.door_detection_data = result
                    if result.door_status == "open":  # makes no sense to open an open door
                        return aborted
                    else:
                        return succeeded

            # def door_feedback_cb(userdata, feedback_msg):
            #     rospy.loginfo("Got the feedback: " + str(feedback_msg))
            #     return succeeded

            smach.StateMachine.add(
            'Ask_for_door_status',
            SimpleActionState(
                '/iri_door_detector/door_detector_action_server',
                DoorDetectorAction,
                goal_cb=door_goal_cb,
                result_cb=door_result_cb,
                output_keys=['door_detection_data']),
                #feedback_cb=door_feedback_cb),
                remapping={'door_detection_data': 'door_detection_data'},
                transitions={succeeded: 'Transform_orientation_reference_frame', aborted: aborted})


            smach.StateMachine.add('Transform_orientation_reference_frame',
                                    TransformOrientationReferenceFrame(),
                                    transitions={succeeded: 'Arm_to_pre_opening_position', aborted: aborted})


            # smach.StateMachine.add('Get_door_handle_pose',
            #     GetDoorHandlePoseStateMachine(),
            #     remapping={'door_handle_in_base_link': 'door_handle_in_base_link'},
            #     transitions={succeeded: 'Arm_to_pre_opening_position', aborted: 'Get_door_handle_pose'})

            # move arm to pre-opening motion pose
            def arm_goal_cb(userdata, old_goal):
                arm_goal_pose = get_pose_for_arm_pre_door_opening()
                arm_goal = get_arm_goal(arm_goal_pose.pose)
                return arm_goal

            def arm_result_cb(userdata, result_status, result):
                if result_status != GoalStatus.SUCCEEDED:
                    rospy.loginfo("MoveArmActionResult result wasn't succeeded, was: " + str(result_status) +
                        "\nmessage: \n" + str(result))
                    return aborted
                else:
                    return succeeded

            smach.StateMachine.add(
            'Arm_to_pre_opening_position',
            SimpleActionState(
                'move_right_arm_torso',  # testing with left arm /move_left_arm
                MoveArmAction,
                goal_cb=arm_goal_cb,
                result_cb=arm_result_cb,
                input_keys=['door_detection_data_in_base_link']),
                transitions={succeeded: 'Arm_to_over_handle', aborted: aborted})  # if we abort we may need to reposition the robot

            fake_dist = 0.2
            

            # rectilinear movement to handle
            def arm_goal_cb(userdata, old_goal):
                arm_goal_pose = copy.deepcopy(userdata.door_detection_data_in_base_link.door_handle)

                # Moving the hand a little bit to the side of the handle detection to push... well, the handle, the pushable part!
                if userdata.door_detection_data_in_base_link.handle_side == "left":
                    arm_goal_pose.pose.position.y = arm_goal_pose.pose.position.y - 0.03
                elif userdata.door_detection_data_in_base_link.handle_side == "right":
                    arm_goal_pose.pose.position.y = arm_goal_pose.pose.position.y + 0.03
                arm_goal_pose.pose.position.x = arm_goal_pose.pose.position.x - 0.19 - fake_dist  # lie to the robot and tell him that the handle is a lot closer # 19cm of hand
                arm_goal_pose.pose.position.z = arm_goal_pose.pose.position.z + 0.05  # move the arm a little bit upside of the handle
                arm_goal_pose.pose.orientation.x = 0.7156
                arm_goal_pose.pose.orientation.y = -0.0113
                arm_goal_pose.pose.orientation.z = 0.6982
                arm_goal_pose.pose.orientation.w = -0.0115

                arm_goal = get_arm_goal(arm_goal_pose.pose)
                rospy.loginfo("arm goal to send: " + str(arm_goal_pose))
                return arm_goal

            smach.StateMachine.add(
            'Arm_to_over_handle',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                result_cb=arm_result_cb,
                input_keys=['door_detection_data_in_base_link']),
                transitions={succeeded: 'Arm_to_down_push_handle', aborted: aborted})

            # rectilinear movement down
            def arm_goal_cb(userdata, old_goal):
                arm_goal_pose = copy.deepcopy(userdata.door_detection_data_in_base_link.door_handle)

                #arm_goal_pose.pose.x =
                #arm_goal_pose.pose.y =  # maybe depeding on the side of the handle move a bit to the other side (to push down easier the handle)
                arm_goal_pose.pose.position.x = arm_goal_pose.pose.position.x - 0.19 - fake_dist  # lie to the robot and tell him that the handle is a lot closer
                arm_goal_pose.pose.position.z = arm_goal_pose.pose.position.z - 0.05  # move the arm a little bit upside of the handle
                arm_goal_pose.pose.orientation.x = 0.7156
                arm_goal_pose.pose.orientation.y = -0.0113
                arm_goal_pose.pose.orientation.z = 0.6982
                arm_goal_pose.pose.orientation.w = -0.0115

                arm_goal = get_arm_goal(arm_goal_pose.pose)
                rospy.loginfo("arm goal to send: " + str(arm_goal_pose))
                return arm_goal

            smach.StateMachine.add(
            'Arm_to_down_push_handle',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                result_cb=arm_result_cb,
                input_keys=['door_detection_data_in_base_link']),
                transitions={succeeded: 'Arm_to_front_push_door', aborted: aborted})

            # push handle to open the door
            def arm_goal_cb(userdata, old_goal):
                arm_goal_pose = copy.deepcopy(userdata.door_detection_data_in_base_link.door_handle)

                #arm_goal_pose.pose.x =
                #arm_goal_pose.pose.y =  # maybe depeding on the side of the handle move a bit to the other side (to push down easier the handle)
                arm_goal_pose.pose.position.x = arm_goal_pose.pose.position.x - 0.19 - fake_dist + 0.1  # lie to the robot and tell him that the handle is a lot closer
                arm_goal_pose.pose.position.z = arm_goal_pose.pose.position.z - 0.05  # move the arm a little bit upside of the handle
                arm_goal_pose.pose.orientation.x = 0.7156
                arm_goal_pose.pose.orientation.y = -0.0113
                arm_goal_pose.pose.orientation.z = 0.6982
                arm_goal_pose.pose.orientation.w = -0.0115

                arm_goal = get_arm_goal(arm_goal_pose.pose)
                rospy.loginfo("arm goal to send: " + str(arm_goal_pose))
                return arm_goal

            smach.StateMachine.add(
            'Arm_to_front_push_door',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                result_cb=arm_result_cb,
                input_keys=['door_detection_data_in_base_link']),
                transitions={succeeded: 'Arm_to_safe_pos', aborted: aborted})



            def arm_goal_cb(userdata, old_goal):
                #arm_goal = get_arm_goal_for_arm_down()
                arm_goal_pose = get_pose_for_arm_down()
                arm_goal = get_arm_goal(arm_goal_pose.pose)
                return arm_goal

            smach.StateMachine.add(
            'Arm_to_safe_pos',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                result_cb=arm_result_cb,
                input_keys=['door_detection_data_in_base_link']),
                transitions={succeeded: succeeded, aborted: aborted})

            # now, outside of this sm, we should move the robot inside
