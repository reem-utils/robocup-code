/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/srv/CancelAllTrajectories.srv */
#ifndef PR_MSGS_SERVICE_CANCELALLTRAJECTORIES_H
#define PR_MSGS_SERVICE_CANCELALLTRAJECTORIES_H
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
struct CancelAllTrajectoriesRequest_ {
  typedef CancelAllTrajectoriesRequest_<ContainerAllocator> Type;

  CancelAllTrajectoriesRequest_()
  {
  }

  CancelAllTrajectoriesRequest_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct CancelAllTrajectoriesRequest
typedef  ::pr_msgs::CancelAllTrajectoriesRequest_<std::allocator<void> > CancelAllTrajectoriesRequest;

typedef boost::shared_ptr< ::pr_msgs::CancelAllTrajectoriesRequest> CancelAllTrajectoriesRequestPtr;
typedef boost::shared_ptr< ::pr_msgs::CancelAllTrajectoriesRequest const> CancelAllTrajectoriesRequestConstPtr;


template <class ContainerAllocator>
struct CancelAllTrajectoriesResponse_ {
  typedef CancelAllTrajectoriesResponse_<ContainerAllocator> Type;

  CancelAllTrajectoriesResponse_()
  : ok(false)
  , reason()
  {
  }

  CancelAllTrajectoriesResponse_(const ContainerAllocator& _alloc)
  : ok(false)
  , reason(_alloc)
  {
  }

  typedef uint8_t _ok_type;
  uint8_t ok;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _reason_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  reason;


  typedef boost::shared_ptr< ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct CancelAllTrajectoriesResponse
typedef  ::pr_msgs::CancelAllTrajectoriesResponse_<std::allocator<void> > CancelAllTrajectoriesResponse;

typedef boost::shared_ptr< ::pr_msgs::CancelAllTrajectoriesResponse> CancelAllTrajectoriesResponsePtr;
typedef boost::shared_ptr< ::pr_msgs::CancelAllTrajectoriesResponse const> CancelAllTrajectoriesResponseConstPtr;

struct CancelAllTrajectories
{

typedef CancelAllTrajectoriesRequest Request;
typedef CancelAllTrajectoriesResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct CancelAllTrajectories
} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/CancelAllTrajectoriesRequest";
  }

  static const char* value(const  ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
";
  }

  static const char* value(const  ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4679398f882e7cbdea165980d3ec2888";
  }

  static const char* value(const  ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x4679398f882e7cbdULL;
  static const uint64_t static_value2 = 0xea165980d3ec2888ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/CancelAllTrajectoriesResponse";
  }

  static const char* value(const  ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool ok\n\
string reason\n\
\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct CancelAllTrajectoriesRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.ok);
    stream.next(m.reason);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct CancelAllTrajectoriesResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<pr_msgs::CancelAllTrajectories> {
  static const char* value() 
  {
    return "4679398f882e7cbdea165980d3ec2888";
  }

  static const char* value(const pr_msgs::CancelAllTrajectories&) { return value(); } 
};

template<>
struct DataType<pr_msgs::CancelAllTrajectories> {
  static const char* value() 
  {
    return "pr_msgs/CancelAllTrajectories";
  }

  static const char* value(const pr_msgs::CancelAllTrajectories&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4679398f882e7cbdea165980d3ec2888";
  }

  static const char* value(const pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/CancelAllTrajectories";
  }

  static const char* value(const pr_msgs::CancelAllTrajectoriesRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4679398f882e7cbdea165980d3ec2888";
  }

  static const char* value(const pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/CancelAllTrajectories";
  }

  static const char* value(const pr_msgs::CancelAllTrajectoriesResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // PR_MSGS_SERVICE_CANCELALLTRAJECTORIES_H
