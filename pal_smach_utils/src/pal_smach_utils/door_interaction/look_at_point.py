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
from tf.transformations import quaternion_from_euler

from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.utils.global_common import *
from pal_smach_utils.navigation.move_action import *
from pal_smach_utils.door_interaction.get_door_handle_position import *


class Look_at_handle(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], input_keys=['door_handle_in_base_link'], output_keys=['door_handle_pose_goal'])

    def execute(self, userdata):
        pose_handle = Pose()
        pose_handle.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))  # making sure it's 0
        pose_handle.position.x = userdata.door_handle_in_base_link.pose.position.x
        pose_handle.position.y = userdata.door_handle_in_base_link.pose.position.y
        pose_handle.position.z = 0.0  # we dont need the Z for moving
        userdata.door_handle_pose_goal = pose_handle

        return succeeded


class ApproachDoorStateMachine(smach.StateMachine):
    """
    Make the robot look to a point.

    Required parameters:
    No parameters.

    Optional parameters:
    No optional parameters.


    No input keys.
    No output keys.
    No io_keys.

    Robot will look at the point passed in the userdata bla
    """

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:

            smach.StateMachine.add('Get_door_handle_pose',
                GetDoorHandlePoseStateMachine(),
                remapping={'door_handle_in_base_link': 'door_handle_in_base_link'},
                transitions={succeeded: 'Look_at_handle'})

            smach.StateMachine.add('Look_at_handle',
                Look_at_handle(),
                transitions={succeeded: succeeded})
