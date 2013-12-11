import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted, transform_pose
from pal_smach_utils.utils.learn_face import LearnFaceStateMachine
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables as cp_vars
from pal_smach_utils.utils.timeout_container import SleepState
from pal_smach_utils.navigation.move_to_caller import MoveToCallerStateMachine
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.speech.take_drink_order import TakeDrinkOrderStateMachine
from pal_smach_utils.speech.sound_action import SpeakActionFromPoolStateMachine, SpeakActionState
from geometry_msgs.msg import PoseStamped, Pose


class MoveToCaller_LearnPerson_TakeDrinkOrder(smach.StateMachine):

    def add_move_to_caller(self, num_persons):
        """ Set some states at the beginning of the SM that only will be added\
        if $ask_to_come is true

        :type last_sleep_name: str
        :param last_sleep_name: The name of the second SleepState state

        :type sleep: int
        :param sleep: Seconds to sleep while the person come to the robot.
        """
        default = "Who want something to drink?"
        phrases = ["Hi everyone! " + default, "Hi all! " + default, "Hello everybody! " + default]
        self.userdata.room_name = cp_vars.M_PARTY_ROOM
        self.LAST_STATE = 'CHECK_BACK_PARTY_ROOM'

        smach.StateMachine.add(
            "ASK_WHO_WANT_DRINK",
            SpeakActionFromPoolStateMachine(phrases),
            transitions={succeeded: "MOVE_TO_CALLER", aborted: "MOVE_TO_CALLER", preempted: "MOVE_TO_CALLER"}
            )

        smach.StateMachine.add(
            "MOVE_TO_CALLER",
            MoveToCallerStateMachine(rotation_left=cp_vars.ROTATE_LEFT),
            transitions={succeeded: "LEARN_FACE", preempted: "ASK_TO_COME", aborted: "ASK_TO_COME"})
            # output_keys = ["out_caller_position"] in /map


        def check_go_back(userdata, max_count):
            """ Check if the robot should go back to party_room """
            self.count += 1
            if self.move_to_caller_aborted is True:
                #The robot is on the same position (party_room), so, don't need move again.
                return aborted
            if self.count < max_count:
                #There is more person to meet, so, move to party room.
                return succeeded
            self.count = 0
            return aborted

        smach.StateMachine.add(
            self.LAST_STATE,
            smach.CBState(check_go_back, outcomes=[succeeded, aborted], cb_kwargs={"max_count": num_persons}),
            transitions={succeeded: "BACK_PARTY_ROOM", aborted: succeeded}
        )

        smach.StateMachine.add(
            "BACK_PARTY_ROOM",
            MoveToRoomStateMachine(announcement="Now I'm backing to a secure position in %s!"),
            transitions={succeeded: succeeded, aborted: succeeded, preempted: succeeded}
            )#input_keys=["room_name"]

    def __init__(self, num_persons, sleep, ask_to_come):
        """Constructor
        :type num_persons: int
        :param num_persons: The number of persons to take drink orders

        :type sleep: int
        :param sleep: The number of seconds that the robot will sleep after ask\
        the person to come if MoveToCaller aborts

        :type ask_to_come: bool
        :param ask_to_come: If true, the robot will ask the person to come and\
        wait $sleep seconds. Otherwise, will move to caller.

        """
        assert type(num_persons) is int and num_persons > 0
        assert type(sleep) is int and sleep > 0
        assert type(ask_to_come) is bool

        smach.StateMachine.__init__(self,
            input_keys=["iterator", "drinks_already_requested"],
            output_keys=["out_person_name", "out_drink_order", "out_caller_position"],
            outcomes=[succeeded, aborted, preempted])

        with self:

            SLEEP_STATE = "SLEEP_" + str(sleep)
            self.count = 0
            self.LAST_STATE = succeeded

            if ask_to_come is not True:
                self.add_move_to_caller(num_persons = num_persons)

            def start_cb(userdata, initial_st_name):
                """Set move_to_caller_aborted to False. This variable is useful if
                the robot should go to the person, but no movements are found."""
                self.move_to_caller_aborted = False

            self.register_start_cb(start_cb);

            def ask_to_come_cb(userdata):
                self.move_to_caller_aborted = True
                if ask_to_come is True:
                    #Calling the first person
                    if userdata.iterator + 1 == num_persons:
                        return "Hi all! Can you that want a drink come here to me learn your face?"
                    #Calling the second/third/... person.
                    return "I'm ready to meet another person!"
                #The MoveToCaller has aborted. If aborts if because no gestures are found.
                return "I'm sorry, I can't see any gesture. Can someone come here in front of me to me learn your face?"

            smach.StateMachine.add(
                "ASK_TO_COME",
                SpeakActionState(text_cb=ask_to_come_cb, input_keys=["iterator"]),
                transitions={succeeded: "SET_CALLER_POSITION_HERE", aborted: "SET_CALLER_POSITION_HERE", preempted: "SET_CALLER_POSITION_HERE"}
            )

            def set_caller_position(userdata):
                out_pose = PoseStamped()
                out_pose.header.frame_id = "/map"
                out_pose.pose = transform_pose(Pose(), "/base_link", "/map")
                userdata.out_caller_position = out_pose
                return succeeded

            smach.StateMachine.add(
                "SET_CALLER_POSITION_HERE",
                smach.CBState(set_caller_position, output_keys=["out_caller_position"], outcomes=[succeeded, aborted]),
                transitions={succeeded: SLEEP_STATE, aborted: SLEEP_STATE}
            )

            smach.StateMachine.add(
                SLEEP_STATE,
                SleepState(duration=sleep),
                transitions={succeeded: "LEARN_FACE", preempted: "LEARN_FACE"}
            )

            smach.StateMachine.add(
                "LEARN_FACE",
                LearnFaceStateMachine(),
                transitions={succeeded: "TAKE_DRINK_ORDER", preempted: "LEARN_FACE", aborted: "LEARN_FACE"})
            # outputs: "out_person_name"

            smach.StateMachine.add(
                "TAKE_DRINK_ORDER",
                TakeDrinkOrderStateMachine(),
                remapping={"in_person_name": "out_person_name"},
                transitions={succeeded: self.LAST_STATE, aborted: "TAKE_DRINK_ORDER", preempted: "TAKE_DRINK_ORDER"}
                )
            #inputs: "in_person_name". outputs:"out_drink_order"


class TakeSeveralDrinkOrdersStateMachine(smach.Iterator):
    """TakeSeveralDrinkOrdersStateMachine

    Requirements:
        Kinect connected on the robot.
        Grammar: robocup/iam and robocup/drinks

    Use this class to take the orders.
    The robot will ask for someone that want a drink and some person should wave the hand. Then the robot will move to the person, learn his
    face and ask for the drink that the person want.

    The orders are returned in a list in `drink_orders' of type DrinkOrder.
    """

    def __init__(self, num_persons, sleep, ask_to_come):
        """Constructor for TakeSeveralDrinkOrdersStateMachine.

        :type num_persons: integer
        :param num_persons: The number of person that the robot should learn and take the drinks orders.

        :type sleep: int
        :param sleep: The number of seconds that the robot will sleep after ask\
        the person to come if MoveToCaller aborts

        :type ask_to_come: bool
        :param ask_to_come: If true, the robot will ask the person to come and\
        wait $sleep seconds. Otherwise, will move to caller.
        """
        smach.Iterator.__init__(
            self,
            outcomes=[succeeded, aborted],
            input_keys=[],
            output_keys=["drink_orders"],
            it=lambda: range(num_persons - 1, -1, -1),
            it_label='iterator',
            exhausted_outcome=succeeded)

        self.userdata.drinks_already_requested = []
        self.userdata.drink_orders = []

        def transition_cb(userdata, active_states):
            """ Append to drinks_already_requested the last drink ordered """
            last_order = userdata.out_drink_order
            last_order.person_pose = userdata.out_caller_position
            self.userdata.drink_orders.append(last_order)
            self.userdata.drinks_already_requested.append(last_order.drink)

        def termination_cb(userdata, terminal_states, outcome):
            """ This function will reset the variables, because if taking one
            order at a time, the second time the drink_orders list still wil
            contain all ordered drinks """
            self.userdata.drinks_already_requested = []
            self.userdata.drink_orders = []

        self.register_transition_cb(transition_cb)
        self.register_termination_cb(termination_cb)

        with self:
            # The input key 'iterator` will evalute to True (and thus
            # result in ConditionalSleepState being executed) for every iteration
            # other than the last one.
            smach.Iterator.set_contained_state(
                'SM_LEARN_FACES',
                MoveToCaller_LearnPerson_TakeDrinkOrder(num_persons=num_persons, sleep=sleep, ask_to_come=ask_to_come),
                loop_outcomes=[succeeded])
