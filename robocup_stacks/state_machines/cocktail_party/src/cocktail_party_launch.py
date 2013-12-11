#! /usr/bin/env python

import roslib
roslib.load_manifest('cocktail_party')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted, print_grasp_errors
from cocktail_party import CocktailPartyStateMachine


def main():
    rospy.init_node('cocktail_party_launch')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:
        smach.StateMachine.add(
            "COCKTAIL_PARTY_TEST",
            CocktailPartyStateMachine(),
            transitions={succeeded: "PRINT_GRASP_ERRORS", preempted: "PRINT_GRASP_ERRORS", aborted: "PRINT_GRASP_ERRORS"}
        )

        smach.StateMachine.add(
            "PRINT_GRASP_ERRORS",
            smach.CBState(print_grasp_errors, outcomes=[succeeded])
        )                            

    sis = smach_ros.IntrospectionServer(
        'cocktail_party_launch_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
