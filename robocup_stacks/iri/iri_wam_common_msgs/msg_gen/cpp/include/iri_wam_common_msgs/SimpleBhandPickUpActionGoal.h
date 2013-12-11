/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_wam_common_msgs/msg/SimpleBhandPickUpActionGoal.msg */
#ifndef IRI_WAM_COMMON_MSGS_MESSAGE_SIMPLEBHANDPICKUPACTIONGOAL_H
#define IRI_WAM_COMMON_MSGS_MESSAGE_SIMPLEBHANDPICKUPACTIONGOAL_H
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
#include "actionlib_msgs/GoalID.h"
#include "iri_wam_common_msgs/SimpleBhandPickUpGoal.h"

namespace iri_wam_common_msgs
{
template <class ContainerAllocator>
struct SimpleBhandPickUpActionGoal_ {
  typedef SimpleBhandPickUpActionGoal_<ContainerAllocator> Type;

  SimpleBhandPickUpActionGoal_()
  : header()
  , goal_id()
  , goal()
  {
  }

  SimpleBhandPickUpActionGoal_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , goal_id(_alloc)
  , goal(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
   ::actionlib_msgs::GoalID_<ContainerAllocator>  goal_id;

  typedef  ::iri_wam_common_msgs::SimpleBhandPickUpGoal_<ContainerAllocator>  _goal_type;
   ::iri_wam_common_msgs::SimpleBhandPickUpGoal_<ContainerAllocator>  goal;


  typedef boost::shared_ptr< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct SimpleBhandPickUpActionGoal
typedef  ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<std::allocator<void> > SimpleBhandPickUpActionGoal;

typedef boost::shared_ptr< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal> SimpleBhandPickUpActionGoalPtr;
typedef boost::shared_ptr< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal const> SimpleBhandPickUpActionGoalConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_wam_common_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "7e7225d144560f8d00a33d8c9460e78e";
  }

  static const char* value(const  ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x7e7225d144560f8dULL;
  static const uint64_t static_value2 = 0x00a33d8c9460e78eULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/SimpleBhandPickUpActionGoal";
  }

  static const char* value(const  ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalID goal_id\n\
SimpleBhandPickUpGoal goal\n\
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
MSG: iri_wam_common_msgs/SimpleBhandPickUpGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# October 2012 - J.L Rivero, G. Alenya, D. Martinez\n\
#\n\
# This action was built after analyze previously the \"standard\" ROS message\n\
# PickUp. The ROS message involve a lot of action we were not consider at\n\
# the moment of writing and adapt that huge input for our needs was over-\n\
# engineer a solution.\n\
#\n\
# A translator PickUp -> SimpleBhandPickUp could be done, if needed\n\
\n\
# SimpleBhandPickUp is composed by the following phases:\n\
#\n\
# 1. Move the ARM from current to pre-grasp (planned if requested)\n\
# 2. Put the fingers into the pre-grasp position\n\
# 3. Move the ARM from pre-grasp to grasp (planned if requested)\n\
# 4. Put the fingers into the grasp position\n\
# 5. Perform the lift movement\n\
\n\
# goal\n\
# A vector of different GCL bhand commands\n\
string[] fingers_position_for_grasp\n\
string[] fingers_position_for_pre_grasp\n\
# Grasp pose is defined in the Stamped \n\
geometry_msgs/PoseStamped grasp_pose\n\
# pre movement relative to the grasp_pose\n\
geometry_msgs/Pose pre_grasp_modifier\n\
# Direction and distance to lift from the grasp_pose\n\
object_manipulation_msgs/GripperTranslation lift\n\
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
MSG: object_manipulation_msgs/GripperTranslation\n\
# defines a translation for the gripper, used in pickup or place tasks\n\
# for example for lifting an object off a table or approaching the table for placing\n\
\n\
# the direction of the translation\n\
geometry_msgs/Vector3Stamped direction\n\
\n\
# the desired translation distance\n\
float32 desired_distance\n\
\n\
# the min distance that must be considered feasible before the\n\
# grasp is even attempted\n\
float32 min_distance\n\
================================================================================\n\
MSG: geometry_msgs/Vector3Stamped\n\
# This represents a Vector3 with reference coordinate frame and timestamp\n\
Header header\n\
Vector3 vector\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const  ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.goal_id);
    stream.next(m.goal);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct SimpleBhandPickUpActionGoal_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
s << std::endl;
    Printer< ::iri_wam_common_msgs::SimpleBhandPickUpGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_WAM_COMMON_MSGS_MESSAGE_SIMPLEBHANDPICKUPACTIONGOAL_H
