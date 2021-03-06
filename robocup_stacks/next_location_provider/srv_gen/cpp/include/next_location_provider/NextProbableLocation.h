/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/next_location_provider/srv/NextProbableLocation.srv */
#ifndef NEXT_LOCATION_PROVIDER_SERVICE_NEXTPROBABLELOCATION_H
#define NEXT_LOCATION_PROVIDER_SERVICE_NEXTPROBABLELOCATION_H
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



#include "geometry_msgs/Pose.h"

namespace next_location_provider
{
template <class ContainerAllocator>
struct NextProbableLocationRequest_ {
  typedef NextProbableLocationRequest_<ContainerAllocator> Type;

  NextProbableLocationRequest_()
  : room()
  {
  }

  NextProbableLocationRequest_(const ContainerAllocator& _alloc)
  : room(_alloc)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _room_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  room;


  typedef boost::shared_ptr< ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct NextProbableLocationRequest
typedef  ::next_location_provider::NextProbableLocationRequest_<std::allocator<void> > NextProbableLocationRequest;

typedef boost::shared_ptr< ::next_location_provider::NextProbableLocationRequest> NextProbableLocationRequestPtr;
typedef boost::shared_ptr< ::next_location_provider::NextProbableLocationRequest const> NextProbableLocationRequestConstPtr;


template <class ContainerAllocator>
struct NextProbableLocationResponse_ {
  typedef NextProbableLocationResponse_<ContainerAllocator> Type;

  NextProbableLocationResponse_()
  : location()
  , loc_position()
  {
  }

  NextProbableLocationResponse_(const ContainerAllocator& _alloc)
  : location(_alloc)
  , loc_position(_alloc)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _location_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  location;

  typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _loc_position_type;
   ::geometry_msgs::Pose_<ContainerAllocator>  loc_position;


  typedef boost::shared_ptr< ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct NextProbableLocationResponse
typedef  ::next_location_provider::NextProbableLocationResponse_<std::allocator<void> > NextProbableLocationResponse;

typedef boost::shared_ptr< ::next_location_provider::NextProbableLocationResponse> NextProbableLocationResponsePtr;
typedef boost::shared_ptr< ::next_location_provider::NextProbableLocationResponse const> NextProbableLocationResponseConstPtr;

struct NextProbableLocation
{

typedef NextProbableLocationRequest Request;
typedef NextProbableLocationResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct NextProbableLocation
} // namespace next_location_provider

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e497569192cccb82020c3a5c262721b9";
  }

  static const char* value(const  ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xe497569192cccb82ULL;
  static const uint64_t static_value2 = 0x020c3a5c262721b9ULL;
};

template<class ContainerAllocator>
struct DataType< ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "next_location_provider/NextProbableLocationRequest";
  }

  static const char* value(const  ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string room\n\
\n\
";
  }

  static const char* value(const  ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "93bb4d064db971c98b3a2587cd6a32dc";
  }

  static const char* value(const  ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x93bb4d064db971c9ULL;
  static const uint64_t static_value2 = 0x8b3a2587cd6a32dcULL;
};

template<class ContainerAllocator>
struct DataType< ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "next_location_provider/NextProbableLocationResponse";
  }

  static const char* value(const  ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string location\n\
geometry_msgs/Pose loc_position\n\
\n\
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

  static const char* value(const  ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::next_location_provider::NextProbableLocationRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.room);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct NextProbableLocationRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::next_location_provider::NextProbableLocationResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.location);
    stream.next(m.loc_position);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct NextProbableLocationResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<next_location_provider::NextProbableLocation> {
  static const char* value() 
  {
    return "4b161fd3eae8ce85c6fdfdca1a4229bc";
  }

  static const char* value(const next_location_provider::NextProbableLocation&) { return value(); } 
};

template<>
struct DataType<next_location_provider::NextProbableLocation> {
  static const char* value() 
  {
    return "next_location_provider/NextProbableLocation";
  }

  static const char* value(const next_location_provider::NextProbableLocation&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<next_location_provider::NextProbableLocationRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4b161fd3eae8ce85c6fdfdca1a4229bc";
  }

  static const char* value(const next_location_provider::NextProbableLocationRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<next_location_provider::NextProbableLocationRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "next_location_provider/NextProbableLocation";
  }

  static const char* value(const next_location_provider::NextProbableLocationRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<next_location_provider::NextProbableLocationResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4b161fd3eae8ce85c6fdfdca1a4229bc";
  }

  static const char* value(const next_location_provider::NextProbableLocationResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<next_location_provider::NextProbableLocationResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "next_location_provider/NextProbableLocation";
  }

  static const char* value(const next_location_provider::NextProbableLocationResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // NEXT_LOCATION_PROVIDER_SERVICE_NEXTPROBABLELOCATION_H

