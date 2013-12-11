#!/usr/bin/env python
import roslib; roslib.load_manifest('pal_smoke_detection_mock')
import rospy
from std_msgs.msg import Float64
import random

def PercentPublisher():
    percent_publisher = rospy.Publisher('/smoke_detector/smoke_percentage', Float64)
    rospy.init_node('smoke_detector')
    rate = rospy.Rate(1) # Hz
    while not rospy.is_shutdown():
        white_percentage = random.randint(3,15)
        percent_publisher.publish(white_percentage)
        rate.sleep()

if __name__ == '__main__':
    PercentPublisher()
    rospy.spin()