#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This module alows us to play and stop any kind of sound in ogg or wav format,
and it also gives as an auxiliary Text to Speach module.

In order to use it you have to:
1)Install the audio-commons of ROS.
http://www.ros.org/wiki/audio_common/Tutorials/

2)Launch soundplay_node.launch, add the following line to your launch.
<include file="$(find sound_play)/soundplay_node.launch" />

"""


import roslib; roslib.load_manifest('pal_smach_utils')
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted


class TakeKeyBoardInputState(smach.State):

    """
    Outputs the string typed with the keyboard.
    Type EXIT to outcome exit the State.
    """

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, 'exit', preempted, aborted], output_keys=['text_introduced_with_keyboard_out'])

    def execute(self, userdata):

        keyboard_text = raw_input('### Write the text you want to input, then press ENTER. If you wanna exit, type EXIT and press ENTER ###')
        userdata.text_introduced_with_keyboard_out = keyboard_text
        if keyboard_text == "EXIT":
            return 'exit'
        return succeeded
