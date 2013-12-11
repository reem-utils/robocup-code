/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_motion_detector/msg/MotionDetectorActionGoal.msg */
#ifndef IRI_MOTION_DETECTOR_MESSAGE_MOTIONDETECTORACTIONGOAL_H
#define IRI_MOTION_DETECTOR_MESSAGE_MOTIONDETECTORACTIONGOAL_H
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


namespace iri_motion_detector
{
template <class ContainerAllocator>
struct MotionDetectorActionGoal_ {
  typedef MotionDetectorActionGoal_<ContainerAllocator> Type;

  MotionDetectorActionGoal_()
  {
  }

  MotionDetectorActionGoal_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct MotionDetectorActionGoal
typedef  ::iri_motion_detector::MotionDetectorActionGoal_<std::allocator<void> > MotionDetectorActionGoal;

typedef boost::shared_ptr< ::iri_motion_detector::MotionDetectorActionGoal> MotionDetectorActionGoalPtr;
typedef boost::shared_ptr< ::iri_motion_detector::MotionDetectorActionGoal const> MotionDetectorActionGoalConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_motion_detector

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_motion_detector/MotionDetectorActionGoal";
  }

  static const char* value(const  ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the goal\n\
\n\
\n\
";
  }

  static const char* value(const  ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct MotionDetectorActionGoal_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_motion_detector::MotionDetectorActionGoal_<ContainerAllocator> & v) 
  {
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_MOTION_DETECTOR_MESSAGE_MOTIONDETECTORACTIONGOAL_H

