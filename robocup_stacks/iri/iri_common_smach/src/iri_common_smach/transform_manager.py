#!/usr/bin/env python

import roslib; roslib.load_manifest('iri_common_smach')
import rospy
import smach
import smach_ros
import threading
import tf

class TransformManager(threading.Thread):
    """
    Bridge to the ROS tf package. Constantly broadcasts
    all tfs, and retrieves them on demand.
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.tfs = []
        self.listener = tf.TransformListener()

    def transform_pose(self, target_frame, req_pose_st):
        """Attempts to retrieve a transform"""
        attempts = 0
        rate = rospy.Rate(10.0)
        while attempts < 50:
            try:
                pose = self.listener.transformPose(target_frame, req_pose_st)
                return pose
            except (tf.LookupException, tf.ConnectivityException):
                attempts+=1
                rate.sleep()
                continue 
        raise Exception("Attempt to transform %s exceeded attempt limit" % target_frame)
