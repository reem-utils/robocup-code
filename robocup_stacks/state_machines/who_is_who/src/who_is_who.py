#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('who_is_who')
import rospy
import smach
import smach_ros

from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Pose, Point, Quaternion

from pal_smach_utils.navigation.enter_room import EnterRoomStateMachine
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.utils.timeout_container import TimeoutContainer
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted

from pal_smach_utils import *
from pal_smach_utils.utils.recognize_face import RecognizeSeveralFacesStateMachine
from pal_smach_utils.speech.sm_listen_go_to_room import ListenGoToRoomStateMachine
from pal_smach_utils.utils.math_utils import multiply_quaternions
from pal_smach_utils.navigation.recognize_and_move_to_caller import RecognizeAndMoveToCallerStateMachine
from pal_smach_utils.navigation.serve_drinks import ServeOrdersStateMachine
from pal_smach_utils.speech.take_drink_orders import TakeDrinkOrdersStateMachine

DOOR_DISTANCE = rospy.get_param('/who_is_who/door_distance')  # meters
RECOGNIZE_CALLER_TIMEOUT = rospy.get_param('/who_is_who/recognize_caller_timeout')  # seconds


class FakeEntry(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted],
            output_keys=['orders', 'guests_locations'])

    def execute(self, userdata):
        userdata.orders = [DrinkOrder('david', 'coke'), DrinkOrder('michael', 'milk')]
        pose = Pose()
        pose.position = Point(0.059, 6.26, 0.0)
        pose.orientation = Quaternion(0, 0, -0.59, 0.8)
        userdata.guests_location = pose
        return succeeded


def main():
    rospy.init_node('who_is_who_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    # PRE: This state machines requires that the face database is empty!
    #      SM_RECOGNIZE_AND_MOVE_TO_CALLER assumes that any known persons
    #      are participating in the test.

    with sm:

        #smach.StateMachine.add('FAKE_ENTRY', FakeEntry(),
        #    transitions={succeeded: 'SM_SERVE_ORDERS'})

        smach.StateMachine.add(
            'ENTER_ROOM',
            EnterRoomStateMachine(DOOR_DISTANCE),
            transitions={succeeded: 'SM_RECOGNIZE_FACES', aborted: 'ENTER_ROOM'})
        # outputs: 'door_position'

        smach.StateMachine.add(
            'SM_RECOGNIZE_FACES',
            RecognizeSeveralFacesStateMachine(num_persons=3, recognize_existing=False),
            transitions={succeeded: 'SM_LISTEN_AND_GO_TO_ROOM'})
        # outputs: 'person_names'

        smach.StateMachine.add(
            'SM_LISTEN_AND_GO_TO_ROOM',
            ListenGoToRoomStateMachine(),
            transitions={succeeded: 'SM_RECOGNIZE_AND_MOVE_TO_CALLER'},
            remapping={'room_location': 'guests_location'})

        # FIXME: split out recognition part from raised arm part!
        smach.StateMachine.add(
            'SM_RECOGNIZE_AND_MOVE_TO_CALLER',
            TimeoutContainer(RECOGNIZE_CALLER_TIMEOUT,
                RecognizeAndMoveToCallerStateMachine()),
            transitions={
                succeeded: 'SM_TAKE_DRINK_ORDERS',
                preempted: 'SM_TAKE_DRINK_ORDERS',
                #aborted:   'SM_RECOGNIZE_AND_MOVE_TO_CALLER'
                aborted:   'SM_TAKE_DRINK_ORDERS'
            })
        # outputs: 'caller_name'

        smach.StateMachine.add(
            'SM_TAKE_DRINK_ORDERS',
            TakeDrinkOrdersStateMachine(),
            transitions={succeeded: 'SM_SERVE_ORDERS'})
        # inputs: 'caller_name', 'person_names', outputs: 'orders'

        smach.StateMachine.add(
            'SM_SERVE_ORDERS',
            ServeOrdersStateMachine(),
            transitions={succeeded: 'MOVE_TO_DOOR'})
        # inputs: 'orders', 'guests_location'

        def move_to_door_goal_cb(userdata, nav_goal):
            pose = userdata.door_position

            # Rotate 180º so the robot faces the right direction (outside)
            rotation = Quaternion(*quaternion_from_euler(0, 0, 3.14))
            pose.orientation = multiply_quaternions(rotation, pose.orientation)

            nav_goal.target_pose.pose = pose
            return nav_goal

        smach.StateMachine.add(
            'MOVE_TO_DOOR',
            MoveActionState(
                "/map",
                goal_cb=move_to_door_goal_cb,
                input_keys=['door_position']),
            transitions={})

    sis = smach_ros.IntrospectionServer(
        'who_is_who_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
