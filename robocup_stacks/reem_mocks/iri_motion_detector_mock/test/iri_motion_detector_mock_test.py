#!/usr/bin/env python
import roslib
roslib.load_manifest('iri_motion_detector_mock')
import rospy
import actionlib

from iri_motion_detector.msg import MotionDetectorActionAction, MotionDetectorActionGoal


def main():
    rospy.init_node('iri_motion_detector_mock_client')

    client = actionlib.SimpleActionClient(
        '/iri_motion_detector', MotionDetectorActionAction)

    print "\nWill wait for server now"
    client.wait_for_server()

    print "Sending goal..."
    goal = MotionDetectorActionGoal()
    client.send_goal(goal)
    print "Goal sent..."
    client.wait_for_result(rospy.Duration.from_sec(5.0))

    result = client.get_result()
    print result

if __name__ == '__main__':
    main()


