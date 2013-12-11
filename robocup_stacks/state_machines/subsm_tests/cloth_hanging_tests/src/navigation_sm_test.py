#! /usr/bin/env python

import roslib; roslib.load_manifest('cloth_hanging_tests')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from cloth_hanging.navigation_part import SMClothHangingNavigationPartStateMachine


def main():
    rospy.init_node('navigation_test_state_machine')
    
    sm = SMClothHangingNavigationPartStateMachine()
    
        
    sis = smach_ros.IntrospectionServer(
        'navigation_test_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()
    
    
if __name__ == '__main__':
    main()



