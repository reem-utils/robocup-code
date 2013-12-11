#! /usr/bin/env python

import roslib;roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import copy
import actionlib
from actionlib_msgs.msg import GoalStatus
from std_msgs.msg import *
from geometry_msgs.msg import *
from smach_ros import SimpleActionState, ServiceState
from geometry_msgs.msg import Pose, Point, Quaternion
from visualization_msgs.msg import Marker
from tf.transformations import quaternion_from_euler, euler_from_quaternion

from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.utils.global_common import *
from pal_smach_utils.navigation.move_action import *
#from pal_smach_utils.door_interaction.get_door_handle_position import *
from door_detector_pal.msg import *



class create_door_handle_goal_move_position(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], input_keys=['door_detection_data_in_base_link'], output_keys=['door_handle_pose_goal'])

    def execute(self, userdata):
        rospy.loginfo("Creating goal to put robot in front of handle")
        pose_handle = Pose()
        if userdata.door_detection_data_in_base_link.handle_side == "left" or userdata.door_detection_data_in_base_link.handle_side == "right":  # closed door
            (r, p, theta) = euler_from_quaternion(( userdata.door_detection_data_in_base_link.door_handle.pose.orientation.x,
                                                    userdata.door_detection_data_in_base_link.door_handle.pose.orientation.y,
                                                    userdata.door_detection_data_in_base_link.door_handle.pose.orientation.z,
                                                    userdata.door_detection_data_in_base_link.door_handle.pose.orientation.w))  # gives back r, p, y
            theta += 3.1416  # the orientation of the door is looking towards the robot, we need the inverse
            pose_handle.orientation = Quaternion(*quaternion_from_euler(0, 0, theta))  # orientation to look parallel to the door
            pose_handle.position.x = userdata.door_detection_data_in_base_link.door_handle.pose.position.x - 0.4  # to align the shoulder with the handle
            pose_handle.position.y = userdata.door_detection_data_in_base_link.door_handle.pose.position.y + 0.2  # refer to upper comment
            pose_handle.position.z = 0.0  # we dont need the Z for moving
            userdata.door_handle_pose_goal = pose_handle
        else:  # open door
            # if it's open... just cross it?
            (r, p, theta) = euler_from_quaternion(( userdata.door_detection_data_in_base_link.door_position.pose.orientation.x,
                                                    userdata.door_detection_data_in_base_link.door_position.pose.orientation.y,
                                                    userdata.door_detection_data_in_base_link.door_position.pose.orientation.z,
                                                    userdata.door_detection_data_in_base_link.door_position.pose.orientation.w))  # gives back r, p, y
            theta += 3.1416  # the orientation of the door is looking towards the robot, we need the inverse
            pose_handle.orientation = Quaternion(*quaternion_from_euler(0, 0, theta))  # orientation to look parallel to the door
            pose_handle.position.x = userdata.door_detection_data_in_base_link.door_position.pose.position.x + 1.0 # enter the door
            pose_handle.position.y = userdata.door_detection_data_in_base_link.door_position.pose.position.y
            userdata.door_handle_pose_goal = pose_handle


        rospy.loginfo("Move base goal: \n" + str(pose_handle))

        return succeeded

# class Activate_door_detection(smach.State):

#     def __init__(self):
#         smach.State.__init__(self, outcomes=[succeeded, aborted])

#     def execute(self, userdata):
#         pub = rospy.Publisher('/iri_door_detector/door_detector_actions/door_action_start', std_msgs.msg.Int8, latch=True)  # I must latch or the listener sometimes loses topic pubs
#         pub.publish(std_msgs.msg.Int8(1))  # Maybe check if it was already running...
#         return succeeded


# class Deactivate_door_detection(smach.State):

#     def __init__(self):
#         smach.State.__init__(self, outcomes=[succeeded, aborted])

#     def execute(self, userdata):
#         pub = rospy.Publisher('/iri_door_detector/door_detector_actions/door_action_start', std_msgs.msg.Int8, latch=True)  # I must latch or the listener sometimes loses topic pubs
#         pub.publish(std_msgs.msg.Int8(0))  # Maybe check if it was already running...
#         return succeeded

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


class ApproachDoorStateMachine(smach.StateMachine):
    """
    Gets the robot in front of the door handle.

    Required parameters:
    No parameters.

    Optional parameters:
    No optional parameters.


    No input keys.
    No output keys.
    No io_keys.

    Robot should be positioned in front of the door handle after this state.
    """

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:

            # smach.StateMachine.add('Get_door_handle_pose',
            #     GetDoorHandlePoseStateMachine(),
            #     remapping={'door_handle_in_base_link': 'door_handle_in_base_link'},
            #     transitions={succeeded: 'Activate_door_detection'})


            # # Activate door detection
            # smach.StateMachine.add(
            # 'Activate_door_detection',
            # Activate_door_detection(),
            # transitions={succeeded: 'Get_door_orientation', aborted: aborted})

            # smach.StateMachine.add(
            #         'Get_door_orientation',
            #         TopicReaderState(
            #                          topic_name='/iri_door_detector/door_cloud/closed_door_marker',
            #                          msg_type=Marker,
            #                          timeout=10),
            #         remapping={'message': 'door_orientation_marker'},
            #         transitions={succeeded: 'Deactivate_door_detection', aborted: 'Get_door_orientation'})


            def door_goal_cb(userdata, old_goal):
                door_goal = DoorDetectorGoal()
                door_goal.votation = 3  # number of voting

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

            # smach.StateMachine.add(
            # 'Deactivate_door_detection',
            # Deactivate_door_detection(),
            # transitions={succeeded: 'Transform_orientation_reference_frame', aborted: aborted})

            smach.StateMachine.add('Transform_orientation_reference_frame',
                                    TransformOrientationReferenceFrame(),
                                    transitions={succeeded: 'Create_goal_for_moving_to_door', aborted: aborted})



            smach.StateMachine.add('Create_goal_for_moving_to_door',
                                    create_door_handle_goal_move_position(),
                                    remapping={'door_handle_pose_goal': 'door_handle_pose_goal',
                                    'door_detection_data_in_base_link': 'door_detection_data_in_base_link'},
                                    transitions={succeeded: 'Move_to_door'})

            smach.StateMachine.add('Move_to_door',
                        MoveActionState(frame_id="/base_link", move_base_action_name="/move_by/move_base", goal_key='door_handle_pose_goal'),
                        transitions={succeeded: succeeded, aborted: aborted, preempted: aborted})
