#!/usr/bin/env python

PACKAGE = "learn_and_follow_operator_test"

import roslib
roslib.load_manifest(PACKAGE)
import rospy

from dynamic_reconfigure.server import Server
from learn_and_follow_operator_test.cfg import learn_and_follow_operator_test_reconfigureConfig


def callback(config, level):
    rospy.loginfo("""Reconfiugre Request: {move_base_topic_goal}""".format(**config))
    rospy.set_param("/params_learn_and_follow_operator_test/move_base_topic", config["move_base_topic_goal"])
    rospy.set_param("/params_learn_and_follow_operator_test/nav_goal_x", config["nav_goal_x"])
    return config

if __name__ == "__main__":
    rospy.init_node(PACKAGE, anonymous=True)

    srv = Server(learn_and_follow_operator_test_reconfigureConfig, callback)
    rospy.spin()
