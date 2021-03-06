/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/estirabot_msgs/srv/RepresentationToString.srv */
#ifndef ESTIRABOT_MSGS_SERVICE_REPRESENTATIONTOSTRING_H
#define ESTIRABOT_MSGS_SERVICE_REPRESENTATIONTOSTRING_H
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

#include "estirabot_msgs/DirtyArea.h"
#include "estirabot_msgs/PointsDistanceMsg.h"
#include "estirabot_msgs/TraversedEllipses.h"



namespace estirabot_msgs
{
template <class ContainerAllocator>
struct RepresentationToStringRequest_ {
  typedef RepresentationToStringRequest_<ContainerAllocator> Type;

  RepresentationToStringRequest_()
  : dirty_areas()
  , distances()
  , traversed_ellipses()
  {
  }

  RepresentationToStringRequest_(const ContainerAllocator& _alloc)
  : dirty_areas(_alloc)
  , distances(_alloc)
  , traversed_ellipses(_alloc)
  {
  }

  typedef std::vector< ::estirabot_msgs::DirtyArea_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::estirabot_msgs::DirtyArea_<ContainerAllocator> >::other >  _dirty_areas_type;
  std::vector< ::estirabot_msgs::DirtyArea_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::estirabot_msgs::DirtyArea_<ContainerAllocator> >::other >  dirty_areas;

  typedef std::vector< ::estirabot_msgs::PointsDistanceMsg_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::estirabot_msgs::PointsDistanceMsg_<ContainerAllocator> >::other >  _distances_type;
  std::vector< ::estirabot_msgs::PointsDistanceMsg_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::estirabot_msgs::PointsDistanceMsg_<ContainerAllocator> >::other >  distances;

  typedef std::vector< ::estirabot_msgs::TraversedEllipses_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::estirabot_msgs::TraversedEllipses_<ContainerAllocator> >::other >  _traversed_ellipses_type;
  std::vector< ::estirabot_msgs::TraversedEllipses_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::estirabot_msgs::TraversedEllipses_<ContainerAllocator> >::other >  traversed_ellipses;


  typedef boost::shared_ptr< ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct RepresentationToStringRequest
typedef  ::estirabot_msgs::RepresentationToStringRequest_<std::allocator<void> > RepresentationToStringRequest;

typedef boost::shared_ptr< ::estirabot_msgs::RepresentationToStringRequest> RepresentationToStringRequestPtr;
typedef boost::shared_ptr< ::estirabot_msgs::RepresentationToStringRequest const> RepresentationToStringRequestConstPtr;


template <class ContainerAllocator>
struct RepresentationToStringResponse_ {
  typedef RepresentationToStringResponse_<ContainerAllocator> Type;

  RepresentationToStringResponse_()
  : state_string()
  {
  }

  RepresentationToStringResponse_(const ContainerAllocator& _alloc)
  : state_string(_alloc)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _state_string_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  state_string;


  typedef boost::shared_ptr< ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct RepresentationToStringResponse
typedef  ::estirabot_msgs::RepresentationToStringResponse_<std::allocator<void> > RepresentationToStringResponse;

typedef boost::shared_ptr< ::estirabot_msgs::RepresentationToStringResponse> RepresentationToStringResponsePtr;
typedef boost::shared_ptr< ::estirabot_msgs::RepresentationToStringResponse const> RepresentationToStringResponseConstPtr;

struct RepresentationToString
{

typedef RepresentationToStringRequest Request;
typedef RepresentationToStringResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct RepresentationToString
} // namespace estirabot_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "2d8b4c9001b9bfee1329ea66851228ae";
  }

  static const char* value(const  ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x2d8b4c9001b9bfeeULL;
  static const uint64_t static_value2 = 0x1329ea66851228aeULL;
};

template<class ContainerAllocator>
struct DataType< ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/RepresentationToStringRequest";
  }

  static const char* value(const  ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/DirtyArea[] dirty_areas\n\
estirabot_msgs/PointsDistanceMsg[] distances\n\
estirabot_msgs/TraversedEllipses[] traversed_ellipses\n\
\n\
================================================================================\n\
MSG: estirabot_msgs/DirtyArea\n\
int32 id\n\
estirabot_msgs/Ellipse ellipse\n\
bool sparse\n\
uint8 area\n\
uint8 shape\n\
\n\
================================================================================\n\
MSG: estirabot_msgs/Ellipse\n\
iri_perception_msgs/ImagePoint center\n\
iri_perception_msgs/ImageSize size\n\
float64 angle\n\
\n\
================================================================================\n\
MSG: iri_perception_msgs/ImagePoint\n\
uint32 x\n\
uint32 y\n\
================================================================================\n\
MSG: iri_perception_msgs/ImageSize\n\
uint32 width\n\
uint32 height\n\
================================================================================\n\
MSG: estirabot_msgs/PointsDistanceMsg\n\
uint32 origIdx\n\
uint32 dstIdx\n\
float64 distance\n\
\n\
================================================================================\n\
MSG: estirabot_msgs/TraversedEllipses\n\
int32 idx1\n\
int32 idx2\n\
int32[] traversedIdxs\n\
\n\
";
  }

  static const char* value(const  ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "5927826b25b95e12353eee87a92ed4ac";
  }

  static const char* value(const  ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x5927826b25b95e12ULL;
  static const uint64_t static_value2 = 0x353eee87a92ed4acULL;
};

template<class ContainerAllocator>
struct DataType< ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/RepresentationToStringResponse";
  }

  static const char* value(const  ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string state_string\n\
\n\
";
  }

  static const char* value(const  ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.dirty_areas);
    stream.next(m.distances);
    stream.next(m.traversed_ellipses);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct RepresentationToStringRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.state_string);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct RepresentationToStringResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<estirabot_msgs::RepresentationToString> {
  static const char* value() 
  {
    return "a1b22891042192e0316f71d2c67c0d87";
  }

  static const char* value(const estirabot_msgs::RepresentationToString&) { return value(); } 
};

template<>
struct DataType<estirabot_msgs::RepresentationToString> {
  static const char* value() 
  {
    return "estirabot_msgs/RepresentationToString";
  }

  static const char* value(const estirabot_msgs::RepresentationToString&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "a1b22891042192e0316f71d2c67c0d87";
  }

  static const char* value(const estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/RepresentationToString";
  }

  static const char* value(const estirabot_msgs::RepresentationToStringRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "a1b22891042192e0316f71d2c67c0d87";
  }

  static const char* value(const estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "estirabot_msgs/RepresentationToString";
  }

  static const char* value(const estirabot_msgs::RepresentationToStringResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // ESTIRABOT_MSGS_SERVICE_REPRESENTATIONTOSTRING_H

