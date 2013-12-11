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
    rospy.init_node('complete_grasp_pipeline_test_reset')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

            smach.StateMachine.add(
            'reset_collision_map',
            ResetCollisionMapStateMachine(),
            transitions={succeeded: succeeded, aborted: aborted})




    sis = smach_ros.IntrospectionServer(
        'complete_grasp_pipeline_test_reset_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
