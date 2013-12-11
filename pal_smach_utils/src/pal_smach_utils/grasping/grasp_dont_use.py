import rospy

from std_msgs.msg import Header
from geometry_msgs.msg import *
from trajectory_msgs.msg import *
from arm_navigation_msgs.msg import *
from control_msgs.msg import *

try:
    from pr_msgs.msg import ObjectPoseList, ObjectPose
except ImportError:
    from object_recognition_mock.msg import ObjectPoseList, ObjectPose

def get_arm_goal(object_pose, frame_id="/base_link"):
    arm_goal = MoveArmGoal()
    
    arm_goal.planner_service_name = "ompl_planning/plan_kinematic_path"

    arm_goal.motion_plan_request = MotionPlanRequest()
    arm_goal.motion_plan_request.workspace_parameters = WorkspaceParameters()

    header = Header(stamp=rospy.Time().now(), frame_id=frame_id)

    position_constraint = PositionConstraint(weight=1.0, header=header)
    position_constraint.link_name = "arm_right_7_link"
    position_constraint.position = object_pose.position
    position_constraint.constraint_region_shape.type = Shape.BOX
    position_constraint.constraint_region_shape.dimensions = [0.040000000000000001] * 3
    position_constraint.constraint_region_orientation.w = 1.0

    orientation_constraint = OrientationConstraint(weight=1.0, header=header)
    orientation_constraint.link_name = "arm_right_7_link"
    orientation_constraint.orientation = object_pose.orientation

    orientation_constraint.absolute_roll_tolerance = 0.02
    orientation_constraint.absolute_pitch_tolerance = 0.02
    orientation_constraint.absolute_yaw_tolerance = 0.02

    arm_goal.motion_plan_request.goal_constraints = Constraints(
        position_constraints=[position_constraint],
        orientation_constraints=[orientation_constraint])

    arm_goal.motion_plan_request.planner_id = ""
    arm_goal.motion_plan_request.group_name = "right_arm_torso"
    arm_goal.motion_plan_request.num_planning_attempts = 10
    arm_goal.motion_plan_request.allowed_planning_time = rospy.Duration(10)
    arm_goal.motion_plan_request.expected_path_duration = rospy.Duration(0)
    arm_goal.motion_plan_request.expected_path_dt = rospy.Duration(0)

    return arm_goal

def get_pose_for_arm_in_front():
    object_pose = ObjectPose()
    object_pose.pose.position = Point(0.30, -0.30, 1.13)
    object_pose.pose.orientation = Quaternion(0.5, -0.5, 0.5, -0.5)
    return object_pose


def get_pose_for_arm_in_initial_grasping_position():
    object_pose = ObjectPose()
    object_pose.pose.position = Point(0.25, -0.35, 1.25)
    object_pose.pose.orientation = Quaternion(0.5, -0.5, 0.5, -0.5)
    return object_pose



def get_pose_for_arm_down():
    # FIXME: Apparently this is in /map instead of /base_link, or something (?)
    object_pose = ObjectPose()
    object_pose.pose.position = Point(0.130007, -0.198804, 0.900355)
    object_pose.pose.orientation = Quaternion(0.87292, -0.244933, 0.127606, -0.402163)
    return object_pose
    
    
def get_arm_goal_for_arm_down(frame_id="/base_link"):
    arm_goal = MoveArmGoal()

    arm_goal.planner_service_name = "ompl_planning/plan_kinematic_path"

    arm_goal.motion_plan_request = MotionPlanRequest()
    arm_goal.motion_plan_request.workspace_parameters = WorkspaceParameters()

    header = Header(stamp=rospy.Time().now(), frame_id=frame_id)

    # FIXME: If we need all this mess, do it properly:
    #   | joint_constraints = []
    #   | for joint_id in range(1, 7+1):
    #   |     ...
    
    joint_constraint1 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint1.joint_name = "arm_right_1_joint"
    joint_constraint1.position = -0.4
    
    joint_constraint2 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint2.joint_name = "arm_right_2_joint"
    joint_constraint2.position = 0.1
    
    joint_constraint3 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint3.joint_name = "arm_right_3_joint"
    joint_constraint3.position = -0.1
    
    joint_constraint4 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint4.joint_name = "arm_right_4_joint"
    joint_constraint4.position = 0.6109
    
    joint_constraint5 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint5.joint_name = "arm_right_5_joint"
    joint_constraint5.position = 0.0
    
    joint_constraint6 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint6.joint_name = "arm_right_6_joint"
    joint_constraint6.position = 0.0
    
    joint_constraint7 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint7.joint_name = "arm_right_7_joint"
    joint_constraint7.position = 0.0
    
    joint_constraint8 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint8.joint_name = "torso_1_joint"
    joint_constraint8.position = 0.0    
    
    joint_constraint9 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint9.joint_name = "torso_2_joint"
    joint_constraint9.position = 0.0  

    arm_goal.motion_plan_request.goal_constraints = Constraints(
        joint_constraints=[joint_constraint1, joint_constraint2, joint_constraint3,
                           joint_constraint4, joint_constraint5, joint_constraint6,
                           joint_constraint7, joint_constraint8, joint_constraint9])

    arm_goal.motion_plan_request.planner_id = ""
    arm_goal.motion_plan_request.group_name = "right_arm_torso"
    arm_goal.motion_plan_request.num_planning_attempts = 10
    arm_goal.motion_plan_request.allowed_planning_time = rospy.Duration(10)
    arm_goal.motion_plan_request.expected_path_duration = rospy.Duration(0)
    arm_goal.motion_plan_request.expected_path_dt = rospy.Duration(0)
          
    return arm_goal
    
def get_close_hand():
    grasp_msg = FollowJointTrajectoryGoal()

    # Set hand to open
    point1 = JointTrajectoryPoint(
        positions=[0.0],
        velocities=[0.0],
        accelerations=[0.0],
        time_from_start = rospy.Duration(1))

    # First movement, half closed
    point2 = JointTrajectoryPoint(
        positions=[0.3],
        velocities=[0.0],
        accelerations=[0.0],
        time_from_start = rospy.Duration(1))

    # Second movement, closed
    point3 = JointTrajectoryPoint(
        positions=[0.4],
        velocities=[0.0],
        accelerations=[0.0],
        time_from_start = rospy.Duration(2))

    # Sam: header (timestamp) is empty because its used to set a delay;
    # empty means start as soon as the message is received.
    grasp_msg.trajectory = JointTrajectory(
        joint_names = ['hand_right_joint'],
        points = [point1, point2, point3])

    return grasp_msg
    
def get_open_hand():
    grasp_msg = FollowJointTrajectoryGoal()

    # Set hand to open
    point1 = JointTrajectoryPoint(
        positions=[0.0],
        velocities=[0.0],
        accelerations=[0.0],
        time_from_start = rospy.Duration(1))

    # Sam: header (timestamp) is empty because its used to set a delay;
    # empty means start as soon as the message is received.
    grasp_msg.trajectory = JointTrajectory(
        joint_names = ['hand_right_joint'],
        points = [point1])

    return grasp_msg

# vim: expandtab ts=4 sw=4
