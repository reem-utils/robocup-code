#! /usr/bin/env python
import roslib
roslib.load_manifest('detect_table_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.object_finding_algorithms.detect_tables_of_zone_sm import DetectTablesOfZoneSM
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers


DISTANCE_TRESHOLD = 1.0


def main():
    #raw_input("Press a key when everything's ready!")  # Can be handy for simulation
    rospy.init_node('detect_tables_zone_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:
        smach.StateMachine.add('START_CONTROLLERS', StartRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: 'TABLES_ZONE_DETECT_TEST', aborted: aborted})

        smach.StateMachine.add('TABLES_ZONE_DETECT_TEST', DetectTablesOfZoneSM(DISTANCE_TRESHOLD),
                               remapping={'out_table_pose_list': 'table_list',
                                          'out_table_orientation_list': 'orient_list'},
                               transitions={succeeded: 'PRINT_TABLE_DATA', 'no_tables': 'PRINT_TABLE_DATA'})

        @smach.cb_interface(input_keys=['in_table_list', 'in_orient_list'], outcomes=[succeeded])
        def print_data(userdata):
            #itl = reduce(lambda acc, x: acc + [x[0]], userdata.in_table_list, [])
            itl = userdata.in_table_list
            print 'List of table poses detected with a treshold of %f: %s' % (DISTANCE_TRESHOLD, itl)
            print 'Orientation_list', userdata.in_orient_list
            print len(itl), len(userdata.in_table_list)
            return succeeded

        smach.StateMachine.add('PRINT_TABLE_DATA', smach.CBState(print_data, input_keys=['in_table_list', 'in_orient_list']),
                               transitions={succeeded: 'STOP_CONTROLLERS'},
                               remapping={'in_table_list': 'table_list',
                                          'in_orient_list': 'orient_list'})

        smach.StateMachine.add('STOP_CONTROLLERS', StopRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})

    sis = smach_ros.IntrospectionServer('detect_tables_of_zone_intros_server', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
