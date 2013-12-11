/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/srv/PauseTrajectory.srv */
#ifndef PR_MSGS_SERVICE_PAUSETRAJECTORY_H
#define PR_MSGS_SERVICE_PAUSETRAJECTORY_H
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
struct PauseTrajectoryRequest_ {
  typedef PauseTrajectoryRequest_<ContainerAllocator> Type;

  PauseTrajectoryRequest_()
  : pause(0)
  {
  }

  PauseTrajectoryRequest_(const ContainerAllocator& _alloc)
  : pause(0)
  {
  }

  typedef int8_t _pause_type;
  int8_t pause;


  typedef boost::shared_ptr< ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct PauseTrajectoryRequest
typedef  ::pr_msgs::PauseTrajectoryRequest_<std::allocator<void> > PauseTrajectoryRequest;

typedef boost::shared_ptr< ::pr_msgs::PauseTrajectoryRequest> PauseTrajectoryRequestPtr;
typedef boost::shared_ptr< ::pr_msgs::PauseTrajectoryRequest const> PauseTrajectoryRequestConstPtr;


template <class ContainerAllocator>
struct PauseTrajectoryResponse_ {
  typedef PauseTrajectoryResponse_<ContainerAllocator> Type;

  PauseTrajectoryResponse_()
  : ok(false)
  , reason()
  {
  }

  PauseTrajectoryResponse_(const ContainerAllocator& _alloc)
  : ok(false)
  , reason(_alloc)
  {
  }

  typedef uint8_t _ok_type;
  uint8_t ok;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _reason_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  reason;


  typedef boost::shared_ptr< ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct PauseTrajectoryResponse
typedef  ::pr_msgs::PauseTrajectoryResponse_<std::allocator<void> > PauseTrajectoryResponse;

typedef boost::shared_ptr< ::pr_msgs::PauseTrajectoryResponse> PauseTrajectoryResponsePtr;
typedef boost::shared_ptr< ::pr_msgs::PauseTrajectoryResponse const> PauseTrajectoryResponseConstPtr;

struct PauseTrajectory
{

typedef PauseTrajectoryRequest Request;
typedef PauseTrajectoryResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct PauseTrajectory
} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "0151c2e2197311074b70533572da3f44";
  }

  static const char* value(const  ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x0151c2e219731107ULL;
  static const uint64_t static_value2 = 0x4b70533572da3f44ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/PauseTrajectoryRequest";
  }

  static const char* value(const  ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int8 pause\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4679398f882e7cbdea165980d3ec2888";
  }

  static const char* value(const  ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x4679398f882e7cbdULL;
  static const uint64_t static_value2 = 0xea165980d3ec2888ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/PauseTrajectoryResponse";
  }

  static const char* value(const  ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool ok\n\
string reason\n\
\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.pause);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct PauseTrajectoryRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.ok);
    stream.next(m.reason);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct PauseTrajectoryResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<pr_msgs::PauseTrajectory> {
  static const char* value() 
  {
    return "a759747906bdd01f886076169018d26e";
  }

  static const char* value(const pr_msgs::PauseTrajectory&) { return value(); } 
};

template<>
struct DataType<pr_msgs::PauseTrajectory> {
  static const char* value() 
  {
    return "pr_msgs/PauseTrajectory";
  }

  static const char* value(const pr_msgs::PauseTrajectory&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "a759747906bdd01f886076169018d26e";
  }

  static const char* value(const pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/PauseTrajectory";
  }

  static const char* value(const pr_msgs::PauseTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "a759747906bdd01f886076169018d26e";
  }

  static const char* value(const pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/PauseTrajectory";
  }

  static const char* value(const pr_msgs::PauseTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // PR_MSGS_SERVICE_PAUSETRAJECTORY_H

