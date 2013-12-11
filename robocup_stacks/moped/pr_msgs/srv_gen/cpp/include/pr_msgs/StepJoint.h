/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/srv/StepJoint.srv */
#ifndef PR_MSGS_SERVICE_STEPJOINT_H
#define PR_MSGS_SERVICE_STEPJOINT_H
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
struct StepJointRequest_ {
  typedef StepJointRequest_<ContainerAllocator> Type;

  StepJointRequest_()
  : joint(0)
  , radians(0.0)
  {
  }

  StepJointRequest_(const ContainerAllocator& _alloc)
  : joint(0)
  , radians(0.0)
  {
  }

  typedef uint8_t _joint_type;
  uint8_t joint;

  typedef double _radians_type;
  double radians;


  typedef boost::shared_ptr< ::pr_msgs::StepJointRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::StepJointRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct StepJointRequest
typedef  ::pr_msgs::StepJointRequest_<std::allocator<void> > StepJointRequest;

typedef boost::shared_ptr< ::pr_msgs::StepJointRequest> StepJointRequestPtr;
typedef boost::shared_ptr< ::pr_msgs::StepJointRequest const> StepJointRequestConstPtr;


template <class ContainerAllocator>
struct StepJointResponse_ {
  typedef StepJointResponse_<ContainerAllocator> Type;

  StepJointResponse_()
  {
  }

  StepJointResponse_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::pr_msgs::StepJointResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::StepJointResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct StepJointResponse
typedef  ::pr_msgs::StepJointResponse_<std::allocator<void> > StepJointResponse;

typedef boost::shared_ptr< ::pr_msgs::StepJointResponse> StepJointResponsePtr;
typedef boost::shared_ptr< ::pr_msgs::StepJointResponse const> StepJointResponseConstPtr;

struct StepJoint
{

typedef StepJointRequest Request;
typedef StepJointResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct StepJoint
} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::StepJointRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::StepJointRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::StepJointRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e76fd844c151f2b85b89aba56e105bdc";
  }

  static const char* value(const  ::pr_msgs::StepJointRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xe76fd844c151f2b8ULL;
  static const uint64_t static_value2 = 0x5b89aba56e105bdcULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::StepJointRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/StepJointRequest";
  }

  static const char* value(const  ::pr_msgs::StepJointRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::StepJointRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "uint8 joint\n\
float64 radians\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::StepJointRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::pr_msgs::StepJointRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::StepJointResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::StepJointResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::StepJointResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::pr_msgs::StepJointResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::StepJointResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/StepJointResponse";
  }

  static const char* value(const  ::pr_msgs::StepJointResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::StepJointResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::StepJointResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::pr_msgs::StepJointResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::StepJointRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.joint);
    stream.next(m.radians);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct StepJointRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::StepJointResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct StepJointResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<pr_msgs::StepJoint> {
  static const char* value() 
  {
    return "e76fd844c151f2b85b89aba56e105bdc";
  }

  static const char* value(const pr_msgs::StepJoint&) { return value(); } 
};

template<>
struct DataType<pr_msgs::StepJoint> {
  static const char* value() 
  {
    return "pr_msgs/StepJoint";
  }

  static const char* value(const pr_msgs::StepJoint&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::StepJointRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e76fd844c151f2b85b89aba56e105bdc";
  }

  static const char* value(const pr_msgs::StepJointRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::StepJointRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/StepJoint";
  }

  static const char* value(const pr_msgs::StepJointRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::StepJointResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e76fd844c151f2b85b89aba56e105bdc";
  }

  static const char* value(const pr_msgs::StepJointResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::StepJointResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/StepJoint";
  }

  static const char* value(const pr_msgs::StepJointResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // PR_MSGS_SERVICE_STEPJOINT_H

