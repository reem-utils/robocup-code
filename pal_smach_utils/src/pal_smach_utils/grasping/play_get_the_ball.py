#!/usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import os
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.timeout_container import SleepState
from pal_smach_utils.speech.sound_action import SpeakActionState
from roslib import packages

START_PLAY_BALL_TXT = "Let's play! Move The ball around and I will try to get it."
END_PLAY_BALL_TXT = "I am getting dizzy, let's stop playing."
NAME_OF_PKG_PLAY_BALL_DEMO = rospy.get_param("names_space_params_play_get_the_ball_test/name_of_pkg_play_ball_demo", "reem_grab_ball")


class StartPlayGetTheBallState(smach.State):

    """
    Tries to get an orange ball that you move infront of Reem.
    """

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted])

    def execute(self, userdata):

        rospy.loginfo("###############" + str(NAME_OF_PKG_PLAY_BALL_DEMO))
        absolute_path_mov_name = os.path.join(packages.get_pkg_dir(NAME_OF_PKG_PLAY_BALL_DEMO), 'scripts/start_demo.sh')
        print str(absolute_path_mov_name)
        assert (os.path.exists(absolute_path_mov_name)), "The path to the start_demo.sh file doesn't exist"
        absolute_path_mov_name
        rospy.loginfo("STARTED PLAY_BALL_DEMO.SH ")
        return succeeded


class StopPlayGetTheBallState(smach.State):

    """
    Tries to get an orange ball that you move infront of Reem.
    """

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted])

    def execute(self, userdata):

        absolute_path_mov_name = os.path.join(packages.get_pkg_dir(NAME_OF_PKG_PLAY_BALL_DEMO), 'scripts/stop_demo.sh')
        print str(absolute_path_mov_name)
        assert (os.path.exists(absolute_path_mov_name)), "The path to the stop_demo.sh file doesn't exist"
        absolute_path_mov_name
        rospy.loginfo("STOPPED PLAY_BALL_DEMO.SH ")

        return succeeded


class PlayGetTheBall(smach.StateMachine):

    """
    Reem plays to try and get the ball moved infront during the time given
    through time_playing. By default it doesnt play.
    """

    def __init__(self, time_playing=0.0):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted])
        self._time_playing = time_playing

        with self:

            start_text = START_PLAY_BALL_TXT
            smach.StateMachine.add('START_PLAY_GET_BALL',
                                   SpeakActionState(start_text),
                                   transitions={succeeded: 'START_PLAY_GET_THE_BALL_STATE'})

            smach.StateMachine.add('START_PLAY_GET_THE_BALL_STATE',
                                   StartPlayGetTheBallState(),
                                   transitions={succeeded: 'TIME_PLAYING', preempted: preempted, aborted: aborted})

            smach.StateMachine.add('TIME_PLAYING',
                                   SleepState(self._time_playing),
                                   transitions={succeeded: 'STOP_PLAY_GET_THE_BALL_STATE', preempted: preempted})

            smach.StateMachine.add('STOP_PLAY_GET_THE_BALL_STATE',
                                   StopPlayGetTheBallState(),
                                   transitions={succeeded: 'END_PLAY_GET_BALL', preempted: preempted, aborted: aborted})

            end_text = END_PLAY_BALL_TXT
            smach.StateMachine.add('END_PLAY_GET_BALL',
                                   SpeakActionState(end_text),
                                   transitions={succeeded: succeeded})
