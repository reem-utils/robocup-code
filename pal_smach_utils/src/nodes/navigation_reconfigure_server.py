#!/usr/bin/env python

PACKAGE = "pal_smach_utils"

import roslib
roslib.load_manifest(PACKAGE)
import rospy

from dynamic_reconfigure.server import Server
from pal_smach_utils.cfg import navigation_reconfigureConfig


def callback(config, level):
    rospy.loginfo("""Reconfiugre Request""")
    rospy.set_param("/params_navigation/move_base_topic_goal", config["move_base_topic_goal"])
    rospy.set_param("/params_navigation/gotolocation_markers_length", config["gotolocation_markers_length"])
    rospy.set_param("/params_navigation/gotolocation_markers_lifetime", config["gotolocation_markers_lifetime"])
    rospy.set_param("/params_navigation/gotolocation_markers_show_only_last_marker", config["gotolocation_markers_show_only_last_marker"])
    rospy.set_param("/params_navigation/gotolocation_markers_enable_arrows", config["gotolocation_markers_enable_arrows"])
    return config

if __name__ == "__main__":
    rospy.init_node(PACKAGE + "_navigation_server_node", anonymous=True)

    srv = Server(navigation_reconfigureConfig, callback)
    rospy.spin()
