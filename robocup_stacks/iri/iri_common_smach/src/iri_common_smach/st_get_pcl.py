#!/usr/bin/env python

import roslib; roslib.load_manifest('iri_common_smach')
import rospy
import smach
import smach_ros
import threading
import time

from sensor_msgs.msg import PointCloud2

class GetPCL(smach.State):
    """
    Custom smach for reading a PCL from a topic
    """
    def __init__(self, pcl_topic = ''):
        smach.State.__init__(self, outcomes=['success','fail'],
                                   input_keys  = ['pcl_topic'],
                                   output_keys = ['pcl_RGB'])

        self._last_pcl_RGB     = None
        self._pcl_RGB_recieved = False
        self.mutex             = threading.Lock()
        self.subscriber        = None
        if (pcl_topic != ''):
            self.subscriber        = rospy.Subscriber(pcl_topic, PointCloud2,
                                                      self.recieve_pcl_callback)

    def recieve_pcl_callback(self, data):
        self.mutex.acquire()
        self._last_pcl_RGB     = data
        self._pcl_RGB_recieved = True
        self.mutex.release()

    def execute(self, userdata):
        # Check if constructor was used
        if (self.subscriber == None):
            self.subscriber = rospy.Subscriber(userdata.pcl_topic, PointCloud2,
                                               self.recieve_pcl_callback)
        # wait for a maximum of 5 seconds
        for i in range(0, 50):
            self.mutex.acquire()
            if self._pcl_RGB_recieved:
                # Ok PCL recieved
                userdata.pcl_RGB = self._last_pcl_RGB;
                self.mutex.release()
                return 'success'
            self.mutex.release()

            time.sleep(.1)

        # we didn't get PCL in the 5 sec
        rospy.loginfo("Waiting more than 5 seconds for PCL")
        return 'fail'

