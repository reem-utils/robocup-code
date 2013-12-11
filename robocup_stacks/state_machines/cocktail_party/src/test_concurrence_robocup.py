#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.utils.concurrence_robocup import ConcurrenceRobocup
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine


def main():
    rospy.init_node('test_concurrence_robocup')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        sm.userdata.room_name = "exit"

        #STATES = [MoveToRoomStateMachine(), SpeakActionState("This is a test!")]

        STATES = [MoveToRoomStateMachine(announcement=None), SpeakActionState("This is a test!")]
        STATE_NAMES = []  # ["MOVE_TO_EXIT", "SPEAK_SOMETHING"]
        outcome_map = None  # {succeeded: {"MOVE_TO_EXIT": succeeded, "SPEAK_SOMETHING": succeeded}}

        smach.StateMachine.add(
            "MOVE_AND_SPEAK",
            ConcurrenceRobocup(states=STATES, state_names=STATE_NAMES, input_keys=["room_name"], outcome_map=outcome_map)
            )

    sis = smach_ros.IntrospectionServer("test_concurrence_robocup_introspection", sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == "__main__":
    main()
