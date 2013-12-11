#! /usr/bin/env python

import roslib;roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import copy
import actionlib
from std_msgs.msg import *
from geometry_msgs.msg import *
from smach_ros import SimpleActionState, ServiceState
from geometry_msgs.msg import Pose, Point, Quaternion
from visualization_msgs.msg import Marker
from tf.transformations import quaternion_from_euler, euler_from_quaternion

from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.utils.global_common import *
from pal_smach_utils.navigation.move_action import *
from pal_smach_utils.door_interaction.approach_door import *
from pal_smach_utils.door_interaction.open_door import *
from attention_system.srv import *


# class create_door_handle_goal_move_position(smach.State):
#     def __init__(self):
#         smach.State.__init__(self, outcomes=[succeeded], input_keys=['door_handle_in_base_link', 'door_orientation_marker_in_base_link'], output_keys=['door_handle_pose_goal'])

#     def execute(self, userdata):
#         rospy.loginfo("Creating goal to put robot in front of handle")
#         pose_handle = Pose()
#         (r, p, theta) = euler_from_quaternion((userdata.door_orientation_marker_in_base_link.pose.orientation.x,
#         userdata.door_orientation_marker_in_base_link.pose.orientation.y,
#         userdata.door_orientation_marker_in_base_link.pose.orientation.z,
#         userdata.door_orientation_marker_in_base_link.pose.orientation.w))  # gives back r, p, y
#         theta += 3.1416  # the orientation of the door is looking towards the robot, we need the contrary
#         pose_handle.orientation = Quaternion(*quaternion_from_euler(0, 0, theta))  # orientation to look parallel to the door
#         pose_handle.position.x = userdata.door_handle_in_base_link.pose.position.x - 0.4  # to align the shoulder with the handle
#         pose_handle.position.y = userdata.door_handle_in_base_link.pose.position.y + 0.2  # refer to upper comment
#         pose_handle.position.z = 0.0  # we dont need the Z for moving
#         userdata.door_handle_pose_goal = pose_handle

#         return succeeded

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

# class TransformOrientationReferenceFrame(smach.State):

#     def __init__(self):
#         smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys=['door_handle_in_base_link', 'door_orientation_marker', 'door_orientation_marker_in_base_link'], output_keys=['door_orientation_marker_in_base_link'])

#     def execute(self, userdata):
#         rospy.loginfo("Transforming pose of door orientation from /head_mount_xtion_rgb_optical_frame to base_link frame.")
#         pose_door_marker = Pose()
#         pose_door_marker.orientation = userdata.door_orientation_marker.pose.orientation
#         pose_door_marker.position = userdata.door_orientation_marker.pose.position
#         pose_in_base_link = transform_pose(pose_door_marker, src_frame="/head_mount_xtion_rgb_optical_frame", dst_frame="/base_link", timeout=30)
#         userdata.door_orientation_marker_in_base_link = copy.deepcopy(userdata.door_handle_in_base_link)  # to allocate message
#         userdata.door_orientation_marker_in_base_link.pose = pose_in_base_link
#         rospy.loginfo("tf returns the pose transformed:\n" + str(pose_in_base_link))
#         if(pose_in_base_link == pose_door_marker):
#             return aborted
#         return succeeded

class AskForViewResource(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted])

    def execute(self, userdata):
        rospy.wait_for_service('/attention_system/ask_for_resource')
        try:
            look_at = rospy.ServiceProxy('/attention_system/ask_for_resource', AttentionResource)
            resp = look_at("DOOR")
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e
            return aborted
        if resp:
            return succeeded
        else:
            return aborted


class ReleaseViewResource(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted])

    def execute(self, userdata):
        rospy.wait_for_service('/attention_system/release_resource')
        try:
            look_at = rospy.ServiceProxy('/attention_system/release_resource', AttentionResource)
            resp = look_at("DOOR")
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e
            return aborted
        if resp:
            return succeeded
        else:
            return aborted


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


class DecideIfDoorIsOpen(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys=['door_detection_data_in_base_link'])

    def execute(self, userdata):
        if userdata.door_detection_data_in_base_link.door_status == "open":
                return succeeded
        else:
            return aborted


class create_move_back_goal_move_position(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys=['goal_pose'])

    def execute(self, userdata):
        pose_obj = Pose()
        pose_obj.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
        pose_obj.position.y = 0.0
        pose_obj.position.z = 0.0
        pose_obj.position.x = -1.0
        userdata.goal_pose = pose_obj
        rospy.loginfo("CREATED GOAL TO GO BACK:\n" + str(pose_obj))

        return succeeded


class EnterDoorStateMachine(smach.StateMachine):
    """
    Enters the door in front (opening it if necessary).

    Required parameters:
    No parameters.

    Optional parameters:
    No optional parameters.


    No input keys.
    No output keys.
    No io_keys.

    Robot should have entered the door in front of him.
    """

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:
            # ask for attention system resource
            # service  /attention_system/ask_for_resource "door"
            smach.StateMachine.add('Ask_for_view_resource',
                        AskForViewResource(),
                        transitions={succeeded: 'Ask_for_door_status', aborted: aborted})


            # Ask for door status
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
                                    transitions={succeeded: 'Decide_if_door_is_open', aborted: aborted})

            smach.StateMachine.add('Decide_if_door_is_open',
                                    DecideIfDoorIsOpen(),
                                    transitions={succeeded: 'Approach_and_enter_door', aborted: 'Approach_and_open_door'})  # succeeded when door is open, aborted otherwise

            # If door closed, approach, open and enter
            smach.StateMachine.add('Approach_and_open_door',
                                    ApproachDoorStateMachine(),
                                    transitions={succeeded: 'Open_door', aborted: aborted})

            smach.StateMachine.add('Open_door',
                                    OpenDoorStateMachine(),
                                    transitions={succeeded: 'Move_back_goal_creation', aborted: aborted})

            # Go back (and put decent body pose?)
            smach.StateMachine.add('Move_back_goal_creation',
                                    create_move_back_goal_move_position(),
                                    transitions={succeeded: 'Move_back'})

            smach.StateMachine.add('Move_back',
                                    MoveActionState("/base_link", move_base_action_name="/move_by/move_base", goal_key='goal_pose'),
                                    transitions={succeeded: 'Approach_and_enter_after_going_back', aborted: aborted, preempted: aborted})

            # Enter door after detecting it again
            smach.StateMachine.add('Approach_and_enter_after_going_back',
                                    ApproachDoorStateMachine(),
                                    transitions={succeeded: succeeded, aborted: aborted})

            # Enter door
            # If door open, approach and enter directly (approach door sm already does that if its open)
            smach.StateMachine.add('Approach_and_enter_door',
                                    ApproachDoorStateMachine(),
                                    transitions={succeeded: 'Release_view_resource', aborted: aborted})

            # Release attention system resource
            # /attention_system/release_resource
            # service
            smach.StateMachine.add('Release_view_resource',
                        ReleaseViewResource(),
                        transitions={succeeded: succeeded, aborted: aborted})




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

            # smach.StateMachine.add(
            # 'Deactivate_door_detection',
            # Deactivate_door_detection(),
            # transitions={succeeded: 'Transform_orientation_reference_frame', aborted: aborted})

            # smach.StateMachine.add('Transform_orientation_reference_frame',
            #                         TransformOrientationReferenceFrame(),
            #                         transitions={succeeded: 'Create_goal_for_moving_to_door', aborted: aborted})



            # smach.StateMachine.add('Create_goal_for_moving_to_door',
            #                         create_door_handle_goal_move_position(),
            #                         remapping={'door_handle_pose_goal': 'door_handle_pose_goal',
            #                         'door_orientation_marker': 'door_orientation_marker',
            #                         'door_orientation_marker_in_base_link': 'door_orientation_marker_in_base_link'},
            #                         transitions={succeeded: 'Move_to_door'})

            # smach.StateMachine.add('Move_to_door',
            #             MoveActionState(frame_id="/base_link", move_base_action_name="/move_by_unsafe/move_base", goal_key='door_handle_pose_goal'),
            #             transitions={succeeded: succeeded, aborted: aborted, preempted: aborted})
