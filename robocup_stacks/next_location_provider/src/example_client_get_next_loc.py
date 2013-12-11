#!/usr/bin/env python
import roslib
roslib.load_manifest('next_location_provider')

import sys

import rospy
from next_location_provider.srv import NextProbableLocation


def next_location_client(room):
    rospy.wait_for_service('get_next_probable_location')
    try:
        next_location = rospy.ServiceProxy('get_next_probable_location',
                                            NextProbableLocation)
        resp1 = next_location(room)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def usage():
    return "Usage: %s [string specifying the desired room]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        room = sys.argv[1]
    else:
        print usage()
        sys.exit(1)
    print "Requesting next probable location of objects in %s" % room
    next_loc = next_location_client(room)
    xy = '(' + str(next_loc.loc_position.position.x) + ', ' + str(next_loc.loc_position.position.y) + ')'
    print "Next %s location for object searching is %s positioned in (x,y) = %s" % (room, next_loc.location, xy)
