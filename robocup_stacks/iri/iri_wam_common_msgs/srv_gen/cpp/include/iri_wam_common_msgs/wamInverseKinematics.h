/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_wam_common_msgs/srv/wamInverseKinematics.srv */
#ifndef IRI_WAM_COMMON_MSGS_SERVICE_WAMINVERSEKINEMATICS_H
#define IRI_WAM_COMMON_MSGS_SERVICE_WAMINVERSEKINEMATICS_H
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

#include "geometry_msgs/PoseStamped.h"


#include "sensor_msgs/JointState.h"

namespace iri_wam_common_msgs
{
template <class ContainerAllocator>
struct wamInverseKinematicsRequest_ {
  typedef wamInverseKinematicsRequest_<ContainerAllocator> Type;

  wamInverseKinematicsRequest_()
  : pose()
  {
  }

  wamInverseKinematicsRequest_(const ContainerAllocator& _alloc)
  : pose(_alloc)
  {
  }

  typedef  ::geometry_msgs::PoseStamped_<ContainerAllocator>  _pose_type;
   ::geometry_msgs::PoseStamped_<ContainerAllocator>  pose;


  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct wamInverseKinematicsRequest
typedef  ::iri_wam_common_msgs::wamInverseKinematicsRequest_<std::allocator<void> > wamInverseKinematicsRequest;

typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsRequest> wamInverseKinematicsRequestPtr;
typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsRequest const> wamInverseKinematicsRequestConstPtr;


template <class ContainerAllocator>
struct wamInverseKinematicsResponse_ {
  typedef wamInverseKinematicsResponse_<ContainerAllocator> Type;

  wamInverseKinematicsResponse_()
  : joints()
  {
  }

  wamInverseKinematicsResponse_(const ContainerAllocator& _alloc)
  : joints(_alloc)
  {
  }

  typedef  ::sensor_msgs::JointState_<ContainerAllocator>  _joints_type;
   ::sensor_msgs::JointState_<ContainerAllocator>  joints;


  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct wamInverseKinematicsResponse
typedef  ::iri_wam_common_msgs::wamInverseKinematicsResponse_<std::allocator<void> > wamInverseKinematicsResponse;

typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsResponse> wamInverseKinematicsResponsePtr;
typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsResponse const> wamInverseKinematicsResponseConstPtr;

struct wamInverseKinematics
{

typedef wamInverseKinematicsRequest Request;
typedef wamInverseKinematicsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct wamInverseKinematics
} // namespace iri_wam_common_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "3f8930d968a3e84d471dff917bb1cdae";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x3f8930d968a3e84dULL;
  static const uint64_t static_value2 = 0x471dff917bb1cdaeULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamInverseKinematicsRequest";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
geometry_msgs/PoseStamped pose\n\
\n\
================================================================================\n\
MSG: geometry_msgs/PoseStamped\n\
# A Pose with reference coordinate frame and timestamp\n\
Header header\n\
Pose pose\n\
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
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "13b568889983e6c4080c58d8e7c2c89c";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x13b568889983e6c4ULL;
  static const uint64_t static_value2 = 0x080c58d8e7c2c89cULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamInverseKinematicsResponse";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
sensor_msgs/JointState joints\n\
\n\
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

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.pose);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct wamInverseKinematicsRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.joints);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct wamInverseKinematicsResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<iri_wam_common_msgs::wamInverseKinematics> {
  static const char* value() 
  {
    return "8ac06277c177a69b8a112af3d82067a8";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematics&) { return value(); } 
};

template<>
struct DataType<iri_wam_common_msgs::wamInverseKinematics> {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamInverseKinematics";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematics&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "8ac06277c177a69b8a112af3d82067a8";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamInverseKinematics";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematicsRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "8ac06277c177a69b8a112af3d82067a8";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamInverseKinematics";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematicsResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IRI_WAM_COMMON_MSGS_SERVICE_WAMINVERSEKINEMATICS_H

