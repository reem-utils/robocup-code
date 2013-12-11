#! /usr/bin/env python
import roslib; roslib.load_manifest('face_recognition_mock')
import rospy
import actionlib

from face_recognition.msg import *

def main():
    rospy.init_node('face_recognition_client')

    client = actionlib.SimpleActionClient(
        'face_recognition', FaceRecognitionAction)
    client.wait_for_server()

    goal = FaceRecognitionGoal()
    client.send_goal(goal)
    client.wait_for_result(rospy.Duration.from_sec(5.0))
    
    result = client.get_result()
    print result

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
