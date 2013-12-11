#! /usr/bin/env python

import roslib; roslib.load_manifest('cloth_hanging_tests')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from cloth_hanging.cool_pose_part import SMClothHangingCoolPosePartStateMachine


def main():
    rospy.init_node('navigation_pose_test_state_machine')
    
    sm = SMClothHangingCoolPosePartStateMachine()
    
        
    sis = smach_ros.IntrospectionServer(
        'navigation_pose_test_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()
    
    
if __name__ == '__main__':
    main()



