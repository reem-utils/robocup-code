/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/srv/GeoVwDetection.srv */
#ifndef IRI_BOW_OBJECT_DETECTOR_SERVICE_GEOVWDETECTION_H
#define IRI_BOW_OBJECT_DETECTOR_SERVICE_GEOVWDETECTION_H
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

#include "iri_perception_msgs/GeoVwSet.h"
#include "sensor_msgs/Image.h"
#include "sensor_msgs/Image.h"


#include "iri_bow_object_detector/ObjectBox.h"

namespace iri_bow_object_detector
{
template <class ContainerAllocator>
struct GeoVwDetectionRequest_ {
  typedef GeoVwDetectionRequest_<ContainerAllocator> Type;

  GeoVwDetectionRequest_()
  : geo_vw_sets()
  , image()
  , mask()
  {
  }

  GeoVwDetectionRequest_(const ContainerAllocator& _alloc)
  : geo_vw_sets(_alloc)
  , image(_alloc)
  , mask(_alloc)
  {
  }

  typedef std::vector< ::iri_perception_msgs::GeoVwSet_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::iri_perception_msgs::GeoVwSet_<ContainerAllocator> >::other >  _geo_vw_sets_type;
  std::vector< ::iri_perception_msgs::GeoVwSet_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::iri_perception_msgs::GeoVwSet_<ContainerAllocator> >::other >  geo_vw_sets;

  typedef  ::sensor_msgs::Image_<ContainerAllocator>  _image_type;
   ::sensor_msgs::Image_<ContainerAllocator>  image;

  typedef  ::sensor_msgs::Image_<ContainerAllocator>  _mask_type;
   ::sensor_msgs::Image_<ContainerAllocator>  mask;


  typedef boost::shared_ptr< ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct GeoVwDetectionRequest
typedef  ::iri_bow_object_detector::GeoVwDetectionRequest_<std::allocator<void> > GeoVwDetectionRequest;

typedef boost::shared_ptr< ::iri_bow_object_detector::GeoVwDetectionRequest> GeoVwDetectionRequestPtr;
typedef boost::shared_ptr< ::iri_bow_object_detector::GeoVwDetectionRequest const> GeoVwDetectionRequestConstPtr;


template <class ContainerAllocator>
struct GeoVwDetectionResponse_ {
  typedef GeoVwDetectionResponse_<ContainerAllocator> Type;

  GeoVwDetectionResponse_()
  : posible_solutions()
  {
  }

  GeoVwDetectionResponse_(const ContainerAllocator& _alloc)
  : posible_solutions(_alloc)
  {
  }

  typedef std::vector< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> >::other >  _posible_solutions_type;
  std::vector< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> >::other >  posible_solutions;


  typedef boost::shared_ptr< ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct GeoVwDetectionResponse
typedef  ::iri_bow_object_detector::GeoVwDetectionResponse_<std::allocator<void> > GeoVwDetectionResponse;

typedef boost::shared_ptr< ::iri_bow_object_detector::GeoVwDetectionResponse> GeoVwDetectionResponsePtr;
typedef boost::shared_ptr< ::iri_bow_object_detector::GeoVwDetectionResponse const> GeoVwDetectionResponseConstPtr;

struct GeoVwDetection
{

typedef GeoVwDetectionRequest Request;
typedef GeoVwDetectionResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct GeoVwDetection
} // namespace iri_bow_object_detector

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "7aed8ecdd54a142914f1d3b1b41af89d";
  }

  static const char* value(const  ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x7aed8ecdd54a1429ULL;
  static const uint64_t static_value2 = 0x14f1d3b1b41af89dULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_bow_object_detector/GeoVwDetectionRequest";
  }

  static const char* value(const  ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/GeoVwSet[] geo_vw_sets\n\
sensor_msgs/Image image\n\
sensor_msgs/Image mask\n\
\n\
================================================================================\n\
MSG: iri_perception_msgs/GeoVwSet\n\
iri_perception_msgs/GeoVw[] geo_vws\n\
\n\
================================================================================\n\
MSG: iri_perception_msgs/GeoVw\n\
uint32 x\n\
uint32 y\n\
uint32 word\n\
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

  static const char* value(const  ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "f290dbb2dae33f32398c0b98cef0d841";
  }

  static const char* value(const  ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xf290dbb2dae33f32ULL;
  static const uint64_t static_value2 = 0x398c0b98cef0d841ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_bow_object_detector/GeoVwDetectionResponse";
  }

  static const char* value(const  ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_bow_object_detector/ObjectBox[] posible_solutions\n\
\n\
\n\
================================================================================\n\
MSG: iri_bow_object_detector/ObjectBox\n\
iri_perception_msgs/ImagePoint point1\n\
iri_perception_msgs/ImagePoint point2\n\
float32 value\n\
================================================================================\n\
MSG: iri_perception_msgs/ImagePoint\n\
uint32 x\n\
uint32 y\n\
";
  }

  static const char* value(const  ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.geo_vw_sets);
    stream.next(m.image);
    stream.next(m.mask);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GeoVwDetectionRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.posible_solutions);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GeoVwDetectionResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<iri_bow_object_detector::GeoVwDetection> {
  static const char* value() 
  {
    return "a9527c0fdb9971ff28f08c026548c643";
  }

  static const char* value(const iri_bow_object_detector::GeoVwDetection&) { return value(); } 
};

template<>
struct DataType<iri_bow_object_detector::GeoVwDetection> {
  static const char* value() 
  {
    return "iri_bow_object_detector/GeoVwDetection";
  }

  static const char* value(const iri_bow_object_detector::GeoVwDetection&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "a9527c0fdb9971ff28f08c026548c643";
  }

  static const char* value(const iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_bow_object_detector/GeoVwDetection";
  }

  static const char* value(const iri_bow_object_detector::GeoVwDetectionRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "a9527c0fdb9971ff28f08c026548c643";
  }

  static const char* value(const iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_bow_object_detector/GeoVwDetection";
  }

  static const char* value(const iri_bow_object_detector::GeoVwDetectionResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IRI_BOW_OBJECT_DETECTOR_SERVICE_GEOVWDETECTION_H
