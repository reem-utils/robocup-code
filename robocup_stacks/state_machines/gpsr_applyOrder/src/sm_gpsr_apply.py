import roslib
roslib.load_manifest('gpsr_applyOrder')

import smach

from generate_goal import printNewGoal

from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from gpsr.msg import order, order_list


class writeOrders(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted, preempted],
            input_keys=['i_orderList'])

    def execute(self, userdata):
        i = 1
        for o in userdata.i_orderList:
            printNewGoal(o.action, o.item, o.person, o.location, i)
            i += 1
        return succeeded


class applyOrders(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:
            smach.StateMachine.add(
                'READ_ORDERS',
                TopicReaderState(topic_name='nlp',msg_type=order_list,timeout=None),
                transitions={aborted: aborted, succeeded: 'DEFINE_GOAL_FILE'},
                remapping={'message': 'o_orderList'}
                )

            smach.StateMachine.add(
                'GENERATE_FILES',
                wirteOrders(),
                tranisitions = {aborted: aborted, succeeded: 'SOLVE_WITH_SOAR'}
                )

            smach.StateMachine.add(
                'SOLVE_WITH_SOAR',
                ,
                transitions = {aborted: aborted, suceeded: 'PRINT_ACTION_COMPLETE'}
                )

            smach.StateMachine.add(
                'PRINT_ACTION_COMPLETE',
                SpeakActionState(text="whooaaaa!"),
                transitions = {succeeded: 'RETURN_TO_REFEREE'}
                )

            smach.StateMachine.add(
                'RETURN_TO_REFEREE',
                #navigate)
                transitions = {succeeded: 'ORDER_FINISHED'}
                )

            smach.StateMachine.add(
                'ORDER_FINISHED',
                SpeakActionState(text="I wonder if it's time for a quick nap. Anythin more to do?"),
                transitions = {aborted: aborted, suceeded: succeeded}
                )
