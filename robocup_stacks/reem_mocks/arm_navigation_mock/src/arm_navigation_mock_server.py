#! /usr/bin/env python

import roslib; roslib.load_manifest('arm_navigation_mock')
import rospy
import actionlib
import actionlib_msgs
import arm_navigation_msgs

from arm_navigation_msgs.msg import *

class ArmNavigationMockServer:

	def __init__(self, name):
		print 'Inside __init__'
		self.server = actionlib.SimpleActionServer(name, MoveArmAction, self._execute, False)
                print 'Starting __init__ Server'
		self.server.start()

	def _execute(self, goal):
		#Print on Screen Goal given
		print 'Executing...'
		rospy.loginfo( "Goal is : StringPlaner ServiceName: %s" % ( goal.planner_service_name ))

		#Simulating Feedback

		Fb = MoveArmFeedback()
		Fb.state = "-Waiting Movement-"
		Fb.time_to_completion.secs = 0
		Fb.time_to_completion.nsecs = 1000000000
		
		for i in range(1,11):
                        print "Moving Arm to Desired Pos"+">> "*i
			self.server.publish_feedback(Fb)
                        rospy.sleep(0.1)
			Fb.state = "-MOVING-"
			Fb.time_to_completion.nsecs -= 100000000

		Fb.state = "-End of Movement-"
		self.server.publish_feedback(Fb)

		Res = MoveArmResult()
		Res.error_code.val = Res.error_code.SUCCESS
		print "Got there"
                self.server.set_succeeded(result=Res)	

if __name__ == '__main__':
  	print '-----Initialising Node Arm_Navigation_Mock-----'
  	rospy.init_node('arm_navigation_mock')
	print '-----Creating Arm_Navigation_Mock_Server-------'
  	server = ArmNavigationMockServer('move_right_arm_torso') # was move_arm
	print 'Waiting for Someone to sendme a Goal'
  	rospy.spin()
	print 'Closing ArmNavigationNode'
