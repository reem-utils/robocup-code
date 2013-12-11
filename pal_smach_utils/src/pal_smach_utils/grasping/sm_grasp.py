#! /usr/bin/env python

import smach
#from actionlib_msgs.msg import GoalStatus
from smach_ros import SimpleActionState, ServiceState

from arm_navigation_msgs.msg import MoveArmAction
from pr2_controllers_msgs.msg import PointHeadGoal, PointHeadAction
from pal_smach_utils.grasping.arm_and_hand_goals import get_arm_goal_for_arm_elbow_back, get_arm_goal_for_arm_travelling_position
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.grasping.sm_scan_for_object_and_grasp import ScanForObjectAndGraspStateMachine
from pal_smach_utils.grasping.reset_collision_map import ResetCollisionMapStateMachine
from reem_final_approach.srv import FinalApproachPose, FinalApproachPoseRequest
from pal_smach_utils.utils.global_common import set_grasp_error

# This is SM_grasp

class pass_pose_to_search_object_key(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys= ['pose_object'], output_keys=['object_to_search_for'])

    def execute(self, userdata):
        b_type = "ObjectPoseList" in str(type(userdata.pose_object))
        obj = userdata.pose_object.object_list[0] if b_type else userdata.pose_object
        if obj.name != None:
            userdata.object_to_search_for = obj.name
            return succeeded
        else:
            set_grasp_error("GraspStateMachine: obj.name is NONE!! cant pass the name throught for grasping!")
            return aborted




class GraspStateMachine(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
        input_keys=['pose_object'])

        with self:

            smach.StateMachine.add('pass_pose_to_search_object_key',
                                       pass_pose_to_search_object_key(),
                                       transitions={succeeded: 'SCAN_AND_GRASP'})



            smach.StateMachine.add('SCAN_AND_GRASP',
                                       ScanForObjectAndGraspStateMachine(),
                                       transitions={succeeded: 'RESET_COLLISION_MAP_', aborted: aborted})



            smach.StateMachine.add('RESET_COLLISION_MAP_',
            ResetCollisionMapStateMachine(),
            transitions = {succeeded: 'Arm_to_elbow_back', aborted: aborted})



            def arm_goal_cb(userdata, old_goal):
                print "Preparing MoveArmGoal() to move the arm to a safe travel position"
                arm_goal = get_arm_goal_for_arm_elbow_back()
                return arm_goal

            def generic_action_result_cb(userdata, status, result):
                """ Generic action result callback that set grasp error if the status is not succeeded. """
                set_grasp_error(str(self._current_label) + " failed", status)

            smach.StateMachine.add(
                'Arm_to_elbow_back',
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal_cb = arm_goal_cb, result_cb=generic_action_result_cb),
                transitions = {succeeded: 'Move_back_for_spacing_for_putting_arm_down', aborted: 'RESET_COLLISION_MAP_'})

            def loc_request_cb(userdata, request):
                req = FinalApproachPoseRequest()
                req.pose.position.x = -0.2
                req.pose.orientation.w = 1.0
                return req

            smach.StateMachine.add(
                'Move_back_for_spacing_for_putting_arm_down',
                ServiceState('/approachToGoal', FinalApproachPose,
                    request_cb=loc_request_cb),
                    transitions={succeeded: 'Scan_table_for_moving_arm_to_travel', aborted: aborted})


            # Scan with head and put travelling pose
            def grasp_target_goal_cb(userdata, old_goal):
                scan_goal = PointHeadGoal()
                return scan_goal

            smach.StateMachine.add(
                'Scan_table_for_moving_arm_to_travel',
                SimpleActionState(
                    '/head_traj_controller/head_scan_snapshot_action',
                    PointHeadAction,
                    goal_cb = grasp_target_goal_cb, result_cb=generic_action_result_cb),
                    transitions = {succeeded: 'Arm_to_safe_travelling_position', aborted: aborted})


            def arm_goal_cb(userdata, old_goal):
                print "Preparing MoveArmGoal() to move the arm to a safe travel position"
                arm_goal = get_arm_goal_for_arm_travelling_position()
                return arm_goal

            smach.StateMachine.add(
                'Arm_to_safe_travelling_position',
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal_cb = arm_goal_cb, result_cb=generic_action_result_cb),
                transitions = {succeeded: succeeded, aborted: aborted})



# vim: expandtab ts=4 sw=4
