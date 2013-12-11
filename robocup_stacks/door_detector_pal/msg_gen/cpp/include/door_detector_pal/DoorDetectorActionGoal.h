/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/door_detector_pal/msg/DoorDetectorActionGoal.msg */
#ifndef DOOR_DETECTOR_PAL_MESSAGE_DOORDETECTORACTIONGOAL_H
#define DOOR_DETECTOR_PAL_MESSAGE_DOORDETECTORACTIONGOAL_H
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
#include "door_detector_pal/DoorDetectorGoal.h"

namespace door_detector_pal
{
template <class ContainerAllocator>
struct DoorDetectorActionGoal_ {
  typedef DoorDetectorActionGoal_<ContainerAllocator> Type;

  DoorDetectorActionGoal_()
  : header()
  , goal_id()
  , goal()
  {
  }

  DoorDetectorActionGoal_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , goal_id(_alloc)
  , goal(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
   ::actionlib_msgs::GoalID_<ContainerAllocator>  goal_id;

  typedef  ::door_detector_pal::DoorDetectorGoal_<ContainerAllocator>  _goal_type;
   ::door_detector_pal::DoorDetectorGoal_<ContainerAllocator>  goal;


  typedef boost::shared_ptr< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct DoorDetectorActionGoal
typedef  ::door_detector_pal::DoorDetectorActionGoal_<std::allocator<void> > DoorDetectorActionGoal;

typedef boost::shared_ptr< ::door_detector_pal::DoorDetectorActionGoal> DoorDetectorActionGoalPtr;
typedef boost::shared_ptr< ::door_detector_pal::DoorDetectorActionGoal const> DoorDetectorActionGoalConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace door_detector_pal

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b5a58e3b24f820b81b1418234a646da0";
  }

  static const char* value(const  ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb5a58e3b24f820b8ULL;
  static const uint64_t static_value2 = 0x1b1418234a646da0ULL;
};

template<class ContainerAllocator>
struct DataType< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "door_detector_pal/DoorDetectorActionGoal";
  }

  static const char* value(const  ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalID goal_id\n\
DoorDetectorGoal goal\n\
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
MSG: door_detector_pal/DoorDetectorGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Goal\n\
# votation == 0 -> Stop\n\
# votation >  0 -> votation is the number of times in a row we need to detect again door closed/open to return results\n\
int8 votation\n\
\n\
";
  }

  static const char* value(const  ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.goal_id);
    stream.next(m.goal);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct DoorDetectorActionGoal_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::door_detector_pal::DoorDetectorActionGoal_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
s << std::endl;
    Printer< ::door_detector_pal::DoorDetectorGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};


} // namespace message_operations
} // namespace ros

#endif // DOOR_DETECTOR_PAL_MESSAGE_DOORDETECTORACTIONGOAL_H
