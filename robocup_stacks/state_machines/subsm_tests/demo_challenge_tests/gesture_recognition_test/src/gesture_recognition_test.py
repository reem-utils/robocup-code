#! /usr/bin/env python

import roslib
roslib.load_manifest('gesture_recognition_test')
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.stop_till_press_enter_and_read_key_board import StopTillPressEnterAndReadKeyBoard
from pal_smach_utils.utils.gesture_recognition import GestureRecognition

DEBUGGING = True
GETURE_RECOG_TXT = "Press enter to start recognizing gestures."
GESTURE_LOOKING_FOR = "Wave"


def main():
    rospy.init_node('sm_gesture_recognition_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Lets see if I can detects some gestures."
        smach.StateMachine.add('TTS_START',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'PAUSE_STATEMACHINE'})

        smach.StateMachine.add('PAUSE_STATEMACHINE',
                               StopTillPressEnterAndReadKeyBoard(intro_text=GETURE_RECOG_TXT, debugging=DEBUGGING),
                               transitions={succeeded: 'GESTURE_RECOGNITION',
                                            preempted: preempted,
                                            aborted: 'TTS_END'},
                               remapping={'keyboard_input_out': 'keyboard_input'})

        smach.StateMachine.add('GESTURE_RECOGNITION',
                               GestureRecognition(GESTURE_LOOKING_FOR),
                               transitions={succeeded: 'PAUSE_STATEMACHINE', preempted: preempted, aborted: aborted},
                               remapping={'gesture_id_out': 'geture_detected'})

        intro_text = "Finished recognizing, have a pleasant day."
        smach.StateMachine.add('TTS_END',
                               SpeakActionState(intro_text),
                               transitions={succeeded: succeeded})

    sm.execute()

    rospy.spin()
if __name__ == '__main__':
    main()
