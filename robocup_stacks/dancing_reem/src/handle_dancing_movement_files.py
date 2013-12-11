# -*- coding: utf-8 -*-
"""
@author: RDaneelOlivaw
"""
import roslib
roslib.load_manifest('dancing_reem')
import rospy
import smach
from mov_files_handler_dancing import MovFilesHandler
#from leds_handling import LedManager
#from safety_zone_handling import SafetyManager
from pal_smach_utils.utils.bpm_conversions import BpmToPeriod

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted


class HandleDancingMovementFiles(smach.State):
    '''
    This State, gives the temporal file PATH where the desired movement was copied with the
    modified speed corresponing to the bpm given.
    input_keys :
    in_bpm_to_use --> BPM of the song that Reem is dancing.
    in_movement_to_modifie --> The movement that we want to modify the speed.
    in_actual_pos --> The position in which Reem is now and database_dancing_directory
    where we can find the in_movement_to_modifie

    output_keys :
    modified_movement_name_path_out --> Path of the temporal file that we have to use in
    order to make Reem perform the movement at the correct speed.

    '''

    def __init__(self, testing_mode=False, beat_harmonic=1.0):
        smach.State.__init__(self,
                             outcomes=[succeeded, 'ended', preempted, aborted],
                             input_keys=['in_bpm_to_use', 'in_movement_to_modifie', 'in_actual_pos'],
                             output_keys=['modified_movement_name_path_out'])
        print "#########################INIT HAndleDancingMovementFiles##############"
        self.movHandler = MovFilesHandler()
        #self.ledManager = LedManager()
        #self.SafetyManager = SafetyManager()
        self._testing_mode = testing_mode
        self._beat_harmonic = beat_harmonic

        self.previousState = 'UNKNOWN'

    def execute(self, userdata):

        pressed_key = ''

        if self._testing_mode:

            # We stop just for testing.
            rospy.loginfo("BPM THAT WE WANT TO INSERT ==> %s", str(userdata.in_bpm_to_use))
            pressed_key = raw_input("##### Press 'a' key to abort execution,'c' key to continue, press 'e' to end: #####")
            while pressed_key != 'a' and pressed_key != 'c' and pressed_key != 'e':
                print pressed_key
                pressed_key = raw_input('##### Wrong key, please try again (^__^). Remmember, a to abort, c to continue: #####')
            if pressed_key == 'a':
                return aborted

        # TODO
        # calls leds based on The Beat of the music.
        #self.ledManager.callLedsForDancing(BpmToFreq(userdata.in_bpm_to_use))

        # We obtain the period corresponding to the BPM
        time_length_movement = BpmToPeriod(userdata.in_bpm_to_use, self._beat_harmonic)

        # selects the movement to execute based on state
        userdata.modified_movement_name_path_out = self.movHandler.selectDancingMovementFile(userdata.in_movement_to_modifie,
                                                                                             userdata.in_actual_pos,
                                                                                             time_length_movement)

        if pressed_key == 'e':
            return 'ended'

        return succeeded
