#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('emergency_situation')
import rospy
import smach
import smach_ros
# import shutil

# from pal_smach_utils.navigation.enter_room import EnterRoomStateMachine
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine

from save_people import SavePeopleStateMachine
from pal_smach_utils.speech.sound_action import SpeakActionState
from detect_fire import DetectFireOrSmokeStateMachine
from pal_smach_utils.navigation.enter_room import EnterRoomStateMachine

from call_fire_department import CallFireDepartmentState
from pal_smach_utils.utils.run_command_on_robot import RunCommandOnRobot

DOOR_DISTANCE = 1.2
# DETECT_PEOPLE_TIMEOUT=2


class DummyExitStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted, preempted], output_keys=['o_room_name_exit'])

    def execute(self, userdata):
        userdata.o_room_name_exit = "exit"  # check room name spelling
        return succeeded


def main():
    rospy.init_node('emergency_situation_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    # PRE: This state machines requires that the face database is empty!
    #      SM_RECOGNIZE_AND_MOVE_TO_CALLER assumes that any known persons
    #      are participating in the test.

    with sm:

        smach.StateMachine.add(
            "ARMS_TO_SAFE_POSITION",
            RunCommandOnRobot(command="rosrun reem_move_arm_action move --arm=left --pose=home_to_init; rosrun reem_move_arm_action move --arm=right --pose=home_to_init;"),
            transitions={succeeded: "SAY_READY", aborted: "SAY_READY"})

        smach.StateMachine.add(
            "SAY_READY",
            SpeakActionState("I'm ready to start the Emergency Situation challenge!"),
            transitions={succeeded: "ENTER_ROOM", aborted: "ENTER_ROOM", preempted:  "ENTER_ROOM"})

        smach.StateMachine.add(
            'ENTER_ROOM',
            EnterRoomStateMachine(DOOR_DISTANCE, orient_after_passing=0),
            transitions={succeeded: 'INFORM_THE_EMERGENCY', aborted: 'ENTER_ROOM'})
        # outputs: 'door_position'

        smach.StateMachine.add(
            'INFORM_THE_EMERGENCY',
            SpeakActionState("I know that there is fire in the kitchen."),
            transitions={succeeded: 'MOVE_TO_KITCHEN', aborted: 'MOVE_TO_KITCHEN'})

        sm.userdata.room_name = 'kitchen'
        smach.StateMachine.add(
            'MOVE_TO_KITCHEN',
            MoveToRoomStateMachine(),
            transitions={succeeded: 'DETECT_FIRE_OR_SMOKE', aborted: aborted})

        smach.StateMachine.add(
            'DETECT_FIRE_OR_SMOKE',
            DetectFireOrSmokeStateMachine(),
            transitions={succeeded: 'SAVE_PEOPLE', aborted: 'DETECT_FIRE_OR_SMOKE'},
            remapping={'location_of_fire': 'location_of_fire'})

        smach.StateMachine.add(
            'SAVE_PEOPLE',
            SavePeopleStateMachine(),
            transitions={aborted: 'SAVE_PEOPLE', succeeded: 'INFORM_FIRE_DEPARTMENT'},
            remapping={'location_list': 'location_list'})

        smach.StateMachine.add(
            'INFORM_FIRE_DEPARTMENT',
            CallFireDepartmentState(),
            transitions={succeeded: 'EVERYBODY_SAVED'})

        smach.StateMachine.add(
            'EVERYBODY_SAVED',
            SpeakActionState("Everybody is saved!"),
            transitions={succeeded: 'EXIT_APARTMENT_DUMMY', aborted: aborted})

        smach.StateMachine.add(
            'EXIT_APARTMENT_DUMMY',
            DummyExitStateMachine(),
            transitions={succeeded: 'EXIT_APARTMENT'},
            remapping={'o_room_name_exit': 'room_name'})

        smach.StateMachine.add(
            'EXIT_APARTMENT',
            MoveToRoomStateMachine(),
            transitions={succeeded: succeeded, aborted: "EXIT_APARTMENT"})

    sis = smach_ros.IntrospectionServer(
        'emergency_situation_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
