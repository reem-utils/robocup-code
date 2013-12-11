import roslib
roslib.load_manifest("pal_smach_utils")
import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted, unknown_face
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables as cp_vars
from pal_smach_utils.utils.recognize_face import RecognizeFaceStateMachine
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.grasping.arm_and_hand_goals import get_pose_for_arm_in_front
from pal_smach_utils.utils.run_script_on_robot import RunScriptOnRobot
from pal_smach_utils.grasping.complete_grasp_pipeline import CompleteGraspPipelineStateMachine

from pal_smach_utils.utils.colors import colors
from smach_ros import SimpleActionState, ServiceState
from reem_final_approach.srv import FinalApproachPose, FinalApproachPoseRequest
from pal_smach_utils.grasping.arm_and_hand_goals import get_arm_goal, get_arm_goal_for_arm_down, get_fully_open_hand
from arm_navigation_msgs.msg import MoveArmAction
from control_msgs.msg import FollowJointTrajectoryAction
from move_to_caller import MoveToCallerStateMachine
from actionlib_msgs.msg import GoalStatus
from pal_smach_utils.utils.timeout_container import SleepState
from pal_smach_utils.utils.concurrence_robocup import ConcurrenceRobocup
from move_base_msgs.msg import MoveBaseGoal


class ServeDrinkStateMachine(smach.StateMachine):
    """ServeDrinkStateMachine.

    Requirements:
        Kinect connected on the robot.
        Drinks located in a table in drinks_location.
        scripts/graspingStartNoKinect.sh should be previously launched.

    Use this class to serve the drink orders.
    Steps of this State Machine:
        First, the kinect to use in the grasp will be activated. After this, the robot will move to drinks_location; enable the controllers of
        the head, left and right arm to be able to look for the objects and grasp; look for the object and grasp it if found; stop the kinect
        used on grasping to avoid conflicts with GestureRecognition driver if the person that has requested the drink is not in the same position;
        stop all controllers; back to the position where the person is located; try recognize the person. If the person is not in the same position,
        the robot will ask where the person is; The robot will serve the drink.

    """
    def __init__(self):
        """Constructor for ServeDrinkStateMachine

        Input keys:
            @type drink_orders: a list of pal_smach_utils/src/pal_smach_utils/utils/DrinkOrder
            @param drink_orders: The drinks names, person names and person positions.

            @type order_index: integer
            @param order_index: an index into the `drink_orders' list.
        """

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
            input_keys=['drink_orders', 'order_index'])

        with self:
            self.userdata.drinks_room = cp_vars.M_ROOM_DRINKS
            self.userdata.party_room = cp_vars.M_PARTY_ROOM

            self.userdata.drink_name = None
            self.userdata.person_name = None
            self.userdata.person_pose = None
            self.userdata.max_order_index = None

            def fulfill_variables_cb(userdata):
                drink_order = userdata.drink_orders[userdata.order_index]

                self.userdata.person_name = drink_order.person_name
                self.person_name = self.userdata.person_name
                self.userdata.drink_name = drink_order.drink
                self.userdata.person_pose = drink_order.person_pose
                self.userdata.max_order_index = len(userdata.drink_orders) - 1

                return succeeded

            smach.StateMachine.add(
                "SET_VARIABLES",
                smach.CBState(fulfill_variables_cb, input_keys=["drink_orders", "order_index"], outcomes=[succeeded]),
                transitions={succeeded: "START_KINECT_GRASP"})

            smach.StateMachine.add(
                "START_KINECT_GRASP",
                RunScriptOnRobot(script_name="kinectToGraspStart.sh"),
                transitions={succeeded: "ANNOUNCE_AND_MOVE_TO_DRINKS_ROOM", aborted: "ANNOUNCE_AND_MOVE_TO_DRINKS_ROOM"}
                )

            def announce_moving(userdata):
                tts = "I'm going to the " + userdata.room_name + " to find "
                count_aux = 0
                for drink_order in userdata.drink_orders:
                    count_aux += 1
                    if count_aux > userdata.order_index:
                        tts += drink_order.drink + " for " + drink_order.person_name + (" and " if count_aux == userdata.max_order_index else ", ")
                tts += "!"
                tts = tts.replace(", !", "!")
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            STATES_1 = [MoveToRoomStateMachine(announcement=None), SpeakActionState(text_cb=announce_moving, input_keys=["drink_orders", "room_name", "order_index", "max_order_index"])]
            STATE_NAMES_1 = ["MOVE_TO_DRINKS_LOCATION", "ANNOUNCE_MOVING"]
            OUTCOME_MAP_1 = {succeeded: {"MOVE_TO_DRINKS_LOCATION": succeeded}}

            smach.StateMachine.add(
                "ANNOUNCE_AND_MOVE_TO_DRINKS_ROOM",
                ConcurrenceRobocup(states=STATES_1, state_names=STATE_NAMES_1, input_keys=["drink_orders", "room_name", "order_index", "max_order_index"],
                    outcome_map=OUTCOME_MAP_1),
                remapping={"room_name": "drinks_room"},
                transitions={succeeded: 'START_ALL_CONTROLLERS', aborted: "ANNOUNCE_AND_MOVE_TO_DRINKS_ROOM"},
                #transitions={succeeded: 'ANNOUNCE_AND_BACK_TO_GUEST', aborted: "ANNOUNCE_AND_MOVE_TO_DRINKS_ROOM"},  # FIXME: This line if want to test without grasp.
                )
            #outputs: 'room_location'

            smach.StateMachine.add(
                "START_ALL_CONTROLLERS",
                StartRobotControllers(head=True, left=True, right=True),
                transitions={succeeded: "ANNOUNCE_SEARCH_AND_GRASP", aborted: "START_ALL_CONTROLLERS", preempted: "START_ALL_CONTROLLERS"}
                )

            def announce_looking_text_cb(userdata):
                tts = "I'm looking for %s!" % userdata.drink_name
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            STATES_2 = [SpeakActionState(text_cb=announce_looking_text_cb, input_keys=["drink_name"]), CompleteGraspPipelineStateMachine()]
            STATE_NAMES_2 = ["ANNOUNCE_LOOKING", "SEARCH_AND_GRASP"]
            OUTCOME_MAP_2 = {succeeded: {"SEARCH_AND_GRASP": succeeded}}

            smach.StateMachine.add(
                "ANNOUNCE_SEARCH_AND_GRASP",
                ConcurrenceRobocup(states=STATES_2, state_names=STATE_NAMES_2, input_keys=["drink_name", "object_to_search_for"], outcome_map=OUTCOME_MAP_2),
                remapping={"object_to_search_for": "drink_name"},
                transitions={succeeded: "STOP_KINECT_GRASP", aborted: "CHECK_FOUND"},
                )

            smach.StateMachine.add(
                "STOP_KINECT_GRASP",
                RunScriptOnRobot(script_name="kinectToGraspStop.sh"),
                transitions={succeeded: "STOP_ALL_CONTROLLERS", aborted: "STOP_KINECT_GRASP_AGAIN"}
                )

            def stop_kinect_grasp_again(userdata):
                rospy.logerr('The kinect to grasping has failed, trying again...')
                outcome = RunScriptOnRobot(script_name="kinectToGraspStop.sh").execute(userdata)
                return outcome

            smach.StateMachine.add(
                "STOP_KINECT_GRASP_AGAIN",
                smach.CBState(stop_kinect_grasp_again, outcomes=[succeeded, aborted]),
                transitions={succeeded: "STOP_ALL_CONTROLLERS", aborted: "STOP_ALL_CONTROLLERS"}
                )

            smach.StateMachine.add(
                "STOP_ALL_CONTROLLERS",
                StopRobotControllers(head=True, left=True, right=True),
                transitions={succeeded: "ANNOUNCE_AND_BACK_TO_GUEST", aborted: "STOP_ALL_CONTROLLERS", preempted: "STOP_ALL_CONTROLLERS"}
                )

            def check_object_found(userdata):
                try:
                    rospy.loginfo("Type is: " + str(type(userdata.object_found)))
                    rospy.loginfo(colors.WHITE_BOLD + "Object Found" + str(userdata.object_found) + colors.NATIVE_COLOR)
                    return succeeded
                except Exception as e:
                    print colors.RED + str(e) + colors.NATIVE_COLOR
                    return aborted

            smach.StateMachine.add(
                "CHECK_FOUND",
                smach.CBState(check_object_found, input_keys=["object_found"], outcomes=[succeeded, aborted]),
                transitions={succeeded: "SAY_FOUND", aborted: "SAY_NOT_FOUND"}
            )

            def need_help_text_cb(userdata):
                tts = "The %s was not found. Someone can put the %s closer?" % (userdata.drink_name, userdata.drink_name)
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            smach.StateMachine.add(
                "SAY_NOT_FOUND",
                SpeakActionState(text_cb=need_help_text_cb, input_keys=["drink_name"]),
                transitions={succeeded: "ANNOUNCE_SEARCH_AND_GRASP", aborted: "ANNOUNCE_SEARCH_AND_GRASP", preempted: "SAY_NOT_FOUND"}
                )

            def say_found_cb(userdata):
                tts = "I found the %s but I can't grasp for some reason. Someone can put it closer?" % userdata.drink_name
                return tts

            smach.StateMachine.add(
                "SAY_FOUND",
                SpeakActionState(text_cb=say_found_cb, input_keys=["drink_name"]),
                transitions={succeeded: "ANNOUNCE_SEARCH_AND_GRASP", aborted: "ANNOUNCE_SEARCH_AND_GRASP", preempted: "SAY_FOUND"}
                )

            def tts_serve_drink_person_cb(userdata):
                tts = "I'm going to serve %s to %s!" % (userdata.drink_name, userdata.person_name)
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            def person_position_goal_cb(userdata, nav_goal):
                move_base_goal = MoveBaseGoal()
                move_base_goal.target_pose = userdata.person_pose
                move_base_goal.target_pose.header.stamp = rospy.Time.now()
                return move_base_goal

            STATES_3 = [SpeakActionState(text_cb=tts_serve_drink_person_cb,
                            input_keys=["person_name", "drink_name"]),
                        MoveActionState(
                            move_base_action_name=cp_vars.A_MOVE_BASE,
                            goal_cb=person_position_goal_cb,
                            input_keys=["person_pose"])]
            STATE_NAMES_3 = ["SAY_DRINK_PERSON", "MOVE_BACK_TO_GUEST"]
            OUTCOME_MAP_3 = {succeeded: {"MOVE_BACK_TO_GUEST": succeeded}}  # outcome_map

            smach.StateMachine.add(
                "ANNOUNCE_AND_BACK_TO_GUEST",
                ConcurrenceRobocup(states=STATES_3, state_names=STATE_NAMES_3, input_keys=["person_name", "drink_name", "person_pose"], outcome_map=OUTCOME_MAP_3),
                remapping={"object_to_search_for": "drink_name"},
                transitions={succeeded: "RECOGNIZE_PERSON_WITHOUT_INSTRUCTIONS", aborted: "ANNOUNCE_UNREACHABLE"},
                )

            def tts_unreachable_cb(userdata):
                return "The location to find %s is unreachable!" % userdata.person_name

            smach.StateMachine.add(
                "ANNOUNCE_UNREACHABLE",
                SpeakActionState(text_cb=tts_unreachable_cb, input_keys=["person_name"]),
                transitions={succeeded: "ANNOUNCE_AND_BACK_TO_GOOD_POSITION", aborted: "ANNOUNCE_AND_BACK_TO_GOOD_POSITION"}
            )

            smach.StateMachine.add(
                "RECOGNIZE_PERSON_WITHOUT_INSTRUCTIONS",
                RecognizeFaceStateMachine(announce_unknown_face=False, instructions_tts=False),
                transitions={succeeded: "CHECK_PERSON", aborted: "ANNOUNCE_AND_BACK_TO_GOOD_POSITION", unknown_face: "ANNOUNCE_AND_BACK_TO_GOOD_POSITION", preempted: "RECOGNIZE_PERSON_WITHOUT_INSTRUCTIONS"}
                )
            # output_keys=["out_person_name"]

            def check_person_cb(userdata):
                return succeeded if userdata.out_person_name.lower() == userdata.person_name.lower() else aborted

            smach.StateMachine.add(
                "CHECK_PERSON",
                smach.CBState(check_person_cb,
                    input_keys=["out_person_name", "person_name"], outcomes=[succeeded, aborted]),
                transitions={succeeded: "START_KINECT_GRASP_TO_ENABLE_RIGHT_ARM_TORSO", aborted: "ANNOUNCE_AND_BACK_TO_GOOD_POSITION"})
                #transitions={succeeded: "STOP_CONTROLLERS_AND_KINECT_GRASP", aborted: "ANNOUNCE_AND_BACK_TO_GOOD_POSITION"})  # FIXME: This line if want to test without grasp.

            smach.StateMachine.add(
                "START_KINECT_GRASP_TO_ENABLE_RIGHT_ARM_TORSO",
                RunScriptOnRobot(script_name="kinectToGraspStart.sh"),
                transitions={succeeded: "ANNOUNCE_AND_BACK_FOR_SPACING", aborted: "ANNOUNCE_AND_BACK_FOR_SPACING"}
                )

            def back_to_good_position_tts_cb(userdata):
                tts = "I'm going back to a good position in %s to find %s!" % (userdata.room_name, userdata.person_name)
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            STATES_4 = [MoveToRoomStateMachine(announcement=None), SpeakActionState(text_cb=back_to_good_position_tts_cb, input_keys=["person_name", "room_name"])]
            STATE_NAMES_4 = ["BACK_TO_GOOD_POSITION", "ANNOUNCE_BACKING"]
            OUTCOME_MAP_4 = {succeeded: {"BACK_TO_GOOD_POSITION": succeeded}}

            smach.StateMachine.add(
                "ANNOUNCE_AND_BACK_TO_GOOD_POSITION",
                ConcurrenceRobocup(states=STATES_4, state_names=STATE_NAMES_4, input_keys=["person_name", "room_name"], outcome_map=OUTCOME_MAP_4),
                remapping={"room_name": "party_room"},
                transitions={succeeded: "ASK_WHERE_ARE_YOU", aborted: "ASK_WHERE_ARE_YOU"}
                )
            #outputs: 'room_location'

            def looking_for_person_cb(userdata):
                tts = "I'm looking for you %s. Where are you?" % userdata.person_name
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            smach.StateMachine.add(
                "ASK_WHERE_ARE_YOU",
                SpeakActionState(text_cb=looking_for_person_cb, input_keys=["person_name"]),
                transitions={succeeded: "MOVE_TO_CALLER", aborted: "MOVE_TO_CALLER", preempted: "ASK_WHERE_ARE_YOU"}
                )

            smach.StateMachine.add(
                "MOVE_TO_CALLER",
                MoveToCallerStateMachine(ask_for_movement_msg_cb=looking_for_person_cb, rotation_left=False, input_keys=["person_name"]),
                transitions={succeeded: "RECOGNIZE_PERSON", aborted: "ASK_WHERE_ARE_YOU", preempted: "MOVE_TO_CALLER"}
                )

            smach.StateMachine.add(
                "RECOGNIZE_PERSON",
                RecognizeFaceStateMachine(),
                transitions={succeeded: "CHECK_PERSON", aborted: "ANNOUNCE_AND_BACK_TO_GOOD_POSITION", unknown_face: "ANNOUNCE_AND_BACK_TO_GOOD_POSITION", preempted: "RECOGNIZE_PERSON"}
                )
            # output_keys=["out_person_name"]

            def take_your_drink_cb(userdata):
                tts = "Please, take your %s %s!" % (userdata.drink_name, userdata.person_name)
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            def move_back_for_spacing_for_putting_arm_in_front(userdata, request):
                req = FinalApproachPoseRequest()
                req.pose.position.x = -0.3
                req.pose.orientation.w = 0.0
                return req

            STATES_5 = [SpeakActionState("I'm going back a bit for put my hand in front!"),
                        ServiceState('/approachToGoal', FinalApproachPose,
                            request_cb=move_back_for_spacing_for_putting_arm_in_front)]
            STATE_NAMES_5 = ["ANNOUNCE_BACKING", "BACK_FOR_SPACING"]
            OUTCOME_MAP_5 = {succeeded: {"BACK_FOR_SPACING": succeeded}}

            smach.StateMachine.add(
                "ANNOUNCE_AND_BACK_FOR_SPACING",
                ConcurrenceRobocup(states=STATES_5, state_names=STATE_NAMES_5, input_keys=["person_name", "room_name"], outcome_map=OUTCOME_MAP_5),
                remapping={"room_name": "party_room"},
                transitions={succeeded: "START_ARMS_CONTROLLERS", aborted: "START_ARMS_CONTROLLERS"}
                )  # If aborts will continue because the hand will be not in front, will be on the top.

            smach.StateMachine.add(
                "START_ARMS_CONTROLLERS",
                StartRobotControllers(head=False, left=True, right=True),
                transitions={succeeded: "HAND_IN_FRONT", aborted: "START_ARMS_CONTROLLERS_AGAIN", preempted: "START_ARMS_CONTROLLERS"}
                )

            smach.StateMachine.add(
                "START_ARMS_CONTROLLERS_AGAIN",
                StartRobotControllers(head=False, left=True, right=True),
                transitions={succeeded: "HAND_IN_FRONT", aborted: "HAND_IN_FRONT", preempted: "HAND_IN_FRONT"}
                )

            def hand_in_front_goal_cb(userdata, old_goal):
                releasing_object_pose = get_pose_for_arm_in_front()
                arm_goal = get_arm_goal(releasing_object_pose, frame_id="/base_link")
                return arm_goal

            smach.StateMachine.add(
                "HAND_IN_FRONT",
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal_cb=hand_in_front_goal_cb),
                transitions={succeeded: "ANNOUNCE_GIVE", aborted: "WARNING_CANT_MOVE_ARM"})

            smach.StateMachine.add(
                "WARNING_CANT_MOVE_ARM",
                SpeakActionState("Sorry! There is something wrong with my arm because I cannot put it exactly in front! Can you bring the drink from my hand? I'll open it now!"),
                transitions={succeeded: "ANNOUNCE_GIVE", aborted: "ANNOUNCE_GIVE"}
            )

            smach.StateMachine.add(
                'ANNOUNCE_GIVE',
                SpeakActionState(text_cb=take_your_drink_cb, input_keys=["drink_name", "person_name"]),
                transitions={succeeded: "SLEEP_BEFORE_OPEN_HAND", aborted: "SLEEP_BEFORE_OPEN_HAND", preempted: "ANNOUNCE_GIVE"}
                )

            smach.StateMachine.add(
                "SLEEP_BEFORE_OPEN_HAND",
                SleepState(2),
                transitions={succeeded: "OPEN_HAND_FULLY", preempted: "OPEN_HAND_FULLY"}
                )

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

            smach.StateMachine.add(
                "OPEN_HAND_FULLY",
                SimpleActionState(
                    '/right_hand_controller/follow_joint_trajectory',
                    FollowJointTrajectoryAction,
                    goal=get_fully_open_hand(),
                    result_cb=open_hand_fully_result_cb,
                    input_keys=['releasing_position']),
                transitions={succeeded: 'SLEEP_AFTER_OPEN_HAND', aborted: "WARNING_CANT_OPEN_HAND"})

            smach.StateMachine.add(
                "WARNING_CANT_OPEN_HAND",
                SpeakActionState("I'm really sorry! I can't open my hand by some unknown reason! Can you bring the drink from my hand? I'll wait 20 seconds!"),
                transitions={succeeded: "SLEEP_BECAUSE_CANT_OPEN_HAND", aborted: "SLEEP_BECAUSE_CANT_OPEN_HAND"}
            )

            smach.StateMachine.add(
                "SLEEP_BECAUSE_CANT_OPEN_HAND",
                SleepState(20),
                transitions={succeeded: "ARM_TO_SAFE_POSITION", preempted: "ARM_TO_SAFE_POSITION"}
            )

            smach.StateMachine.add(
                "SLEEP_AFTER_OPEN_HAND",
                SleepState(2),
                transitions={succeeded: "ARM_TO_SAFE_POSITION", preempted: "ARM_TO_SAFE_POSITION"}
                )

            smach.StateMachine.add(
                "ARM_TO_SAFE_POSITION",
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal=get_arm_goal_for_arm_down()),
                transitions={succeeded: "STOP_CONTROLLERS_AND_KINECT_GRASP", aborted: "ARM_TO_SAFE_POSITION", preempted: "ARM_TO_SAFE_POSITION"})

            STATES_6 = [StopRobotControllers(head=False, left=True, right=True), RunScriptOnRobot(script_name="kinectToGraspStop.sh")]
            STATE_NAMES_6 = ["STOP_ARM_CONTROLLERS", "STOP_KINECT_GRASP_AFTER_BACK_RIGHT_ARM_SAFE"]

            smach.StateMachine.add(
                "STOP_CONTROLLERS_AND_KINECT_GRASP",
                ConcurrenceRobocup(states=STATES_6, state_names=STATE_NAMES_6),
                transitions={succeeded: succeeded, aborted: succeeded}
                )


class ServeOrdersStateMachine(smach.Iterator):
    """ServeOrdersStateMachine

    Use this class to serve the drink orders.
    This class will execute ServeDrinkStateMachine() iterating X times.
    X is number_persons.
    """

    def __init__(self, number_persons):
        assert type(number_persons) is int and number_persons > 0
        smach.Iterator.__init__(
            self,
            outcomes=[succeeded, preempted, aborted],
            input_keys=['drink_orders'],
            output_keys=[],
            it=range(number_persons),
            it_label='order_index',
            exhausted_outcome=succeeded)

        with self:
            smach.Iterator.set_contained_state(
                'SM_SERVE_DRINK',
                ServeDrinkStateMachine(),
                loop_outcomes=['succeeded'])

# vim: expandtab ts=4 sw=4
