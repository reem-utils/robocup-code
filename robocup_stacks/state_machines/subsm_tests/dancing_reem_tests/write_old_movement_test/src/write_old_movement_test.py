#! /usr/bin/env python

import roslib
roslib.load_manifest('write_old_movement_test')
import os
import rospy
import smach
import smach_ros
from roslib import packages
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from write_old_movement import WriteOldMovement


DUMB_MOVEMENT_XML_NAME = os.path.join(packages.get_pkg_dir('dancing_reem'), 'dancing_movements_database/testing_movement_files/waiting_to_send_movement.xml')
#DUMB_MOVEMENT_XML_NAME = os.path.join(packages.get_pkg_dir('dancing_reem'), 'dancing_movements_database/testing_movement_files/transition_from_middle_to_sides_without_parameter.xml')

#DUMB_MOVEMENT_XML_NAME = '/mnt_flash/robocup2013/reem_at_iri/dancing_reem/dancing_movements_database/testing_movement_files/transition_from_middle_to_sides_without_parameter.xml'

MOVING_MOCK_TIME = 2.0


class PrintUserData1(smach.State):

    def __init__(self,
                 message_name1='Message1'):
            smach.State.__init__(self,
                                 outcomes=[succeeded, preempted, aborted],
                                 input_keys=['message1'])

            self._message_name1 = message_name1

    def execute(self, userdata):
            rospy.loginfo('This is the %s: %s' % (self._message_name1, str(userdata.message1)))

            return succeeded


class InitVars(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['move_name_path_out'])

    def execute(self, userdata):

        userdata.move_name_path_out = DUMB_MOVEMENT_XML_NAME
        return succeeded


def main():
    rospy.init_node('sm_write_old_movement_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add('INIT_VARS_STATE',
                               InitVars(),
                               transitions={succeeded: 'WAIT_TO_SEND_NEXT_MOVEMENT',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'move_name_path_out': 'movement_name_path'})

        smach.StateMachine.add('WAIT_TO_SEND_NEXT_MOVEMENT',
                               WriteOldMovement(),
                               transitions={succeeded: 'PRINT_DATA_1',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'in_file_name': 'movement_name_path',
                                          'old_file_name_out': 'old_movement_name_path'})

        smach.StateMachine.add('PRINT_DATA_1',
                               PrintUserData1('old_movement_name_path'),
                               transitions={succeeded: succeeded,
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'message1': 'old_movement_name_path'})


    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
