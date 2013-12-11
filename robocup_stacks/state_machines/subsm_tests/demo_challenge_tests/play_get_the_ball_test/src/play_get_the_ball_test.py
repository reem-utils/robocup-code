#! /usr/bin/env python

import roslib
roslib.load_manifest('play_get_the_ball_test')
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.stop_till_press_enter_and_read_key_board import StopTillPressEnterAndReadKeyBoard
from pal_smach_utils.grasping.play_get_the_ball import PlayGetTheBall

DEBUGGING = True
GETURE_RECOG_TXT = "Press enter to start playing."
TIME_PLAYING = 10


def main():
    rospy.init_node('sm_play_get_the_ball_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Lets play."
        smach.StateMachine.add('TTS_START',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'PAUSE_STATEMACHINE'})

        smach.StateMachine.add('PAUSE_STATEMACHINE',
                               StopTillPressEnterAndReadKeyBoard(intro_text=GETURE_RECOG_TXT, debugging=DEBUGGING),
                               transitions={succeeded: 'PLAY_GET_THE_BALL',
                                            preempted: preempted,
                                            aborted: 'TTS_END'},
                               remapping={'keyboard_input_out': 'keyboard_input'})

        smach.StateMachine.add('PLAY_GET_THE_BALL',
                               PlayGetTheBall(TIME_PLAYING),
                               transitions={succeeded: 'TTS_END', preempted: preempted, aborted: aborted})

        intro_text = "Finished playing, have a pleasant day."
        smach.StateMachine.add('TTS_END',
                               SpeakActionState(intro_text),
                               transitions={succeeded: succeeded})

    sm.execute()

    rospy.spin()
if __name__ == '__main__':
    main()
