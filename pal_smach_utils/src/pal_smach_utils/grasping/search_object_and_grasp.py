# vim: expandtab ts=4 sw=4
# -.- coding: utf-8 -.-
# Author RDaneelOlivaw

import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
import math

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState

from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Pose, Quaternion

from complete_grasp_pipeline import CompleteGraspPipelineStateMachine
from pal_smach_utils.navigation.move_action import MoveActionState
from move_base_msgs.msg import MoveBaseGoal
from pal_smach_utils.utils.colors import Colors

colors = Colors()
# every turn is of 45 degrees, so it will perform 3
ORIENTATION_PARAMETER = 0.78

FOUND_AND_GRASPED_OBJECT_FRASE = "Great! I have the "
DIDNT_FIND_OBJECT_FRASE = " should be around here, but I couldn't find it. "
SOMETHING_WENT_WRONG_FRASE = "I might be having some technical difficulties in this moment."


class InitTurningCounter(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded,
                                       preempted,
                                       aborted],
                             output_keys=['init_times_turned_out'])

    def execute(self, userdata):

        userdata.init_times_turned_out = 1

        return succeeded

"""
class DecideIfContinueTurningAround(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['continue',
                                       'dont_continue',
                                       preempted,
                                       aborted],
                             input_keys=['in_times_turned'],
                             output_keys=['times_turned_out'])

    def execute(self, userdata):

        radians_turned = userdata.in_times_turned * ORIENTATION_PARAMETER
        if radians_turned >= (math.pi * 2.0):
            return 'dont_continue'

        userdata.times_turned_out = userdata.in_times_turned + 1
        return 'continue'
"""


class DecideIfContinueTurningAround(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['continue',
                                       'dont_continue',
                                       preempted,
                                       aborted],
                             input_keys=['in_times_turned'],
                             output_keys=['times_turned_out'])

    def execute(self, userdata):

        if userdata.in_times_turned >= 3:
            return 'dont_continue'

        userdata.times_turned_out = userdata.in_times_turned + 1
        return 'continue'


class SearchObjectAndGrasp(smach.StateMachine):
    # When you have grasping.

    #To use this stateMachine you should be near the location where the object should be.
    #It looks for the object. If found, it goes and grasps. Otherwise, it turns a fraction
    #of a turn and tries again. If a complete 360 degrees turned, it outputs that it didnt find the object.


    def __init__(self):
        smach.StateMachine.__init__(self,
                                    ['object_grasped_succesfully',
                                     'didnt_grasp_object',
                                     preempted,
                                     aborted],
                                    input_keys=['in_fetch_object_name'])

        with self:

            smach.StateMachine.add('INIT_TURNING_COUNTER',
                                   InitTurningCounter(),
                                   transitions={succeeded: 'SEARCH_AND_GRASP_OBJECT',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'init_times_turned_out': 'times_turned'})

            # If Aborted, is because it didnt find the object. Therefore it has to turn a certain degrees
            # just in case the object is elsewhere outside the field of view of the robot.

            smach.StateMachine.add('SEARCH_AND_GRASP_OBJECT',
                                   CompleteGraspPipelineStateMachine(ask_for_help=False),
                                   remapping={'object_to_search_for': 'in_fetch_object_name'},
                                   transitions={succeeded: "OBJECT_FOUND_AND_GRASPED",
                                                aborted: 'DECIDE_IF_CONTINUE_TURNING_AROUND',
                                                preempted: "SAY_NEED_HELP"})

            smach.StateMachine.add('DECIDE_IF_CONTINUE_TURNING_AROUND',
                                   DecideIfContinueTurningAround(),
                                   transitions={'continue': 'TURN_AROUND',
                                                'dont_continue': 'DIDNT_FIND_OBJECT',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_times_turned': 'times_turned',
                                              'times_turned_out': 'times_turned'})

            # When aborted, it wil just search for the object there. Just to avoid abortions.
            def turn_cb(userdata, nav_goal):
                nav_goal = MoveBaseGoal()
                nav_goal.target_pose.header.stamp = rospy.Time.now()
                nav_goal.target_pose.header.frame_id = "/base_link"
                nav_goal.target_pose.pose.position.x = 0.0
                nav_goal.target_pose.pose.position.y = 0.0
                nav_goal.target_pose.pose.position.z = 0.0
                if userdata.times_turned == 2:
                    #Turns Left 45 degrees
                    nav_goal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, ORIENTATION_PARAMETER))
                elif userdata.times_turned == 3:
                    #Turns returns to pose and turns Right 45
                    nav_goal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, -2*ORIENTATION_PARAMETER))
                return nav_goal

            smach.StateMachine.add('TURN_AROUND',
                                   MoveActionState("/base_link", goal_cb=turn_cb, input_keys=['times_turned']),
                                   transitions={succeeded: 'SEARCH_AND_GRASP_OBJECT',
                                                aborted: 'SEARCH_AND_GRASP_OBJECT'},
                                   remapping={'times_turned': 'times_turned'})

            def say_text_cb1(userdata):
                text_say = "The " + userdata.in_fetch_object_name + DIDNT_FIND_OBJECT_FRASE
                return text_say
            smach.StateMachine.add('DIDNT_FIND_OBJECT',
                                   SpeakActionState(text_cb=say_text_cb1, input_keys=['in_fetch_object_name']),
                                   transitions={succeeded: 'didnt_grasp_object'})

            def say_text_cb3(userdata):
                text_say = FOUND_AND_GRASPED_OBJECT_FRASE + userdata.in_fetch_object_name
                return text_say
            smach.StateMachine.add('OBJECT_FOUND_AND_GRASPED',
                                   SpeakActionState(text_cb=say_text_cb3, input_keys=['in_fetch_object_name']),
                                   transitions={succeeded: 'object_grasped_succesfully'})

            def say_text_cb4(userdata):
                text_say = SOMETHING_WENT_WRONG_FRASE
                return text_say
            smach.StateMachine.add('SAY_NEED_HELP',
                                   SpeakActionState(text_cb=say_text_cb4, input_keys=['in_fetch_object_name']),
                                   transitions={succeeded: aborted})

"""


class SearchObjectAndGrasp(smach.StateMachine):
    # This is when there is no grasping
    def __init__(self):
        smach.StateMachine.__init__(self,
                                    ['object_grasped_succesfully',
                                     'didnt_grasp_object',
                                     preempted,
                                     aborted],
                                    input_keys=['in_fetch_object_name'])

        with self:

            smach.StateMachine.add('INIT_TURNING_COUNTER',
                                   InitTurningCounter(),
                                   transitions={succeeded: 'DECIDE_IF_CONTINUE_TURNING_AROUND',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'init_times_turned_out': 'times_turned'})

            # If Aborted, is because it didnt find the object. Therefore it has to turn a certain degrees
            # just in case the object is elsewhere outside the field of view of the robot.

            smach.StateMachine.add('DECIDE_IF_CONTINUE_TURNING_AROUND',
                                   DecideIfContinueTurningAround(),
                                   transitions={'continue': 'TURN_AROUND',
                                                'dont_continue': 'OBJECT_FOUND_AND_GRASPED',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_times_turned': 'times_turned',
                                              'times_turned_out': 'times_turned'})

            # When aborted, it wil just search for the object there. Just to avoid abortions.
            def turn_cb(userdata, nav_goal):
                nav_goal = MoveBaseGoal()
                nav_goal.target_pose.header.stamp = rospy.Time.now()
                nav_goal.target_pose.header.frame_id = "/base_link"
                nav_goal.target_pose.pose.position.x = 0.0
                nav_goal.target_pose.pose.position.y = 0.0
                nav_goal.target_pose.pose.position.z = 0.0
                if userdata.times_turned == 2:
                    #Turns Left 45 degrees
                    nav_goal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, ORIENTATION_PARAMETER))
                elif userdata.times_turned == 3:
                    #Turns returns to pose and turns Right 45
                    nav_goal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, -2*ORIENTATION_PARAMETER))
                return nav_goal

            smach.StateMachine.add('TURN_AROUND',
                                   MoveActionState("/base_link", goal_cb=turn_cb, input_keys=['times_turned']),
                                   transitions={succeeded: 'DECIDE_IF_CONTINUE_TURNING_AROUND',
                                                aborted: 'DECIDE_IF_CONTINUE_TURNING_AROUND'},
                                   remapping={'times_turned': 'times_turned'})

            def say_text_cb1(userdata):
                text_say = "The " + userdata.in_fetch_object_name + DIDNT_FIND_OBJECT_FRASE
                return text_say
            smach.StateMachine.add('DIDNT_FIND_OBJECT',
                                   SpeakActionState(text_cb=say_text_cb1, input_keys=['in_fetch_object_name']),
                                   transitions={succeeded: 'didnt_grasp_object'})

            def say_text_cb3(userdata):
                text_say = FOUND_AND_GRASPED_OBJECT_FRASE + userdata.in_fetch_object_name
                return text_say
            smach.StateMachine.add('OBJECT_FOUND_AND_GRASPED',
                                   SpeakActionState(text_cb=say_text_cb3, input_keys=['in_fetch_object_name']),
                                   transitions={succeeded: 'object_grasped_succesfully'})

            def say_text_cb4(userdata):
                text_say = SOMETHING_WENT_WRONG_FRASE
                return text_say
            smach.StateMachine.add('SAY_NEED_HELP',
                                   SpeakActionState(text_cb=say_text_cb4, input_keys=['in_fetch_object_name']),
                                   transitions={succeeded: aborted})

"""
