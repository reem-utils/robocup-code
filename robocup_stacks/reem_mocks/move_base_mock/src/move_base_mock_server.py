#! /usr/bin/env python

import roslib; roslib.load_manifest('move_base_mock')
import rospy
import actionlib
import actionlib_msgs
#from move_base_msgs import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback

#from move_base_mock.msg import *


class MoveBaseMockServer:

        def __init__(self, name):
                self.server = actionlib.SimpleActionServer(name, MoveBaseAction, self._execute, False)
                self.server.start()

        def _execute(self, goal):
                #Print on screen the goal given
                rospy.loginfo("Goal is: x=%f y=%f" % (goal.target_pose.pose.position.x, goal.target_pose.pose.position.y))
                rospy.loginfo("Orientation is: x=%f y=%f z=%f w=%f" % (goal.target_pose.pose.orientation.x, goal.target_pose.pose.orientation.y, goal.target_pose.pose.orientation.z, goal.target_pose.pose.orientation.w))

                #Simulate Feedback
                Fb = MoveBaseFeedback()
                Fb.base_position.pose.position.x = 0
                Fb.base_position.pose.position.y = 0

                for i in range(1, 11):
                        print "Moving"+">> "*i
                        self.server.publish_feedback(Fb)
                        rospy.sleep(0.1)

                Fb.base_position.pose.position.x = goal.target_pose.pose.position.x
                Fb.base_position.pose.position.y = goal.target_pose.pose.position.y
                self.server.publish_feedback(Fb)

                Res = MoveBaseResult()
                #Res.observations = []
                #Res.observations = "We are on position: x=%f y=%f" % (goal.target_pose.pose.position.x,goal.target_pose.pose.position.y)
                #Res.success = []
                #Res.success.append(True)
                print "Got there"
                self.server.set_succeeded(result=Res)


if __name__ == '__main__':
    rospy.init_node('move_base_mock')
    print ('Navigation action server started')
    server = MoveBaseMockServer('/move_base')
    server2 = MoveBaseMockServer('/move_by/move_base')
    rospy.spin()
