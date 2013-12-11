from math_utils import normalize_vector, vector_magnitude, multiply_vector
from geometry_msgs.msg import Pose

def pose_at_distance(pose,distance):
    """
    Returns a pose that has the same orientation as the original
    but the position is at a distance from the original.
    Very usefull when you want to mantain a distance from an object. 
    """
    unit_vector = normalize_vector(pose.position)
    k = vector_magnitude(pose.position)
    distance_des = k - distance
    dist_vector = multiply_vector(unit_vector, distance_des)
    new_pose = Pose()
    new_pose.position = dist_vector
    new_pose.orientation = pose.orientation
    return new_pose
# vim: expandtab ts=4 sw=4
