#! /usr/bin/env python

import roslib; roslib.load_manifest('actionlib_tutorials')
import rospy

import actionlib

from gpsrSoar.msg import *

class gpsrASAction(object):

  def __init__(self, name):
    self._action_name = name
    self._as = actionlib.SimpleActionServer(self._action_name, gpsrSoar.msg.gpsrAction, execute_cb=self.execute_cb)
    self._as.start()
    
  def execute_cb(self, goal):
    action = goal.action 
    loc = goal.location
    it = goal.item
    pers = goal.person
    
    success = False
    for i in xrange(1, goal.order):
      # check that preempt has not been requested by the client
      if self._as.is_preempt_requested():
        rospy.loginfo('%s: Preempted' % self._action_name)
        self._as.set_preempted()
        success = False
        break

      self._feedback.order_id = i
      self._as.publish_feedback(self._feedback)
      
    if success:
      self._result.order_id  = goal.order
      rospy.loginfo('%s: Succeeded' % self._action_name)
      self._as.set_succeeded(self._result)
      
if __name__ == '__main__':
  rospy.init_node('gpsrAS')
  gpsrASAction(rospy.get_name())
  rospy.spin()
