#!/usr/bin/env python
import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
from smach import StateMachine
from smach_ros import ServiceState
from pal_vision_msgs import *
from pal_vision_msgs.msg import *
#from std_msgs.msg import Empty
from geometry_msgs.msg import Pose, Point
from std_srvs.srv import Empty
import math
import tf
import dynamic_reconfigure.client
from smach_utils import TimeoutMonitor

class EnablePatrolState(ServiceState):
    def __init__(self, feedback_to_provide=None):
        ServiceState.__init__(self, '/RosPatrolService/start', Empty, output_keys=['action_feedback'])
        self._dyn_reconfigure_client = dynamic_reconfigure.client.Client('/move_base/PalLocalPlanner')
        self.feedback = feedback_to_provide
        
    def execute(self, ud):
        try:
            params = { 'travel_speed_sfl' : 0.45 }
            config = self._dyn_reconfigure_client.update_configuration(params)
        except:
            print 'Error setting travel_speed_sfl parameter'
        if self.feedback != None :
            ud.action_feedback = self.feedback
        return ServiceState.execute(self, ud)

class DisablePatrolState(ServiceState):
    def __init__(self):
        ServiceState.__init__(self, '/RosPatrolService/stop', Empty)        
        
        
class SelectTargetPersonState(TimeoutMonitor):
    def __init__(self):
        TimeoutMonitor.__init__(self,cb = self.callback, 
                                topic_name='detected_persons', 
                                msg_type=DetectedPerson,
                                last_msg_timeout=rospy.Duration(3.0),
				outcomes=['done','failed','preempted','approach'],
                                io_keys=['nb_checks','pose'])
        
    def callback(userdata, received_msg):
        """
        Callback for the state CHECK_DISTANCE.
        Checks if the detected person is within the closeDetectionLimit before
        approaching.
        """
        pos = received_msg.position3D
        dist = distance(Point(), pos)
        close_enough = dist <= CLOSE_DETECTION_LIMIT
    
        rospy.loginfo('Checking distance of person detected at (%f, %f, %f) dist: %f (limit: %f) OK: %d', pos.x, pos.y, pos.z, dist, CLOSE_DETECTION_LIMIT, close_enough)
    
        # Check that the person is not moving
        last_pos = userdata.pose.position
        if userdata.nb_checks == 0:
            # if it's the first in_detection_zone check, person_is_waiting = True
            person_is_waiting = True
        else:
            rospy.loginfo('The person position has changed (%f, %f) in the XY plane of the robot frame wrt the last detection', math.fabs(last_pos.x - pos.x), math.fabs(last_pos.y - pos.y))
            # person_is_waiting is True if the position has not changed too much
            person_is_waiting = (math.fabs(last_pos.x - pos.x) < MAX_STILL_PERSON_DISPLAEMENT and
                                 math.fabs(last_pos.y - pos.y) < MAX_STILL_PERSON_DISPLAEMENT)
        if close_enough and person_is_waiting:
            userdata.nb_checks += 1
            userdata.pose.position = pos
            if userdata.nb_checks == NB_CHECK_FOR_TARGET_MSGS:
                userdata.nb_checks = 0
                if dist <= HANDSHAKING_DISTANCE + 0.2:
                    return 'done'
                else:
                    return 'approach'
            else:
                return 'check_again'
        userdata.pose = Pose()
        userdata.nb_checks = 0
        return 'failed'
    
    

class CheckFaceAndDistanceState(TimeoutMonitor):
    def __init__(self):
                TimeoutMonitor.__init__(self,
                                        last_msg_timeout=rospy.Duration(3.0),
                                        topic_name='detected_persons', msg_type=DetectedPerson,
                                        outcomes=['done', 'failed', 'check_again'],
                                        cb=self.callback,
                                        io_keys=['nb_checks','pose'])
                
    def callback(self, userdata, received_msg):
        """
        Callback for the state CHECK_FACE_AND_DISTANCE.
        For the moment we also check if the person is moving or not. This will
        not be necessary when the WAIT_FOR_GRASPING state will check if the person
        grasps the hand of the robot (TODO GRA-HAS-11).
        """
        looking_at_robot = face_detected(received_msg)
        pos = received_msg.position3D
        dist = distance(Point(), pos)
        close_enough = dist <= CLOSE_DETECTION_LIMIT
        in_detection_zone = (pos.x == 0 or
                            (math.atan(pos.y/pos.x) >= MIN_ANGLE_DETECTION and
                             math.atan(pos.y/pos.x) <= MAX_ANGLE_DETECTION))
    
        rospy.loginfo('The person is located at angle: %f degrees. Valid interval is [%f, %f]', math.atan(pos.y/pos.x)*180/3.1415, MIN_ANGLE_DETECTION*180/3.1415, MAX_ANGLE_DETECTION*180/3.1415)
    
        safe = dist >= MIN_SAFETY_DISTANCE
    
        # Check that the person is not moving
        last_pos = userdata.pose.position
        if userdata.nb_checks == 0:
            # if it's the first in_detection_zone check, person_is_waiting = True
            person_is_waiting = True
        else:
            # person_is_waiting is True if the position has not changed too much
            rospy.loginfo('The person has moved (%f, %f) in the robot frame XY plane (max displacement in each axis: %f)', math.fabs(last_pos.x - pos.x), math.fabs(last_pos.y - pos.y), MAX_STILL_PERSON_DISPLAEMENT)
            person_is_waiting = (math.fabs(last_pos.x - pos.x) < MAX_STILL_PERSON_DISPLAEMENT and
                                 math.fabs(last_pos.y - pos.y) < MAX_STILL_PERSON_DISPLAEMENT)
        if looking_at_robot and close_enough and safe and in_detection_zone and person_is_waiting:
            userdata.nb_checks += 1
            userdata.pose.position = pos
            if userdata.nb_checks == NB_CHECK_FOR_FACE_MSGS:
                userdata.nb_checks = 0
                return 'done'
            else:
                return 'check_again'
        userdata.pose = Pose()
        userdata.nb_checks = 0
        return 'failed'
    
    
