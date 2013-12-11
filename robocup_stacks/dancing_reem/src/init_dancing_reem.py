# -*- encoding: utf-8 -*-
import roslib; roslib.load_manifest('dancing_reem')
import rospy
import smach
import smach_ros
from roslib import packages
import os
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from mov_files_handler_dancing import MovFilesHandler
from write_old_movement import WriteOldMovement


INIT_FUTURE_CURRENT_POS = 'middle'
INIT_CURRENT_POS = 'initial'
INIT_NEXT_MOVEMENT_NAME = 'transition_from_initial_to_middle.xml'
FALSE_MOVEMENT_XML_NAME = os.path.join(packages.get_pkg_dir('dancing_reem'), 'dancing_movements_database/testing_movement_files/empty_movement.xml')
#DUMB_MOVEMENT_XML_NAME = '/mnt_flash/robocup2013/reem_at_iri/dancing_reem/dancing_movements_database/testing_movement_files/empty_movement.xml'


class WritingOldMovText():
    """
    Structure to use the State WriteOldMovement
    """
    def __init__(self):
        self.setTxt()

    def setTxt(self):
        self.in_file_name = ""
        self.old_file_name_out = ""


class InitDancingReem(smach.State):

    def __init__(self):

        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['initial_future_position_out',
                                          'initial_current_position_out',
                                          'next_movement_name_out',
                                          'prob_vector_out',
                                          'repeat_out',
                                          'dict_movement_databse_out',
                                          'old_movement_name_path_out',
                                          'time_sent_last_movement_out'])

        self.movHandler = MovFilesHandler()

    def execute(self, userdata):

        print "INIT ---> FUTURE CURRENT POSITION == " + str(INIT_FUTURE_CURRENT_POS)
        print "INIT --->        CURRENT POSITION == " + str(INIT_CURRENT_POS)
        print "INIT ---> MOVEMENT NAME ==> " + str(INIT_NEXT_MOVEMENT_NAME)

        userdata.initial_future_position_out = INIT_FUTURE_CURRENT_POS
        userdata.initial_current_position_out = INIT_CURRENT_POS
        userdata.next_movement_name_out = INIT_NEXT_MOVEMENT_NAME
        userdata.prob_vector_out = [0.0]
        # We dont want that the robots repeats any movement
        userdata.repeat_out = False

        #Dictionary Movement Database
        userdata.dict_movement_databse_out = self.movHandler.movements

        #Add old movement path and set time you sent it. It will be a false movement,
        #because there isnt any movement before init to middle.
        # We now write the old move in the /tmp/tmp_mov_file_old.xml
        userdata.old_movement_name_path_out = FALSE_MOVEMENT_XML_NAME
        t = WritingOldMovText()
        t.in_file_name = FALSE_MOVEMENT_XML_NAME
        writeOldMovSM = WriteOldMovement()
        writeOldMovSM.execute(t)
        #We initialise the counter
        now = rospy.Time.now()
        userdata.time_sent_last_movement_out = now

        return succeeded
