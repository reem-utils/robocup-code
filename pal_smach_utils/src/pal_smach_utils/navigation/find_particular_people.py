import smach

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted

#Import from current directory
from find_and_recognize_person import FindAndRecognizePersonStateMachine

from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.navigation.move_to_caller import MoveToCallerStateMachine
from pal_smach_utils.speech.sound_action import SpeakActionState

rotated_360_degrees = "rotated_360_degrees"
COUNT_NUMBER = 4


class CheckCount(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[aborted, succeeded])
        self.count = 0

    def execute(self, userdata):
        if self.count == COUNT_NUMBER:
            self.count = 0
            return aborted
        self.count += 1
        return succeeded


class FindParticularPeopleStateMachine(smach.StateMachine):

    def __init__(self, name_key=None, name_cb=None, input_keys=[]):

        if name_key and name_cb:
            raise ValueError("You've set more than one of `name_key' and `name_cb'")
        elif not name_key and not name_cb:
            raise ValueError("Neither `name_key' nor `name_cb' were set!")

        if name_key:
            assert input_keys == []
            input_keys = [name_key]

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                input_keys=input_keys, output_keys=['person_pos'])

        class CheckResult(smach.State):

            def __init__(self):
                smach.State.__init__(self, outcomes=[succeeded, aborted],
                    input_keys=input_keys + ['person_name'])

            def execute(self, userdata):
                if name_cb:
                    target_person_name = name_cb(userdata)
                else:
                    target_person_name = getattr(userdata, name_key)
                if userdata.person_name.lower() == target_person_name.lower():
                    return succeeded

                return aborted

        with self:

            def say_person_name_cb(userdata):
                order = userdata.drink_orders[userdata.order_index]
                where_are_you_msg = "I'll look for %s!" % order.person_name
                return where_are_you_msg

            smach.StateMachine.add("SAY_PERSON_NAME",
                SpeakActionState(text_cb=say_person_name_cb, input_keys=["drink_orders", "order_index"]),
                transitions={succeeded: "SM_FRP", aborted: "SM_FRP", preempted: "SM_FRP"}
                )

            smach.StateMachine.add(
                'SM_FRP',
                FindAndRecognizePersonStateMachine(),
                transitions={succeeded: 'CHECK_PERSON'})
            # outputs: 'person_name', 'person_pos'

            smach.StateMachine.add(
                'CHECK_PERSON',
                CheckResult(),
                transitions={succeeded: succeeded, aborted: 'CHECK_COUNT'})

            smach.StateMachine.add(
                "CHECK_COUNT",
                CheckCount(),
                transitions={succeeded: "ROTATE", aborted: "ASK_WHERE_ARE_YOU"}
                )

            def looking_for_person_cb(userdata):
                order = userdata.drink_orders[userdata.order_index]
                self.where_are_you_msg = "I'm looking for you %s. Where are you?" % order.person_name
                return self.where_are_you_msg

            smach.StateMachine.add("ASK_WHERE_ARE_YOU",
                SpeakActionState(text_cb=looking_for_person_cb, input_keys=["drink_orders", "order_index"]),
                transitions={aborted: "ASK_WHERE_ARE_YOU", succeeded: "MOVE_TO_CALLER", preempted: "MOVE_TO_CALLER"}
                )

            smach.StateMachine.add(
                "MOVE_TO_CALLER",
                MoveToCallerStateMachine(ask_for_movement_msg_cb=looking_for_person_cb, input_keys=input_keys),
                transitions={succeeded: succeeded}
                )

            pose = Pose()
            pose.position = Point(0, 0, 0)
            pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 30))

            smach.StateMachine.add(
                'ROTATE',
                MoveActionState("/base_link", pose=pose),
                transitions={succeeded: 'SM_FRP'})
