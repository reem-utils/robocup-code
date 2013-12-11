#! /usr/bin/env python

import roslib
roslib.load_manifest('dancing_reem')
import smach
import rospy
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from init_dancing_reem import InitDancingReem
from bpm_analysis import BpmAnalysisSM
from pal_smach_utils.utils.play_sound_sm import PlaySoundOnceState, StopSoundState
from pal_smach_utils.utils.song_duration_sm import SongDurationState
from pal_smach_utils.utils.time_controlling_states import GetCurrentROSTimeState
from move_head_to_the_beat import MoveHeadToTheBeat
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers
from dancing_cicle import DancingReemCicle
from pal_smach_utils.utils.concurrence_robocup import ConcurrenceRobocup
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.time_out import TimeOut
#from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction

DANCE_FRASE = "Now I remmember, I going to dance "
TESTING = False
BEAT_HARMONIC = 2.0
TIME_SAY_SONG_NAME = 1.0


class FakeDance(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             input_keys=['song_bpm',
                                         'song_path',
                                         'song_duration',
                                         'time_song_started_playing'])

    def execute(self, userdata):
        rospy.loginfo("SONG BPM =" + str(userdata.song_bpm))
        rospy.loginfo("SONG PATH =" + str(userdata.song_path))
        rospy.loginfo("WHEN DID SONG START =" + str(userdata.time_song_started_playing))
        wait_seconds = userdata.song_duration / 1000.0
        rospy.loginfo("TimeOut of =" + str(wait_seconds))
        rospy.sleep(userdata.song_duration / 1000.0)

        return succeeded


def main():

    rospy.init_node('sm_dancing_reem_and_nod')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        intro_text = "I feel like dancing now! Give me a minute to remmember song."
        smach.StateMachine.add('START',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'START_ROBOT_CONTROLERS'})

        smach.StateMachine.add('START_ROBOT_CONTROLERS',
                               StartRobotControllers(head=True, left=False, right=False),
                               transitions={succeeded: 'INIT_DANCING_REEM',
                                            preempted: preempted,
                                            aborted: aborted})

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
                                          'dict_movement_databse_out': 'dict_available_movements',
                                          'old_movement_name_path_out': 'old_movement_name_path',
                                          'time_sent_last_movement_out': 'time_sent_last_movement'})

        smach.StateMachine.add('BPM_ANALYSIS',
                               BpmAnalysisSM(),
                               transitions={succeeded: 'GET_SONG_DURATION',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'bpm_out': 'song_bpm',
                                          'song_path_out': 'song_path'})

        smach.StateMachine.add('GET_SONG_DURATION',
                               SongDurationState(),
                               transitions={succeeded: 'ANOUNCE_DANCING_START_SONG',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'in_song_path': 'song_path',
                                          'song_duration_out': 'song_duration'})

        def say_text_cb(userdata):
                song_path_name_list = userdata.song_path.split("/")
                length_list = len(song_path_name_list) - 1
                if length_list < 0:
                    length_list = 0
                song_full_name = song_path_name_list[length_list]
                song_name = song_full_name.split(".")[0]
                text_say = DANCE_FRASE + song_name
                return text_say
        smach.StateMachine.add('ANOUNCE_DANCING_START_SONG',
                               SpeakActionState(text_cb=say_text_cb, input_keys=['song_path']),
                               transitions={succeeded: 'WAIT'})

        smach.StateMachine.add('WAIT',
                               TimeOut(TIME_SAY_SONG_NAME),
                               transitions={succeeded: 'PLAY_SONG',
                                            preempted: preempted,
                                            aborted: aborted})

        smach.StateMachine.add('PLAY_SONG',
                               PlaySoundOnceState(),
                               transitions={succeeded: 'SET_TIME',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'sound_file_path': 'song_path'})

        smach.StateMachine.add('SET_TIME',
                               GetCurrentROSTimeState(),
                               transitions={succeeded: 'WAIT2',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'starting_ros_time_out': 'time_song_started_playing'})

        smach.StateMachine.add('WAIT2',
                               TimeOut(5),
                               transitions={succeeded: 'DANCE_AND_NOD',
                                            preempted: preempted,
                                            aborted: aborted})

        #### CONCURRENT MAIN NOD and EXECUTE

        STATES_2 = [MoveHeadToTheBeat(BEAT_HARMONIC), DancingReemCicle(BEAT_HARMONIC, TESTING)]
        STATE_NAMES_2 = ["MOVE_HEAD_TO_THE_BEAT", "DANCING_REEM_CICLE"]

        smach.StateMachine.add("DANCE_AND_NOD",
                               ConcurrenceRobocup(states=STATES_2,
                                                  state_names=STATE_NAMES_2,
                                                  input_keys=['in_song_duration',
                                                              'in_start_time',
                                                              'in_beat',
                                                              'song_bpm',
                                                              'song_path',
                                                              'song_duration',
                                                              'time_song_started_playing']),
                               remapping={'in_song_duration': 'song_duration',
                                          'in_start_time': 'time_song_started_playing',
                                          'in_beat': 'song_bpm'},
                               transitions={succeeded: "STOP_SOUND", aborted: "SAY_NEED_HELP"})

        #### MAIN FINISHED
        smach.StateMachine.add('STOP_SOUND',
                               StopSoundState(),
                               transitions={succeeded: succeeded,
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'sound_file_path': 'sound_file_path'})

        smach.StateMachine.add('STOP_ROBOT_CONTROLERS',
                               StopRobotControllers(),
                               transitions={succeeded: succeeded,
                                            preempted: preempted,
                                            aborted: aborted})

        intro_text = "Ups, I think I need some technical help."
        smach.StateMachine.add('SAY_NEED_HELP',
                               SpeakActionState(intro_text),
                               transitions={succeeded: succeeded})

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()


"""
        smach.StateMachine.add('MOVE_HEAD_TO_THE_BEAT',
                               MoveHeadToTheBeat(BEAT_HARMONIC),
                               transitions={'song_finished': 'STOP_ROBOT_CONTROLERS',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'in_song_duration': 'song_duration',
                                          'in_start_time': 'time_song_started_playing',
                                          'in_beat': 'song_bpm'})

        smach.StateMachine.add('DANCING_REEM_CICLE',
                               DancingReemCicle(BEAT_HARMONIC, TESTING),
                               transitions={succeeded: 'STOP_SOUND',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'song_bpm': 'song_bpm',
                                          'song_path': 'song_path',
                                          'song_duration': 'song_duration',
                                          'time_song_started_playing': 'time_song_started_playing'})
"""
