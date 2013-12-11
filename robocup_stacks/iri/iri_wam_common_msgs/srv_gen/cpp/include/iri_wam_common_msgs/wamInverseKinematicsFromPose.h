/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_wam_common_msgs/srv/wamInverseKinematicsFromPose.srv */
#ifndef IRI_WAM_COMMON_MSGS_SERVICE_WAMINVERSEKINEMATICSFROMPOSE_H
#define IRI_WAM_COMMON_MSGS_SERVICE_WAMINVERSEKINEMATICSFROMPOSE_H
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
#include "geometry_msgs/PoseStamped.h"


#include "sensor_msgs/JointState.h"

namespace iri_wam_common_msgs
{
template <class ContainerAllocator>
struct wamInverseKinematicsFromPoseRequest_ {
  typedef wamInverseKinematicsFromPoseRequest_<ContainerAllocator> Type;

  wamInverseKinematicsFromPoseRequest_()
  : current_joints()
  , desired_pose()
  {
  }

  wamInverseKinematicsFromPoseRequest_(const ContainerAllocator& _alloc)
  : current_joints(_alloc)
  , desired_pose(_alloc)
  {
  }

  typedef  ::sensor_msgs::JointState_<ContainerAllocator>  _current_joints_type;
   ::sensor_msgs::JointState_<ContainerAllocator>  current_joints;

  typedef  ::geometry_msgs::PoseStamped_<ContainerAllocator>  _desired_pose_type;
   ::geometry_msgs::PoseStamped_<ContainerAllocator>  desired_pose;


  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct wamInverseKinematicsFromPoseRequest
typedef  ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<std::allocator<void> > wamInverseKinematicsFromPoseRequest;

typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest> wamInverseKinematicsFromPoseRequestPtr;
typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest const> wamInverseKinematicsFromPoseRequestConstPtr;


template <class ContainerAllocator>
struct wamInverseKinematicsFromPoseResponse_ {
  typedef wamInverseKinematicsFromPoseResponse_<ContainerAllocator> Type;

  wamInverseKinematicsFromPoseResponse_()
  : desired_joints()
  {
  }

  wamInverseKinematicsFromPoseResponse_(const ContainerAllocator& _alloc)
  : desired_joints(_alloc)
  {
  }

  typedef  ::sensor_msgs::JointState_<ContainerAllocator>  _desired_joints_type;
   ::sensor_msgs::JointState_<ContainerAllocator>  desired_joints;


  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct wamInverseKinematicsFromPoseResponse
typedef  ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<std::allocator<void> > wamInverseKinematicsFromPoseResponse;

typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse> wamInverseKinematicsFromPoseResponsePtr;
typedef boost::shared_ptr< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse const> wamInverseKinematicsFromPoseResponseConstPtr;

struct wamInverseKinematicsFromPose
{

typedef wamInverseKinematicsFromPoseRequest Request;
typedef wamInverseKinematicsFromPoseResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct wamInverseKinematicsFromPose
} // namespace iri_wam_common_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "be8fec34cd428186cfc1337e06f88da0";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xbe8fec34cd428186ULL;
  static const uint64_t static_value2 = 0xcfc1337e06f88da0ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamInverseKinematicsFromPoseRequest";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
sensor_msgs/JointState current_joints\n\
geometry_msgs/PoseStamped desired_pose\n\
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
================================================================================\n\
MSG: geometry_msgs/PoseStamped\n\
# A Pose with reference coordinate frame and timestamp\n\
Header header\n\
Pose pose\n\
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

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "40a9639c04de352ae9a0ff36925bbb6a";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x40a9639c04de352aULL;
  static const uint64_t static_value2 = 0xe9a0ff36925bbb6aULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamInverseKinematicsFromPoseResponse";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
sensor_msgs/JointState desired_joints\n\
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

  static const char* value(const  ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.current_joints);
    stream.next(m.desired_pose);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct wamInverseKinematicsFromPoseRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.desired_joints);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct wamInverseKinematicsFromPoseResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<iri_wam_common_msgs::wamInverseKinematicsFromPose> {
  static const char* value() 
  {
    return "7e13d4c3acd3af5f93705f0bcad791ff";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematicsFromPose&) { return value(); } 
};

template<>
struct DataType<iri_wam_common_msgs::wamInverseKinematicsFromPose> {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamInverseKinematicsFromPose";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematicsFromPose&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "7e13d4c3acd3af5f93705f0bcad791ff";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamInverseKinematicsFromPose";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematicsFromPoseRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "7e13d4c3acd3af5f93705f0bcad791ff";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamInverseKinematicsFromPose";
  }

  static const char* value(const iri_wam_common_msgs::wamInverseKinematicsFromPoseResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IRI_WAM_COMMON_MSGS_SERVICE_WAMINVERSEKINEMATICSFROMPOSE_H
