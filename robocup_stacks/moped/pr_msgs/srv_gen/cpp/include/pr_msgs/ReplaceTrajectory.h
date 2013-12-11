/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/srv/ReplaceTrajectory.srv */
#ifndef PR_MSGS_SERVICE_REPLACETRAJECTORY_H
#define PR_MSGS_SERVICE_REPLACETRAJECTORY_H
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

#include "pr_msgs/JointTraj.h"



namespace pr_msgs
{
template <class ContainerAllocator>
struct ReplaceTrajectoryRequest_ {
  typedef ReplaceTrajectoryRequest_<ContainerAllocator> Type;

  ReplaceTrajectoryRequest_()
  : traj()
  , id(0)
  {
  }

  ReplaceTrajectoryRequest_(const ContainerAllocator& _alloc)
  : traj(_alloc)
  , id(0)
  {
  }

  typedef  ::pr_msgs::JointTraj_<ContainerAllocator>  _traj_type;
   ::pr_msgs::JointTraj_<ContainerAllocator>  traj;

  typedef uint32_t _id_type;
  uint32_t id;


  typedef boost::shared_ptr< ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ReplaceTrajectoryRequest
typedef  ::pr_msgs::ReplaceTrajectoryRequest_<std::allocator<void> > ReplaceTrajectoryRequest;

typedef boost::shared_ptr< ::pr_msgs::ReplaceTrajectoryRequest> ReplaceTrajectoryRequestPtr;
typedef boost::shared_ptr< ::pr_msgs::ReplaceTrajectoryRequest const> ReplaceTrajectoryRequestConstPtr;


template <class ContainerAllocator>
struct ReplaceTrajectoryResponse_ {
  typedef ReplaceTrajectoryResponse_<ContainerAllocator> Type;

  ReplaceTrajectoryResponse_()
  : id(0)
  {
  }

  ReplaceTrajectoryResponse_(const ContainerAllocator& _alloc)
  : id(0)
  {
  }

  typedef uint32_t _id_type;
  uint32_t id;


  typedef boost::shared_ptr< ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ReplaceTrajectoryResponse
typedef  ::pr_msgs::ReplaceTrajectoryResponse_<std::allocator<void> > ReplaceTrajectoryResponse;

typedef boost::shared_ptr< ::pr_msgs::ReplaceTrajectoryResponse> ReplaceTrajectoryResponsePtr;
typedef boost::shared_ptr< ::pr_msgs::ReplaceTrajectoryResponse const> ReplaceTrajectoryResponseConstPtr;

struct ReplaceTrajectory
{

typedef ReplaceTrajectoryRequest Request;
typedef ReplaceTrajectoryResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct ReplaceTrajectory
} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "f88b0684f828fc14e642b3386053416d";
  }

  static const char* value(const  ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xf88b0684f828fc14ULL;
  static const uint64_t static_value2 = 0xe642b3386053416dULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/ReplaceTrajectoryRequest";
  }

  static const char* value(const  ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/JointTraj traj\n\
uint32 id\n\
\n\
================================================================================\n\
MSG: pr_msgs/JointTraj\n\
pr_msgs/Joints[] positions\n\
float32[] blend_radius\n\
uint32 options\n\
\n\
# options should be powers of 2, so that they can be OR'd together\n\
uint32 opt_WaitForStart=1\n\
uint32 opt_CancelOnStall=2\n\
uint32 opt_CancelOnForceInput=4\n\
uint32 opt_CancelOnTactileInput=8\n\
#uint32 opt_          =16  # placeholder for next value\n\
\n\
================================================================================\n\
MSG: pr_msgs/Joints\n\
float64[] j\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "309d4b30834b338cced19e5622a97a03";
  }

  static const char* value(const  ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x309d4b30834b338cULL;
  static const uint64_t static_value2 = 0xced19e5622a97a03ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/ReplaceTrajectoryResponse";
  }

  static const char* value(const  ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "uint32 id\n\
\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.traj);
    stream.next(m.id);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ReplaceTrajectoryRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.id);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ReplaceTrajectoryResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<pr_msgs::ReplaceTrajectory> {
  static const char* value() 
  {
    return "97dd1d908c94df542702cce333822c2a";
  }

  static const char* value(const pr_msgs::ReplaceTrajectory&) { return value(); } 
};

template<>
struct DataType<pr_msgs::ReplaceTrajectory> {
  static const char* value() 
  {
    return "pr_msgs/ReplaceTrajectory";
  }

  static const char* value(const pr_msgs::ReplaceTrajectory&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "97dd1d908c94df542702cce333822c2a";
  }

  static const char* value(const pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/ReplaceTrajectory";
  }

  static const char* value(const pr_msgs::ReplaceTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "97dd1d908c94df542702cce333822c2a";
  }

  static const char* value(const pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/ReplaceTrajectory";
  }

  static const char* value(const pr_msgs::ReplaceTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // PR_MSGS_SERVICE_REPLACETRAJECTORY_H

