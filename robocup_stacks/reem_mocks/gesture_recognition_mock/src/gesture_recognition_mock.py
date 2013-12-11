#! /usr/bin/env python
import roslib
roslib.load_manifest('gesture_recognition_mock')
import rospy
import random
from pal_vision_msgs.msg import Gesture
from geometry_msgs.msg import Point


GESTURE_LIST = ["Wave", "Wave", "Wave", "Nod", "", ""]


def random_gesture():
    header = rospy.Header()
    header.frame_id = "/gesture_detection_frame"
    point = Point()
    point.x = random.randint(0, 10)
    point.y = random.randint(0, 10)
    point.z = 1.0
    #gesture = Gesture(rospy.Header(), GESTURE_LIST[random.randint(0, len(GESTURE_LIST) - 1)], point)
    gesture = Gesture(header, GESTURE_LIST[random.randint(0, len(GESTURE_LIST) - 1)], point)
    return gesture


def gesture_recog():
    pub = rospy.Publisher('recognized_gestures', Gesture)
    rospy.init_node('gesture_recognition_mock')
    rate = rospy.Rate(2)  # Hz
    while not rospy.is_shutdown():
        message = random_gesture()
        rospy.loginfo("THIS IS THE GESTURE DETECTED ==>\n" + str(message))
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        gesture_recog()
    except rospy.ROSInterruptException:
        pass
