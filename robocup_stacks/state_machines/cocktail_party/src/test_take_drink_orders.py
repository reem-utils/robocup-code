#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
#from pal_smach_utils.utils.drink_order import DrinkOrder
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables
from pal_smach_utils.utils.check_dependences import CheckDependencesState
from take_several_drink_orders import TakeSeveralDrinkOrdersStateMachine
from pal_smach_utils.utils.drop_faces import DropAllFacesStateMachine
from pal_smach_utils.utils.run_script_local import RunScriptLocal


class DebugDrinkOrders(smach.State):
        def __init__(self):
            smach.State.__init__(self, input_keys=["drink_orders"], output_keys=[], outcomes=[succeeded, preempted, aborted])

        def execute(self, userdata):
            print "===========>>> [DEBUG] DRINK_ORDERS <<<==================="
            for order in userdata.drink_orders:
                print "Person: %-10s, Drink: %s" % (order.person_name, order.drink)
            return succeeded


def main():
    """Test for TakeSeveralDrinkOrdersStateMachine. Will delete all faces and
    restart personServer. The kinect should be connected and gestureRecognitionStart.sh
    should be previously executed."""

    rospy.init_node('test_take_drink_orders_state_machine')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:
        variables = cocktail_party_variables
        #sm.userdata.drink_orders = [DrinkOrder("Homer", "milk"), DrinkOrder("Lisa", "coke"), DrinkOrder("Bart", "coke")]

#        smach.StateMachine.add(
#            "CHECK_DEPENDENCES",
#            CheckDependencesState(
#                topic_names=variables.TOPICS,
#                service_names=variables.SERVICES,
#                action_names=variables.ACTIONS,
#                map_locations=variables.MAP_LOCATIONS),
#                #CheckDependencesState(),
#            transitions={succeeded: "DROP_FACES", aborted: aborted}
#            )

        smach.StateMachine.add(
            "DROP_FACES",
            DropAllFacesStateMachine(),
            transitions={succeeded: "TAKE_DRINK_ORDERS", aborted: aborted}
            )
#
#        smach.StateMachine.add(
#            "START_GESTURE_RECOGNITION",
#            RunScriptLocal(script_name="gestureRecognitionStart.sh"),
#            transitions={succeeded: "TAKE_DRINK_ORDERS", aborted: "START_GESTURE_RECOGNITION"}
#            )

        smach.StateMachine.add(
            "TAKE_DRINK_ORDERS",
            TakeSeveralDrinkOrdersStateMachine(num_persons=variables.NUMBER_PERSONS)  # ,
#            transitions={succeeded: "DEBUG_DRINK_ORDERS"}
            )
#        smach.StateMachine.add(
#            "DEBUG_DRINK_ORDERS",
#            DebugDrinkOrders(),
#            transitions={succeeded: "STOP_GESTURE_RECOGNITION"}
#            )
#
#        smach.StateMachine.add(
#            "STOP_GESTURE_RECOGNITION",
#            RunScriptLocal(script_name="gestureRecognitionStop.sh"),
#            transitions={succeeded: succeeded, aborted: aborted}
#            )

    sis = smach_ros.IntrospectionServer(
        'test_take_drink_orders_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
