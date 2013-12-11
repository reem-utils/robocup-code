#!/usr/bin/env python
import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
from smach import StateMachine
from smach_ros import ServiceState
from pal_vision_msgs import *
from pal_behaviour_msgs.srv import *
from pal_behaviour_msgs.msg import BehaviourArgument 
#from std_msgs.msg import Empty
from geometry_msgs.msg import Pose, Point
from std_srvs.srv import Empty
import math
import tf
from smach_utils import TimeoutMonitor

class PresentToPersonState(ServiceState):
    def __init__(self):
        event = BehaviourEventRequest()
        event.name = 'presentToPerson'
        
        #event.name = 'say'
        #arg = BehaviourArgument()
        #arg.key = 'text'
        #arg.value = 'Hello World'
        #event.arguments = [arg,]
        ServiceState.__init__(self, '/behaviour', BehaviourEvent, request = event)

