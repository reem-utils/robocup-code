/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/estirabot_msgs/srv/TransformPose.srv */
#ifndef ESTIRABOT_MSGS_SERVICE_TRANSFORMPOSE_H
#define ESTIRABOT_MSGS_SERVICE_TRANSFORMPOSE_H
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


#include "geometry_msgs/PoseStamped.h"

namespace estirabot_msgs
{
template <class ContainerAllocator>
struct TransformPoseRequest_ {
  typedef TransformPoseRequest_<ContainerAllocator> Type;

  TransformPoseRequest_()
  : orig_pose_st()
  , target_frame()
  {
  }

  TransformPoseRequest_(const ContainerAllocator& _alloc)
  : orig_pose_st(_alloc)
  , target_frame(_alloc)
  {
  }

  typedef  ::geometry_msgs::PoseStamped_<ContainerAllocator>  _orig_pose_st_type;
   ::geometry_msgs::PoseStamped_<ContainerAllocator>  orig_pose_st;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _target_frame_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  target_frame;


  typedef boost::shared_ptr< ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct TransformPoseRequest
typedef  ::estirabot_msgs::TransformPoseRequest_<std::allocator<void> > TransformPoseRequest;

typedef boost::shared_ptr< ::estirabot_msgs::TransformPoseRequest> TransformPoseRequestPtr;
typedef boost::shared_ptr< ::estirabot_msgs::TransformPoseRequest const> TransformPoseRequestConstPtr;


template <class ContainerAllocator>
struct TransformPoseResponse_ {
  typedef TransformPoseResponse_<ContainerAllocator> Type;

  TransformPoseResponse_()
  : target_pose_st()
  {
  }

  TransformPoseResponse_(const ContainerAllocator& _alloc)
  : target_pose_st(_alloc)
  {
  }

  typedef  ::geometry_msgs::PoseStamped_<ContainerAllocator>  _target_pose_st_type;
   ::geometry_msgs::PoseStamped_<ContainerAllocator>  target_pose_st;


  typedef boost::shared_ptr< ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct TransformPoseResponse
typedef  ::estirabot_msgs::TransformPoseResponse_<std::allocator<void> > TransformPoseResponse;

typedef boost::shared_ptr< ::estirabot_msgs::TransformPoseResponse> TransformPoseResponsePtr;
typedef boost::shared_ptr< ::estirabot_msgs::TransformPoseResponse const> TransformPoseResponseConstPtr;

struct TransformPose
{

typedef TransformPoseRequest Request;
typedef TransformPoseResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct TransformPose
} // namespace estirabot_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "5c3b8f582e3ffb1d002f2aa68fef2c7a";
  }

  static const char* value(const  ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x5c3b8f582e3ffb1dULL;
  static const uint64_t static_value2 = 0x002f2aa68fef2c7aULL;
};

template<class ContainerAllocator>
struct DataType< ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/TransformPoseRequest";
  }

  static const char* value(const  ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "geometry_msgs/PoseStamped orig_pose_st\n\
string target_frame\n\
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

  static const char* value(const  ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "80b8c3ae5a4a56d7e393f8ea4d9bb994";
  }

  static const char* value(const  ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x80b8c3ae5a4a56d7ULL;
  static const uint64_t static_value2 = 0xe393f8ea4d9bb994ULL;
};

template<class ContainerAllocator>
struct DataType< ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/TransformPoseResponse";
  }

  static const char* value(const  ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "geometry_msgs/PoseStamped target_pose_st\n\
\n\
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

  static const char* value(const  ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::estirabot_msgs::TransformPoseRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.orig_pose_st);
    stream.next(m.target_frame);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct TransformPoseRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::estirabot_msgs::TransformPoseResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.target_pose_st);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct TransformPoseResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<estirabot_msgs::TransformPose> {
  static const char* value() 
  {
    return "d970a793ffec2eaf87d550a3deb0c796";
  }

  static const char* value(const estirabot_msgs::TransformPose&) { return value(); } 
};

template<>
struct DataType<estirabot_msgs::TransformPose> {
  static const char* value() 
  {
    return "estirabot_msgs/TransformPose";
  }

  static const char* value(const estirabot_msgs::TransformPose&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<estirabot_msgs::TransformPoseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d970a793ffec2eaf87d550a3deb0c796";
  }

  static const char* value(const estirabot_msgs::TransformPoseRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<estirabot_msgs::TransformPoseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/TransformPose";
  }

  static const char* value(const estirabot_msgs::TransformPoseRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<estirabot_msgs::TransformPoseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d970a793ffec2eaf87d550a3deb0c796";
  }

  static const char* value(const estirabot_msgs::TransformPoseResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<estirabot_msgs::TransformPoseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/TransformPose";
  }

  static const char* value(const estirabot_msgs::TransformPoseResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // ESTIRABOT_MSGS_SERVICE_TRANSFORMPOSE_H

