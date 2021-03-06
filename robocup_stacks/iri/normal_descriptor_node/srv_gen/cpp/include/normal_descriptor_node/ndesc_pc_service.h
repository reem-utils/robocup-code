/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/srv/ndesc_pc_service.srv */
#ifndef NORMAL_DESCRIPTOR_NODE_SERVICE_NDESC_PC_SERVICE_H
#define NORMAL_DESCRIPTOR_NODE_SERVICE_NDESC_PC_SERVICE_H
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

#include "sensor_msgs/PointCloud2.h"


#include "normal_descriptor_node/ndesc_pc.h"

namespace normal_descriptor_node
{
template <class ContainerAllocator>
struct ndesc_pc_serviceRequest_ {
  typedef ndesc_pc_serviceRequest_<ContainerAllocator> Type;

  ndesc_pc_serviceRequest_()
  : cloth_cloud()
  {
  }

  ndesc_pc_serviceRequest_(const ContainerAllocator& _alloc)
  : cloth_cloud(_alloc)
  {
  }

  typedef  ::sensor_msgs::PointCloud2_<ContainerAllocator>  _cloth_cloud_type;
   ::sensor_msgs::PointCloud2_<ContainerAllocator>  cloth_cloud;


  typedef boost::shared_ptr< ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ndesc_pc_serviceRequest
typedef  ::normal_descriptor_node::ndesc_pc_serviceRequest_<std::allocator<void> > ndesc_pc_serviceRequest;

typedef boost::shared_ptr< ::normal_descriptor_node::ndesc_pc_serviceRequest> ndesc_pc_serviceRequestPtr;
typedef boost::shared_ptr< ::normal_descriptor_node::ndesc_pc_serviceRequest const> ndesc_pc_serviceRequestConstPtr;


template <class ContainerAllocator>
struct ndesc_pc_serviceResponse_ {
  typedef ndesc_pc_serviceResponse_<ContainerAllocator> Type;

  ndesc_pc_serviceResponse_()
  : ndesc_pc_msg()
  {
  }

  ndesc_pc_serviceResponse_(const ContainerAllocator& _alloc)
  : ndesc_pc_msg(_alloc)
  {
  }

  typedef  ::normal_descriptor_node::ndesc_pc_<ContainerAllocator>  _ndesc_pc_msg_type;
   ::normal_descriptor_node::ndesc_pc_<ContainerAllocator>  ndesc_pc_msg;


  typedef boost::shared_ptr< ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ndesc_pc_serviceResponse
typedef  ::normal_descriptor_node::ndesc_pc_serviceResponse_<std::allocator<void> > ndesc_pc_serviceResponse;

typedef boost::shared_ptr< ::normal_descriptor_node::ndesc_pc_serviceResponse> ndesc_pc_serviceResponsePtr;
typedef boost::shared_ptr< ::normal_descriptor_node::ndesc_pc_serviceResponse const> ndesc_pc_serviceResponseConstPtr;

struct ndesc_pc_service
{

typedef ndesc_pc_serviceRequest Request;
typedef ndesc_pc_serviceResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct ndesc_pc_service
} // namespace normal_descriptor_node

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "0c9882caba11d56443567dca3aa788b1";
  }

  static const char* value(const  ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x0c9882caba11d564ULL;
  static const uint64_t static_value2 = 0x43567dca3aa788b1ULL;
};

template<class ContainerAllocator>
struct DataType< ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "normal_descriptor_node/ndesc_pc_serviceRequest";
  }

  static const char* value(const  ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "sensor_msgs/PointCloud2 cloth_cloud\n\
\n\
================================================================================\n\
MSG: sensor_msgs/PointCloud2\n\
# This message holds a collection of N-dimensional points, which may\n\
# contain additional information such as normals, intensity, etc. The\n\
# point data is stored as a binary blob, its layout described by the\n\
# contents of the \"fields\" array.\n\
\n\
# The point cloud data may be organized 2d (image-like) or 1d\n\
# (unordered). Point clouds organized as 2d images may be produced by\n\
# camera depth sensors such as stereo or time-of-flight.\n\
\n\
# Time of sensor data acquisition, and the coordinate frame ID (for 3d\n\
# points).\n\
Header header\n\
\n\
# 2D structure of the point cloud. If the cloud is unordered, height is\n\
# 1 and width is the length of the point cloud.\n\
uint32 height\n\
uint32 width\n\
\n\
# Describes the channels and their layout in the binary data blob.\n\
PointField[] fields\n\
\n\
bool    is_bigendian # Is this data bigendian?\n\
uint32  point_step   # Length of a point in bytes\n\
uint32  row_step     # Length of a row in bytes\n\
uint8[] data         # Actual point data, size is (row_step*height)\n\
\n\
bool is_dense        # True if there are no invalid points\n\
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
MSG: sensor_msgs/PointField\n\
# This message holds the description of one point entry in the\n\
# PointCloud2 message format.\n\
uint8 INT8    = 1\n\
uint8 UINT8   = 2\n\
uint8 INT16   = 3\n\
uint8 UINT16  = 4\n\
uint8 INT32   = 5\n\
uint8 UINT32  = 6\n\
uint8 FLOAT32 = 7\n\
uint8 FLOAT64 = 8\n\
\n\
string name      # Name of field\n\
uint32 offset    # Offset from start of point struct\n\
uint8  datatype  # Datatype enumeration, see above\n\
uint32 count     # How many elements in the field\n\
\n\
";
  }

  static const char* value(const  ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "8cdceef08036d5eb578c44812398184b";
  }

  static const char* value(const  ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x8cdceef08036d5ebULL;
  static const uint64_t static_value2 = 0x578c44812398184bULL;
};

template<class ContainerAllocator>
struct DataType< ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "normal_descriptor_node/ndesc_pc_serviceResponse";
  }

  static const char* value(const  ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "normal_descriptor_node/ndesc_pc ndesc_pc_msg\n\
\n\
\n\
================================================================================\n\
MSG: normal_descriptor_node/ndesc_pc\n\
Header header\n\
int32 num_orient_bins\n\
int32 num_spa_bins\n\
int32 num\n\
int32 len\n\
int32 width\n\
int32 height\n\
normal_descriptor_node/ndesc[] descriptors\n\
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
MSG: normal_descriptor_node/ndesc\n\
float32[] descriptor\n\
geometry_msgs/Vector3 point3d\n\
int32 u\n\
int32 v\n\
float32 ori\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const  ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.cloth_cloud);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ndesc_pc_serviceRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.ndesc_pc_msg);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ndesc_pc_serviceResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<normal_descriptor_node::ndesc_pc_service> {
  static const char* value() 
  {
    return "820ec8d4b51fd678aefcb5618d6d715c";
  }

  static const char* value(const normal_descriptor_node::ndesc_pc_service&) { return value(); } 
};

template<>
struct DataType<normal_descriptor_node::ndesc_pc_service> {
  static const char* value() 
  {
    return "normal_descriptor_node/ndesc_pc_service";
  }

  static const char* value(const normal_descriptor_node::ndesc_pc_service&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "820ec8d4b51fd678aefcb5618d6d715c";
  }

  static const char* value(const normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "normal_descriptor_node/ndesc_pc_service";
  }

  static const char* value(const normal_descriptor_node::ndesc_pc_serviceRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "820ec8d4b51fd678aefcb5618d6d715c";
  }

  static const char* value(const normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "normal_descriptor_node/ndesc_pc_service";
  }

  static const char* value(const normal_descriptor_node::ndesc_pc_serviceResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // NORMAL_DESCRIPTOR_NODE_SERVICE_NDESC_PC_SERVICE_H

