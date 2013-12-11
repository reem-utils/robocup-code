#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import roslib
roslib.load_manifest('dancing_reem')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from init_dancing_reem import InitDancingReem
from bpm_analysis import BpmAnalysisSM
from stochastic_movement_selection import StochasticMovementSelection
#from send_mov import SendMov
from pal_smach_utils.utils.play_sound_sm import PlaySoundOnceState, StopSoundState
from pal_smach_utils.utils.song_duration_sm import SongDurationState
from pal_smach_utils.utils.time_controlling_states import GetCurrentROSTimeState, TellIfSongHasFinished
from execute_movement import ExecuteMovement
#from alive_engine import SendMov
from handle_dancing_movement_files import HandleDancingMovementFiles

TESTING = False
BEAT_HARMONIC = 1.0


class GetMovementForDancingReemSM(smach.StateMachine):

    """
    Makes Reem dance to a random picked song in mp3_library of dancing_reem pkg.
    """

    def __init__(self):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:

            smach.StateMachine.add('INIT_DANCING_REEM',
                                   InitDancingReem(),
                                   transitions={succeeded: 'BPM_ANALYSIS',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'initial_future_position_out': 'future_current_position',
                                              'initial_current_position_out': 'current_position',
                                              'next_movement_name_out': 'selected_movement',
                                              'prob_vector_out': 'probability_vector',
                                              'repeat_out': 'repeat_out',
                                              'dict_movement_databse_out': 'dict_available_movements'})

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
                                   transitions={succeeded: 'MODIFY_NEXT_MOVEMENT_SPEED',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'starting_ros_time_out': 'time_song_started_playing'})

            smach.StateMachine.add('STOCHASTIC_MOVEMENT_SELECTION',
                                   StochasticMovementSelection(),
                                   transitions={succeeded: 'MODIFY_NEXT_MOVEMENT_SPEED',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_probability_vector': 'probability_vector',
                                              'in_prev_current_position': 'current_position',
                                              'in_movement_database_dict': 'dict_available_movements',
                                              'in_current_position': 'future_current_position',
                                              'probability_vector': 'probability_vector',
                                              'selected_random_movement_out': 'selected_movement',
                                              'new_current_position_out': 'future_current_position',
                                              'new_prev_current_position_out': 'current_position'})

            smach.StateMachine.add('MODIFY_NEXT_MOVEMENT_SPEED',
                                   HandleDancingMovementFiles(TESTING, BEAT_HARMONIC),
                                   transitions={succeeded: 'TELL_IF_SONG_HAS_FINISHED',
                                                'ended': 'TELL_IF_SONG_HAS_FINISHED',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_bpm_to_use': 'song_bpm',
                                              'in_movement_to_modifie': 'selected_movement',
                                              'in_actual_pos': 'current_position',
                                              'modified_movement_name_path_out': 'next_movement_name_path'})

            smach.StateMachine.add('TELL_IF_SONG_HAS_FINISHED',
                                   TellIfSongHasFinished(),
                                   transitions={'song_not_finished': 'EXECUTE_MOVEMENT',
                                                'song_finished': 'STOP_SOUND',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_starting_ros_time': 'time_song_started_playing',
                                              'song_duration': 'song_duration'})

            smach.StateMachine.add('EXECUTE_MOVEMENT',
                                   ExecuteMovement(),
                                   transitions={succeeded: 'STOCHASTIC_MOVEMENT_SELECTION',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_next_movement_name_path': 'next_movement_name_path'})

            smach.StateMachine.add('STOP_SOUND',
                                   StopSoundState(),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'sound_file_path': 'sound_file_path'})
