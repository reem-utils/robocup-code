#! /usr/bin/env python
import roslib
roslib.load_manifest('detect_table_test')
import rospy
import smach
import smach_ros

from geometry_msgs.msg import PoseStamped
from pal_smach_utils.object_finding_algorithms.detect_furniture import DetectFurniture
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers

DIST_TO_TABLE = 0.2


def main():
    rospy.init_node('detect_furniture_test')
    publisher = rospy.Publisher('/detect_furniture_pose', PoseStamped)

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:
        smach.StateMachine.add('START_CONTROLLERS', StartRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: 'FURNITURE_DETECT_TEST', aborted: aborted})

        smach.StateMachine.add('FURNITURE_DETECT_TEST', DetectFurniture(distance_treshold=0.65),
                               remapping={'furniture_info': 'furniture_data'},
                               transitions={succeeded: 'PRINT_FURNITURE_DATA', 'no_furniture': 'FURNITURE_DETECT_TEST'})

        @smach.cb_interface(input_keys=['furn_data'], outcomes=[succeeded])
        def print_data(userdata):
            res = userdata.furn_data
            i = 0  # Result to print
            print res

            ps = res[i][1]

            raw_input('Press a key when ready to publish the data.\n')  # To wait for publish
            publisher.publish(ps)
            print 'Detected %d furniture' % len(res)
            return succeeded
        smach.StateMachine.add('PRINT_FURNITURE_DATA', smach.CBState(print_data, input_keys=['furn_data']),
                               transitions={succeeded: 'STOP_CONTROLLERS'},
                               remapping={'furn_data': 'furniture_data'})

        smach.StateMachine.add('STOP_CONTROLLERS', StopRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})

    sis = smach_ros.IntrospectionServer(
        'detect_furniture_intros_server', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
