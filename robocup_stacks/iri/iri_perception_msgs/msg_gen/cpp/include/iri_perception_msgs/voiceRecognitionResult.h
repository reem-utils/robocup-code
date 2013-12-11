/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg/voiceRecognitionResult.msg */
#ifndef IRI_PERCEPTION_MSGS_MESSAGE_VOICERECOGNITIONRESULT_H
#define IRI_PERCEPTION_MSGS_MESSAGE_VOICERECOGNITIONRESULT_H
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


namespace iri_perception_msgs
{
template <class ContainerAllocator>
struct voiceRecognitionResult_ {
  typedef voiceRecognitionResult_<ContainerAllocator> Type;

  voiceRecognitionResult_()
  : answer()
  , code(0)
  {
  }

  voiceRecognitionResult_(const ContainerAllocator& _alloc)
  : answer(_alloc)
  , code(0)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _answer_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  answer;

  typedef int16_t _code_type;
  int16_t code;


  typedef boost::shared_ptr< ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct voiceRecognitionResult
typedef  ::iri_perception_msgs::voiceRecognitionResult_<std::allocator<void> > voiceRecognitionResult;

typedef boost::shared_ptr< ::iri_perception_msgs::voiceRecognitionResult> voiceRecognitionResultPtr;
typedef boost::shared_ptr< ::iri_perception_msgs::voiceRecognitionResult const> voiceRecognitionResultConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_perception_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "5183d64c9f825deb413210477946bb58";
  }

  static const char* value(const  ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x5183d64c9f825debULL;
  static const uint64_t static_value2 = 0x413210477946bb58ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/voiceRecognitionResult";
  }

  static const char* value(const  ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#result definition\n\
string answer\n\
int16 code\n\
\n\
";
  }

  static const char* value(const  ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.answer);
    stream.next(m.code);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct voiceRecognitionResult_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_perception_msgs::voiceRecognitionResult_<ContainerAllocator> & v) 
  {
    s << indent << "answer: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.answer);
    s << indent << "code: ";
    Printer<int16_t>::stream(s, indent + "  ", v.code);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_PERCEPTION_MSGS_MESSAGE_VOICERECOGNITIONRESULT_H

