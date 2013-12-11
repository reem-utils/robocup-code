#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('reem_final_approach_mock')
import rospy
from reem_final_approach.srv import FinalApproachPose, FinalApproachPoseResponse


def final_approach_cb(req):
    rospy.loginfo('Final Approach \'/approachToGoal was called')
    return FinalApproachPoseResponse()
s_final_approach = {'name': '/approachToGoal', 'service_class': FinalApproachPose, 'handler': final_approach_cb}


if __name__ == '__main__':
    rospy.init_node('reem_final_approach_mock')

    rospy.Service(**s_final_approach)

    rospy.spin()
