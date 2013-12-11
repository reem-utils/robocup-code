#! /usr/bin/env python

import roslib; roslib.load_manifest('search_with_confidence_test')
import rospy
import smach
import actionlib

#from smach_ros import SimpleActionState, ServiceState
import smach_ros
from std_msgs import *


from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.grasping.arm_and_hand_goals import *
#from pal_smach_utils.grasping.search_object_with_confidence import *
from pal_smach_utils.grasping.grasp_first_recognized_object import *


    
class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, input_keys = ['releasing_position'], output_keys = ['releasing_position', 'object_to_search_for'], outcomes=[succeeded])

    def execute(self, userdata):
        print "Dummy state to wait 2s"
        rospy.sleep(2) # in seconds
        userdata.object_to_search_for =  ""
        print "will search for whatever"
        #userdata.releasing_position = get_pose_for_arm_in_front()
        return succeeded 

    
def main():
    rospy.init_node('sm_grasp_first_recognized_object_test_state_machine')
    
    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add(
            		'dummy_state_wait5s',
            		DummyStateMachine(),
            		transitions = {succeeded: 'SM_grasp_first_recognized_object'})
	
	      ## Add some release object position key called: releasing_position
        smach.StateMachine.add(
                    'SM_grasp_first_recognized_object',
                    GraspFirstRecognizedObjectStateMachine(),
                    transitions = {succeeded: succeeded, aborted: aborted})
        
                    
         # NOT USING ANYTHING  MORE

        
    sis = smach_ros.IntrospectionServer(
        'sm_grasp_first_recognized_object_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()
    
    
if __name__ == '__main__':
    main()

