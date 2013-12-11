# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:56:47 2012

@author: ricardo
"""

import roslib
#roslib.load_manifest('alive_engine')
roslib.load_manifest('dancing_reem')
import rospy
import smach
import actionlib
from std_srvs.srv import Empty, EmptyResponse
from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction
from safety_zone_handling import SafetyManager


class SendMov(smach.State):
    ''' we use this implementation of action client instead of the SimpleActionstate because this one allows interruption and better control
    '''
    def __init__(self):
        smach.State.__init__(self,
                            input_keys=['file_name', 'repeat'],
                            outcomes=['succeeded', 'preempted', 'aborted'])

        """ Creates the service that receives requests to start/stop the movement """
	self.stop_srv = rospy.Service('/dancing_engine/stop', Empty, self.movements_not_allowed)
        self.start_srv = rospy.Service('/dancing_engine/start', Empty, self.movements_allowed)

        """ Creates the connection to the service that will execute the movements """
        self.client = actionlib.SimpleActionClient('/motion_manager', MotionManagerAction)
        self.safetyManager = SafetyManager()
        rospy.loginfo('Waiting for motion manager server')
        self.client.wait_for_server()
        self.goal = MotionManagerGoal()
        #self.goal.plan = rospy.get_param('/alive_engine/validateTrajectory')
        self.goal.plan = False
        self.movs_allowed = True  # by default, the alive engine starts stopped. It needs to be activated externally through a service call (/dancing_engine/start)

    def movements_not_allowed(self, req):

        # cancelling any previous goal
        self.client.cancel_goal()
        self.movs_allowed = False
        return EmptyResponse()

    def movements_allowed(self, req):
        self.movs_allowed = True
        return EmptyResponse()

    def execute(self, userdata):

        # if the movements are not allowed, then we not send movements to the server
        if self.movs_allowed == True:
            rospy.loginfo('Sending movement file %s' % userdata.file_name)

            # sending the goal
            self.goal.filename = userdata.file_name
            self.goal.checkSafety = False
            self.goal.repeat = userdata.repeat
            self.goal.priority = 0 #Reem alive priority
            self.goal.queueTimeout = 0 #Don't queue movements, just execute
            # cancelling any previous goal
            self.client.cancel_goal() #NOTE: removing cancel of goal because the motion manager is already doing it # NOTE2: not any longer
            self.client.send_goal(self.goal)
        else:
            rospy.logerr('Alive started but not active. Your movement' + userdata.file_name + ' will not be executed')

        return 'succeeded'
