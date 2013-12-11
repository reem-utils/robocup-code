#! /usr/bin/env python
import roslib
roslib.load_manifest('next_location_provider')
import rospy
from next_location_provider.srv import NextProbableLocation, NextProbableLocationResponse
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler
import pal_smach_utils.object_finding_algorithms.ofb_utils as ofb_utils
from pal_smach_utils.utils.global_common import transform_pose
from nav_msgs.srv import GetPlan

PARAM_NAME = "/mmap/locations_prob/"
MAKE_PLAN = True


class CircularOrderedList:
    '''Class to handle a circular ordered list. It's prepaired to receive a list of binary tuples'''

    def __init__(self, l):
        self._list = sorted(l, key=lambda x: x[1], reverse=True)
        self._i = -1

    def next(self):
        self._i = (self._i + 1) % len(self._list)
        return self._list[self._i]

    def next_same(self):  # Return the next values and all of them that are the same
        self._i = (self._i + 1) % len(self._list)
        next = self._list[self._i]
        ret = [next]
        j = self._i + 1
        while j < len(self._list) and self._list[j][1] == next[1]:
            ret.append(self._list[j])
            j = j + 1
        return ret

    def swap_elements(self, e1, e2):  # Swap the elements e1 and e2 in the list
        ie1 = self._list.index(e1)
        ie2 = self._list.index(e2)
        self._list[ie1] = e2
        self._list[ie2] = e1

    def __getitem__(self, i):
        return self._list[i]

    def __setitem__(self, i, value):
        #self._list[i] = value
        #self._list.sort(key=lambda x: x[1], reverse=True)
        del self._list[i]  # Delete the element we want to replace
        for k, val in enumerate(self._list):  # Insert the element at it's location in order
            if val[1] < value[1]:
                self._list.insert(k, value)
                break

    def __str__(self):
        return str(self._list)


class NextProbableLocationServer:
    def __init__(self, make_plan):
        self._cols = {}  # Empty dictionary. It will store a CircularOrderedList for each roomself.
        self._make_plan = make_plan

    def printLists(self):
        global __cols
        print "Ordered lists that the service will use:"
        for room, value in rospy.get_param(PARAM_NAME).iteritems():
            print room, self._cols[room]
        print

    def handle_next_location(self, req):
        print "Next probable location service: Recieved request for next probable search location in %s" % req.room
        ret = NextProbableLocationResponse()

        # Look through all the location with the same probabilities and get the minimum
        nexts = self._cols[req.room].next_same()
        min_param = rospy.get_param(PARAM_NAME + req.room + '/' + nexts[0][0])
        ret.location = nexts[0][0]
        if len(nexts) > 1:
            make_plan = None
            if self._make_plan:
                try:
                    rospy.wait_for_service('/move_base/make_plan', 0.1)
                    make_plan = rospy.ServiceProxy('/move_base/make_plan', GetPlan)
                except rospy.ROSException:
                    pass  # make_plan is already set to None

            robot_pose = Pose()
            robot_pose.position.x = 0
            robot_pose.position.y = 0
            robot_pose.position.z = 0
            robot_pose = transform_pose(robot_pose, '/base_link', '/map', timeout=3)  # Get robot's pose in /map coordinates
            robot_tuple = (robot_pose.position.x, robot_pose.position.y)

            pose_tuple = (min_param[1], min_param[2])
            min_dist = ofb_utils.distance(robot_tuple, pose_tuple, make_plan)
            for name, _ in nexts[1:]:
                param = rospy.get_param(PARAM_NAME + req.room + '/' + name)
                pose_tuple = (param[1], param[2])
                d = ofb_utils.distance(robot_tuple, pose_tuple, make_plan)
                if d < min_dist:
                    min_dist = d
                    min_param = param
                    ret.location = name
            # All the locations in nexts have the same probabilty
            self._cols[req.room].swap_elements(nexts[0], (ret.location, nexts[0][1]))

        pose = Pose()
        pose.position = Point(min_param[1], min_param[2], 0)
        pose.orientation = Quaternion(*quaternion_from_euler(0, 0, min_param[3]))
        ret.loc_position = pose
        return ret


def get_next_location_Server():
    rospy.init_node('get_next_location_Server')
    nlp = NextProbableLocationServer(MAKE_PLAN)
    print
    print "-------------------- Next probable location service ---------------------"
    for room, value in rospy.get_param(PARAM_NAME).iteritems():
        room_items = rospy.get_param(PARAM_NAME + room).items()
        nlp._cols[room] = CircularOrderedList(reduce(lambda l_acc, tupl: l_acc + [(tupl[0], tupl[1][0])], room_items, []))
        #__cols[room] = CircularOrderedList(rospy.get_param(PARAM_NAME + room).items())
        # The reduce may not be necessary and you could create the COL like the line above. The reduce simply creates a list of tuples
        # of (location, number)
    nlp.printLists()
    rospy.Service('get_next_probable_location', NextProbableLocation, nlp.handle_next_location)
    print "Ready to provide search locations in a probability order"
    print "-------------------------------------------------------------------------"
    rospy.spin()


if __name__ == '__main__':
    get_next_location_Server()
