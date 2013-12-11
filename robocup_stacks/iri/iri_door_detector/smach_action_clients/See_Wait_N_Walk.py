#!/usr/bin/env python

import roslib; roslib.load_manifest('iri_door_detector')
import rospy
import smach
import smach_ros
import iri_door_detector.msg
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from arm_navigation_msgs.msg import *
from smach_ros import SimpleActionState

def main():
    rospy.init_node('smach_example_state_machine')

    sm = smach.StateMachine(outcomes=['succeeded','aborted','preempted'])
    with sm:

	#---smach callbacks

	def find_a_door_goal_cb(userdata, goal):
		find_a_door_goal = iri_door_detector.msg.FindADoorGoal()
       		find_a_door_goal.start = 1
       		return find_a_door_goal

	@smach.cb_interface(
		outcomes=['succeeded_closed','succeeded_open','aborted','preempted'])

	def find_a_door_base_result_cb(userdata, status, result):
		#according to actionlib_msgs/GoalStatus.msg, SUCCEEDED = 3
		rospy.loginfo("status code %d" % status)
		rospy.loginfo("\n door state: %s" % result.state + "\n base poses: \n %s" % result.base_poses)
		if status == 3 and result.state == "fully_open": 
			return 'succeeded_open'
		elif status == 3 and result.state == "open_left": 
			return 'succeeded_open'
		elif status == 3 and result.state == "open_right": 
       			return 'succeeded_open'
		elif status == 3 and result.state == "closed_right":
			return 'succeeded_closed'
		elif status == 3 and result.state == "closed_left": 
       			return 'succeeded_closed'
		else:
			return 'aborted'


	#---smach states
	
	#Find a door 
	smach.StateMachine.add('FIND_A_DOOR_BASE',
		SimpleActionState('/iri_door_detector/door_detector_actions/find_a_door',
                		iri_door_detector.msg.FindADoorAction,
                		goal_cb=find_a_door_goal_cb,
				result_slots=['base_poses',
					      'state']),
		transitions={'succeeded':'BASE_POSES',
			     'aborted':'FIND_A_DOOR_BASE'},
                remapping={'base_poses':'user_data_base_poses',
                           'state':'user_data_state'})
	
	#Print goal for move_base
	smach.StateMachine.add('BASE_POSES',
		SimpleActionState('/iri_door_detector/door_detector_actions/find_a_door',
                		iri_door_detector.msg.FindADoorAction,
                		result_cb=find_a_door_base_result_cb),
		transitions={'succeeded_open':'MOVE_BASE_OPEN',
			     'succeeded_closed':'FIND_A_DOOR_BASE',
			     'aborted':'FIND_A_DOOR_BASE'})

	#Move towards the door
	smach.StateMachine.add('MOVE_BASE_OPEN',
		SimpleActionState('move_by_unsafe',
                		MoveBaseAction,
                		goal_slots=['target_pose']),
		transitions={'succeeded':'succeeded',
			     'aborted':'FIND_A_DOOR_BASE'},
		remapping={'target_pose':'user_data_base_poses'})


    # Execute SMACH plan
    outcome = sm.execute()

if __name__ == '__main__':
    main()
