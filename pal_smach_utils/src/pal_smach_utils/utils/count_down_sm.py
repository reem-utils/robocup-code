#! /usr/bin/env python
# -.- coding: utf-8 -.-
# vim: expandtab ts=4 sw=4

import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.time_out import TimeOut


class InitCounter(smach.State):
    def __init__(self, number=0):
        smach.State.__init__(self,
                             outcomes=[succeeded,
                                       preempted,
                                       aborted],
                             output_keys=['init_counter_out'])
        self._number = number

    def execute(self, userdata):

        userdata.init_counter_out = self._number

        return succeeded


class DecideIfContinueCounting(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['continue',
                                       'dont_continue',
                                       preempted,
                                       aborted],
                             input_keys=['in_counter'],
                             output_keys=['counter_out'])

    def execute(self, userdata):

        if userdata.in_counter == 1:
            return 'dont_continue'

        #JUST for safety
        if userdata.in_counter < 0:
            rospy.loginfo("########### CAREFULL; Variable negative when it shouldnt.")
            return 'dont_continue'

        userdata.counter_out = userdata.in_counter - 1
        return 'continue'


class CountDownSM(smach.StateMachine):

    def __init__(self, time_lapse=1.0, counting_number=0):
        smach.StateMachine.__init__(self,
                                    [succeeded,
                                     preempted,
                                     aborted])

        with self:

            def say_text_cb1(userdata):
                text_say = "Starting countdown."
                return text_say
            smach.StateMachine.add('STARING_COUNTDOWN',
                                   SpeakActionState(text_cb=say_text_cb1),
                                   transitions={succeeded: 'INIT_COUNTER'})

            smach.StateMachine.add('INIT_COUNTER',
                                   InitCounter(counting_number),
                                   transitions={succeeded: 'COUNT_OUTLOUD',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'init_counter_out': 'counter'})

            def say_text_cb2(userdata):
                text_say = str(userdata.counter) + "..."
                return text_say
            smach.StateMachine.add('COUNT_OUTLOUD',
                                   SpeakActionState(text_cb=say_text_cb2, input_keys=['counter']),
                                   transitions={succeeded: 'COUNTING_TIME_STATE'})

            smach.StateMachine.add('COUNTING_TIME_STATE',
                                   TimeOut(time_lapse),
                                   transitions={succeeded: 'DECIDE_IF_CONTINUE_COUNTING',
                                                preempted: preempted,
                                                aborted: aborted})

            smach.StateMachine.add('DECIDE_IF_CONTINUE_COUNTING',
                                   DecideIfContinueCounting(),
                                   transitions={'continue': 'COUNT_OUTLOUD',
                                                'dont_continue': 'STARING_GO_COUNT',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_counter': 'counter',
                                              'counter_out': 'counter'})

            def say_text_cb3(userdata):
                text_say = "There you go!"
                return text_say
            smach.StateMachine.add('STARING_GO_COUNT',
                                   SpeakActionState(text_cb=say_text_cb3),
                                   transitions={succeeded: succeeded})
