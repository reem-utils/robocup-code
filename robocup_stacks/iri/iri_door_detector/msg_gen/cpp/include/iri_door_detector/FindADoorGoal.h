/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_door_detector/msg/FindADoorGoal.msg */
#ifndef IRI_DOOR_DETECTOR_MESSAGE_FINDADOORGOAL_H
#define IRI_DOOR_DETECTOR_MESSAGE_FINDADOORGOAL_H
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


namespace iri_door_detector
{
template <class ContainerAllocator>
struct FindADoorGoal_ {
  typedef FindADoorGoal_<ContainerAllocator> Type;

  FindADoorGoal_()
  : start(0)
  {
  }

  FindADoorGoal_(const ContainerAllocator& _alloc)
  : start(0)
  {
  }

  typedef int8_t _start_type;
  int8_t start;


  typedef boost::shared_ptr< ::iri_door_detector::FindADoorGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_door_detector::FindADoorGoal_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct FindADoorGoal
typedef  ::iri_door_detector::FindADoorGoal_<std::allocator<void> > FindADoorGoal;

typedef boost::shared_ptr< ::iri_door_detector::FindADoorGoal> FindADoorGoalPtr;
typedef boost::shared_ptr< ::iri_door_detector::FindADoorGoal const> FindADoorGoalConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_door_detector::FindADoorGoal_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_door_detector::FindADoorGoal_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_door_detector

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_door_detector::FindADoorGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_door_detector::FindADoorGoal_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_door_detector::FindADoorGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "38a5030c9e97c3d3e682c962d13fed20";
  }

  static const char* value(const  ::iri_door_detector::FindADoorGoal_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x38a5030c9e97c3d3ULL;
  static const uint64_t static_value2 = 0xe682c962d13fed20ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_door_detector::FindADoorGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_door_detector/FindADoorGoal";
  }

  static const char* value(const  ::iri_door_detector::FindADoorGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_door_detector::FindADoorGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the goal\n\
int8 start\n\
\n\
";
  }

  static const char* value(const  ::iri_door_detector::FindADoorGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::iri_door_detector::FindADoorGoal_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_door_detector::FindADoorGoal_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.start);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct FindADoorGoal_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_door_detector::FindADoorGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_door_detector::FindADoorGoal_<ContainerAllocator> & v) 
  {
    s << indent << "start: ";
    Printer<int8_t>::stream(s, indent + "  ", v.start);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_DOOR_DETECTOR_MESSAGE_FINDADOORGOAL_H

