/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_door_detector/msg/FindADoorActionResult.msg */
#ifndef IRI_DOOR_DETECTOR_MESSAGE_FINDADOORACTIONRESULT_H
#define IRI_DOOR_DETECTOR_MESSAGE_FINDADOORACTIONRESULT_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"
#include "actionlib_msgs/GoalStatus.h"
#include "iri_door_detector/FindADoorResult.h"

namespace iri_door_detector
{
template <class ContainerAllocator>
struct FindADoorActionResult_ {
  typedef FindADoorActionResult_<ContainerAllocator> Type;

  FindADoorActionResult_()
  : header()
  , status()
  , result()
  {
  }

  FindADoorActionResult_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , status(_alloc)
  , result(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::actionlib_msgs::GoalStatus_<ContainerAllocator>  _status_type;
   ::actionlib_msgs::GoalStatus_<ContainerAllocator>  status;

  typedef  ::iri_door_detector::FindADoorResult_<ContainerAllocator>  _result_type;
   ::iri_door_detector::FindADoorResult_<ContainerAllocator>  result;


  typedef boost::shared_ptr< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct FindADoorActionResult
typedef  ::iri_door_detector::FindADoorActionResult_<std::allocator<void> > FindADoorActionResult;

typedef boost::shared_ptr< ::iri_door_detector::FindADoorActionResult> FindADoorActionResultPtr;
typedef boost::shared_ptr< ::iri_door_detector::FindADoorActionResult const> FindADoorActionResultConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_door_detector

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "6cc5ec3da569ede50554339713683f58";
  }

  static const char* value(const  ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x6cc5ec3da569ede5ULL;
  static const uint64_t static_value2 = 0x0554339713683f58ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_door_detector/FindADoorActionResult";
  }

  static const char* value(const  ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
FindADoorResult result\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: actionlib_msgs/GoalStatus\n\
GoalID goal_id\n\
uint8 status\n\
uint8 PENDING         = 0   # The goal has yet to be processed by the action server\n\
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server\n\
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing\n\
                            #   and has since completed its execution (Terminal State)\n\
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)\n\
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due\n\
                            #    to some failure (Terminal State)\n\
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,\n\
                            #    because the goal was unattainable or invalid (Terminal State)\n\
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing\n\
                            #    and has not yet completed execution\n\
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,\n\
                            #    but the action server has not yet confirmed that the goal is canceled\n\
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing\n\
                            #    and was successfully cancelled (Terminal State)\n\
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be\n\
                            #    sent over the wire by an action server\n\
\n\
#Allow for the user to associate a string with GoalStatus for debugging\n\
string text\n\
\n\
\n\
================================================================================\n\
MSG: actionlib_msgs/GoalID\n\
# The stamp should store the time at which this goal was requested.\n\
# It is used by an action server when it tries to preempt all\n\
# goals that were requested before a certain time\n\
time stamp\n\
\n\
# The id provides a way to associate feedback and\n\
# result message with specific goal requests. The id\n\
# specified must be unique.\n\
string id\n\
\n\
\n\
================================================================================\n\
MSG: iri_door_detector/FindADoorResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the result\n\
geometry_msgs/PoseStamped base_poses\n\
arm_navigation_msgs/MotionPlanRequest arm_poses\n\
string planner_service_name\n\
string state\n\
\n\
================================================================================\n\
MSG: geometry_msgs/PoseStamped\n\
# A Pose with reference coordinate frame and timestamp\n\
Header header\n\
Pose pose\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/MotionPlanRequest\n\
# This service contains the definition for a request to the motion\n\
# planner and the output it provides\n\
\n\
# Parameters for the workspace that the planner should work inside\n\
arm_navigation_msgs/WorkspaceParameters workspace_parameters\n\
\n\
# Starting state updates. If certain joints should be considered\n\
# at positions other than the current ones, these positions should\n\
# be set here\n\
arm_navigation_msgs/RobotState start_state\n\
\n\
# The goal state for the model to plan for. The goal is achieved\n\
# if all constraints are satisfied\n\
arm_navigation_msgs/Constraints goal_constraints\n\
\n\
# No state at any point along the path in the produced motion plan will violate these constraints\n\
arm_navigation_msgs/Constraints path_constraints\n\
\n\
# The name of the motion planner to use. If no name is specified,\n\
# a default motion planner will be used\n\
string planner_id\n\
\n\
# The name of the group of joints on which this planner is operating\n\
string group_name\n\
\n\
# The number of times this plan is to be computed. Shortest solution\n\
# will be reported.\n\
int32 num_planning_attempts\n\
\n\
# The maximum amount of time the motion planner is allowed to plan for\n\
duration allowed_planning_time\n\
\n\
# An expected path duration (in seconds) along with an expected discretization of the path allows the planner to determine the discretization of the trajectory that it returns\n\
duration expected_path_duration\n\
duration expected_path_dt\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/WorkspaceParameters\n\
# This message contains a set of parameters useful in\n\
# setting up the workspace for planning\n\
arm_navigation_msgs/Shape  workspace_region_shape\n\
geometry_msgs/PoseStamped    workspace_region_pose\n\
\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/Shape\n\
byte SPHERE=0\n\
byte BOX=1\n\
byte CYLINDER=2\n\
byte MESH=3\n\
\n\
byte type\n\
\n\
\n\
#### define sphere, box, cylinder ####\n\
# the origin of each shape is considered at the shape's center\n\
\n\
# for sphere\n\
# radius := dimensions[0]\n\
\n\
# for cylinder\n\
# radius := dimensions[0]\n\
# length := dimensions[1]\n\
# the length is along the Z axis\n\
\n\
# for box\n\
# size_x := dimensions[0]\n\
# size_y := dimensions[1]\n\
# size_z := dimensions[2]\n\
float64[] dimensions\n\
\n\
\n\
#### define mesh ####\n\
\n\
# list of triangles; triangle k is defined by tre vertices located\n\
# at indices triangles[3k], triangles[3k+1], triangles[3k+2]\n\
int32[] triangles\n\
geometry_msgs/Point[] vertices\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/RobotState\n\
# This message contains information about the robot state, i.e. the positions of its joints and links\n\
sensor_msgs/JointState joint_state\n\
arm_navigation_msgs/MultiDOFJointState multi_dof_joint_state\n\
\n\
================================================================================\n\
MSG: sensor_msgs/JointState\n\
# This is a message that holds data to describe the state of a set of torque controlled joints. \n\
#\n\
# The state of each joint (revolute or prismatic) is defined by:\n\
#  * the position of the joint (rad or m),\n\
#  * the velocity of the joint (rad/s or m/s) and \n\
#  * the effort that is applied in the joint (Nm or N).\n\
#\n\
# Each joint is uniquely identified by its name\n\
# The header specifies the time at which the joint states were recorded. All the joint states\n\
# in one message have to be recorded at the same time.\n\
#\n\
# This message consists of a multiple arrays, one for each part of the joint state. \n\
# The goal is to make each of the fields optional. When e.g. your joints have no\n\
# effort associated with them, you can leave the effort array empty. \n\
#\n\
# All arrays in this message should have the same size, or be empty.\n\
# This is the only way to uniquely associate the joint name with the correct\n\
# states.\n\
\n\
\n\
Header header\n\
\n\
string[] name\n\
float64[] position\n\
float64[] velocity\n\
float64[] effort\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/MultiDOFJointState\n\
#A representation of a multi-dof joint state\n\
time stamp\n\
string[] joint_names\n\
string[] frame_ids\n\
string[] child_frame_ids\n\
geometry_msgs/Pose[] poses\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/Constraints\n\
# This message contains a list of motion planning constraints.\n\
\n\
arm_navigation_msgs/JointConstraint[] joint_constraints\n\
arm_navigation_msgs/PositionConstraint[] position_constraints\n\
arm_navigation_msgs/OrientationConstraint[] orientation_constraints\n\
arm_navigation_msgs/VisibilityConstraint[] visibility_constraints\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/JointConstraint\n\
# Constrain the position of a joint to be within a certain bound\n\
string joint_name\n\
\n\
# the bound to be achieved is [position - tolerance_below, position + tolerance_above]\n\
float64 position\n\
float64 tolerance_above\n\
float64 tolerance_below\n\
\n\
# A weighting factor for this constraint\n\
float64 weight\n\
================================================================================\n\
MSG: arm_navigation_msgs/PositionConstraint\n\
# This message contains the definition of a position constraint.\n\
Header header\n\
\n\
# The robot link this constraint refers to\n\
string link_name\n\
\n\
# The offset (in the link frame) for the target point on the link we are planning for\n\
geometry_msgs/Point target_point_offset\n\
\n\
# The nominal/target position for the point we are planning for\n\
geometry_msgs/Point position\n\
\n\
# The shape of the bounded region that constrains the position of the end-effector\n\
# This region is always centered at the position defined above\n\
arm_navigation_msgs/Shape constraint_region_shape\n\
\n\
# The orientation of the bounded region that constrains the position of the end-effector. \n\
# This allows the specification of non-axis aligned constraints\n\
geometry_msgs/Quaternion constraint_region_orientation\n\
\n\
# Constraint weighting factor - a weight for this constraint\n\
float64 weight\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/OrientationConstraint\n\
# This message contains the definition of an orientation constraint.\n\
Header header\n\
\n\
# The robot link this constraint refers to\n\
string link_name\n\
\n\
# The type of the constraint\n\
int32 type\n\
int32 LINK_FRAME=0\n\
int32 HEADER_FRAME=1\n\
\n\
# The desired orientation of the robot link specified as a quaternion\n\
geometry_msgs/Quaternion orientation\n\
\n\
# optional RPY error tolerances specified if \n\
float64 absolute_roll_tolerance\n\
float64 absolute_pitch_tolerance\n\
float64 absolute_yaw_tolerance\n\
\n\
# Constraint weighting factor - a weight for this constraint\n\
float64 weight\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/VisibilityConstraint\n\
# This message contains the definition of a visibility constraint.\n\
Header header\n\
\n\
# The point stamped target that needs to be kept within view of the sensor\n\
geometry_msgs/PointStamped target\n\
\n\
# The local pose of the frame in which visibility is to be maintained\n\
# The frame id should represent the robot link to which the sensor is attached\n\
# The visual axis of the sensor is assumed to be along the X axis of this frame\n\
geometry_msgs/PoseStamped sensor_pose\n\
\n\
# The deviation (in radians) that will be tolerated\n\
# Constraint error will be measured as the solid angle between the \n\
# X axis of the frame defined above and the vector between the origin \n\
# of the frame defined above and the target location\n\
float64 absolute_tolerance\n\
\n\
\n\
================================================================================\n\
MSG: geometry_msgs/PointStamped\n\
# This represents a Point with reference coordinate frame and timestamp\n\
Header header\n\
Point point\n\
\n\
";
  }

  static const char* value(const  ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.status);
    stream.next(m.result);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct FindADoorActionResult_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_door_detector::FindADoorActionResult_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "status: ";
s << std::endl;
    Printer< ::actionlib_msgs::GoalStatus_<ContainerAllocator> >::stream(s, indent + "  ", v.status);
    s << indent << "result: ";
s << std::endl;
    Printer< ::iri_door_detector::FindADoorResult_<ContainerAllocator> >::stream(s, indent + "  ", v.result);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_DOOR_DETECTOR_MESSAGE_FINDADOORACTIONRESULT_H

