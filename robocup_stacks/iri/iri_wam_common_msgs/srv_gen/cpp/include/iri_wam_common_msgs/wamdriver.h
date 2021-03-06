/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_wam_common_msgs/srv/wamdriver.srv */
#ifndef IRI_WAM_COMMON_MSGS_SERVICE_WAMDRIVER_H
#define IRI_WAM_COMMON_MSGS_SERVICE_WAMDRIVER_H
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




namespace iri_wam_common_msgs
{
template <class ContainerAllocator>
struct wamdriverRequest_ {
  typedef wamdriverRequest_<ContainerAllocator> Type;

  wamdriverRequest_()
  : call(0)
  {
  }

  wamdriverRequest_(const ContainerAllocator& _alloc)
  : call(0)
  {
  }

  typedef int32_t _call_type;
  int32_t call;


  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct wamdriverRequest
typedef  ::iri_wam_common_msgs::wamdriverRequest_<std::allocator<void> > wamdriverRequest;

typedef boost::shared_ptr< ::iri_wam_common_msgs::wamdriverRequest> wamdriverRequestPtr;
typedef boost::shared_ptr< ::iri_wam_common_msgs::wamdriverRequest const> wamdriverRequestConstPtr;


template <class ContainerAllocator>
struct wamdriverResponse_ {
  typedef wamdriverResponse_<ContainerAllocator> Type;

  wamdriverResponse_()
  : success(0)
  {
  }

  wamdriverResponse_(const ContainerAllocator& _alloc)
  : success(0)
  {
  }

  typedef int8_t _success_type;
  int8_t success;


  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct wamdriverResponse
typedef  ::iri_wam_common_msgs::wamdriverResponse_<std::allocator<void> > wamdriverResponse;

typedef boost::shared_ptr< ::iri_wam_common_msgs::wamdriverResponse> wamdriverResponsePtr;
typedef boost::shared_ptr< ::iri_wam_common_msgs::wamdriverResponse const> wamdriverResponseConstPtr;

struct wamdriver
{

typedef wamdriverRequest Request;
typedef wamdriverResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct wamdriver
} // namespace iri_wam_common_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "ecfaae01671243d4ba0e6650022394c5";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xecfaae01671243d4ULL;
  static const uint64_t static_value2 = 0xba0e6650022394c5ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamdriverRequest";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int32 call\n\
\n\
";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "0b13460cb14006d3852674b4c614f25f";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x0b13460cb14006d3ULL;
  static const uint64_t static_value2 = 0x852674b4c614f25fULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamdriverResponse";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int8 success\n\
\n\
\n\
";
  }

  static const char* value(const  ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.call);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct wamdriverRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.success);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct wamdriverResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<iri_wam_common_msgs::wamdriver> {
  static const char* value() 
  {
    return "7845bcca17e28428f0ba550cb354008a";
  }

  static const char* value(const iri_wam_common_msgs::wamdriver&) { return value(); } 
};

template<>
struct DataType<iri_wam_common_msgs::wamdriver> {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamdriver";
  }

  static const char* value(const iri_wam_common_msgs::wamdriver&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "7845bcca17e28428f0ba550cb354008a";
  }

  static const char* value(const iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamdriver";
  }

  static const char* value(const iri_wam_common_msgs::wamdriverRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "7845bcca17e28428f0ba550cb354008a";
  }

  static const char* value(const iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/wamdriver";
  }

  static const char* value(const iri_wam_common_msgs::wamdriverResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IRI_WAM_COMMON_MSGS_SERVICE_WAMDRIVER_H

