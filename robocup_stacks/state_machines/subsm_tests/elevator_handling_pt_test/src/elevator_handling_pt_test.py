#! /usr/bin/env python

import roslib
roslib.load_manifest('learn_and_follow_operator_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.learn_person import LearnPerson
from pal_smach_utils.navigation.follow_and_stop import FollowAndStop

from pal_smach_utils.speech.sound_action import SpeakActionState


DISTANCE_TO_FOLLOW = 1.0


def main():
    rospy.init_node('sm_learn_and_follow_operator_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Please stay still while I learn how you are."
        smach.StateMachine.add('TTS_SAY_CALIB',
                               SpeakActionState(intro_text),
                               #transitions={succeeded: 'TTS_SAY_READY_TO_FOLLOW'})
                               transitions={succeeded: 'SM_LEARN_PERSON'})

        smach.StateMachine.add('SM_LEARN_PERSON',
                               LearnPerson(),
                               transitions={succeeded: 'TTS_SAY_READY_TO_FOLLOW',
                                            aborted: aborted},
                               remapping={'PT_Id_of_person': 'out_targetId',
                                          'LP_all_person_data': 'out_personTrackingData'})

        #sm.userdata.out_targetId = 1
        #sm.userdata.out_personTrackingData = peopleTracking()
        ready_text = "I'm ready to follow you my sweety."
        smach.StateMachine.add('TTS_SAY_READY_TO_FOLLOW',
                               SpeakActionState(ready_text),
                               transitions={succeeded: 'FOLLOW_ME'})

        smach.StateMachine.add('FOLLOW_ME',
                               FollowAndStop(DISTANCE_TO_FOLLOW, "follow_me"),
                               remapping={'in_targetId': 'out_targetId',
                                          'in_personTrackingData': 'out_personTrackingData'},
                               transitions={succeeded: succeeded})

    sis = smach_ros.IntrospectionServer('elevator_handling_test_sm', sm, '/ELEVATOR_HANDLING_TEST')
    sis.start()
    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
