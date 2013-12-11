#! /usr/bin/env python

import roslib
roslib.load_manifest('follow_any_person_test')
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.navigation.set_distance_new_location import Set_L_New_Location
from pal_smach_utils.utils.stop_till_press_enter_and_read_key_board import StopTillPressEnterAndReadKeyBoard
from pal_smach_utils.navigation.track_operator import GoToLocationL
from person_creator import DummyPersonCreator

DISTANCE_TO_FOLLOW = 0.8
DEBUGGING = True
robot_lost_person = True
OPTIONS = "far_front, far_right, far_left, near_front, near_right, near_left, line_front, line_right, line_left \n"
FOLLOW_ANY_PERSON_TXT = "Write the person to create ==>\n" + OPTIONS + ", press ENTER for random or type EXIT for end\n" + "--> "


def main():
    rospy.init_node('sm_follow_any_person_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Starting Stalker Mode."
        smach.StateMachine.add('TTS_START',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'PAUSE_STATEMACHINE_WRITE_NEXT_PERSON'})

        smach.StateMachine.add('PAUSE_STATEMACHINE_WRITE_NEXT_PERSON',
                               StopTillPressEnterAndReadKeyBoard(intro_text=FOLLOW_ANY_PERSON_TXT, debugging=DEBUGGING),
                               transitions={succeeded: 'DUMMY_PERSON_CREATOR',
                                            preempted: preempted,
                                            aborted: 'TTS_END'},
                               remapping={'keyboard_input_out': 'keyboard_input'})

        smach.StateMachine.add('DUMMY_PERSON_CREATOR',
                               DummyPersonCreator(),
                               transitions={succeeded: 'SET_L_NEW_LOCATION'},
                               remapping={'person_info': 'keyboard_input',
                                          'person_location_out':  'FO_people_location'})

        smach.StateMachine.add('SET_L_NEW_LOCATION',
                               Set_L_New_Location(DISTANCE_TO_FOLLOW, not(robot_lost_person)),
                               transitions={succeeded: 'GO_TO_LOCATION'},
                               remapping={'l_navgoal': 'sm_FO_navgoal',
                                          'l_lost_person': 'sm_FO_Lost_person',
                                          'l_no_people_counter': 'sm_no_people_counter',
                                          'FO_people_location': 'FO_people_location'})

        smach.StateMachine.add('GO_TO_LOCATION',
                               GoToLocationL(),
                               transitions={succeeded: 'PAUSE_STATEMACHINE_WRITE_NEXT_PERSON', preempted: preempted, aborted: aborted},
                               remapping={'sm_FO_navgoal': 'sm_FO_navgoal',
                                          'sm_FO_Lost_person': 'sm_FO_Lost_person',
                                          'old_person_data': 'in_old_person_data'})

        intro_text = "I am tired to follow you, let's go party!"
        smach.StateMachine.add('TTS_END',
                               SpeakActionState(intro_text),
                               transitions={succeeded: succeeded})

    sm.execute()

    rospy.spin()
if __name__ == '__main__':
    main()
