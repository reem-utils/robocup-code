/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_motion_detector/msg/MotionDetectorActionActionGoal.msg */
#ifndef IRI_MOTION_DETECTOR_MESSAGE_MOTIONDETECTORACTIONACTIONGOAL_H
#define IRI_MOTION_DETECTOR_MESSAGE_MOTIONDETECTORACTIONACTIONGOAL_H
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
#include "iri_motion_detector/MotionDetectorActionGoal.h"

namespace iri_motion_detector
{
template <class ContainerAllocator>
struct MotionDetectorActionActionGoal_ {
  typedef MotionDetectorActionActionGoal_<ContainerAllocator> Type;

  MotionDetectorActionActionGoal_()
  : header()
  , goal_id()
  , goal()
  {
  }

  MotionDetectorActionActionGoal_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , goal_id(_alloc)
  , goal(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
   ::actionlib_msgs::GoalID_<ContainerAllocator>  goal_id;

  typedef  ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator>  _goal_type;
   ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator>  goal;


  typedef boost::shared_ptr< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct MotionDetectorActionActionGoal
typedef  ::iri_motion_detector::MotionDetectorActionActionGoal_<std::allocator<void> > MotionDetectorActionActionGoal;

typedef boost::shared_ptr< ::iri_motion_detector::MotionDetectorActionActionGoal> MotionDetectorActionActionGoalPtr;
typedef boost::shared_ptr< ::iri_motion_detector::MotionDetectorActionActionGoal const> MotionDetectorActionActionGoalConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_motion_detector

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4b30be6cd12b9e72826df56b481f40e0";
  }

  static const char* value(const  ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x4b30be6cd12b9e72ULL;
  static const uint64_t static_value2 = 0x826df56b481f40e0ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_motion_detector/MotionDetectorActionActionGoal";
  }

  static const char* value(const  ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalID goal_id\n\
MotionDetectorActionGoal goal\n\
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
MSG: iri_motion_detector/MotionDetectorActionGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the goal\n\
\n\
\n\
";
  }

  static const char* value(const  ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.goal_id);
    stream.next(m.goal);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct MotionDetectorActionActionGoal_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_motion_detector::MotionDetectorActionActionGoal_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
s << std::endl;
    Printer< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_MOTION_DETECTOR_MESSAGE_MOTIONDETECTORACTIONACTIONGOAL_H

