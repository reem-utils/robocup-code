import math
import rospy
from visualization_msgs.msg import MarkerArray, Marker
from geometry_msgs.msg import Pose, PoseStamped


def euclidean_distance(p, q):
    # p and q are expected to be tuples or maybe lists
    return math.sqrt(reduce(lambda acc, x: acc+(x[0]-x[1])**2, zip(p, q), 0))


def squared_distance(p, q):
    # p and q are expected to be tuples or maybe lists
    return reduce(lambda acc, x: acc+(x[0]-x[1])**2, zip(p, q), 0)


def plan_distance(plan):
    # plan is expected to be a geometry_msgs/PoseStamped[] object (from the poses field of a nav_msgs/Path object)
    # Returns the total distance of the plan
    d = 0
    for i in range(1, len(plan)):
        #print "d(%d, %d)" % (i-1, i)
        pos = plan[i-1].pose.position
        pos_i = plan[i].pose.position
        d += euclidean_distance((pos.x, pos.y), (pos_i.x, pos_i.y))
    return d


def distance(start_node, goal_node, make_plan=None):
    #Distance between two positions. Both start_node and goal_node are expected to be tuples (x, y)
    if make_plan is not None:
        start = PoseStamped()
        start.header.frame_id = '/map'
        start.pose = Pose()
        start.pose.position.x = start_node[0]
        start.pose.position.y = start_node[1]

        goal = PoseStamped()
        goal.header.frame_id = '/map'
        goal.pose = Pose()
        goal.pose.position.x = goal_node[0]
        goal.pose.position.y = goal_node[1]

        try:
            resp = make_plan(start, goal, 0)
            if len(resp.plan.poses) > 0:
                distance = plan_distance(resp.plan.poses)
            else:  # The path wasn't computed for whatever reason
                distance = euclidean_distance(start_node, goal_node)
        except rospy.ServiceException:  # The call to make_plan failed
            distance = euclidean_distance(start_node, goal_node)
    else:
        distance = euclidean_distance(start_node, goal_node)
    return distance


def get_corners(c1, c2, c3, c4):
    # Returns 2 points that represent the square corners of the room.
    cs = [c1, c2, c3, c4]
    xs = reduce(lambda x, y: x + [y[0]], cs, [])  # get x components in a list
    ys = reduce(lambda x, y: x + [y[1]], cs, [])  # get y components in a list
    minx = min(xs)
    miny = min(ys)
    maxx = max(xs)
    maxy = max(ys)
    return ((minx, miny), (maxx, maxy))


def publish_markerArray(publisher, points, rgba=(1, 0, 0, 1), shape=Marker.CUBE, duration=rospy.Duration(360), ns='ns'):
        #points is expected to be a list of tuples (x,y)
        #It's recommended that the publisher is created with latch=True
        _id = 0
        ma = MarkerArray()
        for p in points:
            m = Marker()
            m.header.frame_id = '/map'
            m.header.stamp = rospy.get_rostime()
            m.ns = ns
            m.id = _id
            m.type = shape
            m.action = m.ADD
            m.pose.position.x = p[0]
            m.pose.position.y = p[1]
            m.pose.orientation.w = 1
            m.scale.x = 0.5
            m.scale.y = 0.5
            m.scale.z = 0.5
            m.color.r = rgba[0]
            m.color.g = rgba[1]
            m.color.b = rgba[2]
            m.color.a = rgba[3]
            m.lifetime = duration
            ma.markers.append(m)
            _id += 1
        publisher.publish(ma)
