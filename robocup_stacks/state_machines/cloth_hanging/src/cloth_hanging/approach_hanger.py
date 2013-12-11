#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

import roslib; roslib.load_manifest('cloth_hanging')
import rospy
import smach
import smach_ros

from smach_ros import SimpleActionState
from smach_ros import ServiceState
from smach import CBState

# generic libraries
import roslib.packages
from actionlib import *

# generic msgs
from actionlib.msg import *
from geometry_msgs.msg import PoseStamped

# pal & reem_at_iri imports
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.topic_reader import TopicReaderState

# iri imports
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

#debugging
from iri_common_smach.utils_msg import build_pose
from geometry_msgs.msg import PoseStamped
#import ipdb


class MoveToHanger(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded','preempted','aborted','approaching'],
                     input_keys=['laser_msg']) #,
                     #output_keys=['ellipses','distances','max_widths','min_widths','sparse','num_objects','arm_position','segmented_pointcloud_sm','plane_coefficients_sm'])
        self.change_threshold = 0.2
        self.distance_offset = 0.3
        self.angle_threshold = 0.4
        
        # publishers
        self.vel_topic = '/cmd_vel'
        self.pose_pub = rospy.Publisher('/debug/grasp_point', PoseStamped, None, False, True)
        self.vel_pub = rospy.Publisher(self.vel_topic, Twist, None, False, True)
        
        # goals
        #self.goal_distance = 0.35
        self.goal_distance = 0.39
        self.goal_angle = 0.05
        self.max_tryouts = 10
        self.current_tryouts = 0
        
        # vars
        self.distance_min = 0.5
        self.distance_max = 4
        self.last_command_velocity = Twist()
    
    def execute(self, userdata):
        rospy.logdebug('Executing MoveToHanger')
        state_result = succeeded
        
        [distance, angle] = self.get_angle_and_position(userdata.laser_msg)
        
        # printing result
        p                 = PoseStamped()
        p.pose            = build_pose(distance*math.cos(angle), distance*math.sin(angle), 0, 0, 1, 0, 0)
        p.header.frame_id = '/base_laser_link'
        p.header.stamp = rospy.Time.now()
        self.pose_pub.publish(p)
        
        command_velocity = Twist()
        
	print "distance is " + str(distance)
        # check distances
        if (distance > self.goal_distance):
            state_result = 'approaching'
            command_velocity.linear.x = 0.4 # move forward
            # decreasing vel
            command_velocity.linear.x = math.pow(math.e, 1 / (-2 * distance)) * 0.4
            
            # check orientation
            if (abs(angle) > self.goal_angle):
                if (angle > 0):
                    command_velocity.angular.z = -0.2 # right?
                    command_velocity.angular.z = - math.pow(math.e, 1 / (-7 * abs(angle)))
                else:
                    command_velocity.angular.z = 0.2 # left?
                    command_velocity.angular.z = math.pow(math.e, 1 / (-7 * abs(angle)))
        elif self.current_tryouts < 2:
            command_velocity = self.last_command_velocity
        
        self.last_command_velocity = command_velocity
        self.vel_pub.publish(command_velocity)
        
        if (state_result == succeeded):
            if self.current_tryouts < self.max_tryouts: # retry
                state_result = 'approaching'
                self.current_tryouts += 1
        else:
            self.current_tryouts = 0
        
        return state_result
    
    def check_new_change(self, laser_msg, init_i, last_i):
        rospy.logdebug( "Change! [" + str(self.distance_max) + "," + str(self.distance_min) + "]")
        # if ((not farther) and smallest object)
        
        check_distance_max = (self.distance_max > laser_msg.ranges[init_i])
        check_distance_min = (self.distance_min < laser_msg.ranges[init_i])
        check_min_object_size = ((last_i - init_i) < self.min_object_size)
        if check_distance_max and check_distance_min and check_min_object_size: 
            # better hanger found
            self.distance_min = laser_msg.ranges[init_i]/2
            self.distance_max = laser_msg.ranges[init_i] + self.distance_offset
            self.min_object_size = last_i - init_i
            rospy.logdebug( "new min " + str(init_i) + " to " + str(last_i))
            return True
        else:
            return False
    
    def get_angle_and_position(self, laser_msg):
        # detection
        angle = laser_msg.angle_min
        last_change_idx=1
        self.min_object_size=100
        detected_object=[-1,-1]
        for i in range(0,len(laser_msg.ranges)):
            if (angle > -self.angle_threshold) and (angle < self.angle_threshold): # in front of the robot
                if (abs(laser_msg.ranges[i] - previous_range) > self.change_threshold): # change found!
                    if self.check_new_change(laser_msg, last_change_idx, i-1):
                        detected_object = [last_change_idx, i-1]
                    last_change_idx = i
                rospy.logdebug( str(angle) + ": " + str(laser_msg.ranges[i]) )
            
            previous_range = laser_msg.ranges[i]
            angle += laser_msg.angle_increment
        
        if (detected_object[0] == -1):
            return [0,0]
        
        winner_min_angle = laser_msg.angle_min + (detected_object[0] * laser_msg.angle_increment)
        winner_max_angle = laser_msg.angle_min + (detected_object[1] * laser_msg.angle_increment)
        rospy.logdebug( "Winner was from " + str(winner_min_angle) + " to " + str(winner_max_angle))
        
        index_mid = int((detected_object[0] + detected_object[1])/2)
        distance = laser_msg.ranges[index_mid]
        angle_mid = (winner_max_angle + winner_min_angle)/2
        rospy.loginfo( "Distance is " + str(distance) + " - Angle is " + str(angle_mid))
        return [distance, angle_mid]
        


class SMClothHangingApproachHangerPartStateMachine(smach.StateMachine):
    """
    Grabs a pointcloud and detects the neck of a cloth, 
    then if it is found, a grasping action is executed
    in that point.

    Required parameters:
    No parameters

    Optional parameters:
    No optional parameters.

    No imput keys.
    No output keys.
    No io_keys.

    """
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:
            
            smach.StateMachine.add('GetLaser', TopicReaderState('/scan_filtered',LaserScan),
                    transitions={succeeded:'MoveToHanger',
                            aborted:aborted},
                    remapping={'message':'laser_msg'})
            
            smach.StateMachine.add('MoveToHanger', 
                    MoveToHanger(),
                    transitions={'approaching':'GetLaser',
                                 succeeded:succeeded,
                                 preempted:preempted,
                                 aborted:aborted})
            
            
            
