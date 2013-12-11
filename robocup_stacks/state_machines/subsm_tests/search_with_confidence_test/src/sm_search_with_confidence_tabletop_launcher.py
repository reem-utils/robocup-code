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
from pal_smach_utils.grasping.search_object_with_confidence import *


    
class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, input_keys = ['releasing_position'], output_keys = ['releasing_position', 'object_to_search_for'], outcomes=[succeeded])

    def execute(self, userdata):
        print "Dummy state to wait 5s"
        rospy.sleep(5) # in seconds
        userdata.object_to_search_for =  ""
        #userdata.releasing_position = get_pose_for_arm_in_front()
        return succeeded 

    
def main():
    rospy.init_node('sm_search_with_confidence_test_state_machine')
    
    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add(
            		'dummy_state_wait1s',
            		DummyStateMachine(),
            		transitions = {succeeded: 'SM_search_with_confidence_tabletop'})
	
	      ## Add some release object position key called: releasing_position
        smach.StateMachine.add(
                    'SM_search_with_confidence_tabletop',
                    SearchObjectWithConfidenceStateMachine(),
                    transitions = {succeeded: succeeded, aborted: aborted})
        
                    
         # NOT USING ANYTHING  MORE

        
    sis = smach_ros.IntrospectionServer(
        'sm_search_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()
    
    
if __name__ == '__main__':
    main()

