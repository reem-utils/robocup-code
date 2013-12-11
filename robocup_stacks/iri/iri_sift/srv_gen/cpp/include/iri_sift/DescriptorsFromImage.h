/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_sift/srv/DescriptorsFromImage.srv */
#ifndef IRI_SIFT_SERVICE_DESCRIPTORSFROMIMAGE_H
#define IRI_SIFT_SERVICE_DESCRIPTORSFROMIMAGE_H
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

#include "sensor_msgs/Image.h"


#include "iri_perception_msgs/DescriptorSet.h"

namespace iri_sift
{
template <class ContainerAllocator>
struct DescriptorsFromImageRequest_ {
  typedef DescriptorsFromImageRequest_<ContainerAllocator> Type;

  DescriptorsFromImageRequest_()
  : image()
  {
  }

  DescriptorsFromImageRequest_(const ContainerAllocator& _alloc)
  : image(_alloc)
  {
  }

  typedef  ::sensor_msgs::Image_<ContainerAllocator>  _image_type;
   ::sensor_msgs::Image_<ContainerAllocator>  image;


  typedef boost::shared_ptr< ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct DescriptorsFromImageRequest
typedef  ::iri_sift::DescriptorsFromImageRequest_<std::allocator<void> > DescriptorsFromImageRequest;

typedef boost::shared_ptr< ::iri_sift::DescriptorsFromImageRequest> DescriptorsFromImageRequestPtr;
typedef boost::shared_ptr< ::iri_sift::DescriptorsFromImageRequest const> DescriptorsFromImageRequestConstPtr;


template <class ContainerAllocator>
struct DescriptorsFromImageResponse_ {
  typedef DescriptorsFromImageResponse_<ContainerAllocator> Type;

  DescriptorsFromImageResponse_()
  : descriptor_set()
  {
  }

  DescriptorsFromImageResponse_(const ContainerAllocator& _alloc)
  : descriptor_set(_alloc)
  {
  }

  typedef  ::iri_perception_msgs::DescriptorSet_<ContainerAllocator>  _descriptor_set_type;
   ::iri_perception_msgs::DescriptorSet_<ContainerAllocator>  descriptor_set;


  typedef boost::shared_ptr< ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct DescriptorsFromImageResponse
typedef  ::iri_sift::DescriptorsFromImageResponse_<std::allocator<void> > DescriptorsFromImageResponse;

typedef boost::shared_ptr< ::iri_sift::DescriptorsFromImageResponse> DescriptorsFromImageResponsePtr;
typedef boost::shared_ptr< ::iri_sift::DescriptorsFromImageResponse const> DescriptorsFromImageResponseConstPtr;

struct DescriptorsFromImage
{

typedef DescriptorsFromImageRequest Request;
typedef DescriptorsFromImageResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct DescriptorsFromImage
} // namespace iri_sift

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b13d2865c5af2a64e6e30ab1b56e1dd5";
  }

  static const char* value(const  ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb13d2865c5af2a64ULL;
  static const uint64_t static_value2 = 0xe6e30ab1b56e1dd5ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_sift/DescriptorsFromImageRequest";
  }

  static const char* value(const  ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
sensor_msgs/Image image\n\
\n\
================================================================================\n\
MSG: sensor_msgs/Image\n\
# This message contains an uncompressed image\n\
# (0, 0) is at top-left corner of image\n\
#\n\
\n\
Header header        # Header timestamp should be acquisition time of image\n\
                     # Header frame_id should be optical frame of camera\n\
                     # origin of frame should be optical center of cameara\n\
                     # +x should point to the right in the image\n\
                     # +y should point down in the image\n\
                     # +z should point into to plane of the image\n\
                     # If the frame_id here and the frame_id of the CameraInfo\n\
                     # message associated with the image conflict\n\
                     # the behavior is undefined\n\
\n\
uint32 height         # image height, that is, number of rows\n\
uint32 width          # image width, that is, number of columns\n\
\n\
# The legal values for encoding are in file src/image_encodings.cpp\n\
# If you want to standardize a new string format, join\n\
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.\n\
\n\
string encoding       # Encoding of pixels -- channel meaning, ordering, size\n\
                      # taken from the list of strings in src/image_encodings.cpp\n\
\n\
uint8 is_bigendian    # is this data bigendian?\n\
uint32 step           # Full row length in bytes\n\
uint8[] data          # actual matrix data, size is (step * rows)\n\
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

  static const char* value(const  ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "db5e12e66d3b02ca867728f150b58d69";
  }

  static const char* value(const  ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xdb5e12e66d3b02caULL;
  static const uint64_t static_value2 = 0x867728f150b58d69ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_sift/DescriptorsFromImageResponse";
  }

  static const char* value(const  ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
iri_perception_msgs/DescriptorSet descriptor_set\n\
\n\
\n\
================================================================================\n\
MSG: iri_perception_msgs/DescriptorSet\n\
Header header\n\
int32 num_orient_bins\n\
int32 num_spa_bins\n\
int32 num\n\
int32 len\n\
int32 width\n\
int32 height\n\
iri_perception_msgs/Descriptor[] descriptors\n\
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
MSG: iri_perception_msgs/Descriptor\n\
float32[] descriptor\n\
geometry_msgs/Vector3 point3d\n\
int32 u\n\
int32 v\n\
float32 orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const  ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.image);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct DescriptorsFromImageRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.descriptor_set);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct DescriptorsFromImageResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<iri_sift::DescriptorsFromImage> {
  static const char* value() 
  {
    return "3f84e2bbe8799c8c0db43a5ff96da0c4";
  }

  static const char* value(const iri_sift::DescriptorsFromImage&) { return value(); } 
};

template<>
struct DataType<iri_sift::DescriptorsFromImage> {
  static const char* value() 
  {
    return "iri_sift/DescriptorsFromImage";
  }

  static const char* value(const iri_sift::DescriptorsFromImage&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "3f84e2bbe8799c8c0db43a5ff96da0c4";
  }

  static const char* value(const iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_sift/DescriptorsFromImage";
  }

  static const char* value(const iri_sift::DescriptorsFromImageRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "3f84e2bbe8799c8c0db43a5ff96da0c4";
  }

  static const char* value(const iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_sift/DescriptorsFromImage";
  }

  static const char* value(const iri_sift::DescriptorsFromImageResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IRI_SIFT_SERVICE_DESCRIPTORSFROMIMAGE_H
