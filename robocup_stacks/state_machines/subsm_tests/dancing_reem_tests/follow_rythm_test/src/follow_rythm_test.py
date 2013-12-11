#! /usr/bin/env python

import roslib
roslib.load_manifest('follow_rythm_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.play_sound_sm import PlaySoundOnceState, StopSoundState
from pal_smach_utils.utils.song_duration_sm import SongDurationState
from pal_smach_utils.utils.time_controlling_states import GetCurrentROSTimeState, TellIfSongHasFinished

from pal_smach_utils.speech.sound_action import SpeakActionState

from init_dancing_reem import InitDancingReem
from bpm_analysis import BpmAnalysisSM
from handle_dancing_movement_files import HandleDancingMovementFiles
from execute_movement import ExecuteMovement
from give_alternative_up_down_mov_path import GiveAlternateUpDownMov, DecideIfTimeToBurnRoof
from init_give_alternative_up_down import InitUpDownMov

TESTING = False
BEAT_HARMONIC = 1.0
#Duration of Up down moving arm in miliseconds.
UP_DOWN_MOV_DURATION = 30.0 * 1000


def main():
    """
    This Tests Reem reading a song and moving its arm to the beat, up and down.
    """
    rospy.init_node('sm_modify_next_movement_speed_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

            intro_text = "Let's start to follow the rythm with my hand."
            smach.StateMachine.add('STARTING_FOLLOW_RYTHM_TEST',
                                   SpeakActionState(intro_text),
                                   transitions={succeeded: 'INIT_DANCING_REEM'})

            smach.StateMachine.add('INIT_DANCING_REEM',
                                   InitDancingReem(),
                                   transitions={succeeded: 'INIT_UP_AND_DOWN_MOV',
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

            smach.StateMachine.add('INIT_UP_AND_DOWN_MOV',
                                   InitUpDownMov(),
                                   transitions={succeeded: 'BPM_ANALYSIS',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'initial_up_down_mov_out': 'current_up_down_mov'})

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

            smach.StateMachine.add('DECIDE_IF_TIME_BURN_THE_ROOF',
                                   DecideIfTimeToBurnRoof(UP_DOWN_MOV_DURATION),
                                   transitions={'continue_up_down': 'GIVE_UP_AND_DOWN_MOV_PATH',
                                                'change_to_stochastic': 'CHANGING_TO_STOCHASTIC',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_current_up_down_mov': 'current_up_down_mov',
                                              'in_song_start_time': 'time_song_started_playing'})

            smach.StateMachine.add('GIVE_UP_AND_DOWN_MOV_PATH',
                                   GiveAlternateUpDownMov(),
                                   transitions={succeeded: 'MODIFY_NEXT_MOVEMENT_SPEED',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_current_up_down_mov': 'current_up_down_mov',
                                              'selected_up_down_movement_out': 'selected_movement',
                                              'new_prev_current_position_out': 'current_position',
                                              'current_up_down_mov_out': 'current_up_down_mov'})

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
                                   ExecuteMovement(BEAT_HARMONIC),
                                   transitions={succeeded: 'DECIDE_IF_TIME_BURN_THE_ROOF',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_old_movement_name_path': 'old_movement_name_path',
                                              'in_time_sent_last_movement': 'time_sent_last_movement',
                                              'in_next_movement_name_path': 'next_movement_name_path',
                                              'in_repeat': 'repeat_out',
                                              'in_execute_bpm': 'song_bpm',
                                              'time_sent_last_movement_out': 'time_sent_last_movement',
                                              'old_movement_name_path_out': 'old_movement_name_path'})

            intro_text = "Now I'm going to burn the roof."
            smach.StateMachine.add('CHANGING_TO_STOCHASTIC',
                                   SpeakActionState(intro_text),
                                   transitions={succeeded: 'STOP_SOUND'})

            smach.StateMachine.add('STOP_SOUND',
                                   StopSoundState(),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'sound_file_path': 'sound_file_path'})

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
