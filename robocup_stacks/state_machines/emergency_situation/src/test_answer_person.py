#! /usr/bin/env python
# -.- coding: utf-8 -.-
import roslib
roslib.load_manifest("emergency_situation")
import smach
import rospy
import smach_ros

from save_people import DummyIHeard, YES_NO_GRAMMAR
from pal_smach_utils.speech.sm_listen_orders import ListenOrders
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted


def main():
    rospy.init_node('test_listen_yes_no')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:

        smach.StateMachine.add(
            "ASK_SPEAK_YES_OR_NO",
            SpeakActionState("Hi! Lets test what i can understand. Say only yes or no please."),
            transitions={succeeded: "LISTEN", aborted: "LISTEN"}
            )

        smach.StateMachine.add(
            'LISTEN',
            ListenOrders(YES_NO_GRAMMAR),
            transitions={succeeded: 'WHAT_I_HEARD2', aborted: 'ASK_SPEAK_YES_OR_NO'},
            remapping={'o_userSaidData': 'i_heard'})

        smach.StateMachine.add(
            'WHAT_I_HEARD2',
            DummyIHeard(),
            transitions={'i_heard_yes': 'I_HEARD_YES', 'i_heard_no': 'I_HEARD_NO', 'i_heard_nothing': 'I_HEARD_NOTHING'})

        smach.StateMachine.add(
            "I_HEARD_YES",
            SpeakActionState("I heard yes!"),
            transitions={succeeded: "LETS_TEST_AGAIN", aborted: "LETS_TEST_AGAIN"}
            )

        smach.StateMachine.add(
            "I_HEARD_NO",
            SpeakActionState("I heard no!"),
            transitions={succeeded: "LETS_TEST_AGAIN", aborted: "LETS_TEST_AGAIN"}
            )

        smach.StateMachine.add(
            "I_HEARD_NOTHING",
            SpeakActionState("I heard nothing!"),
            transitions={succeeded: "LETS_TEST_AGAIN", aborted: "LETS_TEST_AGAIN"}
            )

        smach.StateMachine.add(
            "LETS_TEST_AGAIN",
            SpeakActionState("Lets test again forever. Speak yes or no please."),
            transitions={succeeded: "LISTEN", aborted: "LISTEN"}
            )

    sis = smach_ros.IntrospectionServer(
        'test_listen_yes_no_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
