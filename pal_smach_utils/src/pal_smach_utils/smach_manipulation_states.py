#!/usr/bin/env python
import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
from smach import StateMachine
from pal_vision_msgs import *
from pal_vision_msgs.msg import *
from geometry_msgs.msg import Pose, Point
import math
import tf
from smach_utils.py import TimeoutMonitor


class SelectTargetPersonState(CBState):
    def __init__(self):
        CBState.__init(self.callback,
                       cb_kwargs={'grasp_waiting_timeout':GRASP_WAITING_TIMEOUT})
    
    @smach.cb_interface(input_keys=[], output_keys=[], outcomes=['done','failed'])
    def callback(selfuserdata, grasp_waiting_timeout):
        """
        Callback for the state WAIT_FOR_GRASPING.
        TODO GRA-HAS-09, GRA-HAS-10 : wait for the person to grasp the robot hand.
        TODO GRA-HAS-08 : check person's height category and pass this information
        to the handshaking state, that shall adapt the motion.
        For the moment, this is a callback state. This might be changed for a more
        convenient one (for example TimeoutMonitor if the information
        concerning hand grasping is published on a topic).
        """
        beginning = rospy.Time.now()
        while ((rospy.Time.now() - beginning) < grasp_waiting_timeout):
            rospy.loginfo('Pretending to wait for the person to grasp robot hand')
            rospy.sleep(rospy.Duration(0.1))
            # if person grasps the hand:
            break # Pretending that the person grasped the robot's hand
        return 'done'
        