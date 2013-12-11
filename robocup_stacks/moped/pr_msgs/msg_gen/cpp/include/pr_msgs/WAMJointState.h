/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/msg/WAMJointState.msg */
#ifndef PR_MSGS_MESSAGE_WAMJOINTSTATE_H
#define PR_MSGS_MESSAGE_WAMJOINTSTATE_H
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

namespace pr_msgs
{
template <class ContainerAllocator>
struct WAMJointState_ {
  typedef WAMJointState_<ContainerAllocator> Type;

  WAMJointState_()
  : header()
  , positions()
  , positions_commanded()
  , torques()
  {
  }

  WAMJointState_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , positions(_alloc)
  , positions_commanded(_alloc)
  , torques(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _positions_type;
  std::vector<double, typename ContainerAllocator::template rebind<double>::other >  positions;

  typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _positions_commanded_type;
  std::vector<double, typename ContainerAllocator::template rebind<double>::other >  positions_commanded;

  typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _torques_type;
  std::vector<double, typename ContainerAllocator::template rebind<double>::other >  torques;


  typedef boost::shared_ptr< ::pr_msgs::WAMJointState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::WAMJointState_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct WAMJointState
typedef  ::pr_msgs::WAMJointState_<std::allocator<void> > WAMJointState;

typedef boost::shared_ptr< ::pr_msgs::WAMJointState> WAMJointStatePtr;
typedef boost::shared_ptr< ::pr_msgs::WAMJointState const> WAMJointStateConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::pr_msgs::WAMJointState_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::pr_msgs::WAMJointState_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::WAMJointState_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::WAMJointState_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::WAMJointState_<ContainerAllocator> > {
  static const char* value() 
  {
    return "9c5a0c31ef05f2ab6b4baacc5cbc9e0d";
  }

  static const char* value(const  ::pr_msgs::WAMJointState_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x9c5a0c31ef05f2abULL;
  static const uint64_t static_value2 = 0x6b4baacc5cbc9e0dULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::WAMJointState_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/WAMJointState";
  }

  static const char* value(const  ::pr_msgs::WAMJointState_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::WAMJointState_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
float64[] positions\n\
float64[] positions_commanded\n\
float64[] torques\n\
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
";
  }

  static const char* value(const  ::pr_msgs::WAMJointState_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::pr_msgs::WAMJointState_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::pr_msgs::WAMJointState_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::WAMJointState_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.positions);
    stream.next(m.positions_commanded);
    stream.next(m.torques);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct WAMJointState_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pr_msgs::WAMJointState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::pr_msgs::WAMJointState_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "positions[]" << std::endl;
    for (size_t i = 0; i < v.positions.size(); ++i)
    {
      s << indent << "  positions[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.positions[i]);
    }
    s << indent << "positions_commanded[]" << std::endl;
    for (size_t i = 0; i < v.positions_commanded.size(); ++i)
    {
      s << indent << "  positions_commanded[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.positions_commanded[i]);
    }
    s << indent << "torques[]" << std::endl;
    for (size_t i = 0; i < v.torques.size(); ++i)
    {
      s << indent << "  torques[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.torques[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // PR_MSGS_MESSAGE_WAMJOINTSTATE_H

