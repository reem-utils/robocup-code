#! /usr/bin/env python

import roslib
roslib.load_manifest('learn_and_follow_operator_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from pal_smach_utils.speech.sound_action import SpeakActionState

from pal_smach_utils.navigation.move_to_caller import MoveToCallerStateMachine
from pal_smach_utils.utils.check_dependences import CheckDependencesState
from pal_smach_utils.utils.cocktail_party_variables import CocktailPartyVariables

def main():
    rospy.init_node('faces_and_waving_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        variables = CocktailPartyVariables()

        smach.StateMachine.add(
                "CHECK_DEPENDENCES",
                CheckDependencesState(
                    topic_names=variables.TOPICS,
                    service_names=variables.SERVICES,
                    action_names=variables.ACTIONS,
                    map_locations=variables.MAP_LOCATIONS),
                transitions={succeeded: "TTS_SAY_INTRO", aborted: aborted}
                )

        intro_text = "Please, wave your hand"
        smach.StateMachine.add('TTS_SAY_INTRO',
                               SpeakActionState(intro_text),
                               transitions={succeeded: succeeded})

        smach.StateMachine.add('MOVE_TO_CALLER',
                               MoveToCallerStateMachine(),
                               transitions={succeeded: succeeded})

    sis = smach_ros.IntrospectionServer('faces_and_waving_test_sm', sm, '/FACES_AND_WAVING_TEST')   
    sis.start()
    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
