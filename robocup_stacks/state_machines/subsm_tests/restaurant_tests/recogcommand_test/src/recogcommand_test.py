#! /usr/bin/env python


import roslib
roslib.load_manifest('recogcommand_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.listen_general_command import RecogCommand
from pal_smach_utils.speech.sound_action import SpeakActionState

GRAMMAR_NAME = rospy.get_param('/restaurant/follow_grammar_name')


def main():
    rospy.init_node('sm_recogcommand_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        intro_text = "I am ready to hear you."
        smach.StateMachine.add('START',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'FOLLOW_ME_COMMAND'})

        smach.StateMachine.add('FOLLOW_ME_COMMAND',
                               RecogCommand(GRAMMAR_NAME, 'action', 'follow', True),
                               transitions={succeeded: 'END',
                                            aborted: 'FOLLOW_ME_COMMAND'})

        intro_text = "Recognise Command finished, have a nice day."
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
