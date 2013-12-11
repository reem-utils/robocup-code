#! /usr/bin/env python
import roslib
roslib.load_manifest('object_finding_behaviour_tests')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.object_finding_algorithms.ofb_second_approach import OFBSecondApproach
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers
from smach import CBState


TEST_ROOM_NAME = 'bedroom'
TEST_ROOM_NAME2 = 'robocup'
TARGET_OBJ = 'milk'


def main():
    rospy.init_node('object_finding_beh_second_approach_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])
    sm.userdata.room_name = TEST_ROOM_NAME
    sm.userdata.room_name2 = TEST_ROOM_NAME2
    sm.userdata.tg_obj = TARGET_OBJ

    with sm:
        smach.StateMachine.add('START_CONTROLLERS', StartRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: 'OFB_SECOND_APPROACH_TEST2', aborted: aborted})

        '''smach.StateMachine.add('OFB_SECOND_APPROACH_TEST',
                               OFBSecondApproach(target_object_key='target_obj'),
                               transitions={succeeded: 'PRINT_OBJECT_DATA', preempted: 'STOP_CONTROLLERS', aborted: 'STOP_CONTROLLERS'},
                               remapping={'out_object_found': 'obj_data', 'in_room_name': 'room_name',
                                          'out_location_inside_room_name': 'location_name',
                                          'target_obj': 'tg_obj'})

        @smach.cb_interface(input_keys=['obj_data', 'room_name', 'location_name'], outcomes=[succeeded])
        def print_data(userdata):
            print "------------------------------------------"
            print "Object found in %s's %s" % (userdata.room_name, userdata.location_name)
            print "Object name is", userdata.obj_data.name
            print "Object position in /map frame is\n", userdata.obj_data.pose.position
            print "------------------------------------------"
            return succeeded

        smach.StateMachine.add('PRINT_OBJECT_DATA', CBState(print_data, input_keys=['obj_data', 'room_name']),
                               transitions={succeeded: 'OFB_SECOND_APPROACH_TEST2'},
                               remapping={'room_name': 'room_name', 'obj_data': 'obj_data'})'''

        ######################################################################################################
        # Now let's test in the second location
        ######################################################################################################

        smach.StateMachine.add('OFB_SECOND_APPROACH_TEST2',
                               OFBSecondApproach(),
                               transitions={succeeded: 'PRINT_OBJECT_DATA2', preempted: 'STOP_CONTROLLERS', aborted: 'STOP_CONTROLLERS'},
                               remapping={'out_object_found': 'obj_data', 'in_room_name': 'room_name2',
                                          'out_location_inside_room_name': 'location_name'})

        @smach.cb_interface(input_keys=['obj_data', 'room_name2', 'location_name'], outcomes=[succeeded])
        def print_data2(userdata):
            print "------------------------------------------"
            print "Object found in %s's %s" % (userdata.room_name2, userdata.location_name)
            print "Object name is", userdata.obj_data.name
            print "Object position in /map frame is\n", userdata.obj_data.pose.position
            print "------------------------------------------"
            return succeeded

        smach.StateMachine.add('PRINT_OBJECT_DATA2', CBState(print_data2, input_keys=['obj_data', 'room_name2']),
                               transitions={succeeded: 'STOP_CONTROLLERS'},
                               remapping={'room_name2': 'room_name2', 'obj_data': 'obj_data'})

        smach.StateMachine.add('STOP_CONTROLLERS', StopRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})

    sis = smach_ros.IntrospectionServer('ofb_second_approach_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
