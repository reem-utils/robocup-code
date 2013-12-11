#! /usr/bin/env python

import roslib; roslib.load_manifest('cloth_hanging_tests')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from cloth_hanging.hang_cloth_part import SMClothHangingHangPartStateMachine


def main():
    rospy.init_node('hang_test_state_machine')
    
    sm = SMClothHangingHangPartStateMachine()
    
        
    sis = smach_ros.IntrospectionServer(
        'hang_test_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()
    
    
if __name__ == '__main__':
    main()



