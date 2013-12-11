/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/msg/JointTraj.msg */
#ifndef PR_MSGS_MESSAGE_JOINTTRAJ_H
#define PR_MSGS_MESSAGE_JOINTTRAJ_H
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

#include "pr_msgs/Joints.h"

namespace pr_msgs
{
template <class ContainerAllocator>
struct JointTraj_ {
  typedef JointTraj_<ContainerAllocator> Type;

  JointTraj_()
  : positions()
  , blend_radius()
  , options(0)
  {
  }

  JointTraj_(const ContainerAllocator& _alloc)
  : positions(_alloc)
  , blend_radius(_alloc)
  , options(0)
  {
  }

  typedef std::vector< ::pr_msgs::Joints_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::pr_msgs::Joints_<ContainerAllocator> >::other >  _positions_type;
  std::vector< ::pr_msgs::Joints_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::pr_msgs::Joints_<ContainerAllocator> >::other >  positions;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _blend_radius_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  blend_radius;

  typedef uint32_t _options_type;
  uint32_t options;

  enum { opt_WaitForStart = 1 };
  enum { opt_CancelOnStall = 2 };
  enum { opt_CancelOnForceInput = 4 };
  enum { opt_CancelOnTactileInput = 8 };

  typedef boost::shared_ptr< ::pr_msgs::JointTraj_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::JointTraj_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct JointTraj
typedef  ::pr_msgs::JointTraj_<std::allocator<void> > JointTraj;

typedef boost::shared_ptr< ::pr_msgs::JointTraj> JointTrajPtr;
typedef boost::shared_ptr< ::pr_msgs::JointTraj const> JointTrajConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::pr_msgs::JointTraj_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::pr_msgs::JointTraj_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::JointTraj_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::JointTraj_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::JointTraj_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e07c641f5910e182dc37fb7a39f1367d";
  }

  static const char* value(const  ::pr_msgs::JointTraj_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xe07c641f5910e182ULL;
  static const uint64_t static_value2 = 0xdc37fb7a39f1367dULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::JointTraj_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/JointTraj";
  }

  static const char* value(const  ::pr_msgs::JointTraj_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::JointTraj_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/Joints[] positions\n\
float32[] blend_radius\n\
uint32 options\n\
\n\
# options should be powers of 2, so that they can be OR'd together\n\
uint32 opt_WaitForStart=1\n\
uint32 opt_CancelOnStall=2\n\
uint32 opt_CancelOnForceInput=4\n\
uint32 opt_CancelOnTactileInput=8\n\
#uint32 opt_          =16  # placeholder for next value\n\
\n\
================================================================================\n\
MSG: pr_msgs/Joints\n\
float64[] j\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::JointTraj_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::JointTraj_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.positions);
    stream.next(m.blend_radius);
    stream.next(m.options);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct JointTraj_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pr_msgs::JointTraj_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::pr_msgs::JointTraj_<ContainerAllocator> & v) 
  {
    s << indent << "positions[]" << std::endl;
    for (size_t i = 0; i < v.positions.size(); ++i)
    {
      s << indent << "  positions[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::pr_msgs::Joints_<ContainerAllocator> >::stream(s, indent + "    ", v.positions[i]);
    }
    s << indent << "blend_radius[]" << std::endl;
    for (size_t i = 0; i < v.blend_radius.size(); ++i)
    {
      s << indent << "  blend_radius[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.blend_radius[i]);
    }
    s << indent << "options: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.options);
  }
};


} // namespace message_operations
} // namespace ros

#endif // PR_MSGS_MESSAGE_JOINTTRAJ_H

