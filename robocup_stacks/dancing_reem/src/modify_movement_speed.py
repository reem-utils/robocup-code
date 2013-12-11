# -*- encoding: utf-8 -*-

import roslib; roslib.load_manifest('dancing_reem')
import rospy
import smach
import smach_ros
import os

from random import randint
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.bpm_conversions import BpmToPeriod
from dancing_utils import MoveNameToPath

BEAT_HARMONIC = 1.0

MOVEMENT_XML_TEMPORAL_FILE_PATH = "/tmp/tmp_mov_file.xml"
MOVEMENT_XML_FILE_NAME = "waiting_1.xml"


# TODO
class ModifyMovementSpeed(smach.State):

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted],
                                        input_keys=['in_bpm_to_use', 'in_movement_to_modifie', 'in_actual_pos', 'in_prev_movement_name_path', 'in_prev_current_position'],
                                        output_keys=['modified_movement_name_path_out'])

    def execute(self, userdata):

        rospy.loginfo("BPM THAT WE WANT TO INSERT ==> %s", str(userdata.in_bpm_to_use))
        pressed_key = raw_input('##### Press a key to abort execution,c key to continue: #####')
        while pressed_key != 'a' and pressed_key != 'c':
            print pressed_key
            pressed_key = raw_input('##### Wrong key, please try again (^__^). Remmember, a to abort, c to continue: #####')
        if pressed_key == 'a':
            return aborted

        time_length_movement = BpmToPeriod(userdata.in_bpm_to_use, BEAT_HARMONIC)
        mov_name = MovementsOperations()
        #Previous mov has to be the PATH to the file, not only the name.
        mov_name.previousMov = MoveNameToPath(userdata.in_prev_movement_name_path, userdata.in_prev_current_position)
        # concatenateMovs needs the file PATHS, not the names, teherefore we have to pass the name paths.
        temporal_file_name_path = mov_name.concatenateMovs(MoveNameToPath(userdata.in_movement_to_modifie, userdata.in_actual_pos), time_length_movement)
        userdata.modified_movement_name_path_out = temporal_file_name_path
        return succeeded


def getTmpFilePath():
    """
    Returns the path of the temporal file that will into
    which will be copied the original movement xml file
    and modified the speed acordingly.
    """

    return MOVEMENT_XML_TEMPORAL_FILE_PATH


class MovementsOperations:

    def __init__(self):
        self.previousMov = ''

    def concatenateMovs(self, file, time_period=0.0):

        ''' this function is required to concatenate the last movement done with the new one to make a safe transition
        '''

        # first time we call this, there is no previous mov
        if self.previousMov == '':
            self.previousMov = file
            return file

        # first we delete the tmp file written last time here
        lastMovString = 'ERRORORORORORRRRR'
        text_added = "<!-- first point added by reem alive to file " + file + " from file " + self.previousMov + " -->"
        tmpFile = getTmpFilePath()  # "/tmp/tmp_mov_file.xml"
        if os.path.isfile(tmpFile):
            os.remove(tmpFile)
        lastMovString = open(self.previousMov, 'r').read()

        # then we open the new and last mov files
        newMovString = open(file, 'r').read()
        self.previousMov = file

        concatenation_string = self.generateMovement(lastMovString, newMovString, time_period)
        concatenation_string += text_added
        with open(tmpFile, "w") as text_file:
            text_file.write(concatenation_string)

        return tmpFile

    def generateMovement(self, sourceMovement, targetMovement, time_period):
        POINT_BEGIN = "<value>"
        POINT_END = "</value>"
        POINT_PLACEHOLDER = "DUCKFROST_SPEED"
        lastPointBegin = sourceMovement.rfind(POINT_BEGIN)
        lastPointEnd = sourceMovement.rfind(POINT_END)

        lastPointString = sourceMovement[lastPointBegin:lastPointEnd + POINT_END.__len__()]
        fullPointString = str(time_period)
        return targetMovement.replace(POINT_PLACEHOLDER, fullPointString)

    #TODO , validate wether to leave it or erase it.
    def selectRandomFile(self, state):
            ''' Selects a random file from the dictionary of movements
                @state param is the name of the type of movements that are going to be used
            '''
            list_of_files = self.movements[state]

            number_of_files = len(list_of_files)
            file = list_of_files[randint(0, number_of_files - 1)]

            file = os.path.join(self.listOfDirectories[state], file)

            return self.concatenateMovs(file)
