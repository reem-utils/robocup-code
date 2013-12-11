import rospy

from std_msgs.msg import Header
from geometry_msgs.msg import *
from trajectory_msgs.msg import *
from arm_navigation_msgs.msg import *
from control_msgs.msg import *
#from pr2_controllers_msgs.msg import *

try:
    from pr_msgs.msg import ObjectPose
except ImportError:
    from common.msg import ObjectPose
    #from object_recognition_mock.msg import ObjectPose


def get_arm_goal(object_pose, frame_id="/base_link"): # you can pass a ObjectPose or just a Pose
    b_type = "ObjectPose" in str(type(object_pose))
    pose_to_release = object_pose.pose if b_type else object_pose

    arm_goal = MoveArmGoal()

    arm_goal.planner_service_name = "ompl_planning/plan_kinematic_path"

    arm_goal.motion_plan_request = MotionPlanRequest()
    arm_goal.motion_plan_request.workspace_parameters = WorkspaceParameters()

    header = Header(stamp=rospy.Time().now(), frame_id=frame_id)

    position_constraint = PositionConstraint(weight=1.0, header=header)
    position_constraint.link_name = "hand_right_grasping_frame"
    position_constraint.position = pose_to_release.position
    position_constraint.constraint_region_shape.type = Shape.BOX
    position_constraint.constraint_region_shape.dimensions = [0.040000000000000001] * 3
    position_constraint.constraint_region_orientation.w = 1.0

    orientation_constraint = OrientationConstraint(weight=1.0, header=header)
    orientation_constraint.link_name = "hand_right_grasping_frame"
    orientation_constraint.orientation = pose_to_release.orientation

    orientation_constraint.absolute_roll_tolerance = 0.3
    orientation_constraint.absolute_pitch_tolerance = 0.3
    orientation_constraint.absolute_yaw_tolerance = 0.3

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
    object_pose.pose.position = Point(0.20, -0.35, 1.13)
    object_pose.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
    return object_pose


# This pose is for skipping the table in simulation right now
# DONT USE THIS POSE... TOO HARD TO CORRECT IT
# def get_pose_intermediate_position():
#     object_pose = ObjectPose()
#     object_pose.pose.position = Point(-0.043, -0.43, 1.21)
#     object_pose.pose.orientation = Quaternion(-0.478029, 0.546582, -0.501975, 0.469848)
#     return object_pose


def get_pose_for_arm_in_initial_grasping_position():
    object_pose = ObjectPose()
    object_pose.pose.position = Point(0.1, -0.45, 1.25)
    object_pose.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
    return object_pose


# DONT USE THIS POSE... TOO HARD TO CORRECT IT
# def get_pose_for_arm_down():
#     # FIXME: Apparently this is in /map instead of /base_link, or something (?)
#     object_pose = ObjectPose()
#     object_pose.pose.position = Point(0.130007, -0.198804, 0.900355)
#     object_pose.pose.orientation = Quaternion(0.87292, -0.244933, 0.127606, -0.402163)
#     return object_pose



def get_pose_for_arm_pre_door_opening():
    object_pose = ObjectPose()
    object_pose.pose.position = Point(-0.1, -0.5, 1.1)
    object_pose.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)
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
    


def get_arm_goal_for_arm_elbow_back(frame_id="/base_link"):
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
    joint_constraint1.position = 1.6
    
    joint_constraint2 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint2.joint_name = "arm_right_2_joint"
    joint_constraint2.position = 2.05
    
    joint_constraint3 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint3.joint_name = "arm_right_3_joint"
    joint_constraint3.position = -1.64
    
    joint_constraint4 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint4.joint_name = "arm_right_4_joint"
    joint_constraint4.position = 1.9 # was 2.2
    
    joint_constraint5 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint5.joint_name = "arm_right_5_joint"
    joint_constraint5.position = 1.3 
    
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

# arm_right_1_joint  45
# arm_right_2_joint  46
# arm_right_3_joint  47
# arm_right_4_joint  48
# arm_right_5_joint  49
# arm_right_6_joint  50
# arm_right_7_joint  51


# [0.3243909482276083,
#  0.1079948229090261,
#  -0.7424174026786586,
#  0.5079999085829296,
#  0.1121641246186449,
#  -0.13428541550315484,
#  0.2593749565575398]


# torso_1_joint  25
# torso_2_joint  26

#  [-0.05754272637542558, -0.09205294784754925]


def get_arm_goal_for_arm_travelling_position(frame_id="/base_link"):
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
    joint_constraint1.position = 0.3243
    
    joint_constraint2 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint2.joint_name = "arm_right_2_joint"
    joint_constraint2.position = 0.25  # was 0.107
    
    joint_constraint3 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint3.joint_name = "arm_right_3_joint"
    joint_constraint3.position = -1.1  # -0.742
    
    joint_constraint4 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint4.joint_name = "arm_right_4_joint"
    joint_constraint4.position = 0.507  
    
    joint_constraint5 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint5.joint_name = "arm_right_5_joint"
    joint_constraint5.position = 0.112
    
    joint_constraint6 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint6.joint_name = "arm_right_6_joint"
    joint_constraint6.position = -0.134
    
    joint_constraint7 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint7.joint_name = "arm_right_7_joint"
    joint_constraint7.position = 0.259
    
    joint_constraint8 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint8.joint_name = "torso_1_joint"
    joint_constraint8.position = -0.0575
    
    joint_constraint9 = JointConstraint(weight=0.0, tolerance_above=0.1, tolerance_below=0.1)
    joint_constraint9.joint_name = "torso_2_joint"
    joint_constraint9.position = -0.092

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

    # Set hand to closed
    point1 = JointTrajectoryPoint(
        positions=[3.0, 3.4, 3.4],  # cant close too much or the object to grasp flies away
        velocities=[0.0, 0.0, 0.0],
        time_from_start = rospy.Duration(1))

    grasp_msg.trajectory = JointTrajectory(
        joint_names = ['hand_right_thumb_joint', 'hand_right_index_1_joint', 'hand_right_middle_1_joint'],
        points = [point1])

    return grasp_msg
    
def get_open_hand():
    grasp_msg = FollowJointTrajectoryGoal()

    # Set hand to open
    point1 = JointTrajectoryPoint(
        positions=[1.0, 0.0, 0.0],  # Open hand has the thumb finger in grasp position
        velocities=[0.0, 0.0, 0.0],
        time_from_start = rospy.Duration(1))

    # Sam: header (timestamp) is empty because its used to set a delay;
    # empty means start as soon as the message is received.
    grasp_msg.trajectory = JointTrajectory(
        joint_names = ['hand_right_thumb_joint', 'hand_right_index_1_joint', 'hand_right_middle_1_joint'],
        points = [point1])





    return grasp_msg


def get_fully_open_hand():
    grasp_msg = FollowJointTrajectoryGoal()

    # Set hand to open
    point1 = JointTrajectoryPoint(
        positions=[0.0, 0.0, 0.0],  # Open hand has the thumb finger in grasp position
        velocities=[0.0, 0.0, 0.0],
        time_from_start = rospy.Duration(1))

    # Sam: header (timestamp) is empty because its used to set a delay;
    # empty means start as soon as the message is received.
    grasp_msg.trajectory = JointTrajectory(
        joint_names = ['hand_right_thumb_joint', 'hand_right_index_1_joint', 'hand_right_middle_1_joint'],
        points = [point1])


    return grasp_msg

# vim: expandtab ts=4 sw=4
