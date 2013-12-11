#! /usr/bin/env python
# -.- coding: utf-8 -.-
'''
STOP TILL PRESS ENTER AND READ KEYBOARD
'''

import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach

from global_common import succeeded, preempted, aborted

VOID_STRING = ''


class StopTillPressEnterAndReadKeyBoard(smach.State):

    """
    Stops untill you press any key.
    Outputs what you typed.
    """

    def __init__(self,
                 intro_text='Press any Key to continue, type EXIT to finish.',
                 abort_string='EXIT',
                 debugging=False):

        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['keyboard_input_out'])

        self._intro_text = intro_text
        self._abort_string = abort_string
        self._debugging = debugging

    def execute(self, userdata):

        #Just for security.
        userdata.keyboard_input_out = VOID_STRING
        if self._debugging:
            string_read = raw_input(self._intro_text)
            userdata.keyboard_input_out = string_read
            rospy.loginfo("String read from Keyboard ==" + string_read)

            if string_read == self._abort_string:
                return aborted

        return succeeded
