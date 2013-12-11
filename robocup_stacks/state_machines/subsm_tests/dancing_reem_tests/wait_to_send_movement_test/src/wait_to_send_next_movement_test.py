#! /usr/bin/env python

import roslib
roslib.load_manifest('wait_to_send_movement_test')
import os
import rospy
import smach
import smach_ros
from roslib import packages
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.time_out import TimeOut
from wait_to_send_next_movement import WaitToSendNextMovement


#DUMB_MOVEMENT_XML_NAME = os.path.join(packages.get_pkg_dir('dancing_reem'), 'dancing_movements_database/testing_movement_files/transition_from_middle_to_sides_without_parameter.xml')
DUMB_MOVEMENT_XML_NAME = os.path.join(packages.get_pkg_dir('dancing_reem'), 'dancing_movements_database/testing_movement_files/waiting_to_send_movement.xml')

#DUMB_MOVEMENT_XML_NAME = '/mnt_flash/robocup2013/reem_at_iri/dancing_reem/dancing_movements_database/testing_movement_files/transition_from_middle_to_sides_without_parameter.xml'

HARMONICS = 1.0
# Send a movement every 3 seconds.
BPM_TEST = 20

MOVING_MOCK_TIME = 2.0


class InitVars(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['bpm_out',
                                          'move_name_path_out',
                                          'repeat_var',
                                          'starting_ros_time_out'])

    def execute(self, userdata):

        userdata.bpm_out = BPM_TEST
        userdata.move_name_path_out = DUMB_MOVEMENT_XML_NAME
        userdata.repeat_var = False
        now = rospy.Time.now()
        userdata.starting_ros_time_out = now
        return succeeded


def main():
    rospy.init_node('sm_wait_to_send_movement_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add('INIT_VARS_STATE',
                               InitVars(),
                               transitions={succeeded: 'WAIT_TO_SEND_NEXT_MOVEMENT',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'bpm_out': 'execute_bpm',
                                          'move_name_path_out': 'old_movement_name_path',
                                          'repeat_var': 'repeat_var',
                                          'starting_ros_time_out': 'time_last_movement'})

        smach.StateMachine.add('WAIT_TO_SEND_NEXT_MOVEMENT',
                               WaitToSendNextMovement(HARMONICS),
                               transitions={succeeded: 'MOCK_MOVING',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'in_time_sent_last_movement': 'time_last_movement',
                                          'in_old_file_name': 'old_movement_name_path',
                                          'in_repeat': 'repeat_var',
                                          'in_bpm': 'execute_bpm',
                                          'time_sent_last_movement_out': 'time_last_movement'})

        smach.StateMachine.add('MOCK_MOVING',
                               TimeOut(MOVING_MOCK_TIME),
                               transitions={succeeded: 'WAIT_TO_SEND_NEXT_MOVEMENT',
                                            preempted: preempted,
                                            aborted: aborted})


    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
