#!/usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Pose
from std_msgs.msg import ColorRGBA

import random

from pal_smach_utils.utils.debug import debugPrint


marker_id = 0
markers_length = 1
MARKER_LIFETIME_DURATION = 0


class PublishMarker(smach.State):
    """
    @userdata.in_pose: A geometry_msgs.msg Pose() object.
    Publishes a basic cilinder marker with fixed dimensions,
    in the input position given.
    """
    def __init__(self, scale=0.2):
        smach.State.__init__(self, input_keys=["in_pose"], outcomes=[succeeded])
        self.publisher = rospy.Publisher("/visualization_marker", Marker)
        self.ellipse = Marker()
        self.ellipse.header.frame_id = "/base_link"
        self.ellipse.header.stamp = rospy.Time.now()
        self.ellipse.type = Marker.CYLINDER
        self.action = Marker.ADD
        self.ellipse.pose.orientation.x = 0
        self.ellipse.pose.orientation.y = 0
        self.ellipse.pose.orientation.z = 0
        self.ellipse.pose.orientation.w = 1
        self.ellipse.scale.x = scale
        self.ellipse.scale.y = scale
        self.ellipse.scale.z = scale

    def execute(self, userdata):
        if (not isinstance(userdata.in_pose, Pose)):
            raise ValueError("ERROR: in_pose need be a Pose() object, not '%s'." % type(userdata.in_pose))

        debugPrint("Will publish marker in: " + str(userdata.in_pose), 4)

        self.ellipse.pose.position.x = userdata.in_pose.position.x
        self.ellipse.pose.position.y = userdata.in_pose.position.y
        self.ellipse.pose.position.z = userdata.in_pose.position.z
        self.ellipse.color.a = 1.0
        self.ellipse.color.r = 255
        self.ellipse.color.g = 0
        self.ellipse.color.b = 0
        self.publisher.publish(self.ellipse)
        debugPrint("Marker published...", 4)
        return succeeded


class PublishMarkerWithName(smach.State):
    """
    @userdata.in_pose: A geometry_msgs.msg Pose() object.
    Publishes a basic cilinder marker with fixed dimensions,
    in the input position given.
    You can input the marker_name and the scale
    """
    def __init__(self, scale=0.2, marker_name="/visualization_marker"):
        smach.State.__init__(self, input_keys=["in_pose"], outcomes=[succeeded])

        self.publisher = rospy.Publisher(marker_name, Marker)
        self._scale = scale

    def execute(self, userdata):
        if (not isinstance(userdata.in_pose, Pose)):
            raise ValueError("ERROR: in_pose need be a Pose() object, not '%s'." % type(userdata.in_pose))

        debugPrint("Will publish marker in: " + str(userdata.in_pose), 4)

        self.marker = Marker()
        self.marker.header.frame_id = "/base_link"
        self.marker.ns = "markers_namespace"
        self.marker.id = marker_id

        global marker_id
        self.marker.id = marker_id
        #set marker_id for the next call
        marker_id = marker_id + 1
        if (marker_id >= markers_length):
            marker_id = 0

        self.marker.header.stamp = rospy.Time.now()
        self.marker.type = Marker.CYLINDER
        self.marker.action = Marker.ADD
        self.marker.pose.orientation.x = 0.0
        self.marker.pose.orientation.y = 0.0
        self.marker.pose.orientation.z = 0.0
        self.marker.pose.orientation.w = 1.0
        self.marker.scale.x = self._scale
        self.marker.scale.y = self._scale
        self.marker.scale.z = self._scale
        self.marker.pose.position.x = userdata.in_pose.position.x
        self.marker.pose.position.y = userdata.in_pose.position.y
        self.marker.pose.position.z = userdata.in_pose.position.z
        self.marker.color.a = 1.0
        self.marker.color.r = 1.0
        self.marker.color.g = random.random()
        self.marker.color.b = 0.0
        self.marker.lifetime = rospy.Duration(MARKER_LIFETIME_DURATION)
        self.publisher.publish(self.marker)
        debugPrint("Marker published...", 4)
        return succeeded


def SetMarkerType(marker_type):
    """
    Sets the marker type given.
    If Marker Nost supported returns assert error.
    Supported ARROW, CUBE, SPHERE AND CYLINDER.
    """

    if marker_type == 'ARROW':
        return Marker.ARROW
    if marker_type == 'CUBE':
        return Marker.CUBE
    if marker_type == 'SPHERE':
        return Marker.SPHERE
    if marker_type == 'CYLINDER':
        return Marker.CYLINDER
    assert (marker_type != 'ARROW' and marker_type != 'CUBE' and marker_type != 'SPHERE' and marker_type != 'CYLINDER'), "Marker Type not supported, changed to default CYLINDER type"
    return Marker.CYLINDER


def SetColour(colour):

    rgb_colour = ColorRGBA()
    rgb_colour.a = 1.0

    if colour == "RED":
        rgb_colour.r = 1.0
        rgb_colour.g = 0.0
        rgb_colour.b = 0.0
        return rgb_colour
    if colour == "GREEN":
        rgb_colour.r = 0.0
        rgb_colour.g = 1.0
        rgb_colour.b = 0.0
        return rgb_colour
    if colour == "BLUE":
        rgb_colour.r = 0.0
        rgb_colour.g = 0.0
        rgb_colour.b = 1.0
        return rgb_colour
    if colour == "RANDOM":
        rgb_colour.r = random.random()
        rgb_colour.g = random.random()
        rgb_colour.b = random.random()
        return rgb_colour

    assert (), "COLOUR not supported, changed to default RED type"
    rgb_colour.r = 1.0
    rgb_colour.g = 0.0
    rgb_colour.b = 0.0
    return rgb_colour


class PublishGeneralMarker(smach.State):
    """
    @userdata.in_pose: A geometry_msgs.msg Pose() object.
    Publishes the figure given pased on the input pose.
    You can input the marker_name and the scale.
    You can state its name.
    You can state the frame ID you want.
    The duration in second of the life of the marker can aslo be modified.
    Basic Colours can be selected (RED,BLUE,GREEN and RANDOM). RED is the default colour.
    You can change the length of the marker ( lets say the length of this marker buffer).
    If no marker_ns is given, but a marker name yes, it will put it in ns also without the / and ns_ at the beginning.
    This a first mesure to avoid different markers have the same ns and id.
    """
    def __init__(self, scale=0.2,
                 marker_ns="markers_namespace",
                 marker_name="/visualization_marker",
                 marker_type="CYLINDER",
                 marker_frame_id="/base_link",
                 marker_id=0,
                 mk_length=1,
                 colour="RED",
                 marker_duration=0):
        smach.State.__init__(self, input_keys=["in_pose"], outcomes=[succeeded])

        self.publisher = rospy.Publisher(marker_name, Marker)
        self._scale = scale
        self._marker_type = marker_type
        self._marker_frame_id = marker_frame_id
        self._marker_id = marker_id
        self._marker_ns = marker_ns
        self._marker_name = marker_name
        self._mk_length = mk_length
        self._colour = colour
        self._marker_duration = marker_duration

    def execute(self, userdata):
        if (not isinstance(userdata.in_pose, Pose)):
            raise ValueError("ERROR: in_pose need be a Pose() object, not '%s'." % type(userdata.in_pose))

        debugPrint("Will publish marker in: " + str(userdata.in_pose), 4)

        self.marker = Marker()
        self.marker.header.frame_id = self._marker_frame_id

        if self._marker_ns == "markers_namespace" and self._marker_name != "/visualization_marker":
            self.marker.ns = "ns_" + self._marker_name.split('/')[1]
        else:
            self.marker.ns = self._marker_ns
        self.marker.id = self._marker_id

        global marker_id
        self.marker.id = marker_id
        #set marker_id for the next call
        marker_id = marker_id + 1
        if (marker_id >= self._mk_length):
            marker_id = 0

        self.marker.header.stamp = rospy.Time.now()
        self.marker.type = SetMarkerType(self._marker_type)
        self.marker.action = Marker.ADD
        self.marker.pose = userdata.in_pose
        self.marker.scale.x = self._scale
        self.marker.scale.y = self._scale
        self.marker.scale.z = self._scale
        self.marker.color = SetColour(self._colour)
        self.marker.lifetime = rospy.Duration(self._marker_duration)
        self.publisher.publish(self.marker)
        debugPrint("Marker published...", 4)
        return succeeded


class UserdataClassForPublishGeneralMarker():

    def __init__(self):
        self.setVar()

    def setVar(self):
        self.in_pose = Pose()


def PublishPoseMarkers(pose, marker_name, marker_type, colour):
    """
    The input is a Pose().
    """

    class_pose = UserdataClassForPublishGeneralMarker()
    class_pose.in_pose = pose
    marker_state = PublishGeneralMarker(marker_name=marker_name, marker_type=marker_type, colour=colour)
    marker_state.execute(class_pose)

    return None
