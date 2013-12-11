/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/tibi_dabo_msgs/msg/guideGoalActionGoal.msg */
#ifndef TIBI_DABO_MSGS_MESSAGE_GUIDEGOALACTIONGOAL_H
#define TIBI_DABO_MSGS_MESSAGE_GUIDEGOALACTIONGOAL_H
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
#include "tibi_dabo_msgs/guideGoalGoal.h"

namespace tibi_dabo_msgs
{
template <class ContainerAllocator>
struct guideGoalActionGoal_ {
  typedef guideGoalActionGoal_<ContainerAllocator> Type;

  guideGoalActionGoal_()
  : header()
  , goal_id()
  , goal()
  {
  }

  guideGoalActionGoal_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , goal_id(_alloc)
  , goal(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
   ::actionlib_msgs::GoalID_<ContainerAllocator>  goal_id;

  typedef  ::tibi_dabo_msgs::guideGoalGoal_<ContainerAllocator>  _goal_type;
   ::tibi_dabo_msgs::guideGoalGoal_<ContainerAllocator>  goal;


  typedef boost::shared_ptr< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct guideGoalActionGoal
typedef  ::tibi_dabo_msgs::guideGoalActionGoal_<std::allocator<void> > guideGoalActionGoal;

typedef boost::shared_ptr< ::tibi_dabo_msgs::guideGoalActionGoal> guideGoalActionGoalPtr;
typedef boost::shared_ptr< ::tibi_dabo_msgs::guideGoalActionGoal const> guideGoalActionGoalConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace tibi_dabo_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "29606d36f7e457c57e5745b072f5ba76";
  }

  static const char* value(const  ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x29606d36f7e457c5ULL;
  static const uint64_t static_value2 = 0x7e5745b072f5ba76ULL;
};

template<class ContainerAllocator>
struct DataType< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "tibi_dabo_msgs/guideGoalActionGoal";
  }

  static const char* value(const  ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalID goal_id\n\
guideGoalGoal goal\n\
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
MSG: tibi_dabo_msgs/guideGoalGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#goal definition\n\
geometry_msgs/PoseStamped target_pose\n\
int32                     target_id  \n\
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
";
  }

  static const char* value(const  ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.goal_id);
    stream.next(m.goal);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct guideGoalActionGoal_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
s << std::endl;
    Printer< ::tibi_dabo_msgs::guideGoalGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};


} // namespace message_operations
} // namespace ros

#endif // TIBI_DABO_MSGS_MESSAGE_GUIDEGOALACTIONGOAL_H

