#! /usr/bin/env python

import rospy
import smach

from smach import CBState
from smach_ros import SimpleActionState, ServiceState
from actionlib import SimpleActionClient
from actionlib_msgs.msg import GoalStatus
#from coord_translator.srv import ObjectTranslator, ObjectTranslatorRequest, ObjectTranslatorDataBase, ObjectTranslatorDataBaseRequest
from pr2_controllers_msgs.msg import PointHeadGoal, PointHeadAction
from arm_navigation_msgs.msg import MoveArmAction

from pal_smach_utils.grasping.reset_collision_map import ResetCollisionMapStateMachine
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.grasping.arm_and_hand_goals import get_arm_goal, get_pose_for_arm_in_front, get_open_hand, get_arm_goal_for_arm_travelling_position, get_close_hand
from reem_final_approach.srv import FinalApproachPose, FinalApproachPoseRequest
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.global_common import set_grasp_error
from control_msgs.msg import FollowJointTrajectoryAction


class WaitState(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted])

    def execute(self, userdata):
    	rospy.sleep(20)
        return succeeded



class MoveArmToGiveMeStateMachine(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
            input_keys=['object_to_search_for', 'object_found'])

        with self:
            self.counter = 0

            def termination_cb(userdata, terminal_states, outcome):
                """Reset the counter that check the number of tries to ARM_TO_HAND_ME_OBJECT_POSE """
                self.counter = 0

            self.register_termination_cb(termination_cb)

            def check_counter(userdata, max_count):
                """ :type max_count: int
                    :param max_count: The maximun number before aborts."""
                self.counter += 1
                rospy.loginfo('Counting %d/%d' % (self.counter, max_count ))
                if self.counter  < max_count:
                    return succeeded
                return aborted

            def arm_goal_cb(userdata, old_goal):
                releasing_object_pose = get_pose_for_arm_in_front()
                arm_goal = get_arm_goal(releasing_object_pose, frame_id="/base_link")
                return arm_goal

            def generic_action_result_cb(userdata, status, result):
                """ Generic action result callback that set grasp error if the status is not succeeded. """
                set_grasp_error(str(self._current_label) + " failed", status)

            smach.StateMachine.add(
            'ARM_TO_HAND_ME_OBJECT_POSE',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb, result_cb=generic_action_result_cb),
                transitions={succeeded: succeeded, aborted: 'CHECK_COUNTER'})

            smach.StateMachine.add(
                'CHECK_COUNTER',
                smach.CBState(check_counter, cb_kwargs={'max_count': 5},outcomes=[succeeded, aborted]),
                transitions={succeeded: 'RESET_COLLISION_MAP_FOR_ARM_FRONT', aborted: aborted }
            )

            smach.StateMachine.add(
            'RESET_COLLISION_MAP_FOR_ARM_FRONT',
            ResetCollisionMapStateMachine(),
            transitions={succeeded: 'ARM_TO_HAND_ME_OBJECT_POSE', aborted: aborted})



class GiveMeObjectStateMachine(smach.StateMachine):
    """
        This SM is for asking for a human to give you
        The object that is in front and that you already saw before
        1) Looks for the object
        2) Says he needs help to grasp the object in a "human friendly" way
        3) Puts arm and hand in pose to wait for the object been given
        4) Says to please put the object in the hand and waits some secs
        5) Close hand, put arm down
    """

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
            input_keys=['object_to_search_for', 'object_found'])

        with self:

            def generic_action_result_cb(userdata, status, result):
                """ Generic action result callback that set grasp error if the status is not succeeded. """
                set_grasp_error(str(self._current_label) + " failed", status)

            @smach.cb_interface(outcomes=[succeeded, aborted])
            def lookAtLocation(userdata):
                head_goal = PointHeadGoal()
                head_goal.target.header.frame_id = "base_link"

                # Iterate until we find the object we are searching for
                index_of_object = 0
                while index_of_object < 10:
                	if userdata.object_found.object_list[index_of_object].name == userdata.object_to_search_for:
                		break;
                	index_of_object += 1

                head_goal.target.point.x = userdata.object_found.object_list[index_of_object].pose.position.x
                head_goal.target.point.y = userdata.object_found.object_list[index_of_object].pose.position.y
                head_goal.target.point.z = userdata.object_found.object_list[index_of_object].pose.position.z
                head_goal.pointing_frame = "stereo_link"
                head_goal.pointing_axis.x = 1.0
                head_goal.pointing_axis.y = 0.0
                head_goal.pointing_axis.z = 0.0
                head_goal.max_velocity = 1.5
                head_goal.min_duration.secs = 1.5

                client = SimpleActionClient("/head_traj_controller/point_head_action", PointHeadAction)
                client.wait_for_server(rospy.Duration(0.5))

                client.send_goal(head_goal)

                return succeeded

            smach.StateMachine.add('LOOK_AT_OBJECT_FOR_HELP',
                                   CBState(lookAtLocation, input_keys=['object_to_search_for','object_found']),
                                   transitions={succeeded: 'TTS_ASK_FOR_HELP_TO_REFEREE',
                                                aborted: aborted})

            def say_text_cb(userdata):
            	# Iterate until we find the object we are searching for
                index_of_object = 0
                while index_of_object < 10:
                	if userdata.object_found.object_list[index_of_object].name == userdata.object_to_search_for:
                		break;
                	index_of_object += 1

                # Create sentence
                side = "left" if userdata.object_found.object_list[index_of_object].pose.position.y > 0 else "right"
                text_say = "Could you help me grasp the " + userdata.object_to_search_for
                text_say +=  "?.. It's in front of me at "
                text_say +=  "%d" % (userdata.object_found.object_list[index_of_object].pose.position.x * 100)
                text_say +=  " centimeters, it's around "
                text_say +=  "%d" % (abs(userdata.object_found.object_list[index_of_object].pose.position.y * 100))
                text_say +=  " centimeters to the "
                text_say +=  side
                text_say +=  ". I'm looking at it!"

                return text_say

            smach.StateMachine.add('TTS_ASK_FOR_HELP_TO_REFEREE',
                                   SpeakActionState(text_cb=say_text_cb, input_keys=['object_to_search_for','object_found']),
                                   transitions={succeeded: 'MOVE_BACK_AND_MOVE_ARM'})


            ###################### CONCURRENCE

            go_back_and_say = smach.Concurrence(outcomes=[succeeded, aborted],
                                                       default_outcome=aborted,
                                                       input_keys=['object_to_search_for', 'object_found'],
                                                       output_keys=[],
                                                       outcome_map={succeeded: {'MOVE_BACK_SPACE_FOR_REFEREE': succeeded,
                                                                                'MOVE_ARM_TO_GIVEME_POSE': succeeded,
                                                                                'TTS_TELL_WHAT_IM_DOING': succeeded}})
            with go_back_and_say:
                def finalapp_request_cb(userdata, request):
                    req = FinalApproachPoseRequest()
                    req.pose.position.x = -0.3
                    req.pose.orientation.w = 1.0
                    return req

                smach.Concurrence.add(
                    'MOVE_BACK_SPACE_FOR_REFEREE',
                    ServiceState('/approachToGoal', FinalApproachPose,
                        request_cb=finalapp_request_cb))
                        #transitions={succeeded: 'ARM_TO_HAND_ME_OBJECT_POSE', aborted: aborted})


                smach.Concurrence.add(
                    'MOVE_ARM_TO_GIVEME_POSE',
                    MoveArmToGiveMeStateMachine())
                    #transitions = {succeeded: 'CLOSE_HAND_FOR_REFEREE', aborted: aborted})

            	def say_text_cb(userdata):
                    text_say = "I'm moving back and raising my arm to help you help me."
                    return text_say

            	smach.Concurrence.add('TTS_TELL_WHAT_IM_DOING',
                                   SpeakActionState(text_cb=say_text_cb))

            smach.StateMachine.add('MOVE_BACK_AND_MOVE_ARM', go_back_and_say,
            	transitions={succeeded: 'OPEN_HAND_AND_ASK_TO_PUT_OBJECT', aborted: aborted})


			# CONCURRENCE ###########################


            ###################### CONCURRENCE

            close_hand_and_say = smach.Concurrence(outcomes=[succeeded, aborted],
                                                       default_outcome=aborted,
                                                       input_keys=['object_to_search_for', 'object_found'],
                                                       output_keys=[],
                                                       outcome_map={succeeded: {'TTS_ASK_NICELY_BEFORE_WAIT': succeeded}})
            with close_hand_and_say:
                def grasp_arm_goal_cb(userdata, old_goal):
                    grasp_msg = get_open_hand()
                    return grasp_msg

                def grasp_arm_result_cb(userdata, status, result):
                    if status == GoalStatus.SUCCEEDED:
                        return succeeded
                    set_grasp_error("Open hand for referee failed")

                smach.Concurrence.add(
                'OPEN_HAND_FOR_REFEREE',
                SimpleActionState(
                    '/right_hand_controller/follow_joint_trajectory',
                    FollowJointTrajectoryAction,
                    goal_cb=grasp_arm_goal_cb,
                    result_cb=grasp_arm_result_cb))
                    #transitions={succeeded: 'TTS_ASK_NICELY_BEFORE_WAIT', aborted: 'OPEN_HAND_FOR_REFEREE'})

                def say_text_cb(userdata):
                    # Create sentence
                    text_say = "Please put the object in my hand and wait for me to close the hand."
                    return text_say

                smach.Concurrence.add('TTS_ASK_NICELY_BEFORE_WAIT',
                                       SpeakActionState(text_cb=say_text_cb))
                                       #transitions={succeeded: 'WAIT_STATE'})

            smach.StateMachine.add('OPEN_HAND_AND_ASK_TO_PUT_OBJECT', close_hand_and_say,
            	transitions={succeeded: 'WAIT_STATE', aborted: aborted})

			# CONCURRENCE ###########################


            smach.StateMachine.add(
                    'WAIT_STATE',
                    WaitState(),
                    transitions = {succeeded: 'CLOSE_HAND_AND_SAY_THANKS', aborted: aborted})


            ###################### CONCURRENCE

            open_hand_and_say = smach.Concurrence(outcomes=[succeeded, aborted],
                                                       default_outcome=aborted,
                                                       input_keys=['object_to_search_for', 'object_found'],
                                                       output_keys=[],
                                                       outcome_map={succeeded: {'TTS_SAY_THANKS': succeeded}})
            with open_hand_and_say:
                def grasp_arm_goal_cb(userdata, old_goal):
                    grasp_msg = get_close_hand()
                    return grasp_msg

                def grasp_arm_result_cb(userdata, status, result):
                    if status == GoalStatus.SUCCEEDED:
                        return succeeded
                    set_grasp_error("Close hand for referee failed")


                smach.Concurrence.add(
                'CLOSE_HAND_FOR_REFEREE',
                SimpleActionState(
                    '/right_hand_controller/follow_joint_trajectory',
                    FollowJointTrajectoryAction,
                    goal_cb=grasp_arm_goal_cb,
                    result_cb=grasp_arm_result_cb,
                    input_keys=['releasing_position']))


                def say_text_cb(userdata):
                    # Create sentence
                    text_say = "Thank you!"
                    return text_say

                smach.Concurrence.add('TTS_SAY_THANKS',
                                       SpeakActionState(text_cb=say_text_cb))


            smach.StateMachine.add('CLOSE_HAND_AND_SAY_THANKS', open_hand_and_say,
            	transitions={succeeded: 'ARM_TO_TRAVEL_POSITION', aborted: aborted})

			# CONCURRENCE ###########################


            def arm_goal_cb(userdata, old_goal):
                arm_goal = get_arm_goal_for_arm_travelling_position()
                return arm_goal

            smach.StateMachine.add(
            'ARM_TO_TRAVEL_POSITION',
            SimpleActionState(
                'move_right_arm_torso',
                MoveArmAction,
                goal_cb=arm_goal_cb,
                result_cb=generic_action_result_cb,
                input_keys=['releasing_position']),
                transitions={succeeded: succeeded, aborted: 'RESET_COLLISION_MAP_FOR_ARM_DOWN'})


            smach.StateMachine.add(
            'RESET_COLLISION_MAP_FOR_ARM_DOWN',
            ResetCollisionMapStateMachine(),
            transitions={succeeded: 'ARM_TO_TRAVEL_POSITION', aborted: aborted})





