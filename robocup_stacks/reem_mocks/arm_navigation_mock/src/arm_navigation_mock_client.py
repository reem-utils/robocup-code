#! /usr/bin/env python

import roslib; roslib.load_manifest('arm_navigation_mock')
import rospy
import actionlib
import actionlib_msgs
import arm_navigation_msgs


from arm_navigation_msgs.msg import *

def anm_feedback_cb(feedbackdata):
	print "Feedback from arm_navigation_mock received: %s" % (feedbackdata)

def anm_action_done_cb(goalstatus, result):
	if goalstatus == 3:
                print "arm_navigation_mock general goal success."
                if (result.error_code.val == result.error_code.SUCCESS):
                        print "arm_navigation_mock subgoal successful with observations: "# + "".join(result.contacts)#TODO see more in depth
                else:
                        print "arm_navigation_mock subgoal failed with observations: "# + "".join(result.contacts)#TODO see more in depth
        else:
                print "arm_navigation_mock general goal fail."

if __name__ == '__main__':
        rospy.init_node('arm_navigation_mock_client')
        client = actionlib.SimpleActionClient('arm_navigation_mock_server', MoveArmAction)
        client.wait_for_server()

        # Simulate a goal. We take only one element  just to make the server work
        goal = MoveArmGoal()
	goal.planner_service_name = "Mock Movement"
	
        client.send_goal(goal, done_cb=anm_action_done_cb, feedback_cb=anm_feedback_cb)
        client.wait_for_result(rospy.Duration.from_sec(5.0))

