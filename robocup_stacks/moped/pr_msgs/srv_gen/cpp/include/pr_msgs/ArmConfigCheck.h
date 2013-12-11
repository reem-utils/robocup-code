/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/srv/ArmConfigCheck.srv */
#ifndef PR_MSGS_SERVICE_ARMCONFIGCHECK_H
#define PR_MSGS_SERVICE_ARMCONFIGCHECK_H
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

#include "sensor_msgs/JointState.h"



namespace pr_msgs
{
template <class ContainerAllocator>
struct ArmConfigCheckRequest_ {
  typedef ArmConfigCheckRequest_<ContainerAllocator> Type;

  ArmConfigCheckRequest_()
  : joint_state()
  {
  }

  ArmConfigCheckRequest_(const ContainerAllocator& _alloc)
  : joint_state(_alloc)
  {
  }

  typedef  ::sensor_msgs::JointState_<ContainerAllocator>  _joint_state_type;
   ::sensor_msgs::JointState_<ContainerAllocator>  joint_state;


  typedef boost::shared_ptr< ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ArmConfigCheckRequest
typedef  ::pr_msgs::ArmConfigCheckRequest_<std::allocator<void> > ArmConfigCheckRequest;

typedef boost::shared_ptr< ::pr_msgs::ArmConfigCheckRequest> ArmConfigCheckRequestPtr;
typedef boost::shared_ptr< ::pr_msgs::ArmConfigCheckRequest const> ArmConfigCheckRequestConstPtr;


template <class ContainerAllocator>
struct ArmConfigCheckResponse_ {
  typedef ArmConfigCheckResponse_<ContainerAllocator> Type;

  ArmConfigCheckResponse_()
  : current_self_collision(false)
  , current_env_collision(false)
  , future_self_collision(false)
  , future_env_collision(false)
  , current_joint_limits_exceeded(false)
  , future_joint_limits_exceeded(false)
  {
  }

  ArmConfigCheckResponse_(const ContainerAllocator& _alloc)
  : current_self_collision(false)
  , current_env_collision(false)
  , future_self_collision(false)
  , future_env_collision(false)
  , current_joint_limits_exceeded(false)
  , future_joint_limits_exceeded(false)
  {
  }

  typedef uint8_t _current_self_collision_type;
  uint8_t current_self_collision;

  typedef uint8_t _current_env_collision_type;
  uint8_t current_env_collision;

  typedef uint8_t _future_self_collision_type;
  uint8_t future_self_collision;

  typedef uint8_t _future_env_collision_type;
  uint8_t future_env_collision;

  typedef uint8_t _current_joint_limits_exceeded_type;
  uint8_t current_joint_limits_exceeded;

  typedef uint8_t _future_joint_limits_exceeded_type;
  uint8_t future_joint_limits_exceeded;


  typedef boost::shared_ptr< ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ArmConfigCheckResponse
typedef  ::pr_msgs::ArmConfigCheckResponse_<std::allocator<void> > ArmConfigCheckResponse;

typedef boost::shared_ptr< ::pr_msgs::ArmConfigCheckResponse> ArmConfigCheckResponsePtr;
typedef boost::shared_ptr< ::pr_msgs::ArmConfigCheckResponse const> ArmConfigCheckResponseConstPtr;

struct ArmConfigCheck
{

typedef ArmConfigCheckRequest Request;
typedef ArmConfigCheckResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct ArmConfigCheck
} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "9ca061465ef0ed08771ed240c43789f5";
  }

  static const char* value(const  ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x9ca061465ef0ed08ULL;
  static const uint64_t static_value2 = 0x771ed240c43789f5ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/ArmConfigCheckRequest";
  }

  static const char* value(const  ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "sensor_msgs/JointState joint_state\n\
\n\
================================================================================\n\
MSG: sensor_msgs/JointState\n\
# This is a message that holds data to describe the state of a set of torque controlled joints. \n\
#\n\
# The state of each joint (revolute or prismatic) is defined by:\n\
#  * the position of the joint (rad or m),\n\
#  * the velocity of the joint (rad/s or m/s) and \n\
#  * the effort that is applied in the joint (Nm or N).\n\
#\n\
# Each joint is uniquely identified by its name\n\
# The header specifies the time at which the joint states were recorded. All the joint states\n\
# in one message have to be recorded at the same time.\n\
#\n\
# This message consists of a multiple arrays, one for each part of the joint state. \n\
# The goal is to make each of the fields optional. When e.g. your joints have no\n\
# effort associated with them, you can leave the effort array empty. \n\
#\n\
# All arrays in this message should have the same size, or be empty.\n\
# This is the only way to uniquely associate the joint name with the correct\n\
# states.\n\
\n\
\n\
Header header\n\
\n\
string[] name\n\
float64[] position\n\
float64[] velocity\n\
float64[] effort\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "27773a29cfec7a99cc44eea74da93860";
  }

  static const char* value(const  ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x27773a29cfec7a99ULL;
  static const uint64_t static_value2 = 0xcc44eea74da93860ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/ArmConfigCheckResponse";
  }

  static const char* value(const  ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool current_self_collision\n\
bool current_env_collision\n\
bool future_self_collision\n\
bool future_env_collision\n\
\n\
bool current_joint_limits_exceeded\n\
bool future_joint_limits_exceeded\n\
\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.joint_state);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ArmConfigCheckRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.current_self_collision);
    stream.next(m.current_env_collision);
    stream.next(m.future_self_collision);
    stream.next(m.future_env_collision);
    stream.next(m.current_joint_limits_exceeded);
    stream.next(m.future_joint_limits_exceeded);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ArmConfigCheckResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<pr_msgs::ArmConfigCheck> {
  static const char* value() 
  {
    return "a5df7a19c6f627a079d9c14658ecf093";
  }

  static const char* value(const pr_msgs::ArmConfigCheck&) { return value(); } 
};

template<>
struct DataType<pr_msgs::ArmConfigCheck> {
  static const char* value() 
  {
    return "pr_msgs/ArmConfigCheck";
  }

  static const char* value(const pr_msgs::ArmConfigCheck&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "a5df7a19c6f627a079d9c14658ecf093";
  }

  static const char* value(const pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/ArmConfigCheck";
  }

  static const char* value(const pr_msgs::ArmConfigCheckRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "a5df7a19c6f627a079d9c14658ecf093";
  }

  static const char* value(const pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/ArmConfigCheck";
  }

  static const char* value(const pr_msgs::ArmConfigCheckResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // PR_MSGS_SERVICE_ARMCONFIGCHECK_H

