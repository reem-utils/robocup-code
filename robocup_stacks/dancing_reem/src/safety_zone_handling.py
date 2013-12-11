# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:39:16 2012

@author: ricardo
"""
import roslib
# This is commented because we dodnt have this code.
#roslib.load_manifest('alive_engine')
roslib.load_manifest('dancing_reem')
import rospy
from pal_navigation_msgs.srv import SafetyZone


class SafetyManager():

    def __init__(self):

        self.SAFETY_ZONE_SERVICE = '/safety_zone'

        self.startSafetyClient()

    def startSafetyClient(self):

        # Checks that service is up
        #rospy.loginfo("Waiting for safety_zone service to start")
        rospy.loginfo("NOT WAITING FRO SAFETY ZONE")
        #rospy.wait_for_service(self.SAFETY_ZONE_SERVICE)

        # generate the persitent connection
        try:
            self.SAFETY_SUBS = rospy.ServiceProxy(self.SAFETY_ZONE_SERVICE, SafetyZone, True)
        except rospy.ServiceException, e:
            rospy.logerr('Service connection failed: %s' % e)

    def callSafetyZone(self):

        try:
            result = self.SAFETY_SUBS(2.0, 120.0, 120.0)
        except rospy.ServiceException, e:
            rospy.logerr('Service call failed: %s' % e)
            return False

        if result.leftSafe == True and result.rightSafe == True:
            return True

        return False
