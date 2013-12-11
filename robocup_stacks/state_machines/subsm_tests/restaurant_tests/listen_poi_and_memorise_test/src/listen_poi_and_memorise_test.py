#! /usr/bin/env python


import roslib
roslib.load_manifest('listen_poi_and_memorise_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.listen_command_for_restaurant import ListenCommandForRestaurant
from pal_smach_utils.speech.sound_action import SpeakActionState
from smach import CBState


def main():
    rospy.init_node('sm_listen_poi_and_memorise_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        intro_text = "I am ready to hear you and memorise a point of interest."
        smach.StateMachine.add('START',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'DECIDE_IF_STOP_TEST'})

        @smach.cb_interface(outcomes=['continue_testing', 'stop_testing'])
        def decide_if_stop(userdata):
            decision = raw_input("YOU WANT TO CONTINUE MEMORISING POIS? ==>  ")
            if decision == "yes" or not decision:
                return 'continue_testing'
            else:
                return 'stop_testing'

        smach.StateMachine.add('DECIDE_IF_STOP_TEST',
                               CBState(decide_if_stop),
                               remapping={'in_learn_person': "in_learn_person"},
                               transitions={'continue_testing': 'LISTEN_COMMANDS_FOR_RESTAURANT',
                                            'stop_testing': 'END'})

        smach.StateMachine.add('LISTEN_COMMANDS_FOR_RESTAURANT',
                               ListenCommandForRestaurant(),
                               transitions={succeeded: 'DECIDE_IF_STOP_TEST'})

        intro_text = "Poi memorised, have a nice day."
        smach.StateMachine.add('END',
                               SpeakActionState(intro_text),
                               transitions={succeeded: succeeded})


    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
