
import smach
import math
import os
import rospy

from tf.transformations import quaternion_from_euler

from geometry_msgs.msg import Pose, Point, Quaternion
from smach_ros import ServiceState, SimpleActionState
#from pal_smach_utils.door_interaction.enter_door import EnterDoorStateMachine
from pal_smach_utils.utils.topic_reader import TopicReaderState
from sensor_msgs.msg import LaserScan
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted, transform_pose
from move_action import MoveActionState
from pal_smach_utils.speech.sound_action import SpeakActionState
from std_srvs.srv import Empty
from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction
from pal_smach_utils.utils.robot_controllers_activation import StopRobotControllers


LASER_TOPIC = '/LMS1xx/LAS_00'
check_for_door = False
robot = os.environ.get('PAL_ROBOT')
if robot == 'rh2c' or robot == 'rh2m' or robot == 'reemh3c' or robot == 'reemh3m' or robot == 'reemh3':
    if robot == 'rh2c' or robot == 'rh2m':
        robot = 'reemh2'
    if robot == 'reemh3c' or robot == 'reemh3m':
        robot = 'reemh3'
    check_for_door = True
    LASER_TOPIC = '/scan_filtered'
    MOTION_FOLDER_PATH = "/mnt_flash/etc/control/robot/" + robot + "/motion/"
    # if robot == 'reemh3':
    #     MOTION_FOLDER_PATH = os.environ.get('HOME') + '/' + os.environ.get('PAL_BRANCH') + '/robot/sources/etc/control/robot/' + robot + "/motion/"


class EnterRoomStateMachine(smach.StateMachine):

    WIDTH = 0.10  # Width in meters to look forward.
    READ_TIMEOUT = 15
    MAX_DIST_TO_DOOR = 3.0

    def __init__(self, distance=1.5, orient_after_passing=math.pi/2, openDoor=False):
        """
        Look for a door, open it (if needed) and enter the room.

        :param distance: The distance in meters to go into the room.
        :param orientation: 0 to look to the front, 1 to rotate towards the door

        :return output_keys: the position to the door (in abs. coordinates)
        """

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        self.door_position = -1

        with self:

            '''if openDoor:
                smach.StateMachine.add('SM_OPEN_DOOR',
                                       EnterDoorStateMachine(),
                                       transitions={succeeded: succeeded, aborted: 'SAY_CANT_OPEN'})

                smach.StateMachine.add('SAY_CANT_OPEN', SpeakActionState(text="I can't open the door. Can you please open it for me?"),
                                       transitions={succeeded: 'CROSSING_DOOR_POS', aborted: 'CROSSING_DOOR_POS'})'''

            if check_for_door:
                plan = True
                checkSafety = False

                rest_goal = MotionManagerGoal()
                rest_goal.plan = plan
                rest_goal.filename = MOTION_FOLDER_PATH + 'rest.xml'
                rest_goal.checkSafety = checkSafety
                rest_goal.repeat = False

                smach.StateMachine.add(
                    "STOP_ROBOT_CONTROLLERS",
                    StopRobotControllers(head=True, left=True, right=True),
                    transitions={succeeded: "DISABLE_REEM_ALIVE", preempted: "DISABLE_REEM_ALIVE", aborted: "DISABLE_REEM_ALIVE" }
                )  # if aborts maybe is because they are already stopped.

                smach.StateMachine.add('DISABLE_REEM_ALIVE',
                                       ServiceState('/alive_engine/stop',
                                                    Empty),
                                       transitions={succeeded: 'CROSSING_DOOR_POS'})


                smach.StateMachine.add('CROSSING_DOOR_POS', SimpleActionState('/motion_manager', MotionManagerAction,
                                                                              goal=rest_goal),
                                       transitions={succeeded: 'CHECK_CAN_PASS', aborted: 'CROSSING_DOOR_POS'})

                @smach.cb_interface(outcomes=[succeeded, aborted, preempted, 'door_too_far'])
                def check_range(userdata, message):
                    length_ranges = len(message.ranges)
                    alpha = math.atan((self.WIDTH/2)/distance)
                    n_elem = int(math.ceil(length_ranges*alpha/(2*message.angle_max)))  # Num elements from the 0 angle to the left or right
                    middle = length_ranges/2
                    cut = [x for x in message.ranges[middle-n_elem:middle+n_elem] if x > 0.01]
                    print "cut: " + str(cut)
                    minimum = min(cut)
                    if self.door_position == -1:
                        if message.ranges[middle] <= self.MAX_DIST_TO_DOOR:
                            self.door_position = message.ranges[middle]
                        else:
                            return 'door_too_far'
                    if (minimum >= distance+self.door_position):
                        return succeeded
                    rospy.loginfo("Distance in front of the robot is too small: " + str(distance+self.door_position) + ". Minimum distance: " + str(minimum))
                    return aborted

                smach.StateMachine.add('CHECK_CAN_PASS',
                                       TopicReaderState(topic_name=LASER_TOPIC,
                                                        msg_type=LaserScan,
                                                        timeout=self.READ_TIMEOUT,
                                                        callback=check_range,
                                                        outcomes=[succeeded, aborted, preempted, 'door_too_far']),
                                       remapping={'message': 'range_readings'},
                                       transitions={succeeded: 'ENTER_ROOM',
                                                    aborted: 'CHECK_CAN_PASS',
                                                    'door_too_far': 'SAY_TOO_FAR_FROM_DOOR'})

                smach.StateMachine.add('SAY_TOO_FAR_FROM_DOOR', SpeakActionState(text="I'm too far from the door."),
                                       transitions={succeeded: 'CHECK_CAN_PASS', aborted: 'CHECK_CAN_PASS'})

            def move_enter_room_cb(userdata, nav_goal):
                pose = Pose()
                pose.position = Point(distance+self.door_position, 0, 0)
                pose.orientation = Quaternion(*quaternion_from_euler(0, 0, orient_after_passing))
                nav_goal.target_pose.pose = transform_pose(pose, 'base_link', 'map')
                return nav_goal

            smach.StateMachine.add('ENTER_ROOM',
                                   MoveActionState("/map", "/move_base", goal_cb=move_enter_room_cb),
                                   transitions={succeeded: 'INTERACT_POS', aborted: 'ENTER_ROOM'} if check_for_door else {aborted: 'ENTER_ROOM'})
#                                   transitions={succeeded: 'succeeded', aborted: 'ENTER_ROOM'} if check_for_door else {aborted: 'ENTER_ROOM'})

            if check_for_door:  # It's safer to navigate with the arms like that
                interact_goal = MotionManagerGoal()
                interact_goal.plan = plan
                interact_goal.checkSafety = checkSafety
                interact_goal.repeat = False
                interact_goal.filename = MOTION_FOLDER_PATH + 'interact.xml'
                smach.StateMachine.add('INTERACT_POS',
                                       SimpleActionState('/motion_manager', MotionManagerAction, goal=interact_goal),
                                       transitions={succeeded: succeeded})

# vim: expandtab ts=4 sw=4
