import roslib; roslib.load_manifest('iri_common_smach')
import rospy
from geometry_msgs.msg import *

def build_quaternion(qx, qy, qz, qw):
    quat = geometry_msgs.msg.Quaternion()
    quat.x = qx
    quat.y = qy
    quat.z = qz
    quat.w = qw

    return quat

def build_pose(x, y, z, q1, q2, q3, q4):
    r = Pose()
    r.position    = geometry_msgs.msg.Vector3(x,y,z)
    r.orientation = build_quaternion(q1, q2, q3, q4)

    return r

def build_pose_stamped_msg(frame_id, x, y, z, q1, q2, q3, q4):
    r                  = PoseStamped()
    r.header.frame_id  = frame_id
    r.header.stamp     = rospy.Time()
    r.pose             = build_pose(x, y, z, q1, q2, q3, q4)

    return r

def build_transform_msg(x, y, z, qx, qy, qz, qw):
    t             = geometry_msgs.msg.Transform()
    t.translation = geometry_msgs.msg.Vector3(x,y,z)
    t.rotation    = build_quaternion(qx, qy, qz, qw)

    return t
