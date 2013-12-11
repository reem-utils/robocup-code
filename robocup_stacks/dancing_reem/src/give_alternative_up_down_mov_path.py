# -*- encoding: utf-8 -*-
import roslib
roslib.load_manifest('dancing_reem')
import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.time_controlling_states import SongHasFinished

CURRENT_POS = 'middle'
UP_ARM_MOVEMENT_NAME = 'middle_arm_up.xml'
DOWN_ARM_MOVEMENT_NAME = 'middle_arm_down.xml'
#UP_DOWN_MOVEMENT = 'middle_down_up_movement.xml'
DOWN = 'down'
UP = 'up'


class GiveAlternateUpDownMov(smach.State):
    """
    Alternates from an Arm up movement to a down arm movement.
    IMPORTANT : You have to run first InitUpDownMov to start the in_current_up_down_mov variable.
    """

    def __init__(self):

        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             input_keys=['in_current_up_down_mov'],
                             output_keys=['selected_up_down_movement_out',
                                          'new_prev_current_position_out',
                                          'current_up_down_mov_out'])

    def execute(self, userdata):

        rospy.loginfo("STARTING GIVE ALTERNATE UP DOWN MOVS")
        if userdata.in_current_up_down_mov == DOWN:
            userdata.selected_up_down_movement_out = UP_ARM_MOVEMENT_NAME
            userdata.current_up_down_mov_out = UP
        else:
            userdata.selected_up_down_movement_out = DOWN_ARM_MOVEMENT_NAME
            userdata.current_up_down_mov_out = DOWN

        userdata.new_prev_current_position_out = CURRENT_POS

        return succeeded


class DecideIfTimeToBurnRoof(smach.State):
    """
    Decides if its time to go to stochastig mode or continue with the up down arm movs.
    Based on:
    1) The time that you asked him to do the up and down mov.
    2) If the last movement Reem did was the down movement, because the arm is in the up
    position and not in the middle starting Pos, which is necesary to be in case of transition.
    """

    def __init__(self, up_down_time=0.0):

        smach.State.__init__(self,
                             outcomes=['continue_up_down', 'change_to_stochastic', preempted, aborted],
                             input_keys=['in_song_start_time',
                                         'in_current_up_down_mov'])

        self._up_down_time = up_down_time

    def execute(self, userdata):

        rospy.loginfo("STARTING DecideIfTimeToBurnRoof")
        if userdata.in_current_up_down_mov == DOWN and TimeEnded(userdata.in_song_start_time, self._up_down_time):
            return 'change_to_stochastic'
        return 'continue_up_down'


def TimeEnded(start_time, duration_ms):

    return SongHasFinished(start_time, duration_ms) == 'song_finished'
