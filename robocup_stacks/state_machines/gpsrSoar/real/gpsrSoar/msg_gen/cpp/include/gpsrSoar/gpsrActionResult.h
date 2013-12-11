/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/state_machines/gpsrSoar/real/gpsrSoar/msg/gpsrActionResult.msg */
#ifndef GPSRSOAR_MESSAGE_GPSRACTIONRESULT_H
#define GPSRSOAR_MESSAGE_GPSRACTIONRESULT_H
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


namespace gpsrSoar
{
template <class ContainerAllocator>
struct gpsrActionResult_ {
  typedef gpsrActionResult_<ContainerAllocator> Type;

  gpsrActionResult_()
  : outcome()
  {
  }

  gpsrActionResult_(const ContainerAllocator& _alloc)
  : outcome(_alloc)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _outcome_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  outcome;


  typedef boost::shared_ptr< ::gpsrSoar::gpsrActionResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::gpsrSoar::gpsrActionResult_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct gpsrActionResult
typedef  ::gpsrSoar::gpsrActionResult_<std::allocator<void> > gpsrActionResult;

typedef boost::shared_ptr< ::gpsrSoar::gpsrActionResult> gpsrActionResultPtr;
typedef boost::shared_ptr< ::gpsrSoar::gpsrActionResult const> gpsrActionResultConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::gpsrSoar::gpsrActionResult_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::gpsrSoar::gpsrActionResult_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace gpsrSoar

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::gpsrSoar::gpsrActionResult_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::gpsrSoar::gpsrActionResult_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::gpsrSoar::gpsrActionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "2b95071cca675b3d5b80ad0bdaf20389";
  }

  static const char* value(const  ::gpsrSoar::gpsrActionResult_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x2b95071cca675b3dULL;
  static const uint64_t static_value2 = 0x5b80ad0bdaf20389ULL;
};

template<class ContainerAllocator>
struct DataType< ::gpsrSoar::gpsrActionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "gpsrSoar/gpsrActionResult";
  }

  static const char* value(const  ::gpsrSoar::gpsrActionResult_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::gpsrSoar::gpsrActionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#result definition\n\
string   outcome\n\
\n\
";
  }

  static const char* value(const  ::gpsrSoar::gpsrActionResult_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::gpsrSoar::gpsrActionResult_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.outcome);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct gpsrActionResult_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::gpsrSoar::gpsrActionResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::gpsrSoar::gpsrActionResult_<ContainerAllocator> & v) 
  {
    s << indent << "outcome: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.outcome);
  }
};


} // namespace message_operations
} // namespace ros

#endif // GPSRSOAR_MESSAGE_GPSRACTIONRESULT_H

