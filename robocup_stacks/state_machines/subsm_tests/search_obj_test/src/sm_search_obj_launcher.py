#! /usr/bin/env python

import roslib; roslib.load_manifest('search_obj_test')
import rospy
import smach
import actionlib

#from smach_ros import SimpleActionState, ServiceState
import smach_ros
from std_msgs import *


from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.grasping.search_objects_behaviour import *
from pal_smach_utils.grasping.arm_and_hand_goals import *


    
class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, input_keys = ['releasing_position'], output_keys = ['releasing_position', 'object_to_search_for'], outcomes=[succeeded])

    def execute(self, userdata):
        print "Dummy state to go to SM_release (generating releasing_position key)!"
        rospy.sleep(5) # in seconds
        userdata.object_to_search_for = "pringles"
        userdata.releasing_position = get_pose_for_arm_in_front()
        return succeeded 

    
def main():
    rospy.init_node('sm_search_obj_test_state_machine')
    
    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add(
            		'dummy_state_generate_position',
            		DummyStateMachine(),
            		transitions = {succeeded: 'SM_search'})
	
	      ## Add some release object position key called: releasing_position
        smach.StateMachine.add(
                    'SM_search',
                    SearchObjectsStateMachine(),
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

