#!/usr/bin/env python

import roslib; roslib.load_manifest('iri_common_smach')
import rospy
import smach
import smach_ros

import tf
from geometry_msgs.msg import PoseStamped
from pprint import pprint 

class GetPoseStampedFromFrames(smach.State):
    """
    Get the transformation between two frames and return it in a PoseStamped form
    """
    def __init__(self,tf_listener):
        smach.State.__init__(self, outcomes    = ['success','fail'],
                                   input_keys  = ['src_frame','dest_frame'],
                                   output_keys = ['pose_st'])
        self.tf_listener = tf_listener

    def execute(self, userdata):
        try:
            self.tf_listener.waitForTransform(userdata.src_frame, userdata.dest_frame, rospy.Time(), rospy.Duration(1.0))
            (trans,rot) = self.tf_listener.lookupTransform(userdata.src_frame, userdata.dest_frame, rospy.Time())
        except (tf.LookupException, tf.ConnectivityException):
            rospy.logerror("Unable to get the trasform between two poses");
            return 'fail'

        tf_tmp                  = PoseStamped()
        tf_tmp.header.frame_id  = userdata.src_frame
        tf_tmp.header.stamp     = rospy.Time()
        tf_tmp.pose.position.x  = trans[0]
        tf_tmp.pose.position.y  = trans[1]
        tf_tmp.pose.position.z  = trans[2]
        tf_tmp.pose.orientation.x = rot[0]
        tf_tmp.pose.orientation.y = rot[1]
        tf_tmp.pose.orientation.z = rot[2]
        tf_tmp.pose.orientation.w = rot[3]

        pprint("POSE FROM FRAMES")
        pprint(tf_tmp)
        userdata.pose_st = tf_tmp;
        return 'success'
