#! /usr/bin/env python

import roslib
roslib.load_manifest('detect_face_test')
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.stop_till_press_enter_and_read_key_board import StopTillPressEnterAndReadKeyBoard
from pal_smach_utils.utils.detect_face import DetectAFace

DEBUGGING = True
GETURE_RECOG_TXT = "Press enter to start recognizing faces."
HOG_FINN = []
#HOG_FINN = [0.3, 0.4]
PROP_BIG_SMALL = "SMALL"
#PROP_FAR_NEAR = "NEAR"
#PROP_CENTERED_RIGHT_LEFT = "CENTERED"
PROP_FAR_NEAR = ""
PROP_CENTERED_RIGHT_LEFT = ""


def main():
    rospy.init_node('sm_detect_face_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Lets see if I can detect some faces."
        smach.StateMachine.add('TTS_START',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'PAUSE_STATEMACHINE'})

        smach.StateMachine.add('PAUSE_STATEMACHINE',
                               StopTillPressEnterAndReadKeyBoard(intro_text=GETURE_RECOG_TXT, debugging=DEBUGGING),
                               transitions={succeeded: 'DETECT_A_FACE',
                                            preempted: preempted,
                                            aborted: 'TTS_END'},
                               remapping={'keyboard_input_out': 'keyboard_input'})

        smach.StateMachine.add('DETECT_A_FACE',
                               DetectAFace(hog_descriptor=HOG_FINN,
                                           prop_big_small=PROP_BIG_SMALL,
                                           prop_far_near=PROP_FAR_NEAR,
                                           prop_centered_right_left=PROP_CENTERED_RIGHT_LEFT),
                               transitions={succeeded: 'SAY_WHERE_FACE_FOUND',
                                            'no_face_found': 'DIDNT_FIND_ANY_FACE',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'face_data_out': 'face_data_out'})

        def say_face_cb(userdata):
                face_data = userdata.face_data_in
                x_dist = face_data.position3D.x
                y_dist = face_data.position3D.y
                person_hight = face_data.position3D.z

                front_word = "I see a person " + str(x_dist) + " metres infront "

                if y_dist > 0:
                    step_word = "and " + str(y_dist) + " metres to the left"
                elif y_dist < 0:
                    step_word = "and " + str(abs(y_dist)) + " metres to the right"
                else:
                    step_word = ""

                hight_frase = ". This person is around " + str(person_hight) + " metres high."

                a_face_text = front_word + step_word + hight_frase
                return a_face_text

        smach.StateMachine.add('SAY_WHERE_FACE_FOUND',
                               SpeakActionState(text_cb=say_face_cb, input_keys=['face_data_in']),
                               transitions={succeeded: 'PAUSE_STATEMACHINE'},
                               remapping={'face_data_in': 'face_data_out'})

        intro_text = "I didn't find any face."
        smach.StateMachine.add('DIDNT_FIND_ANY_FACE',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'PAUSE_STATEMACHINE'})

        intro_text = "Finished , have a pleasant day."
        smach.StateMachine.add('TTS_END',
                               SpeakActionState(intro_text),
                               transitions={succeeded: succeeded})

    sm.execute()

    rospy.spin()
if __name__ == '__main__':
    main()
