/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/reem_mocks/upperbody_mock/msg/UpperBodyGoal.msg */
#ifndef UPPERBODY_MOCK_MESSAGE_UPPERBODYGOAL_H
#define UPPERBODY_MOCK_MESSAGE_UPPERBODYGOAL_H
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


namespace upperbody_mock
{
template <class ContainerAllocator>
struct UpperBodyGoal_ {
  typedef UpperBodyGoal_<ContainerAllocator> Type;

  UpperBodyGoal_()
  : motion_file()
  , validate_trajectory(false)
  {
  }

  UpperBodyGoal_(const ContainerAllocator& _alloc)
  : motion_file(_alloc)
  , validate_trajectory(false)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _motion_file_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  motion_file;

  typedef uint8_t _validate_trajectory_type;
  uint8_t validate_trajectory;


  typedef boost::shared_ptr< ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::upperbody_mock::UpperBodyGoal_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct UpperBodyGoal
typedef  ::upperbody_mock::UpperBodyGoal_<std::allocator<void> > UpperBodyGoal;

typedef boost::shared_ptr< ::upperbody_mock::UpperBodyGoal> UpperBodyGoalPtr;
typedef boost::shared_ptr< ::upperbody_mock::UpperBodyGoal const> UpperBodyGoalConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace upperbody_mock

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::upperbody_mock::UpperBodyGoal_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "01ac87505eebb9c7b9fa60cf18135069";
  }

  static const char* value(const  ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x01ac87505eebb9c7ULL;
  static const uint64_t static_value2 = 0xb9fa60cf18135069ULL;
};

template<class ContainerAllocator>
struct DataType< ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "upperbody_mock/UpperBodyGoal";
  }

  static const char* value(const  ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# goal\n\
# name of XML file containing motions for the robot\n\
string motion_file\n\
\n\
# true if trajectory validation is to be performed\n\
bool validate_trajectory\n\
\n\
";
  }

  static const char* value(const  ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.motion_file);
    stream.next(m.validate_trajectory);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct UpperBodyGoal_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::upperbody_mock::UpperBodyGoal_<ContainerAllocator> & v) 
  {
    s << indent << "motion_file: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.motion_file);
    s << indent << "validate_trajectory: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.validate_trajectory);
  }
};


} // namespace message_operations
} // namespace ros

#endif // UPPERBODY_MOCK_MESSAGE_UPPERBODYGOAL_H
