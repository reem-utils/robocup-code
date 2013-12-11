/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/estirabot_msgs/srv/ArmMovementsPosesSrv.srv */
#ifndef ESTIRABOT_MSGS_SERVICE_ARMMOVEMENTSPOSESSRV_H
#define ESTIRABOT_MSGS_SERVICE_ARMMOVEMENTSPOSESSRV_H
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



namespace estirabot_msgs
{
template <class ContainerAllocator>
struct ArmMovementsPosesSrvRequest_ {
  typedef ArmMovementsPosesSrvRequest_<ContainerAllocator> Type;

  ArmMovementsPosesSrvRequest_()
  : poses()
  , secondary_arm()
  , plane_coefficients()
  , movement_type(0)
  {
  }

  ArmMovementsPosesSrvRequest_(const ContainerAllocator& _alloc)
  : poses(_alloc)
  , secondary_arm(_alloc)
  , plane_coefficients(_alloc)
  , movement_type(0)
  {
  }

  typedef std::vector< ::geometry_msgs::PoseStamped_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::PoseStamped_<ContainerAllocator> >::other >  _poses_type;
  std::vector< ::geometry_msgs::PoseStamped_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::PoseStamped_<ContainerAllocator> >::other >  poses;

  typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _secondary_arm_type;
  std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  secondary_arm;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _plane_coefficients_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  plane_coefficients;

  typedef uint8_t _movement_type_type;
  uint8_t movement_type;


  typedef boost::shared_ptr< ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ArmMovementsPosesSrvRequest
typedef  ::estirabot_msgs::ArmMovementsPosesSrvRequest_<std::allocator<void> > ArmMovementsPosesSrvRequest;

typedef boost::shared_ptr< ::estirabot_msgs::ArmMovementsPosesSrvRequest> ArmMovementsPosesSrvRequestPtr;
typedef boost::shared_ptr< ::estirabot_msgs::ArmMovementsPosesSrvRequest const> ArmMovementsPosesSrvRequestConstPtr;


template <class ContainerAllocator>
struct ArmMovementsPosesSrvResponse_ {
  typedef ArmMovementsPosesSrvResponse_<ContainerAllocator> Type;

  ArmMovementsPosesSrvResponse_()
  : success(false)
  , too_far_points_indexes()
  {
  }

  ArmMovementsPosesSrvResponse_(const ContainerAllocator& _alloc)
  : success(false)
  , too_far_points_indexes(_alloc)
  {
  }

  typedef uint8_t _success_type;
  uint8_t success;

  typedef std::vector<uint32_t, typename ContainerAllocator::template rebind<uint32_t>::other >  _too_far_points_indexes_type;
  std::vector<uint32_t, typename ContainerAllocator::template rebind<uint32_t>::other >  too_far_points_indexes;


  typedef boost::shared_ptr< ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ArmMovementsPosesSrvResponse
typedef  ::estirabot_msgs::ArmMovementsPosesSrvResponse_<std::allocator<void> > ArmMovementsPosesSrvResponse;

typedef boost::shared_ptr< ::estirabot_msgs::ArmMovementsPosesSrvResponse> ArmMovementsPosesSrvResponsePtr;
typedef boost::shared_ptr< ::estirabot_msgs::ArmMovementsPosesSrvResponse const> ArmMovementsPosesSrvResponseConstPtr;

struct ArmMovementsPosesSrv
{

typedef ArmMovementsPosesSrvRequest Request;
typedef ArmMovementsPosesSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct ArmMovementsPosesSrv
} // namespace estirabot_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b21012be072db3abc0ae9ef5270fd1e3";
  }

  static const char* value(const  ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb21012be072db3abULL;
  static const uint64_t static_value2 = 0xc0ae9ef5270fd1e3ULL;
};

template<class ContainerAllocator>
struct DataType< ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/ArmMovementsPosesSrvRequest";
  }

  static const char* value(const  ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
geometry_msgs/PoseStamped[] poses\n\
\n\
bool[] secondary_arm\n\
\n\
float32[] plane_coefficients\n\
\n\
\n\
uint8 movement_type\n\
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

  static const char* value(const  ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "a964b72cbcc23dde94a9f7a989f6928b";
  }

  static const char* value(const  ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xa964b72cbcc23ddeULL;
  static const uint64_t static_value2 = 0x94a9f7a989f6928bULL;
};

template<class ContainerAllocator>
struct DataType< ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/ArmMovementsPosesSrvResponse";
  }

  static const char* value(const  ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
bool success\n\
\n\
uint32[] too_far_points_indexes\n\
\n\
";
  }

  static const char* value(const  ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.poses);
    stream.next(m.secondary_arm);
    stream.next(m.plane_coefficients);
    stream.next(m.movement_type);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ArmMovementsPosesSrvRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.success);
    stream.next(m.too_far_points_indexes);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ArmMovementsPosesSrvResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<estirabot_msgs::ArmMovementsPosesSrv> {
  static const char* value() 
  {
    return "c44995b3495201366633238004174553";
  }

  static const char* value(const estirabot_msgs::ArmMovementsPosesSrv&) { return value(); } 
};

template<>
struct DataType<estirabot_msgs::ArmMovementsPosesSrv> {
  static const char* value() 
  {
    return "estirabot_msgs/ArmMovementsPosesSrv";
  }

  static const char* value(const estirabot_msgs::ArmMovementsPosesSrv&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "c44995b3495201366633238004174553";
  }

  static const char* value(const estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/ArmMovementsPosesSrv";
  }

  static const char* value(const estirabot_msgs::ArmMovementsPosesSrvRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "c44995b3495201366633238004174553";
  }

  static const char* value(const estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/ArmMovementsPosesSrv";
  }

  static const char* value(const estirabot_msgs::ArmMovementsPosesSrvResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // ESTIRABOT_MSGS_SERVICE_ARMMOVEMENTSPOSESSRV_H

