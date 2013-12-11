#! /usr/bin/env python

import roslib
roslib.load_manifest('complete_grasp_pipeline_test')
import rospy
import copy
import smach
import math
import smach_ros

from smach_ros import SimpleActionState, ServiceState
from pal_smach_utils.utils.global_common import *
from pal_smach_utils.grasping.complete_grasp_pipeline import CompleteGraspPipelineStateMachine
from trajectory_msgs.msg import *
from control_msgs.msg import *
from pal_smach_utils.grasping.arm_and_hand_goals import *

from pal_smach_utils.grasping.reset_collision_map import ResetCollisionMapStateMachine


def main():
    rospy.init_node('complete_grasp_pipeline_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:
            sm.userdata.object_to_search_for = "coke"
            smach.StateMachine.add(
            'CompleteGraspPipelineStateMachine_call',
            CompleteGraspPipelineStateMachine(),
            transitions={succeeded: 'Hand_to_normal_position', aborted: aborted})


            def grasp_arm_goal_cb(userdata, old_goal):
                grasp_msg = get_fully_open_hand()
                return grasp_msg

            smach.StateMachine.add(
            'Hand_to_normal_position',
            SimpleActionState(
                '/right_hand_controller/follow_joint_trajectory',
                FollowJointTrajectoryAction,
                goal_cb=grasp_arm_goal_cb),
                transitions={succeeded: 'reset_collision_map', aborted: aborted})

            smach.StateMachine.add(
            'reset_collision_map',
            ResetCollisionMapStateMachine(),
            transitions={succeeded: succeeded, aborted: aborted})




    sis = smach_ros.IntrospectionServer(
        'complete_grasp_pipeline_test_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
