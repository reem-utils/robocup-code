import rospy

from std_msgs.msg import Header
from geometry_msgs.msg import *
from trajectory_msgs.msg import *
from arm_navigation_msgs.msg import *
from control_msgs.msg import *


def get_head_look_down():
    head_msg = FollowJointTrajectoryGoal()

    # Set hand to open
    point1 = JointTrajectoryPoint(
        positions=[-0.3, 0.5],
        velocities=[0.0, 0.0],
        accelerations=[0.0, 0.0],
        time_from_start = rospy.Duration(2))

    # Sam: header (timestamp) is empty because its used to set a delay;
    # empty means start as soon as the message is received.
    head_msg.trajectory = JointTrajectory(
        joint_names = ['head_1_joint', 'head_2_joint'],
        points = [point1])

    return head_msg



def get_head_look_front():
    head_msg = FollowJointTrajectoryGoal()

    # Set hand to open
    point1 = JointTrajectoryPoint(
        positions=[0.0, 0.2],
        velocities=[0.0, 0.0],
        accelerations=[0.0, 0.0],
        time_from_start = rospy.Duration(2))

    # Sam: header (timestamp) is empty because its used to set a delay;
    # empty means start as soon as the message is received.
    head_msg.trajectory = JointTrajectory(
        joint_names = ['head_1_joint', 'head_2_joint'],
        points = [point1])

    return head_msg



# Returns a FollowJointTrajectoryGoal() with the position specified by the parameters
# horizontal must be ( position first is on the rotation over Z [1.0 == all left, 0.0 = middle, -1.0 =all right], vertical is rotation over X )
# time is in seconds
def get_head_look_arbitrary(horizontal, vertical, time):

    head_msg = FollowJointTrajectoryGoal()

    # Set hand to open
    point1 = JointTrajectoryPoint(
        positions=[horizontal, vertical],
        velocities=[0.0, 0.0],
        accelerations=[0.0, 0.0],
        time_from_start = rospy.Duration(time))

    # Sam: header (timestamp) is empty because its used to set a delay;
    # empty means start as soon as the message is received.
    head_msg.trajectory = JointTrajectory(
        joint_names = ['head_1_joint', 'head_2_joint'],
        points = [point1])

    return head_msg


