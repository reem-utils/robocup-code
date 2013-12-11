/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg/ImagePoint.msg */
#ifndef IRI_PERCEPTION_MSGS_MESSAGE_IMAGEPOINT_H
#define IRI_PERCEPTION_MSGS_MESSAGE_IMAGEPOINT_H
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


namespace iri_perception_msgs
{
template <class ContainerAllocator>
struct ImagePoint_ {
  typedef ImagePoint_<ContainerAllocator> Type;

  ImagePoint_()
  : x(0)
  , y(0)
  {
  }

  ImagePoint_(const ContainerAllocator& _alloc)
  : x(0)
  , y(0)
  {
  }

  typedef uint32_t _x_type;
  uint32_t x;

  typedef uint32_t _y_type;
  uint32_t y;


  typedef boost::shared_ptr< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_perception_msgs::ImagePoint_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ImagePoint
typedef  ::iri_perception_msgs::ImagePoint_<std::allocator<void> > ImagePoint;

typedef boost::shared_ptr< ::iri_perception_msgs::ImagePoint> ImagePointPtr;
typedef boost::shared_ptr< ::iri_perception_msgs::ImagePoint const> ImagePointConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_perception_msgs::ImagePoint_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_perception_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::ImagePoint_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> > {
  static const char* value() 
  {
    return "64be90712af6ea79ae6f103da824ffcf";
  }

  static const char* value(const  ::iri_perception_msgs::ImagePoint_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x64be90712af6ea79ULL;
  static const uint64_t static_value2 = 0xae6f103da824ffcfULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/ImagePoint";
  }

  static const char* value(const  ::iri_perception_msgs::ImagePoint_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> > {
  static const char* value() 
  {
    return "uint32 x\n\
uint32 y\n\
";
  }

  static const char* value(const  ::iri_perception_msgs::ImagePoint_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.x);
    stream.next(m.y);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ImagePoint_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_perception_msgs::ImagePoint_<ContainerAllocator> & v) 
  {
    s << indent << "x: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.y);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_PERCEPTION_MSGS_MESSAGE_IMAGEPOINT_H

