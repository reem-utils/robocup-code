#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from smach_ros import SimpleActionState
from actionlib_msgs.msg import GoalStatus

from arm_navigation_msgs.msg import MoveArmAction
from pal_smach_utils.grasping.arm_and_hand_goals import get_fully_open_hand
from control_msgs.msg import FollowJointTrajectoryAction
from pal_smach_utils.grasping.arm_and_hand_goals import get_pose_for_arm_in_front
from pal_smach_utils.grasping.arm_and_hand_goals import get_arm_goal, get_arm_goal_for_arm_down
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers


def main():
    """Run the same code used by ServeOrdersStateMachine when serving the drink to a person.
    The controllers will be activated, the robot will put the hand in front, open it fully
    and move the hand to initial position again."""

    rospy.init_node('test_release_object')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:

            sm.add(
                "START_ALL_CONTROLLERS",
                StartRobotControllers(head=True, left=True, right=True),
                transitions={succeeded: "HAND_IN_FRONT", aborted: "START_ALL_CONTROLLERS", preempted: "START_ALL_CONTROLLERS"}
                )

            def hand_in_front_goal_cb(userdata, old_goal):
                releasing_object_pose = get_pose_for_arm_in_front()
                arm_goal = get_arm_goal(releasing_object_pose, frame_id="/base_link")
                return arm_goal

            sm.add(
                "HAND_IN_FRONT",
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal_cb=hand_in_front_goal_cb),
                transitions={succeeded: "OPEN_HAND_FULLY", aborted: "HAND_IN_FRONT"})

            def open_hand_fully_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED:
                    return succeeded
                else:  # TODO: See if this is important, Hilario says maybe it's a problem of gazebo
                    rospy.loginfo("Other than succeded: result of right_hand_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code))
                    if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
                        rospy.loginfo("Continuing even with this error as it's not really aborted...")
                        return succeeded
                    else:
                        return aborted

            sm.add(
                "OPEN_HAND_FULLY",
                SimpleActionState(
                    '/right_hand_controller/follow_joint_trajectory',
                    FollowJointTrajectoryAction,
                    goal=get_fully_open_hand(),
                    result_cb=open_hand_fully_result_cb,
                    input_keys=['releasing_position']),
                transitions={succeeded: 'ARM_TO_SAFE_POSITION', aborted: "OPEN_HAND_FULLY"})

            sm.add(
                "ARM_TO_SAFE_POSITION",
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal=get_arm_goal_for_arm_down()),
                transitions={succeeded: "STOP_ALL_CONTROLLERS", aborted: "ARM_TO_SAFE_POSITION", preempted: "ARM_TO_SAFE_POSITION"})

            sm.add(
                "STOP_ALL_CONTROLLERS",
                StopRobotControllers(head=True, left=True, right=True)
                #transitions={succeeded: "DEBUG_SERVE_DRINK_TO_PERSON", aborted: "STOP_ALL_CONTROLLERS", preempted: "STOP_ALL_CONTROLLERS"}
                )



    sis = smach_ros.IntrospectionServer(
        'test_release_object_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
