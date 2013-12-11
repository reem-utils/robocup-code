/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/srv/Enable.srv */
#ifndef PR_MSGS_SERVICE_ENABLE_H
#define PR_MSGS_SERVICE_ENABLE_H
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
struct EnableRequest_ {
  typedef EnableRequest_<ContainerAllocator> Type;

  EnableRequest_()
  : Enable(false)
  {
  }

  EnableRequest_(const ContainerAllocator& _alloc)
  : Enable(false)
  {
  }

  typedef uint8_t _Enable_type;
  uint8_t Enable;


  typedef boost::shared_ptr< ::pr_msgs::EnableRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::EnableRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct EnableRequest
typedef  ::pr_msgs::EnableRequest_<std::allocator<void> > EnableRequest;

typedef boost::shared_ptr< ::pr_msgs::EnableRequest> EnableRequestPtr;
typedef boost::shared_ptr< ::pr_msgs::EnableRequest const> EnableRequestConstPtr;


template <class ContainerAllocator>
struct EnableResponse_ {
  typedef EnableResponse_<ContainerAllocator> Type;

  EnableResponse_()
  : ok(false)
  , reason()
  {
  }

  EnableResponse_(const ContainerAllocator& _alloc)
  : ok(false)
  , reason(_alloc)
  {
  }

  typedef uint8_t _ok_type;
  uint8_t ok;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _reason_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  reason;


  typedef boost::shared_ptr< ::pr_msgs::EnableResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::EnableResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct EnableResponse
typedef  ::pr_msgs::EnableResponse_<std::allocator<void> > EnableResponse;

typedef boost::shared_ptr< ::pr_msgs::EnableResponse> EnableResponsePtr;
typedef boost::shared_ptr< ::pr_msgs::EnableResponse const> EnableResponseConstPtr;

struct Enable
{

typedef EnableRequest Request;
typedef EnableResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct Enable
} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::EnableRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::EnableRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::EnableRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "132b53c6b897b73e7dc72146d30f3b1e";
  }

  static const char* value(const  ::pr_msgs::EnableRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x132b53c6b897b73eULL;
  static const uint64_t static_value2 = 0x7dc72146d30f3b1eULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::EnableRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/EnableRequest";
  }

  static const char* value(const  ::pr_msgs::EnableRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::EnableRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool Enable\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::EnableRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::pr_msgs::EnableRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::EnableResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::EnableResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::EnableResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4679398f882e7cbdea165980d3ec2888";
  }

  static const char* value(const  ::pr_msgs::EnableResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x4679398f882e7cbdULL;
  static const uint64_t static_value2 = 0xea165980d3ec2888ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::EnableResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/EnableResponse";
  }

  static const char* value(const  ::pr_msgs::EnableResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::EnableResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool ok\n\
string reason\n\
\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::EnableResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::EnableRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.Enable);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct EnableRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::EnableResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.ok);
    stream.next(m.reason);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct EnableResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<pr_msgs::Enable> {
  static const char* value() 
  {
    return "46e2c93ae1cc7896720bf5acee0f2e89";
  }

  static const char* value(const pr_msgs::Enable&) { return value(); } 
};

template<>
struct DataType<pr_msgs::Enable> {
  static const char* value() 
  {
    return "pr_msgs/Enable";
  }

  static const char* value(const pr_msgs::Enable&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::EnableRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "46e2c93ae1cc7896720bf5acee0f2e89";
  }

  static const char* value(const pr_msgs::EnableRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::EnableRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/Enable";
  }

  static const char* value(const pr_msgs::EnableRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::EnableResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "46e2c93ae1cc7896720bf5acee0f2e89";
  }

  static const char* value(const pr_msgs::EnableResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::EnableResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/Enable";
  }

  static const char* value(const pr_msgs::EnableResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // PR_MSGS_SERVICE_ENABLE_H

