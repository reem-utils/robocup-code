#! /usr/bin/env python

#import roslib; roslib.load_manifest('pal_smach_utils')
import roslib
import rospy
import smach
import actionlib
from smach_ros import SimpleActionState, ServiceState

from std_msgs.msg import *
from arm_navigation_msgs.msg import *
from actionlib_msgs import *
from actionlib_msgs.msg import GoalStatus
#from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

try:
    from pr_msgs.msg import ObjectPoseList, ObjectPose
    from pr_msgs.srv import *
except ImportError:
    from pr_msgs.msg import ObjectPoseList, ObjectPose

from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped
from object_manipulation_msgs.msg import *
#from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.math_utils import *
from pal_smach_utils.grasping.arm_and_hand_goals import *
from trajectory_msgs.msg import *
#from control_msgs.msg import *
from std_srvs.srv import *
from pr2_controllers_msgs.msg import PointHeadGoal, PointHeadAction
from reem_final_approach.srv import *

class CheckForWhereToReleaseStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, input_keys=['releasing_position'], outcomes=[succeeded, aborted])

    def execute(self, userdata):
        rospy.sleep(0.5)  # in seconds
        if userdata.releasing_position is not None: # then we need to put the hand somewhere specific (for tables)
            return succeeded
        else:
            return aborted # we just put the hand in front... for someone


class ReleaseObjectStateMachine(smach.StateMachine):
    # Defined here: https://docs.google.com/drawings/d/1L3muMd6uwvDVhdYN4e5OfHX3sCSxmeCC_EdFhfTQ5cQ/edit
    def __init__(self, speak=True):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                                    input_keys=['releasing_position'])

        with self:

            # Scan with head before doing any movement!
            def grasp_target_goal_cb(userdata, old_goal):
                scan_goal = PointHeadGoal()
                return scan_goal

            smach.StateMachine.add(
                'Scan_table_for_moving_arm',
                SimpleActionState(
                    '/head_traj_controller/head_scan_snapshot_action',
                    PointHeadAction,
                    goal_cb = grasp_target_goal_cb),
                    transitions = {succeeded: 'CheckForWhereToRelease', aborted: aborted})  

            smach.StateMachine.add(
            'CheckForWhereToRelease',
            CheckForWhereToReleaseStateMachine(),
            transitions={succeeded:'HAND_TO_RELEASING_POSITION', aborted: 'HAND_TO_HARDCODED_RELEASE_POSE'})





            def arm_goal_cb(userdata, old_goal):
                initial_grasping_pose = userdata.releasing_position
                arm_goal = get_arm_goal(initial_grasping_pose, frame_id="/base_link")
                return arm_goal

            smach.StateMachine.add(
            'HAND_TO_RELEASING_POSITION',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                input_keys=['releasing_position']),
                transitions={succeeded: 'release_open_hand', aborted: 'HAND_TO_RELEASING_POSITION'})


            def arm_goal_cb(userdata, old_goal):
                releasing_object_pose = get_pose_for_arm_in_front()
                arm_goal = get_arm_goal(releasing_object_pose, frame_id="/base_link")
                return arm_goal

            smach.StateMachine.add(
            'HAND_TO_HARDCODED_RELEASE_POSE',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                input_keys=['releasing_position']),
                transitions={succeeded: 'release_open_hand', aborted: 'HAND_TO_HARDCODED_RELEASE_POSE'})





            def grasp_arm_goal_cb(userdata, old_goal):
                grasp_msg = get_open_hand()
                return grasp_msg

            def grasp_arm_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED:
                    #rospy.loginfo("Succeeded: result of right_hand_controller: " + str(result.error_code) )
                    return succeeded
                else:  # TODO: See if this is important, Hilario says maybe it's a problem of gazebo
                    rospy.loginfo("Other than succeded: result of right_hand_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code))
                    if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
                        rospy.loginfo("Continuing even with this error as it's not really aborted...")
                        return succeeded
                    else:
                        return aborted

            smach.StateMachine.add(
            'release_open_hand',
            SimpleActionState(
                '/right_hand_controller/follow_joint_trajectory',
                FollowJointTrajectoryAction,
                goal_cb=grasp_arm_goal_cb,
                result_cb=grasp_arm_result_cb,
                input_keys=['releasing_position']),
                transitions={succeeded: 'release_open_hand_fully', aborted: 'release_open_hand'})


            def grasp_arm_goal_cb(userdata, old_goal):
                grasp_msg = get_fully_open_hand()
                return grasp_msg

            def grasp_arm_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED:
                    return succeeded
                else:  # TODO: See if this is important, Hilario says maybe it's a problem of gazebo
                    rospy.loginfo("Other than succeded: result of right_hand_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code))
                    if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
                        rospy.loginfo("Continuing even with this error as it's not really aborted...")
                        return succeeded
                    else:
                        return aborted

            smach.StateMachine.add(
            'release_open_hand_fully',
            SimpleActionState(
                '/right_hand_controller/follow_joint_trajectory',
                FollowJointTrajectoryAction,
                goal_cb=grasp_arm_goal_cb,
                result_cb=grasp_arm_result_cb,
                input_keys=['releasing_position']),
                transitions={succeeded: 'Move_back_for_spacing_for_putting_arm_down', aborted: 'release_open_hand_fully'})




            def loc_request_cb(userdata, request):
                req = FinalApproachPoseRequest()
                req.pose.position.x = -0.3
                req.pose.orientation.w = 1.0
                return req

            smach.StateMachine.add(
                'Move_back_for_spacing_for_putting_arm_down',
                ServiceState('/approachToGoal', FinalApproachPose,
                    request_cb=loc_request_cb),
                    transitions={succeeded: 'Scan_table_for_moving_arm_down', aborted: aborted})

            def grasp_target_goal_cb(userdata, old_goal):
                scan_goal = PointHeadGoal()
                return scan_goal

            smach.StateMachine.add(
                'Scan_table_for_moving_arm_down',
                SimpleActionState(
                    '/head_traj_controller/head_scan_snapshot_action',
                    PointHeadAction,
                    goal_cb = grasp_target_goal_cb),
                    transitions = {succeeded: 'Arm_to_safe_travelling_position', aborted: aborted})  

            def arm_goal_cb(userdata, old_goal):
                arm_goal = get_arm_goal_for_arm_down()
                return arm_goal

            smach.StateMachine.add(
            'Arm_to_safe_travelling_position',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                input_keys=['releasing_position']),
                transitions={succeeded: succeeded, aborted: aborted})

# vim: expandtab ts=4 sw=4
