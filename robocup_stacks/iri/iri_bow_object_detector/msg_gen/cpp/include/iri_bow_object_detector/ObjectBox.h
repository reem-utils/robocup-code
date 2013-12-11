/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/msg/ObjectBox.msg */
#ifndef IRI_BOW_OBJECT_DETECTOR_MESSAGE_OBJECTBOX_H
#define IRI_BOW_OBJECT_DETECTOR_MESSAGE_OBJECTBOX_H
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

#include "iri_perception_msgs/ImagePoint.h"
#include "iri_perception_msgs/ImagePoint.h"

namespace iri_bow_object_detector
{
template <class ContainerAllocator>
struct ObjectBox_ {
  typedef ObjectBox_<ContainerAllocator> Type;

  ObjectBox_()
  : point1()
  , point2()
  , value(0.0)
  {
  }

  ObjectBox_(const ContainerAllocator& _alloc)
  : point1(_alloc)
  , point2(_alloc)
  , value(0.0)
  {
  }

  typedef  ::iri_perception_msgs::ImagePoint_<ContainerAllocator>  _point1_type;
   ::iri_perception_msgs::ImagePoint_<ContainerAllocator>  point1;

  typedef  ::iri_perception_msgs::ImagePoint_<ContainerAllocator>  _point2_type;
   ::iri_perception_msgs::ImagePoint_<ContainerAllocator>  point2;

  typedef float _value_type;
  float value;


  typedef boost::shared_ptr< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ObjectBox
typedef  ::iri_bow_object_detector::ObjectBox_<std::allocator<void> > ObjectBox;

typedef boost::shared_ptr< ::iri_bow_object_detector::ObjectBox> ObjectBoxPtr;
typedef boost::shared_ptr< ::iri_bow_object_detector::ObjectBox const> ObjectBoxConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_bow_object_detector

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> > {
  static const char* value() 
  {
    return "3b124018a1260659fa76923e9a54718c";
  }

  static const char* value(const  ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x3b124018a1260659ULL;
  static const uint64_t static_value2 = 0xfa76923e9a54718cULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_bow_object_detector/ObjectBox";
  }

  static const char* value(const  ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/ImagePoint point1\n\
iri_perception_msgs/ImagePoint point2\n\
float32 value\n\
================================================================================\n\
MSG: iri_perception_msgs/ImagePoint\n\
uint32 x\n\
uint32 y\n\
";
  }

  static const char* value(const  ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.point1);
    stream.next(m.point2);
    stream.next(m.value);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ObjectBox_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> & v) 
  {
    s << indent << "point1: ";
s << std::endl;
    Printer< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> >::stream(s, indent + "  ", v.point1);
    s << indent << "point2: ";
s << std::endl;
    Printer< ::iri_perception_msgs::ImagePoint_<ContainerAllocator> >::stream(s, indent + "  ", v.point2);
    s << indent << "value: ";
    Printer<float>::stream(s, indent + "  ", v.value);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_BOW_OBJECT_DETECTOR_MESSAGE_OBJECTBOX_H

