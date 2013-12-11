/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/srv/GetHandProperty.srv */
#ifndef PR_MSGS_SERVICE_GETHANDPROPERTY_H
#define PR_MSGS_SERVICE_GETHANDPROPERTY_H
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

#include "ros/service_traits.h"




namespace pr_msgs
{
template <class ContainerAllocator>
struct GetHandPropertyRequest_ {
  typedef GetHandPropertyRequest_<ContainerAllocator> Type;

  GetHandPropertyRequest_()
  : nodeid(0)
  , property(0)
  {
  }

  GetHandPropertyRequest_(const ContainerAllocator& _alloc)
  : nodeid(0)
  , property(0)
  {
  }

  typedef int32_t _nodeid_type;
  int32_t nodeid;

  typedef int32_t _property_type;
  int32_t property;


  typedef boost::shared_ptr< ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct GetHandPropertyRequest
typedef  ::pr_msgs::GetHandPropertyRequest_<std::allocator<void> > GetHandPropertyRequest;

typedef boost::shared_ptr< ::pr_msgs::GetHandPropertyRequest> GetHandPropertyRequestPtr;
typedef boost::shared_ptr< ::pr_msgs::GetHandPropertyRequest const> GetHandPropertyRequestConstPtr;


template <class ContainerAllocator>
struct GetHandPropertyResponse_ {
  typedef GetHandPropertyResponse_<ContainerAllocator> Type;

  GetHandPropertyResponse_()
  : value(0)
  , ok(false)
  , reason()
  {
  }

  GetHandPropertyResponse_(const ContainerAllocator& _alloc)
  : value(0)
  , ok(false)
  , reason(_alloc)
  {
  }

  typedef int32_t _value_type;
  int32_t value;

  typedef uint8_t _ok_type;
  uint8_t ok;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _reason_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  reason;


  typedef boost::shared_ptr< ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct GetHandPropertyResponse
typedef  ::pr_msgs::GetHandPropertyResponse_<std::allocator<void> > GetHandPropertyResponse;

typedef boost::shared_ptr< ::pr_msgs::GetHandPropertyResponse> GetHandPropertyResponsePtr;
typedef boost::shared_ptr< ::pr_msgs::GetHandPropertyResponse const> GetHandPropertyResponseConstPtr;

struct GetHandProperty
{

typedef GetHandPropertyRequest Request;
typedef GetHandPropertyResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct GetHandProperty
} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "9ed9d5b98f25032a6d549c1cb96e061b";
  }

  static const char* value(const  ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x9ed9d5b98f25032aULL;
  static const uint64_t static_value2 = 0x6d549c1cb96e061bULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/GetHandPropertyRequest";
  }

  static const char* value(const  ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int32 nodeid\n\
int32 property\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "1a586ea1d6033f5c3d181e12f9b4e533";
  }

  static const char* value(const  ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x1a586ea1d6033f5cULL;
  static const uint64_t static_value2 = 0x3d181e12f9b4e533ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/GetHandPropertyResponse";
  }

  static const char* value(const  ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int32 value\n\
bool ok\n\
string reason\n\
\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::GetHandPropertyRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.nodeid);
    stream.next(m.property);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GetHandPropertyRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::GetHandPropertyResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.value);
    stream.next(m.ok);
    stream.next(m.reason);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GetHandPropertyResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<pr_msgs::GetHandProperty> {
  static const char* value() 
  {
    return "2dcf1331b4912a45435689f10658fe42";
  }

  static const char* value(const pr_msgs::GetHandProperty&) { return value(); } 
};

template<>
struct DataType<pr_msgs::GetHandProperty> {
  static const char* value() 
  {
    return "pr_msgs/GetHandProperty";
  }

  static const char* value(const pr_msgs::GetHandProperty&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::GetHandPropertyRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "2dcf1331b4912a45435689f10658fe42";
  }

  static const char* value(const pr_msgs::GetHandPropertyRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::GetHandPropertyRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/GetHandProperty";
  }

  static const char* value(const pr_msgs::GetHandPropertyRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::GetHandPropertyResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "2dcf1331b4912a45435689f10658fe42";
  }

  static const char* value(const pr_msgs::GetHandPropertyResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::GetHandPropertyResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/GetHandProperty";
  }

  static const char* value(const pr_msgs::GetHandPropertyResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // PR_MSGS_SERVICE_GETHANDPROPERTY_H

