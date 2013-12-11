""" Contains the MoveToCallerStateMachine """
import smach
import math
from smach_ros import SimpleActionState
from geometry_msgs.msg import Quaternion, Pose, Point, PoseStamped
from tf.transformations import quaternion_from_euler
from move_base_msgs.msg import MoveBaseGoal
from rospy import loginfo, Duration, Time
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted, transform_pose, check_topic
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers
from pal_smach_utils.utils.publish_marker import PublishMarker
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables as cp_vars
from pal_smach_utils.utils.gesture_recognition import GestureRecognition
from pal_smach_utils.utils.pose_at_distance import pose_at_distance
from pal_smach_utils.utils.colors import colors as C
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.speech.sound_action import SpeakActionState
from pr2_controllers_msgs.msg import PointHeadAction, PointHeadGoal
from geometry_msgs.msg import PointStamped
from pal_smach_utils.utils.run_script_on_robot import RunScriptOnRobot, ROBOT_SCRIPTS_PATH
from pal_smach_utils.utils.timeout_container import SleepState

ASK_FOR_MOVEMENT_MSG = "I'm looking for someone waving the hand."
DEGREES_TO_ROTATE = 90
DEGREES_IN_RADIANS = DEGREES_TO_ROTATE * math.pi / 180
COUNTNUMBER = 360 / DEGREES_TO_ROTATE
# Look at a point 45 degrees up
X_HEAD_VALUE = 1.0
Y_HEAD_VALUE = 0.0
Z_HEAD_VALUE = 0.0
MAX_HEAD_VEL = 1.0
Y_VARIANCE = 0.25
# POINTING_FRAME_RH2 = "/head_sonar_20_link"
POINTING_FRAME_RH3 = "/head_mount_xtion_link"
HEAD_ACTION_TIMEOUT = 5
NO_ROTATE = "no_rotate"


class MoveToCallerStateMachine(smach.StateMachine):
    """MoveToCallerStateMachine.

    Use this State Machine to move the robot to someone that is waving the hand.

    Requirements:
        Kinect

    When calling this State Machine, the robot will execute the script gestureRecognitionStart.sh that enables the kinect.
    Will look for someone waving the hand. If no movements are found, will rotate 90 degrees and look for movement again.

    """
    def __init__(self, ask_for_movement_msg_cb=None, rotation_left=True, input_keys=[], output_keys=[]):
        """Constructor for MoveToCallerStateMachine.

        @type ask_for_movement_msg_cb: callable|None
        @param ask_for_movement_msg_cb: The function that provide the tts when the robot don't detect movements.

        @type rotation_left: boolean
        @param rotation_left: If True, the robot will rotate left if don't detect movement. It will rotate right otherwise.

        """
        smach.StateMachine.__init__(self, input_keys=input_keys, output_keys=output_keys + ["out_caller_position"],
            outcomes=[succeeded, aborted, preempted])

        def generic_goal_cb(userdata):
            """ This function call ask_for_movement_msg_cb if defined when no
            movements are found. Otherwise, will return a default message """
            if ask_for_movement_msg_cb is not None:
                return ask_for_movement_msg_cb(userdata)
            return ASK_FOR_MOVEMENT_MSG

        def check_topic_again(userdata):
            """ This function should be called if the first check_topic aborts.
            Was created because some times the driver is not found, so, with
            this function we save time running the StateMachine.
            """
            SleepState(duration=5).execute(userdata)
            return check_topic(userdata, cp_vars.T_RECOGNIZED_GESTURES)


        with self:

            self.input_keys = input_keys
            self.output_keys = output_keys

            up_movement = PointStamped()
            up_movement.point.x = 0.4  # X_HEAD_VALUE
            up_movement.point.y = 0.0  # Y_HEAD_VALUE
            up_movement.point.z = 1.65  # Z_HEAD_VALUE
            up_movement.header.frame_id = "/base_link"

            self.head_up_goal = PointHeadGoal()
            self.head_up_goal.pointing_frame = POINTING_FRAME_RH3
            self.head_up_goal.pointing_axis.x = 1.0
            self.head_up_goal.pointing_axis.y = 0.0
            self.head_up_goal.pointing_axis.z = 0.0
            self.head_up_goal.min_duration = Duration(1)  # FIXME: What means min_duration
            self.head_up_goal.max_velocity = MAX_HEAD_VEL
            self.head_up_goal.target = up_movement

            self.head_movements = 0
            self.body_movements = 0

            def my_termination_cb(userdata, terminal_states, outcome):
                """
                This function does:
                    Reset the counters because when this StateMachine is called more
                    than one time, the robot can rotate the head/body in a wrong order.

                    Stop the head controllers
                """
                if outcome == aborted:
                    userdata.out_caller_position = PoseStamped()
                    userdata.out_caller_position.header.frame_id = "/base_link"

                self.head_movements = 0
                self.body_movements = 0
                #The code below is useful to avoid problems if this SM aborts
                loginfo("STOPPING HEAD CONTROLLERS")
                StopRobotControllers(head=True, left=False, right=False).execute(userdata)
                loginfo("STOPPING GESTURE_RECOGNITION")
                RunScriptOnRobot(robot_scripts_path=ROBOT_SCRIPTS_PATH, script_name="gestureRecognitionStop.sh").execute(userdata)


            self.register_termination_cb(my_termination_cb)

#            SOME TIMES GESTURE RECOGNITION ONLY WORKS IF RESTARTED, I DONT KNOW WHY. REMOVING RESTARTING
#            BECAUSE NOW THIS SM IS CHECKING IF THE TOPIC 'EXISTS'
#            smach.StateMachine.add(
#                "FIRST_STOP_GESTURE_RECOGNITION",
#                RunScriptOnRobot(robot_scripts_path=ROBOT_SCRIPTS_PATH, script_name="gestureRecognitionStop.sh"),
#                transitions={succeeded: "START_GESTURE_RECOGNITION", aborted: "START_GESTURE_RECOGNITION"}
#                )

            smach.StateMachine.add(
                "START_GESTURE_RECOGNITION",
                RunScriptOnRobot(robot_scripts_path=ROBOT_SCRIPTS_PATH, script_name="gestureRecognitionStart.sh"),
                transitions={succeeded: "START_HEAD_CONTROLLERS", aborted: "START_HEAD_CONTROLLERS"}
                )

            smach.StateMachine.add(
                "START_HEAD_CONTROLLERS",
                StartRobotControllers(head=True, left=False, right=False),
                transitions={succeeded: "RAISE_THE_HEAD", aborted: "RAISE_THE_HEAD", preempted: "RAISE_THE_HEAD"}
                ) # If aborts will continue to avoid infinity loops

            def head_position_cb(userdata, message):
                """ Send a PointHeadGoal object to the robot move the head. The position can be on looking in front, left or right """
                self.head_movements += 1

                if (self.head_movements % 3) is 0:
                    loginfo(C.BACKGROUND_GREEN + "MOVING HEAD LEFT" + C.NATIVE_COLOR)
                    self.head_up_goal.target.point.y = Y_VARIANCE
                    return self.head_up_goal  # Left

                if (self.head_movements % 3) is 1:
                    loginfo(C.BACKGROUND_GREEN + "MOVING HEAD CENTER" + C.NATIVE_COLOR)
                    self.head_up_goal.target.point.y = 0.0
                    return self.head_up_goal  # Center

                loginfo(C.BACKGROUND_GREEN + "MOVING HEAD RIGHT" + C.NATIVE_COLOR)
                self.head_up_goal.target.point.y = - Y_VARIANCE
                return self.head_up_goal  # Right

            smach.StateMachine.add(
                "RAISE_THE_HEAD",
                SimpleActionState(
                    cp_vars.A_HEAD_CONTROLLER,
                    PointHeadAction, goal_cb=head_position_cb, exec_timeout=Duration(HEAD_ACTION_TIMEOUT)),
                transitions={succeeded: "CHECK_TOPIC", aborted: "CHECK_TOPIC", preempted: "CHECK_TOPIC"}
                )

            smach.StateMachine.add(
                "CHECK_TOPIC",
                smach.CBState(check_topic, cb_args=[cp_vars.T_RECOGNIZED_GESTURES], outcomes=[succeeded, aborted]),
                transitions={succeeded: "GET_WAVE_GESTURE_POSITION", aborted: "CHECK_TOPIC_AGAIN"}
            )

            smach.StateMachine.add(
                "CHECK_TOPIC_AGAIN",
                smach.CBState(check_topic_again, outcomes=[succeeded, aborted]),
                transitions={succeeded: "GET_WAVE_GESTURE_POSITION", aborted: aborted}
            )

            smach.StateMachine.add(
                "GET_WAVE_GESTURE_POSITION",
                GestureRecognition(),
                transitions={succeeded: "ANALYZE_AND_TRANSFORM_RESULT", aborted: "ROTATE_HEAD_CHECK", preempted: "ROTATE_HEAD_CHECK"}
                )
            #output_keys=['gesture_id_out', "out_person_position"]

            def convert_to_base_link(userdata):
                """ This function convert the received pose from the kinect to base_link """
                pose = Pose()
                pose.position = userdata.in_position.position3D

                if math.isnan(pose.position.x) or math.isnan(pose.position.y) or math.isnan(pose.position.z):
                    userdata.out_goal_position = userdata.in_position
                    return aborted

                parent_frame_id = "/gesture_detection_frame"
                outpose = transform_pose(pose, parent_frame_id, "/base_link")
                outpose.position.z = 0.0
                userdata.out_goal_position = outpose
                return succeeded

            smach.StateMachine.add(
                "ANALYZE_AND_TRANSFORM_RESULT",  # Analyse if in out_position exists some NOT A NUMBER
                smach.CBState(convert_to_base_link, input_keys=["in_position"], output_keys=["out_goal_position"], outcomes=[succeeded, aborted]),
                remapping={"in_position": "out_person_position"},
                transitions={succeeded: "STOP_HEAD_CONTROLLERS", aborted: "GET_WAVE_GESTURE_POSITION"}
                )
            # output_keys=["out_goal_position"]

            def check_rotate_head(userdata, max_rotations=1):
                """ Check if the head should be rotated. Returns succeeded if yes, aborted otherwise """
                self.head_movements += 1
                if (self.head_movements % max_rotations) is 0:
                    return succeeded
                return aborted

            smach.StateMachine.add(
                "ROTATE_HEAD_CHECK",
                smach.CBState(check_rotate_head, outcomes=[succeeded, aborted]),
                transitions={succeeded: "MOVE_HEAD", aborted: "ROTATE_ROBOT_CHECK"}
                )

            smach.StateMachine.add(
                'MOVE_HEAD',
                SimpleActionState(
                    cp_vars.A_HEAD_CONTROLLER,
                    PointHeadAction, goal_cb=head_position_cb, exec_timeout=Duration(HEAD_ACTION_TIMEOUT)),
                transitions={succeeded: "ROTATE_ROBOT_CHECK", aborted: "ROTATE_ROBOT_CHECK", preempted: "ROTATE_ROBOT_CHECK"}
                )

            def check_rotate_robot(userdata, max_rotations=4):
                """ Check if the robot already have rotated $max_rotations times. """
                #TODO add a parameter head_rotations, to be 'generic' and easy to maintain. Actualy this value is 3
                self.body_movements += 1
#                print str(self.body_movements)  + "/" + str(max_rotations * 3) + " = " + str(self.body_movements % (max_rotations * 3))
                if (self.body_movements % (max_rotations * 3)) is 0:  # The body was rotated 3 times
                    userdata.out_caller_position = None
                    return aborted
                if (self.body_movements % 3) is 0:  # The head was rotated 3 times
                    return succeeded
                return NO_ROTATE  # The robot shouldn't rotate the body yet

            smach.StateMachine.add(
                "ROTATE_ROBOT_CHECK",
                smach.CBState(check_rotate_robot, output_keys=["out_caller_position"], outcomes=[succeeded, aborted, NO_ROTATE]),
                transitions={succeeded: "ROTATE_ROBOT", NO_ROTATE: "ASK_FOR_MOVEMENT", aborted: aborted}
                )

            def rotate_goal_cb(userdata, nav_goal):
                """ Send a MoveBaseGoal object to rotate the robot """
                pose = Pose()
                pose.position = Point(0, 0, 0)

                if rotation_left is True:
                    pose.orientation = Quaternion(*quaternion_from_euler(0, 0, DEGREES_IN_RADIANS))
                    loginfo(C.BACKGROUND_GREEN + "ROTATING ROBOT TO LEFT" + C.NATIVE_COLOR)
                else:
                    pose.orientation = Quaternion(*quaternion_from_euler(0, 0, -DEGREES_IN_RADIANS))
                    loginfo(C.BACKGROUND_GREEN + "ROTATING ROBOT TO RIGHT" + C.NATIVE_COLOR)

                move_base_goal = MoveBaseGoal()
                move_base_goal.target_pose.header.stamp = Time.now()
                move_base_goal.target_pose.header.frame_id = "/base_link"
                move_base_goal.target_pose.pose = pose

                return move_base_goal

            smach.StateMachine.add(
                "ROTATE_ROBOT",
                MoveActionState(goal_cb=rotate_goal_cb),
                transitions={succeeded: "ASK_FOR_MOVEMENT", aborted: "ASK_FOR_MOVEMENT", preempted: "ASK_FOR_MOVEMENT"}
                )

            smach.StateMachine.add(
                "ASK_FOR_MOVEMENT",
                SpeakActionState(text_cb=generic_goal_cb, input_keys=self.input_keys, output_keys=self.output_keys),
                transitions={succeeded: "GET_WAVE_GESTURE_POSITION", aborted: "GET_WAVE_GESTURE_POSITION", preempted: "GET_WAVE_GESTURE_POSITION"}
                )

            smach.StateMachine.add(
                "STOP_HEAD_CONTROLLERS",
                StopRobotControllers(head=True, left=False, right=False),
                transitions={succeeded: "STOP_GESTURE_RECOGNITION", aborted: "STOP_GESTURE_RECOGNITION", preempted: "STOP_GESTURE_RECOGNITION"}
                )

            smach.StateMachine.add(
                "STOP_GESTURE_RECOGNITION",
                RunScriptOnRobot(robot_scripts_path=ROBOT_SCRIPTS_PATH, script_name="gestureRecognitionStop.sh"),
                transitions={succeeded: "PUBLISH_MARKER", aborted: "PUBLISH_MARKER"}
                #If aborts this SM will continue to avoid possible infinity loops.
                )

            smach.StateMachine.add(
                "PUBLISH_MARKER",
                PublishMarker(),
                remapping={"in_pose": "out_goal_position"},
                transitions={succeeded: "MOVE_TO_DETECTED_POSITION"}
                )

            def move_to_caller_goal_cb(userdata, nav_goal):
                """ Returns a MoveBaseGoal object with the position where the movement was detected
                and set userdata.out_caller_position variable with a PoseStamped object """
                move_base_goal = MoveBaseGoal()
                move_base_goal.target_pose.header.frame_id = "/map"

                pose_detected = pose_at_distance(userdata.in_goal_position, 0.5)
                pose_detected.position.z = 0

                teta = math.atan2(pose_detected.position.y, pose_detected.position.x)
                pose_detected.orientation = Quaternion(*quaternion_from_euler(0, 0, teta))
                pose = transform_pose(pose_detected, "/base_link", "/map")
                move_base_goal.target_pose.pose = pose
                userdata.out_caller_position = move_base_goal.target_pose

                move_base_goal.target_pose.header.stamp = Time.now()

                return move_base_goal

            smach.StateMachine.add(
                'MOVE_TO_DETECTED_POSITION',
                MoveActionState(
                     move_base_action_name=cp_vars.A_MOVE_BASE,  # A_MOVE_BY
                    goal_cb=move_to_caller_goal_cb,
                    input_keys=['in_goal_position'],
                    output_keys=["out_caller_position"]),
                remapping={"in_goal_position": "out_goal_position"},
                transitions={succeeded: "ANNOUNCE_CALLER", aborted: "ASK_COME_HERE", preempted: "ASK_COME_HERE"})
                #output_keys=["out_caller_position"]

            smach.StateMachine.add(
                "ANNOUNCE_CALLER",
                SpeakActionState("You were looking for me? Here I am!"),
                transitions={succeeded: succeeded, aborted: succeeded})

            smach.StateMachine.add(
                "ASK_COME_HERE",
                SpeakActionState(text="Sorry, I can't go where you are. Can you come here please?"),
                transitions={succeeded: "SLEEP_A_TIME", aborted: "SLEEP_A_TIME"}
            )

            smach.StateMachine.add(
                "SLEEP_A_TIME",
                SleepState(5),
                transitions={succeeded: succeeded, preempted: succeeded}
            )
