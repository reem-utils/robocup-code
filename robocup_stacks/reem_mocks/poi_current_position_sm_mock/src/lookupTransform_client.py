#! /usr/bin/env python
# -.- coding: utf-8 -.-
#LOOKUPTRANSFORM.PY
# vim: expandtab ts=4 sw=4
    

LOOP = 5

import roslib; roslib.load_manifest('poi_current_position_sm_mock')

import rospy


from poi_current_position_sm_mock.srv import *
from geometry_msgs.msg import *
from random import random, randint


def lookupTransform_client(req):
    rospy.wait_for_service('lookupTransform')
    try:
        answer = rospy.ServiceProxy('lookupTransform', lookupTransform)
        responding = answer(req)
        return responding
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":

    i = 0
    while i <= LOOP :
        request = lookupTransformRequest()
        request.target_frame = "/map"
        request.source_frame = "/base_link"
        request.transform_time = rospy.Time(secs=0, nsecs=0)    
        print "Requesting::: %s"%str(request)
        print "Response :::%s"%(lookupTransform_client(request))
        i += 1 




