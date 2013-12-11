from roslib import load_manifest
load_manifest("pal_smach_utils")

from smach import StateMachine, CBState
from rospy import loginfo

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.utils.colors import colors as C
from pal_smach_utils.navigation.take_several_drink_orders import TakeSeveralDrinkOrdersStateMachine
from pal_smach_utils.navigation.serve_drinks import ServeOrdersStateMachine
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine


class TakeServeDrinkOrdersSM(StateMachine):
    """ Use this class to take the drink orders and serve. """
    def __init__(self, num_persons, all_at_a_time, room_name, sleep, ask_to_come):
        """ Constructor for TakeServeDrinkOrdersSM

        :type num_persons: integer
        :param num_persons:  The number of persons to be served

        :type all_at_a_time: boolean
        :param all_at_a_time: If True, the robot will take all drink orders first,\
        and after this, will serve, otherwise will take and serve ONE drink at a time.

        :type room_name: string
        :param room_name: The room where the robot should go to take drink orders \
        if 'all_at_a_time' is not True

        :type sleep: int
        :param sleep: The number of seconds that the robot will sleep after ask\
        the person to come if MoveToCaller aborts

        :type ask_to_come: bool
        :param ask_to_come: If true, the robot will ask the person to come and\
        wait $sleep seconds. Otherwise, will move to caller.
        """
        assert type(all_at_a_time) is bool
        assert type(num_persons) is int and num_persons > 0
        assert type(room_name) is str and len(room_name) > 0
        assert type(sleep) is int and sleep > 0
        StateMachine.__init__(self, input_keys=[], output_keys=[], outcomes=[succeeded, aborted, preempted])

        NUMBER_PERSONS = 1
        TAKE_ORDER_STATE= "TAKE_DRINK_ORDER"
        DEBUG_STATE = "DEBUG_DRINK_ORDER"
        SERVE_ORDER_STATE = "SERVE_ORDER"
        FINAL_STATE = "CHECK_REPEAT"
        MOVE_BACK_ROOM = "MOVE_BACK_PARTY_ROOM"

        with self:

            if all_at_a_time is True:
                NUMBER_PERSONS = num_persons
                TAKE_ORDER_STATE += "S"
                DEBUG_STATE += "S"
                SERVE_ORDER_STATE += "S"
                FINAL_STATE = succeeded

            def start_cb(userdata, initial_st_name):
                """ Set the variable userdata.room_name used by MoveToRoom """
                userdata.room_name = room_name

            self.register_start_cb(start_cb)

            StateMachine.add(
                TAKE_ORDER_STATE,
                TakeSeveralDrinkOrdersStateMachine(num_persons=NUMBER_PERSONS, sleep=sleep, ask_to_come=ask_to_come),
                transitions={succeeded: DEBUG_STATE}
                #The aborted transition is not been catched because in theory will never abort.
            )# outputs: "drink_orders"

            def print_drink_orders(userdata):
                print C.WHITE_BOLD + "DRINK ORDER(S)"
                for order in userdata.drink_orders:
                    loginfo( "Person: %-10s, Drink: %s" % (order.person_name, order.drink))
                print C.NATIVE_COLOR
                return succeeded

            StateMachine.add(
                DEBUG_STATE,
                CBState(print_drink_orders, input_keys=["drink_orders"], outcomes=[succeeded, aborted]),
                transitions={succeeded: SERVE_ORDER_STATE, aborted: SERVE_ORDER_STATE}
            )

            StateMachine.add(
                SERVE_ORDER_STATE,
                ServeOrdersStateMachine(number_persons=NUMBER_PERSONS),
                transitions={succeeded: FINAL_STATE, aborted: FINAL_STATE, preempted: FINAL_STATE}
                )

            if all_at_a_time is not True:
                self.people_served = 0
                def check_repeat(userdata):
                    """ Check if still should take and serve drinks"""
                    self.people_served += 1
                    if self.people_served < num_persons:
                        return succeeded
                    return aborted

                StateMachine.add(
                    FINAL_STATE,
                    CBState(check_repeat, outcomes=[succeeded,aborted]),
                    transitions={succeeded: MOVE_BACK_ROOM, aborted: succeeded}
                )

                StateMachine.add(
                    MOVE_BACK_ROOM,
                    MoveToRoomStateMachine(announcement="I'm going to %s to take another drink order."),
                    transitions={succeeded: TAKE_ORDER_STATE, aborted: TAKE_ORDER_STATE, preempted: TAKE_ORDER_STATE}
                )
                #input_keys=["room_name"]

# vim: expandtab ts=4 sw=4
