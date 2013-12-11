#! /usr/bin/env python
# -*- encoding: utf-8 -*-


import roslib
roslib.load_manifest('play_sound_test')
import rospy
import smach
from roslib import packages
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.play_sound_sm import SpeakText, PlaySoundOnceState, StopSoundState
from pal_smach_utils.utils.timeout_container import SleepState
import os


TIMEOUT = 10.0
PATH_TO_SEND = os.path.join(packages.get_pkg_dir('dancing_reem'), 'mp3_lib/Daft_Punk_ft_Pharrell_Get_Lucky.wav')
PATH_TO_SEND_WAV = os.path.join(packages.get_pkg_dir('dancing_reem'), 'mp3_lib/Daft_Punk_ft_Pharrell_Get_Lucky.wav')
TEXT_TO_SAY1 = "We are starting the Playing songs test. Let's go!"
TEXT_TO_SAY2 = "We have finished the test. Let's go and bake a pie"


class SoundDummyState(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['path', 'text1', 'text2'])

    def execute(self, userdata):

        userdata.path = PATH_TO_SEND
        userdata.text1 = TEXT_TO_SAY1
        userdata.text2 = TEXT_TO_SAY2
        print "DUMMY SATE ENDED"
        return succeeded


def main():
    rospy.init_node('play_sound_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add('DUMMY_STATE_GENERATE_SOUND_PATH',
                               SoundDummyState(),
                               transitions={succeeded: 'SAY_START',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'path': 'sound_file_path',
                                          'text1': 'text_to_say1',
                                          'text2': 'text_to_say2'})

        smach.StateMachine.add('SAY_START',
                               SpeakText(),
                               transitions={succeeded: 'PLAY_SOUND',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'text_to_say': 'text_to_say1'})

        smach.StateMachine.add('PLAY_SOUND',
                               PlaySoundOnceState(to_execute_sound_file_path=PATH_TO_SEND_WAV),
                               transitions={succeeded: 'WAIT1',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'sound_file_path': 'sound_file_path'})

        smach.StateMachine.add('WAIT1',
                               SleepState(TIMEOUT),
                               transitions={succeeded: 'STOP_SOUND',
                                            preempted: preempted})

        smach.StateMachine.add('STOP_SOUND',
                               StopSoundState(),
                               transitions={succeeded: 'WAIT2',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'sound_file_path': 'sound_file_path'})

        smach.StateMachine.add('WAIT2',
                               SleepState(TIMEOUT),
                               transitions={succeeded: 'SAY_FINISHED',
                                            preempted: preempted})

        smach.StateMachine.add('SAY_FINISHED',
                               SpeakText(),
                               transitions={succeeded: succeeded,
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'text_to_say': 'text_to_say2'})


    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
