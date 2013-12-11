#! /usr/bin/env python
# -*- encoding: utf-8 -*-


import roslib
roslib.load_manifest('talking_test')
import rospy
import smach
from pal_smach_utils.utils.take_keyboard_input_state import TakeKeyBoardInputState
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.play_sound_sm import SpeakText

"""
Voices available:
el_diphone --> spanish male
suo_fi_lj_diphone --> finish women
 hy_fi_mv_diphone --> finish male
 rab_diphone --> english male
 don_diphone --> english male
 ked_diphone --> english male
 kal_diphone --> english male
 czech_ph -->   Czech
 czech_krb -->  Czech kid
 pc_diphone --> Italian male
 lp_diphone
"""
#VOICE_NAME = 'voice_don_diphone'
VOICE_NAME = 'voice_ked_diphone'


def main():
    rospy.init_node('talking_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add('READ_INPUT_KEYBOARD',
                               TakeKeyBoardInputState(),
                               transitions={succeeded: 'SAY_START',
                                            'exit': succeeded,
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'text_introduced_with_keyboard_out': 'text_to_say'})

        smach.StateMachine.add('SAY_START',
                               SpeakText(VOICE_NAME),
                               transitions={succeeded: 'READ_INPUT_KEYBOARD',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'text_to_say': 'text_to_say'})

    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
