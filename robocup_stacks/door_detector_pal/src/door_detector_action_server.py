#! /usr/bin/env python

import roslib; roslib.load_manifest('door_detector_pal')
import rospy
import actionlib

import geometry_msgs.msg
from geometry_msgs.msg import Pose, PointStamped
import visualization_msgs.msg
from std_msgs.msg import *

import iri_door_detector.msg
import door_detector_pal.msg

class DoorDetectorAction(object):
    # create messages that are used to publish feedback/result
    _feedback = door_detector_pal.msg.DoorDetectorFeedback()
    _result   = door_detector_pal.msg.DoorDetectorResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, door_detector_pal.msg.DoorDetectorAction, execute_cb=self.execute_cb)
        self._as.start()
        self._open_door_counter = 0
        self._closed_door_counter = 0
        self._published_feedback_from_detection = True

    # I can't use one callback for two topics as they have different messages
    def callback_closed_door_handle(self, door_handle):
        rospy.loginfo("callback_closed_door_handle called")
        self._closed_door_counter += 1
        self._published_feedback_from_detection = False

        if door_handle.pose.orientation.w > -1.05 and door_handle.pose.orientation.w < -0.95:  # here we use w for the side of the handle
            self._result.handle_side = "left"
        elif door_handle.pose.orientation.w < 1.05 and door_handle.pose.orientation.w > 0.95:
            self._result.handle_side = "right"
        else:
            self._result.handle_side = "error finding side of handle, w is: " + str(door_handle.pose.orientation.w)

        self._result.door_status = "closed"
        self._result.door_handle.pose.position = door_handle.pose.position
        self._result.door_handle.header.frame_id = "/head_mount_xtion_rgb_optical_frame"

        # INSERT THE DATA MAGICALLY!
        # side of the handle "left" or "right"
        # string handle_side
        # # status of the door "open" or "closed"
        # string door_status
        # # if it's closed and we have the position of the handle
        # geometry_msgs/PoseStamped door_handle
        # # if it's open and we have the position of the door centroid
        # geometry_msgs/PoseStamped door_position

    def callback_closed_door_orientation(self, closed_door_marker):
            rospy.loginfo("closed door marker:\n" + str(closed_door_marker))
            rospy.loginfo("self._result.door_handle:\n" + str(self._result.door_handle))
            self._result.door_handle.pose.orientation = closed_door_marker.pose.orientation

    def callback_open_door_centroid(self, door_centroid):
            rospy.loginfo("callback_open_door_centroid called")
            self._open_door_counter += 1
            self._published_feedback_from_detection = False

            # /*Initilalize door state (0 = fully open door,
            # -2, -1 = open left, 1, 2 = open right)*/
            if door_centroid.pose.orientation.w == 0:  # here we use w for the side of the door rotation axis
                self._result.handle_side = "fully open"
            elif door_centroid.pose.orientation.w <= -1:
                self._result.handle_side = "open left hinge"
            elif door_centroid.pose.orientation.w >= 1:
                self._result.handle_side = "open right hinge"
            else:
                self._result.handle_side = "error finding side of door hinge, w is: " + str(door_centroid.pose.orientation.w)

            self._result.door_status = "open"
            self._result.door_position.pose.position = door_centroid.pose.position
            self._result.door_position.header.frame_id = "/head_mount_xtion_rgb_optical_frame"

    def callback_open_door_orientation(self, open_door_marker):
            rospy.loginfo("open door marker:\n" + str(open_door_marker))
            rospy.loginfo("self._result.door_position:\n" + str(self._result.door_position))
            self._result.door_position.pose.orientation = open_door_marker.pose.orientation

    def execute_cb(self, goal):
        # Start variables
        self._feedback.comment = "Starting to search door"

        # Publish some info
        rospy.loginfo("Starting to search door")

        # Subscribing to topics
        # Can't use message filters because all the messages must have headers with timestamp
        door_handle_sub = rospy.Subscriber("/iri_door_detector/closed_door_detector/door_handle", geometry_msgs.msg.PoseStamped, callback=self.callback_closed_door_handle)
        door_centroid_sub = rospy.Subscriber("/iri_door_detector/open_door_detector/door_centroid", geometry_msgs.msg.PoseStamped, callback=self.callback_open_door_centroid)

        rospy.loginfo("Subscribed to /iri_door_detector/closed_door_detector/door_handle and /iri_door_detector/open_door_detector/door_centroid")

        closed_door_orientation_sub = rospy.Subscriber("/iri_door_detector/door_cloud/closed_door_marker", visualization_msgs.msg.Marker, callback=self.callback_closed_door_orientation)
        open_door_orientation_sub = rospy.Subscriber("/iri_door_detector/door_cloud/open_door_marker", visualization_msgs.msg.Marker, callback=self.callback_open_door_orientation)

        rospy.loginfo("Subscribed to /iri_door_detector/door_cloud/closed_door_marker and /iri_door_detector/door_cloud/open_door_marker")

        # Set door detectors to ON
        pub = rospy.Publisher('/iri_door_detector/door_detector_actions/door_action_start', std_msgs.msg.Int8, latch=True)  # I must latch or the listener sometimes loses topic pubs
        pub.publish(std_msgs.msg.Int8(1))  # Maybe check if it was already running...

        rospy.loginfo("Published on /iri_door_detector/door_detector_actions/door_action_start")

        # publish the feedback
        self._as.publish_feedback(self._feedback)

        while self._open_door_counter < goal.votation and self._closed_door_counter < goal.votation:
            if self._as.is_preempt_requested():
                # Cancelling goal feedback
                self._feedback.comment = "Cancelling goal..."
                self._as.publish_feedback(self._feedback)
                self._as.set_aborted()
                break

            # continue doing stuff until we get the votation
            if not self._published_feedback_from_detection:
                self._feedback.comment = "Open door count: " + str(self._open_door_counter) + "/" + str(goal.votation) + "\nClosed door count: " + str(self._closed_door_counter) + "/" + str(goal.votation)
                rospy.loginfo(self._feedback)
                self._as.publish_feedback(self._feedback)
                self._published_feedback_from_detection = True
            rospy.sleep(0.5)  # checking at 2Hz

        pub = rospy.Publisher('/iri_door_detector/door_detector_actions/door_action_start', std_msgs.msg.Int8, latch=True)  # I must latch or the listener sometimes loses topic pubs
        pub.publish(std_msgs.msg.Int8(0))  # Maybe check if it was already running...

        # Publishing last feedback
        self._feedback.comment = "Open door count: " + str(self._open_door_counter) + "/" + str(goal.votation) + "\nClosed door count: " + str(self._closed_door_counter) + "/" + str(goal.votation)
        rospy.loginfo(self._feedback)
        self._as.publish_feedback(self._feedback)

        # Unregistering from topics
        door_handle_sub.unregister()
        closed_door_orientation_sub.unregister()
        door_centroid_sub.unregister()
        open_door_orientation_sub.unregister()

        door_result_pub = rospy.Publisher('/iri_door_detector/door_detector_action_server/door_result', PointStamped, latch=True)

        # Cleaning up
        if self._open_door_counter >= goal.votation:  # we only want to give the data that we are sure about
            self._result.door_handle.pose = Pose()
            door_result_pub.publish(PointStamped(header=Header(stamp=rospy.Time().now(), frame_id='head_mount_xtion_rgb_optical_frame'), point=self._result.door_position.pose.position))  # Maybe check if it was already running...
        else:
            self._result.door_position.pose = Pose()
            door_result_pub.publish(PointStamped(header=Header(stamp=rospy.Time().now(), frame_id='head_mount_xtion_rgb_optical_frame'), point=self._result.door_handle.pose.position))  # Maybe check if it was already running...

        self._open_door_counter = 0
        self._closed_door_counter = 0

        # When we are finished send results
        rospy.loginfo("Succeeded, Result:\n" + str(self._result))
        self._as.set_succeeded(self._result)


if __name__ == '__main__':
    rospy.init_node('door_detector_action_server')
    DoorDetectorAction(rospy.get_name())
    rospy.spin()
