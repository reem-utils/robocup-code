#! /usr/bin/env python
import roslib
roslib.load_manifest('detect_table_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.object_finding_algorithms.detect_furniture_of_zone_sm import DetectFurnitureOfZoneSM
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers


DISTANCE_TRESHOLD = 1.0


def main():
    #raw_input("Press a key when everything's ready!")  # Can be handy for simulation
    rospy.init_node('detect_furniture_zone_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:
        smach.StateMachine.add('START_CONTROLLERS', StartRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: 'FURNITURE_ZONE_DETECT_TEST', aborted: aborted})

        smach.StateMachine.add('FURNITURE_ZONE_DETECT_TEST', DetectFurnitureOfZoneSM(DISTANCE_TRESHOLD),
                               remapping={'out_furniture_pose_list': 'furniture_list',
                                          'out_furniture_orientation_list': 'orient_list',
                                          'out_furniture_name_list': 'name_list'},
                               transitions={succeeded: 'PRINT_FURNITURE_DATA', 'no_furniture': 'PRINT_FURNITURE_DATA'})

        @smach.cb_interface(input_keys=['in_furniture_list', 'in_orient_list', 'in_name_list'], outcomes=[succeeded])
        def print_data(userdata):
            itl = userdata.in_furniture_list
            print 'List of furniture poses detected with a treshold of %f: %s' % (DISTANCE_TRESHOLD, itl)
            print 'Orientation_list', userdata.in_orient_list
            print 'Name list', userdata.in_name_list
            return succeeded

        smach.StateMachine.add('PRINT_FURNITURE_DATA', smach.CBState(print_data, input_keys=['in_furniture_list',
                                                                                             'in_orient_list', 'in_name_list']),
                               transitions={succeeded: 'STOP_CONTROLLERS'},
                               remapping={'in_furniture_list': 'furniture_list',
                                          'in_orient_list': 'orient_list',
                                          'in_name_list': 'name_list'})

        smach.StateMachine.add('STOP_CONTROLLERS', StopRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})

    sis = smach_ros.IntrospectionServer('detect_furniture_of_zone_intros_server', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
