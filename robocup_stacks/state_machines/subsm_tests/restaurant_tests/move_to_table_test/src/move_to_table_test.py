#! /usr/bin/env python


import roslib
roslib.load_manifest('move_to_table_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.navigation.move_to_table import MoveToTable


def main():
    rospy.init_node('sm_move_to_table_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        intro_text = "I am ready to move to a table"
        smach.StateMachine.add('START',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'FOLLOW_ME_COMMAND'})

        smach.StateMachine.add('FOLLOW_ME_COMMAND',
                               MoveToTable(),
                               transitions={'got_to_table': 'END',
                                            'didnt_get_to_table': 'END'})

        intro_text = "Finished Move to a table test, have a nice day."
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
