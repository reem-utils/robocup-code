/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/srv/GetPointCloud2.srv */
#ifndef IRI_PERCEPTION_MSGS_SERVICE_GETPOINTCLOUD2_H
#define IRI_PERCEPTION_MSGS_SERVICE_GETPOINTCLOUD2_H
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

namespace iri_perception_msgs
{
template <class ContainerAllocator>
struct GetPointCloud2Request_ {
  typedef GetPointCloud2Request_<ContainerAllocator> Type;

  GetPointCloud2Request_()
  : topic()
  {
  }

  GetPointCloud2Request_(const ContainerAllocator& _alloc)
  : topic(_alloc)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _topic_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  topic;


  typedef boost::shared_ptr< ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct GetPointCloud2Request
typedef  ::iri_perception_msgs::GetPointCloud2Request_<std::allocator<void> > GetPointCloud2Request;

typedef boost::shared_ptr< ::iri_perception_msgs::GetPointCloud2Request> GetPointCloud2RequestPtr;
typedef boost::shared_ptr< ::iri_perception_msgs::GetPointCloud2Request const> GetPointCloud2RequestConstPtr;


template <class ContainerAllocator>
struct GetPointCloud2Response_ {
  typedef GetPointCloud2Response_<ContainerAllocator> Type;

  GetPointCloud2Response_()
  : pointcloud()
  {
  }

  GetPointCloud2Response_(const ContainerAllocator& _alloc)
  : pointcloud(_alloc)
  {
  }

  typedef  ::sensor_msgs::PointCloud2_<ContainerAllocator>  _pointcloud_type;
   ::sensor_msgs::PointCloud2_<ContainerAllocator>  pointcloud;


  typedef boost::shared_ptr< ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct GetPointCloud2Response
typedef  ::iri_perception_msgs::GetPointCloud2Response_<std::allocator<void> > GetPointCloud2Response;

typedef boost::shared_ptr< ::iri_perception_msgs::GetPointCloud2Response> GetPointCloud2ResponsePtr;
typedef boost::shared_ptr< ::iri_perception_msgs::GetPointCloud2Response const> GetPointCloud2ResponseConstPtr;

struct GetPointCloud2
{

typedef GetPointCloud2Request Request;
typedef GetPointCloud2Response Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct GetPointCloud2
} // namespace iri_perception_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d8f94bae31b356b24d0427f80426d0c3";
  }

  static const char* value(const  ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd8f94bae31b356b2ULL;
  static const uint64_t static_value2 = 0x4d0427f80426d0c3ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/GetPointCloud2Request";
  }

  static const char* value(const  ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
string topic\n\
\n\
";
  }

  static const char* value(const  ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> > {
  static const char* value() 
  {
    return "56680b720436a8fbd002ea7abe6966e1";
  }

  static const char* value(const  ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x56680b720436a8fbULL;
  static const uint64_t static_value2 = 0xd002ea7abe6966e1ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/GetPointCloud2Response";
  }

  static const char* value(const  ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
sensor_msgs/PointCloud2 pointcloud\n\
\n\
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

  static const char* value(const  ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.topic);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GetPointCloud2Request_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.pointcloud);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GetPointCloud2Response_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<iri_perception_msgs::GetPointCloud2> {
  static const char* value() 
  {
    return "31a6edbc839290281d09656fd7f53d42";
  }

  static const char* value(const iri_perception_msgs::GetPointCloud2&) { return value(); } 
};

template<>
struct DataType<iri_perception_msgs::GetPointCloud2> {
  static const char* value() 
  {
    return "iri_perception_msgs/GetPointCloud2";
  }

  static const char* value(const iri_perception_msgs::GetPointCloud2&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> > {
  static const char* value() 
  {
    return "31a6edbc839290281d09656fd7f53d42";
  }

  static const char* value(const iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/GetPointCloud2";
  }

  static const char* value(const iri_perception_msgs::GetPointCloud2Request_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> > {
  static const char* value() 
  {
    return "31a6edbc839290281d09656fd7f53d42";
  }

  static const char* value(const iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/GetPointCloud2";
  }

  static const char* value(const iri_perception_msgs::GetPointCloud2Response_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IRI_PERCEPTION_MSGS_SERVICE_GETPOINTCLOUD2_H

