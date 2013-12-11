/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/reem_mocks/object_recognition_mock/srv/enable.srv */
#ifndef OBJECT_RECOGNITION_MOCK_SERVICE_ENABLE_H
#define OBJECT_RECOGNITION_MOCK_SERVICE_ENABLE_H
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




namespace object_recognition_mock
{
template <class ContainerAllocator>
struct enableRequest_ {
  typedef enableRequest_<ContainerAllocator> Type;

  enableRequest_()
  : enable(false)
  {
  }

  enableRequest_(const ContainerAllocator& _alloc)
  : enable(false)
  {
  }

  typedef uint8_t _enable_type;
  uint8_t enable;


  typedef boost::shared_ptr< ::object_recognition_mock::enableRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::object_recognition_mock::enableRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct enableRequest
typedef  ::object_recognition_mock::enableRequest_<std::allocator<void> > enableRequest;

typedef boost::shared_ptr< ::object_recognition_mock::enableRequest> enableRequestPtr;
typedef boost::shared_ptr< ::object_recognition_mock::enableRequest const> enableRequestConstPtr;


template <class ContainerAllocator>
struct enableResponse_ {
  typedef enableResponse_<ContainerAllocator> Type;

  enableResponse_()
  : correct(false)
  {
  }

  enableResponse_(const ContainerAllocator& _alloc)
  : correct(false)
  {
  }

  typedef uint8_t _correct_type;
  uint8_t correct;


  typedef boost::shared_ptr< ::object_recognition_mock::enableResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::object_recognition_mock::enableResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct enableResponse
typedef  ::object_recognition_mock::enableResponse_<std::allocator<void> > enableResponse;

typedef boost::shared_ptr< ::object_recognition_mock::enableResponse> enableResponsePtr;
typedef boost::shared_ptr< ::object_recognition_mock::enableResponse const> enableResponseConstPtr;

struct enable
{

typedef enableRequest Request;
typedef enableResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct enable
} // namespace object_recognition_mock

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::object_recognition_mock::enableRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::object_recognition_mock::enableRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::object_recognition_mock::enableRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "8c1211af706069c994c06e00eb59ac9e";
  }

  static const char* value(const  ::object_recognition_mock::enableRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x8c1211af706069c9ULL;
  static const uint64_t static_value2 = 0x94c06e00eb59ac9eULL;
};

template<class ContainerAllocator>
struct DataType< ::object_recognition_mock::enableRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "object_recognition_mock/enableRequest";
  }

  static const char* value(const  ::object_recognition_mock::enableRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::object_recognition_mock::enableRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
bool enable\n\
\n\
";
  }

  static const char* value(const  ::object_recognition_mock::enableRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::object_recognition_mock::enableRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::object_recognition_mock::enableResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::object_recognition_mock::enableResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::object_recognition_mock::enableResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "0d7b90c75811aaad705aac4e2b606238";
  }

  static const char* value(const  ::object_recognition_mock::enableResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x0d7b90c75811aaadULL;
  static const uint64_t static_value2 = 0x705aac4e2b606238ULL;
};

template<class ContainerAllocator>
struct DataType< ::object_recognition_mock::enableResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "object_recognition_mock/enableResponse";
  }

  static const char* value(const  ::object_recognition_mock::enableResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::object_recognition_mock::enableResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
bool correct\n\
\n\
";
  }

  static const char* value(const  ::object_recognition_mock::enableResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::object_recognition_mock::enableResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::object_recognition_mock::enableRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.enable);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct enableRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::object_recognition_mock::enableResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.correct);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct enableResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<object_recognition_mock::enable> {
  static const char* value() 
  {
    return "99eaaa12ab016a770e9c949413327e2b";
  }

  static const char* value(const object_recognition_mock::enable&) { return value(); } 
};

template<>
struct DataType<object_recognition_mock::enable> {
  static const char* value() 
  {
    return "object_recognition_mock/enable";
  }

  static const char* value(const object_recognition_mock::enable&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<object_recognition_mock::enableRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "99eaaa12ab016a770e9c949413327e2b";
  }

  static const char* value(const object_recognition_mock::enableRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<object_recognition_mock::enableRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "object_recognition_mock/enable";
  }

  static const char* value(const object_recognition_mock::enableRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<object_recognition_mock::enableResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "99eaaa12ab016a770e9c949413327e2b";
  }

  static const char* value(const object_recognition_mock::enableResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<object_recognition_mock::enableResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "object_recognition_mock/enable";
  }

  static const char* value(const object_recognition_mock::enableResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // OBJECT_RECOGNITION_MOCK_SERVICE_ENABLE_H

