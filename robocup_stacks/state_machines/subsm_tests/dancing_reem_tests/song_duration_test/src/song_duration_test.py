#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import roslib;roslib.load_manifest('song_duration_test')
import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.play_sound_sm import PlaySoundOnceState, StopSoundState
from bpm_analysis import BpmAnalysisSM
from pal_smach_utils.utils.song_duration_sm import SongDurationState
from pal_smach_utils.utils.time_controlling_states import TellIfSongHasFinished, GetCurrentROSTimeState


def main():

    rospy.init_node('song_duration_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add('BPM_ANALYSIS',
                                BpmAnalysisSM(),
                                transitions={succeeded: 'GET_SONG_DURATION',
                                            preempted: preempted,
                                            aborted: aborted},
                                remapping={'bpm_out': 'song_bpm',
                                            'song_path_out': 'song_path'})

        smach.StateMachine.add('GET_SONG_DURATION',
                                SongDurationState(),
                                transitions={succeeded: 'PLAY_SONG',
                                            preempted: preempted,
                                            aborted: aborted},
                                remapping={'in_song_path': 'song_path',
                                            'song_duration_out': 'song_duration'})


        smach.StateMachine.add('PLAY_SONG',
                                PlaySoundOnceState(),
                                transitions={succeeded: 'SET_TIME',
                                            preempted: preempted,
                                            aborted: aborted},
                                remapping={'sound_file_path': 'song_path'})

        smach.StateMachine.add('SET_TIME',
                                GetCurrentROSTimeState(),
                                transitions={succeeded: 'TELL_IF_SONG_HAS_FINISHED',
                                            preempted: preempted,
                                            aborted: aborted},
                                remapping={'starting_ros_time_out': 'time_song_started_playing'})

        smach.StateMachine.add('TELL_IF_SONG_HAS_FINISHED',
                                        TellIfSongHasFinished(),
                                        transitions={'song_not_finished': 'TELL_IF_SONG_HAS_FINISHED',
                                                        'song_finished': 'STOP_SOUND',
                                                    preempted: preempted,
                                                    aborted: aborted},
                                        remapping={'in_starting_ros_time': 'time_song_started_playing',
                                                    'song_duration': 'song_duration' })

        smach.StateMachine.add('STOP_SOUND',
                                StopSoundState(),
                                transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                remapping={'sound_file_path': 'sound_file_path'})


    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
