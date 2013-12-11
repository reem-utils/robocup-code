#! /usr/bin/env python

import roslib
roslib.load_manifest('execute_movement_xml_test')
import rospy
import smach
import smach_ros
from roslib import packages
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from execute_movement import ExecuteMovement
import os
from pal_smach_utils.utils.check_dependences import CheckDependencesState
from pal_smach_utils.utils.time_controlling_states import GetCurrentROSTimeState
from write_old_movement import WriteOldMovement

DUMB_MOVEMENT_XML_NAME = os.path.join(packages.get_pkg_dir('dancing_reem'), 'dancing_movements_database/testing_movement_files/transition_from_middle_to_sides_without_parameter.xml')
DUMB_MOVEMENT_XML_NAME2 = os.path.join(packages.get_pkg_dir('dancing_reem'), 'dancing_movements_database/testing_movement_files/waiting_to_send_movement.xml')


#DUMB_MOVEMENT_XML_NAME = '/mnt_flash/robocup2013/reem_at_iri/dancing_reem/dancing_movements_database/testing_movement_files/transition_from_middle_to_sides_without_parameter.xml'
#DUMB_MOVEMENT_XML_NAME2 = '/mnt_flash/robocup2013/reem_at_iri/dancing_reem/dancing_movements_database/testing_movement_files/transition_from_sides_to_middle_without_parameter.xml'

"""
robot = os.environ.get('PAL_ROBOT')
ros_master_uri = os.environ.get('ROS_MASTER_URI')
remotelly_executing = ros_master_uri.rfind('localhost')
rospy.loginfo ('remotelly_executing ', remotelly_executing)
MOTION_FOLDER_PATH = ''
if robot == 'rh2c' or robot == 'rh2m' or robot == 'reemh3c' or robot == 'reemh3m' or robot == 'reemh3' or remotelly_executing == -1:
    check_for_door = True
    LASER_TOPIC = '/scan_filtered'
    MOTION_FOLDER_PATH = "/mnt_flash/stacks/reem_alive/alive_engine/config/database/Stopped/interact_1.xml"
    if remotelly_executing == -1:
        MOTION_FOLDER_PATH = packages.get_pkg_dir('common') + '/config/interact_1.xml'
"""


HARMONICS = 1.0
# Send a movement every 3 seconds.
BPM_TEST = 20

STOPPING = False

TOPICS = None
SERVICES = None
ACTIONS = ["/motion_manager"]
MAP_LOC = None


def StopTillPressEnter(go):
    string_entered = ""
    if go:
        string_entered = raw_input('Press any Key to continue, type EXIT to finish.')

    return string_entered


class WritingOldMovText():

    def __init__(self):
        self.setTxt()

    def setTxt(self):
        self.in_file_name = ""
        self.old_file_name_out = ""


class InitNumbers(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['movement_number_out',
                                          'out_bpm',
                                          'init_old_movement_name_path',
                                          'init_time_sent_last_movement'])

    def execute(self, userdata):

        userdata.movement_number_out = 0
        userdata.out_bpm = BPM_TEST
        userdata.init_old_movement_name_path = DUMB_MOVEMENT_XML_NAME2
        # We now write the old move in the /tmp/tmp_mov_file_old.xml
        t = WritingOldMovText()
        t.in_file_name = DUMB_MOVEMENT_XML_NAME2
        writeOldMovSM = WriteOldMovement()
        writeOldMovSM.execute(t)
        #We initialise the counter
        now = rospy.Time.now()
        userdata.init_time_sent_last_movement = now
        return succeeded


class ExecuteMovementXMLDummyState(smach.State):

    """
    Fills the move_name_out with a testing_movement absolute path.
    """

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             input_keys=['in_movement_number'],
                             output_keys=['move_name_path_out', 'movement_number_out', 'repeat_var_out'])

    def execute(self, userdata):
        userdata.repeat_var_out = False
        if StopTillPressEnter(STOPPING) == 'EXIT':
            return aborted

        if userdata.in_movement_number == 1:
            userdata.move_name_path_out = DUMB_MOVEMENT_XML_NAME2
            rospy.loginfo("MOVEMENT " + DUMB_MOVEMENT_XML_NAME2 + " selected")
            userdata.movement_number_out = 2
        else:
            userdata.move_name_path_out = DUMB_MOVEMENT_XML_NAME
            rospy.loginfo("MOVEMENT " + DUMB_MOVEMENT_XML_NAME + " selected")
            userdata.movement_number_out = 1
        return succeeded


def main():
    rospy.init_node('sm_init_dancing_reem_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add("CHECK_DEPENDENCES",
                               CheckDependencesState(topic_names=TOPICS,
                                                     service_names=SERVICES,
                                                     action_names=ACTIONS,
                                                     map_locations=MAP_LOC),
                               transitions={succeeded: "INIT_NUMBERS_STATE", aborted: aborted})

        smach.StateMachine.add('INIT_NUMBERS_STATE',
                               InitNumbers(),
                               transitions={succeeded: 'STOCHASTIC_DUMMY_STATE',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'movement_number_out': 'movement_number',
                                          'out_bpm': 'bpm',
                                          'init_old_movement_name_path': 'old_movement_name_path',
                                          'init_time_sent_last_movement': 'time_sent_last_movement'})

        smach.StateMachine.add('STOCHASTIC_DUMMY_STATE',
                               ExecuteMovementXMLDummyState(),
                               transitions={succeeded: 'EXECUTE_MOVEMENT',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'in_movement_number': 'movement_number',
                                          'move_name_path_out': 'next_movement_name_path',
                                          'movement_number_out': 'movement_number',
                                          'repeat_var_out': 'repeat_var'})

        smach.StateMachine.add('EXECUTE_MOVEMENT',
                               ExecuteMovement(HARMONICS),
                               transitions={succeeded: 'STOCHASTIC_DUMMY_STATE',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'in_old_movement_name_path': 'old_movement_name_path',
                                          'in_time_sent_last_movement': 'time_sent_last_movement',
                                          'in_next_movement_name_path': 'next_movement_name_path',
                                          'in_repeat': 'repeat_var',
                                          'in_execute_bpm': 'bpm',
                                          'time_sent_last_movement_out': 'time_sent_last_movement',
                                          'old_movement_name_path_out': 'old_movement_name_path'})

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
