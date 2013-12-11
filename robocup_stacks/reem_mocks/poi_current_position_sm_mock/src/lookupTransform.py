#! /usr/bin/env python
# -.- coding: utf-8 -.-
#LOOKUPTRANSFORM.PY
# vim: expandtab ts=4 sw=4


import roslib; roslib.load_manifest('poi_current_position_sm_mock')

import rospy


from poi_current_position_sm_mock.srv import *
from geometry_msgs.msg import *
from random import random, randint


DETERMINISTIC_CALL = False
DETERMINISTIC_COORDS = [10,10,0]


def handle_lookupTransform_call(data):

    print "Received " + str(data)

    if not DETERMINISTIC_CALL:
        x = randint(0, 1000) / 10.0
        y = randint(0, 1000) / 10.0
        z = randint(0, 100) / 10.0
        mode = ":::RANDOM:::"
    else:
        x,y,z = DETERMINISTIC_COORDS
        mode = ":::DETERMINISTIC:::"

    print "Received " + str(data)
    response = lookupTransformResponse()
    response.transform.transform.translation.x = x
    response.transform.transform.translation.y = y
    response.transform.transform.rotation.z = z
    print mode +  ":::Response:::" + str(response)
    rospy.sleep(0.5)
    return response




def lookupTransformServer():
        rospy.init_node('lookupTransform')
        s = rospy.Service('lookupTransform' , lookupTransform , handle_lookupTransform_call)
        print "::: lookupTransform Ready :::"
        rospy.spin()


if __name__ == '__main__':
        lookupTransformServer()



