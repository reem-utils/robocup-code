#! /usr/bin/env python

import roslib; roslib.load_manifest('complete_grasp_pipeline_test')
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
from pal_smach_utils.grasping.arm_movement_to_travel import *
from pal_smach_utils.grasping.arm_movement_grasp_sequence import *

from pal_smach_utils.grasping.give_me_object import *

class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], input_keys=['object_to_search_for', 'object_found'], output_keys=['object_to_search_for', 'object_found'])

    def execute(self, userdata):
        print "Setting up userdata with: "

        userdata.object_to_search_for = "coke"

        msg = ObjectPoseList()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "/openni_depth_frame"
        msg.object_list = [None] * 2
        msg.object_list[0] = ObjectPose()
        msg.object_list[0].name = "coke"
        msg.object_list[0].pose = Pose()
        msg.object_list[0].pose.position.x = 0.611990241005
        msg.object_list[0].pose.position.y = -0.317951137319
        msg.object_list[0].pose.position.z = -0.38978881074
        msg.object_list[0].pose.orientation.x = 0.946857988834
        msg.object_list[0].pose.orientation.y = -0.0297971088439
        msg.object_list[0].pose.orientation.z = -0.295009255409
        msg.object_list[0].pose.orientation.w = 0.12466647476
        userdata.object_found = msg


        print userdata.object_to_search_for
        print userdata.object_found

        return succeeded


def main():
    rospy.init_node('sm_test_thing')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        # Using this state to wait and to initialize object_to_search_for input_key (needed by SearchAndGraspStateMachine() )
        smach.StateMachine.add(
            'dummy_state',
            DummyStateMachine(),
            transitions={succeeded: 'GiveMeObjectStateMachine'})

        smach.StateMachine.add(
                    'GiveMeObjectStateMachine',
                    GiveMeObjectStateMachine(),
                    transitions={succeeded: succeeded, aborted: aborted})
         # NOT USING ANYTHING  MORE

    sis = smach_ros.IntrospectionServer(
        'sm_test_thing_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
