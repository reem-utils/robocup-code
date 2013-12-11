# -*- encoding: utf-8 -*-
import roslib
roslib.load_manifest('dancing_reem')
import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from mov_files_handler_dancing import MovFilesHandler

INIT_FIRST_UP_DOWN_MOV = 'down'


class InitUpDownMov(smach.State):

    def __init__(self):

        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['initial_up_down_mov_out'])

        self.movHandler = MovFilesHandler()

    def execute(self, userdata):

        rospy.loginfo("STARTING INIT UP DOWN MOVS, with value ==> " + str(INIT_FIRST_UP_DOWN_MOV))
        userdata.initial_up_down_mov_out = INIT_FIRST_UP_DOWN_MOV

        return succeeded
