/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/srv/SetImage.srv */
#ifndef IRI_PERCEPTION_MSGS_SERVICE_SETIMAGE_H
#define IRI_PERCEPTION_MSGS_SERVICE_SETIMAGE_H
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



namespace iri_perception_msgs
{
template <class ContainerAllocator>
struct SetImageRequest_ {
  typedef SetImageRequest_<ContainerAllocator> Type;

  SetImageRequest_()
  : image_in()
  {
  }

  SetImageRequest_(const ContainerAllocator& _alloc)
  : image_in(_alloc)
  {
  }

  typedef  ::sensor_msgs::Image_<ContainerAllocator>  _image_in_type;
   ::sensor_msgs::Image_<ContainerAllocator>  image_in;


  typedef boost::shared_ptr< ::iri_perception_msgs::SetImageRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_perception_msgs::SetImageRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct SetImageRequest
typedef  ::iri_perception_msgs::SetImageRequest_<std::allocator<void> > SetImageRequest;

typedef boost::shared_ptr< ::iri_perception_msgs::SetImageRequest> SetImageRequestPtr;
typedef boost::shared_ptr< ::iri_perception_msgs::SetImageRequest const> SetImageRequestConstPtr;


template <class ContainerAllocator>
struct SetImageResponse_ {
  typedef SetImageResponse_<ContainerAllocator> Type;

  SetImageResponse_()
  : success(false)
  {
  }

  SetImageResponse_(const ContainerAllocator& _alloc)
  : success(false)
  {
  }

  typedef uint8_t _success_type;
  uint8_t success;


  typedef boost::shared_ptr< ::iri_perception_msgs::SetImageResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_perception_msgs::SetImageResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct SetImageResponse
typedef  ::iri_perception_msgs::SetImageResponse_<std::allocator<void> > SetImageResponse;

typedef boost::shared_ptr< ::iri_perception_msgs::SetImageResponse> SetImageResponsePtr;
typedef boost::shared_ptr< ::iri_perception_msgs::SetImageResponse const> SetImageResponseConstPtr;

struct SetImage
{

typedef SetImageRequest Request;
typedef SetImageResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct SetImage
} // namespace iri_perception_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::SetImageRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::SetImageRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_perception_msgs::SetImageRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "db7d5340a17ebc717da28ab27c870995";
  }

  static const char* value(const  ::iri_perception_msgs::SetImageRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xdb7d5340a17ebc71ULL;
  static const uint64_t static_value2 = 0x7da28ab27c870995ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_perception_msgs::SetImageRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/SetImageRequest";
  }

  static const char* value(const  ::iri_perception_msgs::SetImageRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_perception_msgs::SetImageRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
sensor_msgs/Image image_in\n\
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

  static const char* value(const  ::iri_perception_msgs::SetImageRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::SetImageResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::SetImageResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_perception_msgs::SetImageResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const  ::iri_perception_msgs::SetImageResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_perception_msgs::SetImageResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/SetImageResponse";
  }

  static const char* value(const  ::iri_perception_msgs::SetImageResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_perception_msgs::SetImageResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
bool success\n\
\n\
\n\
";
  }

  static const char* value(const  ::iri_perception_msgs::SetImageResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::iri_perception_msgs::SetImageResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_perception_msgs::SetImageRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.image_in);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct SetImageRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_perception_msgs::SetImageResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.success);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct SetImageResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<iri_perception_msgs::SetImage> {
  static const char* value() 
  {
    return "3c9d3f37fa6b00d25eaac8ccbaa373ab";
  }

  static const char* value(const iri_perception_msgs::SetImage&) { return value(); } 
};

template<>
struct DataType<iri_perception_msgs::SetImage> {
  static const char* value() 
  {
    return "iri_perception_msgs/SetImage";
  }

  static const char* value(const iri_perception_msgs::SetImage&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_perception_msgs::SetImageRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "3c9d3f37fa6b00d25eaac8ccbaa373ab";
  }

  static const char* value(const iri_perception_msgs::SetImageRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_perception_msgs::SetImageRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/SetImage";
  }

  static const char* value(const iri_perception_msgs::SetImageRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_perception_msgs::SetImageResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "3c9d3f37fa6b00d25eaac8ccbaa373ab";
  }

  static const char* value(const iri_perception_msgs::SetImageResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_perception_msgs::SetImageResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/SetImage";
  }

  static const char* value(const iri_perception_msgs::SetImageResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IRI_PERCEPTION_MSGS_SERVICE_SETIMAGE_H

