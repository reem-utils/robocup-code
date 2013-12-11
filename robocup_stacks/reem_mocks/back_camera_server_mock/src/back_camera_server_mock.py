#!/usr/bin/env python
import roslib; roslib.load_manifest('back_camera_server_mock')
import rospy
from pal_vision_msgs.srv import FollowMeStart, FollowMeStop, FollowMeStartResponse, FollowMeStopResponse
from pal_vision_msgs.msg import FollowMeResponse
from std_msgs.msg import Header

start_publishing = False
ISTHERE = True


def handle_timing(time):
    global start_publishing
    start_publishing = True
    print "Server started \n"
    return FollowMeStartResponse()


def stop_handler(req):
    global start_publishing
    start_publishing = False
    print "Server stopped \n"
    return FollowMeStopResponse()


def back_camera_server():
    rospy.init_node("back_camera_server_mock")
    print "Running!!!! \n"
    is_there_person = rospy.Service('/followMeServer/start', FollowMeStart, handle_timing)
    stop = rospy.Service('/followMeServer/stop', FollowMeStop, stop_handler)
    rate = rospy.Rate(1)
    print "Before the loop \n"
    while not rospy.is_shutdown():
        global start_publishing
        if start_publishing:
            ISTHERE = input('Is there anyone behind? (True or False): ')
            back_camera_publisher = rospy.Publisher('/followMe/result', FollowMeResponse)
            # print back_camera_publisher
            result = FollowMeResponse(rospy.Header(), ISTHERE)
            back_camera_publisher.publish(result)
            rate.sleep()
    # Publish followMe/result

if __name__ == "__main__":
    back_camera_server()
