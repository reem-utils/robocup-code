#! /usr/bin/env python
# -*- encoding: utf-8 -*-


import roslib
roslib.load_manifest('talking_test')
import rospy
import smach
from pal_smach_utils.utils.take_keyboard_input_state import TakeKeyBoardInputState
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState


def main():
    rospy.init_node('talking_tts_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add('READ_INPUT_KEYBOARD',
                               TakeKeyBoardInputState(),
                               transitions={succeeded: 'SAY_START',
                                            'exit': succeeded,
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'text_introduced_with_keyboard_out': 'text_to_say'})

        def say_text_cb(userdata):
            text_say = userdata.text
            return text_say
        smach.StateMachine.add('SAY_START',
                               SpeakActionState(text_cb=say_text_cb,
                                                input_keys=['text']),
                               transitions={succeeded: 'READ_INPUT_KEYBOARD'},
                               remapping={'text': 'text_to_say'})

    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
