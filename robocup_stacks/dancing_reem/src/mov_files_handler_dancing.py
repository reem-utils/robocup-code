# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:53:06 2012

@author: ricardo
"""
import roslib; roslib.load_manifest('dancing_reem')
import os
import rospy

from roslib import packages
from random import randint

MOVEMENT_XML_TEMPORAL_FILE_PATH = "/tmp/tmp_mov_file.xml"
USE_MOCK_TMPFILEPATH = True
PACKAGE_WHERE_TO_FIND_DANCING_MOVEMENTS = 'dancing_reem'
DANCING_DATABASE_DIR = 'dancing_movements_database'
ADD_LAST_POSITION_AS_FIRST_MOVEMENT = False


class MovFilesHandler ():

    def __init__(self):
        self.setMovementsDatabase()
        self.waving_st = 1

    def setMovementsDatabase(self):

        self.movements = {}
        self.setDirectoryNames()

    def setDirectoryNames(self):

        """
        Sets the dictionary database movement dancing reem structure.
        """

        base = packages.get_pkg_dir(PACKAGE_WHERE_TO_FIND_DANCING_MOVEMENTS)
        dbdir = os.path.join(base, DANCING_DATABASE_DIR)

        self.DANGEROUS_DIR = os.path.join(dbdir, 'dangerous')
        self.MIDDLE_DIR = os.path.join(dbdir, 'middle')
        self.UP_DIR = os.path.join(dbdir, 'up')
        self.SIDES_DIR = os.path.join(dbdir, 'sides')
        self.INITIAL_DIR = os.path.join(dbdir, 'initial')

        self.listOfDirectories = {'dangerous':  self.DANGEROUS_DIR,
                                  'middle':     self.MIDDLE_DIR,
                                  'up':         self.UP_DIR,
                                  'sides':      self.SIDES_DIR,
                                  'initial':    self.INITIAL_DIR}

        self.movements = {'dangerous':        filter(lambda x: x.endswith('.xml'), os.listdir(self.DANGEROUS_DIR)),
                          'middle':       filter(lambda x: x.endswith('.xml'), os.listdir(self.MIDDLE_DIR)),
                          'up':      filter(lambda x: x.endswith('.xml'), os.listdir(self.UP_DIR)),
                          'sides':           filter(lambda x: x.endswith('.xml'), os.listdir(self.SIDES_DIR)),
                          'initial':          filter(lambda x: x.endswith('.xml'), os.listdir(self.INITIAL_DIR))}

        self.previousMov = ''

    # FIXME, the calls to the listOfDirectories is like is was a list, but it seems a
    #Dictionary.
    def selectRandomFile(self, state):
        list_of_files = self.movements[state]

        number_of_files = len(list_of_files)
        file = list_of_files[randint(0, number_of_files - 1)]

        file = os.path.join(self.listOfDirectories[state], file)
        rospy.loginfo('Chosen file: %s', file)

        return self.concatenateMovs(file)

    def MoveNameToPathBetter(self, movement_name, current_pos):

        """
        Given a movement name and the current pos it returns the absolute path to that file.
        In Case it doesn't exist, it will raise an assertion.
        """
        absolute_path_mov_name = os.path.join(self.listOfDirectories.get(current_pos), movement_name)
        print "This is the ORIGINAL movement PATH"

        print str(absolute_path_mov_name)
        assert (os.path.exists(absolute_path_mov_name)), "The path to the movement file doesn't exist"
        return absolute_path_mov_name

    def selectDancingMovementFile(self, movement_to_modifie, current_position, time_period=0.0):

        """
        Given the current position and a movement name in that position,
        it returns a movement_path ( which isn't necesarily the original one)
        to a modified copy of the movement requested and with the desired speed.
        If no speed is stated, then speed 0 will be written.
        """

        movement_path = self.MoveNameToPathBetter(movement_to_modifie, current_position)
        print "PREV MOV" + str(self.previousMov)
        movement_path_to_be_used = self.concatenateMovs(movement_path, time_period, USE_MOCK_TMPFILEPATH)

        return movement_path_to_be_used

    def concatenateMovs(self, file_path, time_period, use_mock_TmpFilePath):

        # this function is required to concatenate the last movement done with the new one to make it a safe transition

        # first time we call this, there is no previous mov
        if self.previousMov == '':
            print "No PREVIOUS MOVEMENT"
            self.previousMov = file_path
            print "INSIDE CONCATENATE ,PREV MOV ==>" + str(self.previousMov)
            #return file_path

        # FIXME, whats this?
        lastMovString = 'ERRORORORORORRRRR'
        text_added = "<!-- first point added by dancing_reem to file_path " + file_path + " from file_path " + self.previousMov + " -->"

        # FIXME, we should use the non Mock.
        if use_mock_TmpFilePath:
            tmpFile = getTmpFilePath_Mock()  # "/tmp/tmp_mov_file.xml"
        else:
            tmpFile = getTmpFilePath()

        # We delete the tmp file_path written last time here
        if os.path.isfile(tmpFile):
            os.remove(tmpFile)

        # Then we open the new and last mov files
        # We read the file in previousMov specified path. And store it in lastMovString
        lastMovString = open(self.previousMov, 'r').read()
        # Here the new movement.
        newMovString = open(file_path, 'r').read()
        #We update the previousMov with the new movement path.
        self.previousMov = file_path

        #
        concatenation_string = self.generateMovement(lastMovString, newMovString, time_period)

        # Here we add at the bottom of the concatenation object what we've done.
        concatenation_string += text_added

        # Here we write the resulting concatenation in the temporal file.
        with open(tmpFile, "w") as text_file:
            text_file.write(concatenation_string)

        return tmpFile

    def generateMovement(self, sourceMovement, targetMovement, time_period):
        POINT_BEGIN = "<value>"
        POINT_END = "</value>"
        POINT_PLACEHOLDER = "<!-- START MOVEMENT -->"
        SPEED_PLACEHOLDER = "MOVEMENT_TIME_PERIOD"

        lastPointBegin = sourceMovement.rfind(POINT_BEGIN)
        lastPointEnd = sourceMovement.rfind(POINT_END)

        # Last point is the last position in which the previous movement ended.
        lastPointString = sourceMovement[lastPointBegin:lastPointEnd + POINT_END.__len__()]
        speedString = str(time_period)
        
        if (ADD_LAST_POSITION_AS_FIRST_MOVEMENT):
            fullPointString = '<point delta_time = "MOVEMENT_TIME_PERIOD" >' + lastPointString + '</point>'
        else:
            fullPointString = ''

        # Replace the Point_PLaceHolder with the last position of the previous movement.
        text_string_no_speed = targetMovement.replace(POINT_PLACEHOLDER, fullPointString)
        text_string_with_speed_replaced = text_string_no_speed.replace(SPEED_PLACEHOLDER, speedString)

        return text_string_with_speed_replaced


# FIXME, this is a temporal function until the real one works.
def getTmpFilePath_Mock():
    """
    Returns the path of the temporal file that will into
    which will be copied the original movement xml file
    and modified the speed acordingly.
    """

    return MOVEMENT_XML_TEMPORAL_FILE_PATH


# FIXME , this doesnt work on my PC.
def getTmpFilePath():

    base_path = '/mnt_flash/etc/control/robot/'
    if os.environ.get('TARGET') == 'desktop':   # if we are not in the robot
        base_path = os.environ.get('HOME') + '/' + os.environ.get('PAL_BRANCH') + '/robot/sources/etc/control/robot/'  # os.environ.get('LAUNCH_PATH')

    robot = os.environ.get('PAL_ROBOT')
    if robot == 'rh2c' or robot == 'rh2m':
        robot = 'reemh2'
    if robot == 'reemh3c' or robot == 'reemh3m':
        robot = 'reemh3'

    file_path = base_path + robot + '/motion/tmp_reem_alive.xml'

    return file_path
