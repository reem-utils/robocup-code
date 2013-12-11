import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
import random

from pal_interaction_msgs.msg import asrresult  # , actiontag

from pal_smach_utils.speech.grammar_state import GrammarState
from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.drink_order import DrinkOrder
from pal_smach_utils.utils.colors import Colors
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables as variables

colors = Colors()

warning = "warning"
drink_changed = "repeated_drink_changed"
# The size of list ALLOWD_DRINKS need be at least 3, because are 3 drink orders in robocup, otherwise AnalizeRepeatedDrink will raiseValueError

COUNT_NUMBER = 2
COUNT_WARNING = 1
LEN_DRINKS = len(variables.ALLOWED_DRINKS)


class CountCheck(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, warning, aborted])
        self.count = 0

    def execute(self, userdata):
        self.count += 1
        rospy.loginfo("Checking count %d/%d" % (self.count, COUNT_NUMBER))
        if self.count == COUNT_WARNING:
            return warning

        if self.count == COUNT_NUMBER:
            self.count = 0
            return aborted

        return succeeded


class DebugDrinkOrder(smach.State):
    def __init__(self):
        smach.State.__init__(self, input_keys=["out_drink_order"], outcomes=[succeeded])

    def execute(self, userdata):
        rospy.loginfo("=========>>>> [DEBUG] New Drink %s to %s <<<========================================",
            userdata.out_drink_order.drink, userdata.out_drink_order.person_name)
        return succeeded


class AnalizeRepeatedDrink(smach.State):
    def __init__(self):
        smach.State.__init__(self,
            input_keys=["in_order", "drinks_already_requested"],
            output_keys=["out_drink_order"],
            outcomes=[succeeded, drink_changed])

    def execute(self, userdata):
        rospy.loginfo("=============>>> Try identify %s in list %s" % (userdata.in_order.drink, userdata.drinks_already_requested))
        if userdata.in_order.drink in userdata.drinks_already_requested:
            while True:
                drink = variables.ALLOWED_DRINKS[random.randint(0, LEN_DRINKS - 1)]
                rospy.loginfo(colors.BACKGROUND_GREEN + "Trying identify '%s' in %s %s" % (drink, userdata.drinks_already_requested, colors.NATIVE_COLOR))
                if drink not in userdata.drinks_already_requested:
                    userdata.out_drink_order = DrinkOrder(userdata.in_order.person_name, drink)
                    return drink_changed
        return succeeded


class TakeDrinkOrderStateMachine(smach.StateMachine):
    """TakeDrinkOrderStateMachine.

    Use this StateMachine to take drink orders.
    Steps of this State Machine:
        Enable the grammar defined on cocktail_party.yaml file as drinks_grammar_name; ask what the person want to drink; get the drink name;
        If the drink was already requested or the robot can't understand what the person is saying, then a new drink will be asigned to the
        person. The asigned drink is a random drink of 'allowed_drinks' variable defined on cocktail_party.yaml file.

    Important:
        The same drink names should be on 'allowed_drinks' variable and in the grammar defined on 'drinks_grammar_name' variable.
        Both variables 'allowed_drinks and drinks_grammar_name' are defined on cocktail_party.yaml file.

    """

    def __init__(self):
        """Constructor for TakeDrinkOrderStateMachine

        Input keys:
            @type in_person_name: string
            @param in_person_name: The person name that want a drink.

            @type drinks_already_requested: list of string
            @param drinks_already_requested: The drink names already requested.

        Output keys:
            @type out_drink_order: pal_smach_utils/src/pal_smach_utils/utils/DrinkOrder
            @return out_drink_order: A DrinkOrder object with the fields person_name and drink.

        """
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
            input_keys=['in_person_name', "drinks_already_requested"], output_keys=['out_drink_order'])

        with self:
            self.last_drink_name = None
            self.count_check = CountCheck()

            smach.StateMachine.add(
                'ENABLE_GRAMMAR',
                GrammarState(variables.DRINKS_GRAMMAR_NAME, enabled=True),
                transitions={succeeded: 'TAKE_ORDERS_TTS', aborted: "TAKE_ORDERS_TTS", preempted: "TAKE_ORDERS_TTS"})

            def orders_welcome_text_cb(userdata):
                tts = "What do you want to drink %s?" % userdata.in_person_name
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            smach.StateMachine.add(
                'TAKE_ORDERS_TTS',
                SpeakActionState(text_cb=orders_welcome_text_cb, input_keys=["in_person_name"]),
                transitions={succeeded: 'TAKE_ORDER', aborted: "TTS_FAILED", preempted: "TTS_FAILED"})

            smach.StateMachine.add(
                "TTS_FAILED",
                SpeakActionState(text="What do you want to drink?"),
                transitions={succeeded: "TAKE_ORDER", aborted: "TAKE_ORDER", preempted: "TAKE_ORDER"}
            )

            def take_order_cb(userdata, message):
                self.last_drink_name = None
                print colors.BACKGROUND_GREEN, "MESSAGE: ", str(message), colors.NATIVE_COLOR

                actiontag = [tag for tag in message.tags if tag.key == 'action']
                drinktag = [tag for tag in message.tags if tag.key == 'object']  # drink
                if actiontag and actiontag[0].value == 'bring':
                    print "\n\nDRINK TAG: ", drinktag
                    userdata.out_drink_order = DrinkOrder(userdata.in_person_name, drinktag[0].value)
                    self.last_drink_name = drinktag[0].value
                    rospy.loginfo("==========>>> New drink: (%s, %s)" % (userdata.in_person_name, drinktag[0].value))
                    return succeeded
                return aborted

            smach.StateMachine.add(
                'TAKE_ORDER',
                TopicReaderState(
                    topic_name=variables.T_USERSAID,
                    msg_type=asrresult,
                    timeout=variables.TAKE_SINGLE_ORDER_TIMEOUT,
                    callback=take_order_cb,
                    input_keys=['in_person_name'],
                    output_keys=['out_drink_order']),
                #remapping={'order': 'order1'},
                transitions={succeeded: "ANALIZE_REPEATED_DRINK", aborted: 'COUNT_CHECK', preempted: "COUNT_CHECK"})

            smach.StateMachine.add(
                "COUNT_CHECK",
                self.count_check,
                transitions={succeeded: "TAKE_ORDER", warning: "SPEAK_HIGHER_PLEASE", aborted: "ASSIGN_A_DRINK"}
                )

            def speak_higher_please_cb(userdata):
                tts = "I'm sorry %s! Can you speak the drink name higher please?" % userdata.in_person_name
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            smach.StateMachine.add(
                "SPEAK_HIGHER_PLEASE",
                SpeakActionState(text_cb=speak_higher_please_cb, input_keys=["in_person_name"]),
                transitions={succeeded: "TAKE_ORDER", aborted: "TAKE_ORDER", preempted: "TAKE_ORDER"}
                )

            def assign_a_drink_cb(userdata):
                userdata.out_drink_order = DrinkOrder(userdata.in_person_name, variables.ALLOWED_DRINKS[0])
                while True:
                    drink = variables.ALLOWED_DRINKS[random.randint(0, LEN_DRINKS - 1)]
                    rospy.loginfo(colors.BACKGROUND_GREEN + "Trying identify '%s' in %s %s" % (drink, userdata.drinks_already_requested, colors.NATIVE_COLOR))
                    if drink not in userdata.drinks_already_requested:
                        userdata.out_drink_order = DrinkOrder(userdata.in_person_name, drink)
                        tts = "I'm sorry %s. I can't understand what you are requesting. I'll bring %s for you!" % (userdata.in_person_name, drink)
                        rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                        return tts

            smach.StateMachine.add(
                "ASSIGN_A_DRINK",
                SpeakActionState(text_cb=assign_a_drink_cb, input_keys=["in_person_name", "drinks_already_requested"], output_keys=["out_drink_order"]),
                transitions={succeeded: "DISABLE_GRAMMAR", aborted: "DISABLE_GRAMMAR_AND_ABORT", preempted: "DISABLE_GRAMMAR"}
                )

            smach.StateMachine.add(
                "ANALIZE_REPEATED_DRINK",
                AnalizeRepeatedDrink(),
                remapping={"in_order": "out_drink_order"},
                transitions={succeeded: "DEBUG_DRINK", drink_changed: "REPEATED_DRINK_WARNING"}
                )

            def repeated_drink_warning(userdata):
                self.count_check.count = 0
                tts = "I'm sorry! I understood %s and this drink has already been requested. I will get %s for you!" % (self.last_drink_name, userdata.in_order.drink)
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            smach.StateMachine.add(
                "REPEATED_DRINK_WARNING",
                SpeakActionState(text_cb=repeated_drink_warning, input_keys=["in_order"]),
                    # output_keys=["out_drink_order"]),
                remapping={'in_order': 'out_drink_order'},
                transitions={succeeded: "DISABLE_GRAMMAR", aborted: "DISABLE_GRAMMAR", preempted: "DISABLE_GRAMMAR"}
                )

            smach.StateMachine.add(
                "DEBUG_DRINK",
                DebugDrinkOrder(),
                remapping={"drink_order": "out_order"},
                transitions={succeeded: "CONFIRM_ORDER"}
                )

            def confirm_order_cb(userdata):
                self.count_check.count = 0
                tts = "Okay %s! I'll get %s for you." % (userdata.in_order.person_name, userdata.in_order.drink)
                rospy.loginfo(colors.BACKGROUND_GREEN + tts + colors.NATIVE_COLOR)
                return tts

            smach.StateMachine.add(
                "CONFIRM_ORDER",
                SpeakActionState(text_cb=confirm_order_cb, input_keys=["in_order"]),
                remapping={"in_order": "out_drink_order"},
                transitions={succeeded: "DISABLE_GRAMMAR", aborted: "DISABLE_GRAMMAR", preempted: "DISABLE_GRAMMAR"})

            smach.StateMachine.add(
                'DISABLE_GRAMMAR',
                GrammarState(variables.DRINKS_GRAMMAR_NAME, enabled=False),
                transitions={succeeded: succeeded})

            smach.StateMachine.add(
                'DISABLE_GRAMMAR_AND_ABORT',
                GrammarState(variables.DRINKS_GRAMMAR_NAME, enabled=False),
                transitions={succeeded: aborted})


