#! /usr/bin/env python

import roslib; roslib.load_manifest('grasp_test')
import rospy
import smach
import smach_ros
import actionlib

#from smach_ros import SimpleActionState, ServiceState
from std_msgs import *

from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.grasping.arm_and_hand_goals import *
from pal_smach_utils.grasping.arm_movement_to_object import *


class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys=['transformed_object_data', 'object_data'])

    def execute(self, userdata):
        print "Dummy state to go to  ArmMovementToObjectStateMachine initializing transformed_object_data and object_data"
        print "[            =D                ]"
        rospy.sleep(5)  # in seconds

        msg = ObjectPoseList()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "/openni_depth_frame"
        msg.object_list = [None] * 2
        msg.object_list[0] = ObjectPose()
        msg.object_list[0].name = "pringles"
        msg.object_list[0].pose = Pose()
        msg.object_list[0].pose.position.x = 0.611990241005
        msg.object_list[0].pose.position.y = -0.317951137319
        msg.object_list[0].pose.position.z = -0.38978881074
        msg.object_list[0].pose.orientation.x = 0.946857988834
        msg.object_list[0].pose.orientation.y = -0.0297971088439
        msg.object_list[0].pose.orientation.z = -0.295009255409
        msg.object_list[0].pose.orientation.w = 0.12466647476
        userdata.object_data = msg

        msgt = ObjectPoseList()
        msgt.header.stamp = rospy.Time.now()
        msgt.header.frame_id = "/base_link"
        msgt.object_list = [None] * 2
        msgt.object_list[0] = ObjectPose()
        msgt.object_list[0].name = "pringles"
        msgt.object_list[0].pose = Pose()
        msgt.object_list[0].pose.position.x = 0.3
        msgt.object_list[0].pose.position.y = -0.3
        msgt.object_list[0].pose.position.z = 1.13
        msgt.object_list[0].pose.orientation.x = 0.5
        msgt.object_list[0].pose.orientation.y = -0.5
        msgt.object_list[0].pose.orientation.z = 0.5
        msgt.object_list[0].pose.orientation.w = -0.5
        userdata.transformed_object_data = msgt.object_list[0]

        return succeeded


def main():
    rospy.init_node('sm_search_and_grasp_test_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        # Using this state to wait and to initialize object_to_search_for input_key (needed by SearchAndGraspStateMachine() )
        smach.StateMachine.add(
            'dummy_state',
            DummyStateMachine(),
            transitions={succeeded: 'SM_grasp'})

        smach.StateMachine.add(
            'SM_grasp',
            ArmMovementToObjectStateMachine(),
            transitions={succeeded: succeeded, aborted: aborted})

         # NOT USING ANYTHING  MORE

    sis = smach_ros.IntrospectionServer(
        'sm_search_and_grasp_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
