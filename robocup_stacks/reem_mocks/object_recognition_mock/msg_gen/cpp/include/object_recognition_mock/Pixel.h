/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/reem_mocks/object_recognition_mock/msg/Pixel.msg */
#ifndef OBJECT_RECOGNITION_MOCK_MESSAGE_PIXEL_H
#define OBJECT_RECOGNITION_MOCK_MESSAGE_PIXEL_H
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


namespace object_recognition_mock
{
template <class ContainerAllocator>
struct Pixel_ {
  typedef Pixel_<ContainerAllocator> Type;

  Pixel_()
  : x(0)
  , y(0)
  {
  }

  Pixel_(const ContainerAllocator& _alloc)
  : x(0)
  , y(0)
  {
  }

  typedef int32_t _x_type;
  int32_t x;

  typedef int32_t _y_type;
  int32_t y;


  typedef boost::shared_ptr< ::object_recognition_mock::Pixel_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::object_recognition_mock::Pixel_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct Pixel
typedef  ::object_recognition_mock::Pixel_<std::allocator<void> > Pixel;

typedef boost::shared_ptr< ::object_recognition_mock::Pixel> PixelPtr;
typedef boost::shared_ptr< ::object_recognition_mock::Pixel const> PixelConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::object_recognition_mock::Pixel_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::object_recognition_mock::Pixel_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace object_recognition_mock

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::object_recognition_mock::Pixel_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::object_recognition_mock::Pixel_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::object_recognition_mock::Pixel_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bd7b43fd41d4c47bf5c703cc7d016709";
  }

  static const char* value(const  ::object_recognition_mock::Pixel_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xbd7b43fd41d4c47bULL;
  static const uint64_t static_value2 = 0xf5c703cc7d016709ULL;
};

template<class ContainerAllocator>
struct DataType< ::object_recognition_mock::Pixel_<ContainerAllocator> > {
  static const char* value() 
  {
    return "object_recognition_mock/Pixel";
  }

  static const char* value(const  ::object_recognition_mock::Pixel_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::object_recognition_mock::Pixel_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# top-left corner: (0,0)\n\
\n\
int32 x\n\
int32 y\n\
";
  }

  static const char* value(const  ::object_recognition_mock::Pixel_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::object_recognition_mock::Pixel_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::object_recognition_mock::Pixel_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.x);
    stream.next(m.y);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct Pixel_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::object_recognition_mock::Pixel_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::object_recognition_mock::Pixel_<ContainerAllocator> & v) 
  {
    s << indent << "x: ";
    Printer<int32_t>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<int32_t>::stream(s, indent + "  ", v.y);
  }
};


} // namespace message_operations
} // namespace ros

#endif // OBJECT_RECOGNITION_MOCK_MESSAGE_PIXEL_H

