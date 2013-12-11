#! /usr/bin/env python

import roslib; roslib.load_manifest('cloth_hanging_tests')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from cloth_hanging.intro_part import SMClothHangingIntroPartStateMachine
#from cloth_hanging.grasp_part import SMClothHangingGraspPartStateMachine
from cloth_hanging.grasp_part import SMClothHangingGraspAndExplanationPartStateMachine
from cloth_hanging.cool_pose_part import SMClothHangingCoolPosePartStateMachine
from cloth_hanging.navigation_part import SMClothHangingNavigationPartStateMachine
from cloth_hanging.hang_cloth_part import SMClothHangingHangPartStateMachine
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine

def main():
    rospy.init_node('cloth_hanging_state_machine')
    
    # Create the top level SMACH state machine
    sm_full = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    # Open the container
    with sm_full:
        sm_intro = SMClothHangingIntroPartStateMachine()
    	#sm_grasp = SMClothHangingGraspPartStateMachine()
    	sm_grasp = SMClothHangingGraspAndExplanationPartStateMachine(False)
    	sm_grasp_retry = SMClothHangingGraspAndExplanationPartStateMachine(True)
    	sm_cool_pose = SMClothHangingCoolPosePartStateMachine()
    	sm_nav = SMClothHangingNavigationPartStateMachine()
    	sm_hang = SMClothHangingHangPartStateMachine()

    	smach.StateMachine.add('INTRO', sm_intro,
                               transitions={succeeded:'GRASP',
                                            aborted:aborted,
                                            preempted:preempted})
    	smach.StateMachine.add('GRASP', sm_grasp,
                               transitions={succeeded:'COOL_POSE',
                               				#'FAILED_VISION':'GRASP_RETRY',
                               				#'FAILED_MOVE_ARM':'GRASP_RETRY',
                               				aborted:'GRASP_RETRY',
                               				preempted:'GRASP_RETRY'})
        smach.StateMachine.add('GRASP_RETRY', sm_grasp_retry,
                               transitions={succeeded:'COOL_POSE',
                                            #'FAILED_VISION':'GRASP_RETRY',
                                            #'FAILED_MOVE_ARM':'GRASP_RETRY',
                                            aborted:'GRASP_RETRY',
                                            preempted:'GRASP_RETRY'})
    	smach.StateMachine.add('COOL_POSE', sm_cool_pose,
                               transitions={succeeded:'NAVIGATION',
                               				aborted:aborted,
                               				preempted:preempted})
    	smach.StateMachine.add('NAVIGATION', sm_nav,
                               transitions={succeeded:'HANGING',
                               				aborted:aborted,
                               				preempted:preempted})
    	smach.StateMachine.add('HANGING', sm_hang,
                               transitions={succeeded:succeeded,
                               				aborted:aborted,
                               				preempted:preempted})
                               				
        # move to exit
        sm_full.userdata.exit_name = 'exit'
        smach.StateMachine.add('MOVE_TO_EXIT',
                                MoveToRoomStateMachine(announcement=None),
                                transitions={succeeded: succeeded,
                                             preempted: preempted,
                                             aborted: 'MOVE_TO_EXIT'},
                                remapping={'room_name': 'exit_name'})
    
        
    sis = smach_ros.IntrospectionServer(
        'cloth_hanging_full_introspection', sm_full, '/SM_ROOT')
    sis.start()

    sm_full.execute()

    rospy.spin()
    sis.stop()
    
    
if __name__ == '__main__':
    main()



