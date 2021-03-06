/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/msg/MaglevSense.msg */
#ifndef PR_MSGS_MESSAGE_MAGLEVSENSE_H
#define PR_MSGS_MESSAGE_MAGLEVSENSE_H
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


namespace pr_msgs
{
template <class ContainerAllocator>
struct MaglevSense_ {
  typedef MaglevSense_<ContainerAllocator> Type;

  MaglevSense_()
  : position()
  , force()
  {
  }

  MaglevSense_(const ContainerAllocator& _alloc)
  : position(_alloc)
  , force(_alloc)
  {
  }

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _position_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  position;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _force_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  force;


  typedef boost::shared_ptr< ::pr_msgs::MaglevSense_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::MaglevSense_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct MaglevSense
typedef  ::pr_msgs::MaglevSense_<std::allocator<void> > MaglevSense;

typedef boost::shared_ptr< ::pr_msgs::MaglevSense> MaglevSensePtr;
typedef boost::shared_ptr< ::pr_msgs::MaglevSense const> MaglevSenseConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::pr_msgs::MaglevSense_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::pr_msgs::MaglevSense_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::MaglevSense_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::MaglevSense_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::MaglevSense_<ContainerAllocator> > {
  static const char* value() 
  {
    return "82871840a2fd06a041e9e9618073ff7c";
  }

  static const char* value(const  ::pr_msgs::MaglevSense_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x82871840a2fd06a0ULL;
  static const uint64_t static_value2 = 0x41e9e9618073ff7cULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::MaglevSense_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/MaglevSense";
  }

  static const char* value(const  ::pr_msgs::MaglevSense_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::MaglevSense_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float32[] position\n\
float32[] force\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::MaglevSense_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::MaglevSense_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.position);
    stream.next(m.force);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct MaglevSense_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pr_msgs::MaglevSense_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::pr_msgs::MaglevSense_<ContainerAllocator> & v) 
  {
    s << indent << "position[]" << std::endl;
    for (size_t i = 0; i < v.position.size(); ++i)
    {
      s << indent << "  position[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.position[i]);
    }
    s << indent << "force[]" << std::endl;
    for (size_t i = 0; i < v.force.size(); ++i)
    {
      s << indent << "  force[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.force[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // PR_MSGS_MESSAGE_MAGLEVSENSE_H

