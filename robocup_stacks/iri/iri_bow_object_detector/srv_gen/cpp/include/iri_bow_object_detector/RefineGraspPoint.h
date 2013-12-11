/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/srv/RefineGraspPoint.srv */
#ifndef IRI_BOW_OBJECT_DETECTOR_SERVICE_REFINEGRASPPOINT_H
#define IRI_BOW_OBJECT_DETECTOR_SERVICE_REFINEGRASPPOINT_H
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

#include "iri_bow_object_detector/ObjectBox.h"
#include "sensor_msgs/Image.h"
#include "iri_perception_msgs/DescriptorSet.h"


#include "iri_perception_msgs/ImagePoint.h"

namespace iri_bow_object_detector
{
template <class ContainerAllocator>
struct RefineGraspPointRequest_ {
  typedef RefineGraspPointRequest_<ContainerAllocator> Type;

  RefineGraspPointRequest_()
  : posible_solutions()
  , image()
  , descriptor_set()
  {
  }

  RefineGraspPointRequest_(const ContainerAllocator& _alloc)
  : posible_solutions(_alloc)
  , image(_alloc)
  , descriptor_set(_alloc)
  {
  }

  typedef std::vector< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> >::other >  _posible_solutions_type;
  std::vector< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::iri_bow_object_detector::ObjectBox_<ContainerAllocator> >::other >  posible_solutions;

  typedef  ::sensor_msgs::Image_<ContainerAllocator>  _image_type;
   ::sensor_msgs::Image_<ContainerAllocator>  image;

  typedef  ::iri_perception_msgs::DescriptorSet_<ContainerAllocator>  _descriptor_set_type;
   ::iri_perception_msgs::DescriptorSet_<ContainerAllocator>  descriptor_set;


  typedef boost::shared_ptr< ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct RefineGraspPointRequest
typedef  ::iri_bow_object_detector::RefineGraspPointRequest_<std::allocator<void> > RefineGraspPointRequest;

typedef boost::shared_ptr< ::iri_bow_object_detector::RefineGraspPointRequest> RefineGraspPointRequestPtr;
typedef boost::shared_ptr< ::iri_bow_object_detector::RefineGraspPointRequest const> RefineGraspPointRequestConstPtr;


template <class ContainerAllocator>
struct RefineGraspPointResponse_ {
  typedef RefineGraspPointResponse_<ContainerAllocator> Type;

  RefineGraspPointResponse_()
  : grasp_point()
  {
  }

  RefineGraspPointResponse_(const ContainerAllocator& _alloc)
  : grasp_point(_alloc)
  {
  }

  typedef  ::iri_perception_msgs::ImagePoint_<ContainerAllocator>  _grasp_point_type;
   ::iri_perception_msgs::ImagePoint_<ContainerAllocator>  grasp_point;


  typedef boost::shared_ptr< ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct RefineGraspPointResponse
typedef  ::iri_bow_object_detector::RefineGraspPointResponse_<std::allocator<void> > RefineGraspPointResponse;

typedef boost::shared_ptr< ::iri_bow_object_detector::RefineGraspPointResponse> RefineGraspPointResponsePtr;
typedef boost::shared_ptr< ::iri_bow_object_detector::RefineGraspPointResponse const> RefineGraspPointResponseConstPtr;

struct RefineGraspPoint
{

typedef RefineGraspPointRequest Request;
typedef RefineGraspPointResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct RefineGraspPoint
} // namespace iri_bow_object_detector

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "0526af87c7b6cc76c0da62278b22490c";
  }

  static const char* value(const  ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x0526af87c7b6cc76ULL;
  static const uint64_t static_value2 = 0xc0da62278b22490cULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_bow_object_detector/RefineGraspPointRequest";
  }

  static const char* value(const  ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
iri_bow_object_detector/ObjectBox[] posible_solutions\n\
sensor_msgs/Image image\n\
iri_perception_msgs/DescriptorSet descriptor_set\n\
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

  static const char* value(const  ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "a1d3d6d5081395c0c4a6d2daa9a86c56";
  }

  static const char* value(const  ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xa1d3d6d5081395c0ULL;
  static const uint64_t static_value2 = 0xc4a6d2daa9a86c56ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_bow_object_detector/RefineGraspPointResponse";
  }

  static const char* value(const  ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
iri_perception_msgs/ImagePoint grasp_point\n\
\n\
\n\
================================================================================\n\
MSG: iri_perception_msgs/ImagePoint\n\
uint32 x\n\
uint32 y\n\
";
  }

  static const char* value(const  ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.posible_solutions);
    stream.next(m.image);
    stream.next(m.descriptor_set);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct RefineGraspPointRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.grasp_point);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct RefineGraspPointResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<iri_bow_object_detector::RefineGraspPoint> {
  static const char* value() 
  {
    return "4df81184ea52bef77e8b614f35924fb4";
  }

  static const char* value(const iri_bow_object_detector::RefineGraspPoint&) { return value(); } 
};

template<>
struct DataType<iri_bow_object_detector::RefineGraspPoint> {
  static const char* value() 
  {
    return "iri_bow_object_detector/RefineGraspPoint";
  }

  static const char* value(const iri_bow_object_detector::RefineGraspPoint&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4df81184ea52bef77e8b614f35924fb4";
  }

  static const char* value(const iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_bow_object_detector/RefineGraspPoint";
  }

  static const char* value(const iri_bow_object_detector::RefineGraspPointRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4df81184ea52bef77e8b614f35924fb4";
  }

  static const char* value(const iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_bow_object_detector/RefineGraspPoint";
  }

  static const char* value(const iri_bow_object_detector::RefineGraspPointResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IRI_BOW_OBJECT_DETECTOR_SERVICE_REFINEGRASPPOINT_H
