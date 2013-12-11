#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.navigation.move_to_caller import MoveToCallerStateMachine
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables as cp_vars


def main():
    """Unit test to MoveToCallerStateMachine. Will look for someone waving the
    hand and move to the position where the movement was found."""

    rospy.init_node('test_move_to_caller_state_machine')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:
        sm.userdata.nombre = "Ruben"

        def test_cb(userdata):
            return "Where are you %s?" % str(userdata.nombre)

        smach.StateMachine.add("MOVE_TO_CALLER",
            MoveToCallerStateMachine(ask_for_movement_msg_cb=test_cb, input_keys=["nombre"], rotation_left=cp_vars.ROTATE_LEFT)
            )

    sis = smach_ros.IntrospectionServer(
        'test_move_to_caller_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
