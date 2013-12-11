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
from smach_utils import *


MAX_STILL_PERSON_DISPLACEMENT = rospy.get_param('/handshaking/maxStillPersonDisplacement', 0.16)


    
    
# Checks if the person in position pose is still during a number of checks provided in constructor
#    outcomes: done, failed, check_again, preempted 
#    input/output_keys : pose -> Position of the still person
class WaitForStillPersonState(TimeoutMonitor):
    def __init__(self, required_still_checks):
        TimeoutMonitor.__init__(self,cb = self.detected_persons_cb, 
                                topic_name='detected_persons', 
                                msg_type=DetectedPerson,
                                last_msg_timeout=rospy.Duration(3.0),
                                io_keys=['pose'],
                                outcomes=['done', 'failed', 'preempted', 'check_again'],
                                provide_self_instance =  True)
        
        self.required_still_checks = required_still_checks
        self.nb_checks = 0  
    @smach.cb_interface(output_keys=['pose'])                   
    def detected_persons_cb(self, userdata, received_msg):
        """
        Checks if the detected person is still for nb_checks 
        """
        pos = received_msg.position3D
        
        # Check that the person is not moving
        last_pos = userdata.pose.position
        
            # person_is_still is True if the position has not changed too much
        person_is_still = (math.fabs(last_pos.x - pos.x) < MAX_STILL_PERSON_DISPLACEMENT and
                             math.fabs(last_pos.y - pos.y) < MAX_STILL_PERSON_DISPLACEMENT)
        rospy.loginfo('The person position has changed (%f, %f) in the XY plane of the robot frame wrt the last detection', math.fabs(last_pos.x - pos.x), math.fabs(last_pos.y - pos.y))
                
        if person_is_still:
            rospy.loginfo('Person is still')
            self.nb_checks += 1
            userdata.pose.position = pos
            if self.nb_checks >= self.required_still_checks:
                self.nb_checks = 0
                return 'done'
            else:
                return 'check_again'
        else:
            rospy.loginfo('Person is NOT still')
            self.nb_checks = 0
            userdata.pose = Pose()
            return 'failed'

# Detect persons within distance_threshold argument provided in constructor
#    outcomes: done, failed, check_again, preempted 
#    output_keys : pose -> Position of the detected person

## Previously named SelectTargetPersonState
class DetectClosePersonState(TimeoutMonitor):
    def __init__(self, distance_threshold):
        
        TimeoutMonitor.__init__(self,cb = self.detect_close_callback, 
                                topic_name='detected_persons', 
                                msg_type=DetectedPerson,
                                output_keys=['pose'],
                                outcomes=['done','failed','preempted','check_again'],
                                provide_self_instance =  True)
        
        self.distance_threshold = distance_threshold
    @smach.cb_interface(output_keys=['pose'])        
    def detect_close_callback(self, userdata, received_msg):
        """
        Callback for the state DetectClosePersonState.
        Checks if the detected person is within the distance_threshold
        """
        if received_msg.confidence < 0.8:
            return 'check_again'
        pos = received_msg.position3D
        dist = distance(Point(), pos)
        close_enough = dist <= self.distance_threshold
    
        rospy.loginfo('Checking distance of person detected at (%f, %f, %f) dist: %f (limit: %f) OK: %d', pos.x, pos.y, pos.z, dist, self.distance_threshold, close_enough)
        current_pos = Pose()
        if close_enough:
            current_pos.position = pos
           # userdata.__setitem__('pose',current_pos)
            userdata.pose = current_pos
            return 'done'
        else:
            userdata.pose = current_pos
            return 'check_again'
    
    
class DetectCloseStillPersonSM(StateMachine):
    def __init__(self, distance_threshold):
        StateMachine.__init__(self, outcomes=['detected','failed','preempted'], input_keys=['sm_distance_threshold'], output_keys=['sm_pose'])
        
        #self.userdata.sm_distance_threshold = 
        #self.userdata.required_still_checks = 
        
        
        with self:
            smach.StateMachine.add('DETECT_CLOSE_PERSON', DetectClosePersonState(distance_threshold),
                                     transitions = {'check_again':'DETECT_CLOSE_PERSON', 'done':'WAIT_FOR_STILL_PERSON', 'failed':'failed', 'preempted':'preempted'},
                                     remapping = {'pose':'sm_pose'})
            
            smach.StateMachine.add('WAIT_FOR_STILL_PERSON', WaitForStillPersonState(2),
                                   transitions = {'check_again':'DETECT_CLOSE_PERSON','done':'detected','failed':'DETECT_CLOSE_PERSON','preempted':'preempted'},
                                   remapping = {'pose':'sm_pose'})
            

class CheckFaceAndDistanceState(TimeoutMonitor):
    def __init__(self):
                TimeoutMonitor.__init__(self,
                                        last_msg_timeout=rospy.Duration(3.0),
                                        topic_name='detected_persons', msg_type=DetectedPerson,
                                        outcomes=['done', 'failed', 'check_again'],
                                        cb=self.callback,
                                        io_keys=['nb_checks','pose'])
                
    def callback(userdata, received_msg):
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
    
    
