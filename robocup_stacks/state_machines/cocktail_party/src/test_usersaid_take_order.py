#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros
import random

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
#from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables
#from pal_smach_utils.utils.check_dependences import CheckDependencesState
from pal_smach_utils.speech.take_drink_order import TakeDrinkOrderStateMachine
from pal_smach_utils.utils.learn_face import PERSON_NAMES


class DebugDrinkOrders(smach.State):
        def __init__(self):
            smach.State.__init__(self, input_keys=["out_drink_order"], output_keys=[], outcomes=[succeeded, preempted, aborted])

        def execute(self, userdata):
            print "===========>>> [DEBUG] DRINK_ORDERS <<<==================="
            print "Person: %-10s, Drink: %s" % (userdata.out_drink_order.person_name, userdata.out_drink_order.drink)
            return succeeded


def main():
    """Unit test for TakeDrinkOrderStateMachine.
    Will test what the robot can hear after ask the person what whant to drink
    """

    rospy.init_node('test_take_drink_order_usersaid')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:
        sm.userdata.drinks_already_requested = []
        sm.userdata.in_person_name = PERSON_NAMES[random.randint(0, len(PERSON_NAMES) - 1)]

        # variables = cocktail_party_variables
        # smach.StateMachine.add(
        #     "CHECK_DEPENDENCES",
        #     CheckDependencesState(
        #         topic_names=variables.TOPICS,
        #         service_names=variables.SERVICES,
        #         action_names=variables.ACTIONS,
        #         map_locations=variables.MAP_LOCATIONS),
        #         #CheckDependencesState(),
        #     transitions={succeeded: "TAKE_DRINK_ORDERS", aborted: aborted}
        #     )

        smach.StateMachine.add(
                    "TAKE_DRINK_ORDER",
                    TakeDrinkOrderStateMachine(),
                    transitions={succeeded: "DEBUG_DRINK_ORDERS", aborted: "TAKE_DRINK_ORDER", preempted: "TAKE_DRINK_ORDER"}
                    )
            #inputs: "in_person_name". outputs:"out_drink_order"

        smach.StateMachine.add(
            "DEBUG_DRINK_ORDERS",
            DebugDrinkOrders()
            )

    sis = smach_ros.IntrospectionServer(
        'test_take_drink_order_usersaid_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
