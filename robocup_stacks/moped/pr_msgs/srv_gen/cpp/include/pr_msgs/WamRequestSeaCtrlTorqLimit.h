/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/srv/WamRequestSeaCtrlTorqLimit.srv */
#ifndef PR_MSGS_SERVICE_WAMREQUESTSEACTRLTORQLIMIT_H
#define PR_MSGS_SERVICE_WAMREQUESTSEACTRLTORQLIMIT_H
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
struct WamRequestSeaCtrlTorqLimitRequest_ {
  typedef WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> Type;

  WamRequestSeaCtrlTorqLimitRequest_()
  {
  }

  WamRequestSeaCtrlTorqLimitRequest_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct WamRequestSeaCtrlTorqLimitRequest
typedef  ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<std::allocator<void> > WamRequestSeaCtrlTorqLimitRequest;

typedef boost::shared_ptr< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest> WamRequestSeaCtrlTorqLimitRequestPtr;
typedef boost::shared_ptr< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest const> WamRequestSeaCtrlTorqLimitRequestConstPtr;


template <class ContainerAllocator>
struct WamRequestSeaCtrlTorqLimitResponse_ {
  typedef WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> Type;

  WamRequestSeaCtrlTorqLimitResponse_()
  {
  }

  WamRequestSeaCtrlTorqLimitResponse_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct WamRequestSeaCtrlTorqLimitResponse
typedef  ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<std::allocator<void> > WamRequestSeaCtrlTorqLimitResponse;

typedef boost::shared_ptr< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse> WamRequestSeaCtrlTorqLimitResponsePtr;
typedef boost::shared_ptr< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse const> WamRequestSeaCtrlTorqLimitResponseConstPtr;

struct WamRequestSeaCtrlTorqLimit
{

typedef WamRequestSeaCtrlTorqLimitRequest Request;
typedef WamRequestSeaCtrlTorqLimitResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct WamRequestSeaCtrlTorqLimit
} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/WamRequestSeaCtrlTorqLimitRequest";
  }

  static const char* value(const  ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
";
  }

  static const char* value(const  ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/WamRequestSeaCtrlTorqLimitResponse";
  }

  static const char* value(const  ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct WamRequestSeaCtrlTorqLimitRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct WamRequestSeaCtrlTorqLimitResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<pr_msgs::WamRequestSeaCtrlTorqLimit> {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const pr_msgs::WamRequestSeaCtrlTorqLimit&) { return value(); } 
};

template<>
struct DataType<pr_msgs::WamRequestSeaCtrlTorqLimit> {
  static const char* value() 
  {
    return "pr_msgs/WamRequestSeaCtrlTorqLimit";
  }

  static const char* value(const pr_msgs::WamRequestSeaCtrlTorqLimit&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/WamRequestSeaCtrlTorqLimit";
  }

  static const char* value(const pr_msgs::WamRequestSeaCtrlTorqLimitRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/WamRequestSeaCtrlTorqLimit";
  }

  static const char* value(const pr_msgs::WamRequestSeaCtrlTorqLimitResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // PR_MSGS_SERVICE_WAMREQUESTSEACTRLTORQLIMIT_H
