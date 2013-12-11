#! /usr/bin/env python
# -*- encoding: utf-8 -*-


import roslib
roslib.load_manifest('metronome_test')
import rospy
import smach
import os
from roslib import packages
from bpm_analysis import BpmAnalysisSM
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.play_sound_sm import PlaySoundAtRateGiven


SOUND_TO_REPEAT_PATH = os.path.join(packages.get_pkg_dir('metronome_test'), 'sounds_lib/146718__fins__button.wav')


class MetronomeDummyState(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                            outcomes=[succeeded, preempted, aborted],
                            output_keys=['sound_to_repeat_path'])

    def execute(self, userdata):

        userdata.sound_to_repeat_path = SOUND_TO_REPEAT_PATH
        print "SOUND TO BE REPEATED = " + str(SOUND_TO_REPEAT_PATH)

        return succeeded


class PrintUserData2(smach.State):

    def __init__(self,
                message_name1='Message1',
                message_name2='Message2'):
            smach.State.__init__(self,
                    outcomes=[succeeded, preempted, aborted],
                    input_keys=['message1', 'message2'])

            self._message_name1 = message_name1
            self._message_name2 = message_name2

    def execute(self, userdata):
            rospy.loginfo('This is the %s: %s' % (self._message_name1, str(userdata.message1)))
            rospy.loginfo('This is the %s: %s' % (self._message_name2, str(userdata.message2)))
            return succeeded


def main():
    rospy.init_node('play_sound_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:


        smach.StateMachine.add('BPM_ANALYSIS',
                                    BpmAnalysisSM(),
                                    transitions={succeeded: 'PRINT_DATA',
                                                preempted: preempted,
                                                aborted: aborted},
                                    remapping={'bpm_out': 'song_bpm',
                                                'song_path_out': 'song_path'})

        smach.StateMachine.add('PRINT_DATA',
                                PrintUserData2('song_bpm', 'song_path'),
                                transitions={
                                    succeeded: 'METRONOME_DUMMY_STATE',
                                    preempted: preempted,
                                    aborted: aborted},
                                remapping={'message1': 'song_bpm',
                                            'message2': 'song_path'})

        smach.StateMachine.add('METRONOME_DUMMY_STATE',
                                    MetronomeDummyState(),
                                    transitions={succeeded: 'PLAY_SOUND',
                                                preempted: preempted,
                                                aborted: aborted},
                                    remapping={'sound_to_repeat_path': 'sound_file_path'})

        smach.StateMachine.add('PLAY_SOUND',
                                PlaySoundAtRateGiven(),
                                transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                remapping={'sound_file_path': 'sound_file_path',
                                            'bpm': 'song_bpm'})


    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
