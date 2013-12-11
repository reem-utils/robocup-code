#!/usr/bin/env python
import roslib
roslib.load_manifest('iri_motion_detector_mock')
import rospy
import actionlib

from iri_motion_detector.msg import MotionDetectorActionAction, MotionDetectorActionResult
from random import randrange


class IriMotionDetectorMock():

    #coordinates = {"x": 0, "y": 0, "z": 0}
    result = MotionDetectorActionResult()
    result.pose.pose.position.x = 1  # randrange(10)
    result.pose.pose.position.y = 1  # randrange(10)
    result.pose.pose.position.z = 0  # randrange(10)

    def __init__(self, name):
        self.server = actionlib.SimpleActionServer(name, MotionDetectorActionAction, self.execute, auto_start=False)
        self.server.start()

    def execute(self, goal):
        print "IriMotionDetectorMock Goal received=========="
        print goal
        print "============================================="
        self.result.pose.pose.position.x = 1 # randrange(-5, 5)
        self.result.pose.pose.position.y = 1 # randrange(-5, 5)
        self.result.pose.pose.position.z = 0 # randrange(-5, 5)

        self.server.set_succeeded(self.result)


def iri_motion_detector_mock():
    rospy.init_node("iri_motion_detector_mock")
    server = IriMotionDetectorMock(rospy.get_name())
    print "IriMotionDetectorMock started... waiting for goals"
    rospy.spin()

if __name__ == "__main__":
    iri_motion_detector_mock()
