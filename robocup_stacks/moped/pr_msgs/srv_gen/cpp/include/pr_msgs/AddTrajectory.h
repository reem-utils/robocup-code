/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/srv/AddTrajectory.srv */
#ifndef PR_MSGS_SERVICE_ADDTRAJECTORY_H
#define PR_MSGS_SERVICE_ADDTRAJECTORY_H
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
struct AddTrajectoryRequest_ {
  typedef AddTrajectoryRequest_<ContainerAllocator> Type;

  AddTrajectoryRequest_()
  : traj()
  {
  }

  AddTrajectoryRequest_(const ContainerAllocator& _alloc)
  : traj(_alloc)
  {
  }

  typedef  ::pr_msgs::JointTraj_<ContainerAllocator>  _traj_type;
   ::pr_msgs::JointTraj_<ContainerAllocator>  traj;


  typedef boost::shared_ptr< ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct AddTrajectoryRequest
typedef  ::pr_msgs::AddTrajectoryRequest_<std::allocator<void> > AddTrajectoryRequest;

typedef boost::shared_ptr< ::pr_msgs::AddTrajectoryRequest> AddTrajectoryRequestPtr;
typedef boost::shared_ptr< ::pr_msgs::AddTrajectoryRequest const> AddTrajectoryRequestConstPtr;


template <class ContainerAllocator>
struct AddTrajectoryResponse_ {
  typedef AddTrajectoryResponse_<ContainerAllocator> Type;

  AddTrajectoryResponse_()
  : ok(false)
  , reason()
  , id(0)
  {
  }

  AddTrajectoryResponse_(const ContainerAllocator& _alloc)
  : ok(false)
  , reason(_alloc)
  , id(0)
  {
  }

  typedef uint8_t _ok_type;
  uint8_t ok;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _reason_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  reason;

  typedef uint32_t _id_type;
  uint32_t id;


  typedef boost::shared_ptr< ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct AddTrajectoryResponse
typedef  ::pr_msgs::AddTrajectoryResponse_<std::allocator<void> > AddTrajectoryResponse;

typedef boost::shared_ptr< ::pr_msgs::AddTrajectoryResponse> AddTrajectoryResponsePtr;
typedef boost::shared_ptr< ::pr_msgs::AddTrajectoryResponse const> AddTrajectoryResponseConstPtr;

struct AddTrajectory
{

typedef AddTrajectoryRequest Request;
typedef AddTrajectoryResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct AddTrajectory
} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "dac72239f9f69a87ec7747c7a90f2ad9";
  }

  static const char* value(const  ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xdac72239f9f69a87ULL;
  static const uint64_t static_value2 = 0xec7747c7a90f2ad9ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/AddTrajectoryRequest";
  }

  static const char* value(const  ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/JointTraj traj\n\
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

  static const char* value(const  ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "ad2e2c70d0557970f2c1628f5539a6dd";
  }

  static const char* value(const  ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xad2e2c70d0557970ULL;
  static const uint64_t static_value2 = 0xf2c1628f5539a6ddULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/AddTrajectoryResponse";
  }

  static const char* value(const  ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool ok\n\
string reason\n\
uint32 id\n\
\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::AddTrajectoryRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.traj);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct AddTrajectoryRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::AddTrajectoryResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.ok);
    stream.next(m.reason);
    stream.next(m.id);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct AddTrajectoryResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<pr_msgs::AddTrajectory> {
  static const char* value() 
  {
    return "718f35ed3e678fbf88689fadd359050d";
  }

  static const char* value(const pr_msgs::AddTrajectory&) { return value(); } 
};

template<>
struct DataType<pr_msgs::AddTrajectory> {
  static const char* value() 
  {
    return "pr_msgs/AddTrajectory";
  }

  static const char* value(const pr_msgs::AddTrajectory&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::AddTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "718f35ed3e678fbf88689fadd359050d";
  }

  static const char* value(const pr_msgs::AddTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::AddTrajectoryRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/AddTrajectory";
  }

  static const char* value(const pr_msgs::AddTrajectoryRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::AddTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "718f35ed3e678fbf88689fadd359050d";
  }

  static const char* value(const pr_msgs::AddTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::AddTrajectoryResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/AddTrajectory";
  }

  static const char* value(const pr_msgs::AddTrajectoryResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // PR_MSGS_SERVICE_ADDTRAJECTORY_H

