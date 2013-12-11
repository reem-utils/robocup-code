#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import roslib
roslib.load_manifest('dancing_reem')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from init_dancing_reem import InitDancingReem
from stochastic_movement_selection import StochasticMovementSelection
from pal_smach_utils.utils.time_controlling_states import TellIfSongHasFinished
from handle_dancing_movement_files import HandleDancingMovementFiles
#from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction
from execute_movement import ExecuteMovement
from pal_smach_utils.utils.time_out import TimeOut

TIME_WAIT_BURN_ROOF = 5.0


class DancingReemCicle(smach.StateMachine):

    """
    Dances till during the time that the duration song.
    """

    def __init__(self, beat_harmonic=1.0, testing=False):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=['song_bpm', 'song_path', 'song_duration', 'time_song_started_playing'])

        with self:

            smach.StateMachine.add('WAIT_BEFORE_BURNING_THE_ROOF',
                                   TimeOut(TIME_WAIT_BURN_ROOF),
                                   transitions={succeeded: 'INIT_DANCING_REEM',
                                                preempted: preempted,
                                                aborted: aborted})

            smach.StateMachine.add('INIT_DANCING_REEM',
                                   InitDancingReem(),
                                   transitions={succeeded: 'STOCHASTIC_MOVEMENT_SELECTION',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'initial_future_position_out': 'future_current_position',
                                              'initial_current_position_out': 'current_position',
                                              'next_movement_name_out': 'selected_movement',
                                              'prob_vector_out': 'probability_vector',
                                              'repeat_out': 'repeat_out',
                                              'dict_movement_databse_out': 'dict_available_movements',
                                              'old_movement_name_path_out': 'old_movement_name_path',
                                              'time_sent_last_movement_out': 'time_sent_last_movement'})

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
                                   HandleDancingMovementFiles(testing, beat_harmonic),
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
                                                'song_finished': succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_starting_ros_time': 'time_song_started_playing',
                                              'song_duration': 'song_duration'})

            smach.StateMachine.add('EXECUTE_MOVEMENT',
                                   ExecuteMovement(beat_harmonic),
                                   transitions={succeeded: 'STOCHASTIC_MOVEMENT_SELECTION',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_old_movement_name_path': 'old_movement_name_path',
                                              'in_time_sent_last_movement': 'time_sent_last_movement',
                                              'in_next_movement_name_path': 'next_movement_name_path',
                                              'in_repeat': 'repeat_out',
                                              'in_execute_bpm': 'song_bpm',
                                              'time_sent_last_movement_out': 'time_sent_last_movement',
                                              'old_movement_name_path_out': 'old_movement_name_path'})
