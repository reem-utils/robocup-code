#!/usr/bin/env python
import roslib; roslib.load_manifest('estirabot_apps')
import rospy
import smach
import smach_ros
import threading
import time
import tf
import geometry_msgs
import unittest

from estirabot_common import *
from geometry_msgs.msg import *
from pprint import pprint

import sys

## A sample python unit test
class TestHomogeneousTranform(unittest.TestCase):
    def setUp(self):
        self.pose        = geometry_msgs.msg.Pose()
        self.transform   = geometry_msgs.msg.Transform()
        self.expected    = geometry_msgs.msg.Pose()
        self.pose_result = geometry_msgs.msg.Pose()

    # stupid python ... why foo is needed here?
    def execute(self):
        self.pose_result = homogeneous_product_pose_transform(self.pose, self.transform)
        self.check_pose_equals(self.pose_result, self.expected)

    def check_pose_equals(self, pose1, pose2):
        self.assertAlmostEqual(pose1.orientation.x,pose2.orientation.x)
        self.assertAlmostEqual(pose1.orientation.y,pose2.orientation.y)
        self.assertAlmostEqual(pose1.orientation.z,pose2.orientation.z)
        self.assertAlmostEqual(pose1.orientation.w,pose2.orientation.w)
        self.assertAlmostEqual(pose1.position.x,pose2.position.x)
        self.assertAlmostEqual(pose1.position.y,pose2.position.y)
        self.assertAlmostEqual(pose1.position.z,pose2.position.z)

class TestHomogeneousTranformOnlyRotation(TestHomogeneousTranform):
    def test_run(self):
        self.pose.orientation.x = 0.0
        self.pose.orientation.y = 0.0
        self.pose.orientation.z = 0.0
        self.pose.orientation.w = 1.0
        self.pose.position.x = 5.0
        self.pose.position.y = 4.0
        self.pose.position.z = 3.0

        self.transform.rotation.x = 1.0
        self.transform.rotation.y = 0.0
        self.transform.rotation.z = 0.0
        self.transform.rotation.w = 0.0

        self.expected.position      = self.pose.position
        self.expected.orientation.x = 1.0
        self.expected.orientation.y = 0.0
        self.expected.orientation.z = 0.0
        self.expected.orientation.w = 0.0

        self.execute()

class TestHomogeneousTranformOnlyTranslation(TestHomogeneousTranform):
    def test_run(self):
        self.pose.orientation.x = 0.0
        self.pose.orientation.y = 0.0
        self.pose.orientation.z = 0.0
        self.pose.orientation.w = 1.0
        self.pose.position.x = 5.0
        self.pose.position.y = 4.0
        self.pose.position.z = 3.0

        self.transform.translation.x = 2.0
        self.transform.translation.y = 2.0
        self.transform.translation.z = 2.0
        self.transform.rotation.x = 0.0
        self.transform.rotation.y = 0.0
        self.transform.rotation.z = 0.0
        self.transform.rotation.w = 1.0

        self.expected.orientation   = self.pose.orientation
        self.expected.position.x = 7.0
        self.expected.position.y = 6.0
        self.expected.position.z = 5.0

        self.execute()

if __name__ == '__main__':
    import rostest
    rostest.rosrun('estirabot_apps', 'testHomogeneoustranformOnlyrotation', 
                                      TestHomogeneousTranformOnlyRotation)
    rostest.rosrun('estirabot_apps', 'testHomogeneoustranformonlytranslation', 
                                      TestHomogeneousTranformOnlyTranslation)
