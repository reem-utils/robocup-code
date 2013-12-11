#! /usr/bin/env python

import roslib; roslib.load_manifest('tabletop_grasping_node_test')
import rospy
import smach
import smach_ros
import actionlib


from smach_ros import SimpleActionState, ServiceState
#from std_msgs import *
from pal_smach_utils.utils.global_common import *
from reem_tabletop_manipulation_launch.msg import GraspTargetAction, GraspTargetGoal
from actionlib_msgs.msg import GoalStatus


class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys = ['object_to_search_for'])

    def execute(self, userdata):
        print "Dummy state... (waiting 1s to initiate)"
        print "[         (  *  )(  *  )        ]"
        rospy.sleep(1) # in seconds
        rospy.loginfo("GO FOR THE GRASPINNNNGGG")
        userdata.object_to_search_for = ""
        return succeeded 



def main():
    rospy.init_node('tabletop_grasping_node_test_state_machine')
    
    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        # Using this state to wait and set userdata
    	smach.StateMachine.add(
    		'dummy_state',
    		DummyStateMachine(),
    		transitions = {succeeded: 'Grasp_target_action'})

    	def grasp_target_goal_cb(userdata, old_goal):
			grasp_target_goal = GraspTargetGoal()
			rospy.loginfo("userdata.keys(): " + str(userdata.keys()))
			grasp_target_goal.onlyPerception = False
			grasp_target_goal.appearanceID = userdata.object_to_search_for  # "coke"
			grasp_target_goal.databaseID = -1 # 18983 juice #18984   # coke is 18744, < 0 numbers are... DONT SEARCH ANYTHING, GET SOMETHING MA FREN
			return grasp_target_goal

        def grasp_target_result_cb(userdata, status, result):
        	rospy.loginfo("Result of the cb: userdata.keys(): " + str(userdata.keys()))
        	rospy.loginfo("Result of the cb: result: " + str(result) )
        	if status == GoalStatus.SUCCEEDED:
        		return succeeded
        	if status == GoalStatus.ABORTED:
        		return aborted
        	#return 'my_outcome'

        smach.StateMachine.add(
            'Grasp_target_action',
            SimpleActionState(
                'tabletop_grasping_node',
                GraspTargetAction,
                goal_cb = grasp_target_goal_cb,
                result_cb = grasp_target_result_cb,
                input_keys = ['object_to_search_for']),
            transitions = {succeeded: succeeded, aborted: aborted})  
	
	      
   
        # If we get here, profit $$$$$

        
    sis = smach_ros.IntrospectionServer(
        'tabletop_grasping_node_test_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()
    
    
if __name__ == '__main__':
    main()



