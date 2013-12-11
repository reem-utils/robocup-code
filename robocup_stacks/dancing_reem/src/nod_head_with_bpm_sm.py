#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import roslib
roslib.load_manifest('dancing_reem')
import smach
from bpm_analysis import BpmAnalysisSM
from pal_smach_utils.utils.song_duration_sm import SongDurationState
from pal_smach_utils.utils.time_controlling_states import GetCurrentROSTimeState
from move_head_to_the_beat import MoveHeadToTheBeat
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers

HARMONICS = 1.0


class NodHeadWithBeatSM(smach.StateMachine):

    """
    When called, this state machine will get the bpm of a random
    song in the mp3_library of the pkg of dancing_reem and extract
    its bpms. Then it will use them to move its head to the beat.
    """

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:


            smach.StateMachine.add('START_ROBOT_CONTROLERS',
                                   StartRobotControllers(head=True, left=False, right=False),
                                   transitions={succeeded: 'BPM_ANALYSIS',
                                                preempted: preempted,
                                                aborted: aborted})


            smach.StateMachine.add('BPM_ANALYSIS',
                                   BpmAnalysisSM(),
                                   transitions={succeeded: 'GET_SONG_DURATION',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'bpm_out': 'song_bpm',
                                              'song_path_out': 'song_path'})

            smach.StateMachine.add('GET_SONG_DURATION',
                                   SongDurationState(),
                                   transitions={succeeded: 'SET_TIME',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_song_path': 'song_path',
                                              'song_duration_out': 'song_duration'})

            smach.StateMachine.add('SET_TIME',
                                   GetCurrentROSTimeState(),
                                   transitions={succeeded: 'MOVE_HEAD_TO_THE_BEAT',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'starting_ros_time_out': 'time_song_started_playing'})

            smach.StateMachine.add('MOVE_HEAD_TO_THE_BEAT',
                                   MoveHeadToTheBeat(HARMONICS),
                                   transitions={succeeded: 'STOP_ROBOT_CONTROLERS',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_song_duration': 'song_duration',
                                              'in_start_time': 'time_song_started_playing',
                                              'in_beat': 'song_bpm'})

            smach.StateMachine.add('STOP_ROBOT_CONTROLERS',
                                   StopRobotControllers(),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted})
