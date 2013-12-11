#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('robot_controllers_mock')
import rospy
from pal_srvs.srv import ControllerStartup, ControllerStartupResponse

def stop_robot_controllers_cb(req):
    rospy.loginfo('Stop Robot Controllers \'/Peer_controller_configurator/orocos_controller_stop was called.')
    r = ControllerStartupResponse()
    r.Result = True
    return r
s_stop_robot_controllers =  { 'name': '/Peer_controller_configurator/orocos_controller_stop', 'service_class': ControllerStartup, 'handler': stop_robot_controllers_cb}


def start_robot_controllers_cb(req):
    rospy.loginfo('Start Robot Controllers \'/Peer_controller_configurator/orocos_controller_start was called.')
    r = ControllerStartupResponse()
    r.Result = True
    return r
s_start_robot_controllers =  {'name': '/Peer_controller_configurator/orocos_controller_start', 'service_class': ControllerStartup, 'handler': start_robot_controllers_cb}


if __name__ == '__main__':
    rospy.init_node('robot_controllers_mock')

    rospy.Service(**s_stop_robot_controllers)
    rospy.Service(**s_start_robot_controllers)

    rospy.spin()
