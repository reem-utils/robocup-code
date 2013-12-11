#! /usr/bin/env python

import roslib; roslib.load_manifest('learn_poi_test')
import rospy
import smach
import actionlib

#from smach_ros import SimpleActionState, ServiceState
import smach_ros
from std_msgs import *


from pal_smach_utils.utils.global_common import *
from pal_smach_utils.speech.listen_poi_name import ListenPoiName
from pal_smach_utils.speech.sm_hear_voice_commands_and_pois import SM_MemorisePois
from pal_smach_utils.speech.grammar_state import GrammarState

POI_GRAMMAR_NAME = 'robocup12/poi_grammar'

def main():
    rospy.init_node('sm_learn_poi_test_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add('START_SPEECHRECOG_POI_GRAMMAR',
                                    GrammarState(POI_GRAMMAR_NAME, enabled=True),
                                    transitions = {succeeded: 'LISTEN_POI'})


        smach.StateMachine.add( 'LISTEN_POI',
                            ListenPoiName(),
                            transitions = { succeeded:'SM_FO_MEMORISE_POI',
                                            aborted: 'LISTEN_POI',
                                            preempted: 'DISABLE_GRAMMAR_WITH_POI'},
                            remapping = {'poi_name':'poi_name'})

        smach.StateMachine.add( 'SM_FO_MEMORISE_POI',
                            SM_MemorisePois(),
                            transitions = {succeeded: 'DISABLE_GRAMMAR_WITH_POI'},
                            remapping = {'FO_POI_name':'poi_name'})

        smach.StateMachine.add( 'DISABLE_GRAMMAR_WITH_POI',
                                GrammarState(POI_GRAMMAR_NAME, enabled=False),
                                transitions = {succeeded: succeeded})


    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()

