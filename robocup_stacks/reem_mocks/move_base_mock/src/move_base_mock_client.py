#! /usr/bin/env python

import roslib; roslib.load_manifest('move_base_mock')
import rospy
import actionlib
import actionlib_msgs
import move_base_msgs

from move_base_mock.msg import *

def mbm_feedback_cb(feedbackdata):
        print "Feedback from move_base_mock received: %s" % (feedbackdata)

def mbm_action_done_cb(goalstatus, result):
        if goalstatus == 3:
                print "move_base_mock general goal success."
                if result.success[0]:
            		print "move_base_mock subgoal successful with observations: " + "".join(result.observations)
                else:
                        print "move_base_mock subgoal failed with observations: " + "".join(result.observations)
        else:
                print "move_base_mock general goal fail."


if __name__ == '__main__':
        rospy.init_node('move_base_mock_client')
        client = actionlib.SimpleActionClient('move_base_mock_server', MoveBase_mockAction)
        client.wait_for_server()

        # Simulate a goal
	goal = MoveBase_mockGoal()
        goal.target_pose.pose.position.x = 10
        goal.target_pose.pose.position.y = 10


        client.send_goal(goal, done_cb=mbm_action_done_cb, feedback_cb=mbm_feedback_cb)
        client.wait_for_result(rospy.Duration.from_sec(5.0))

                                   
