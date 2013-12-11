/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg/voiceRecognitionAnswer.msg */
#ifndef IRI_PERCEPTION_MSGS_MESSAGE_VOICERECOGNITIONANSWER_H
#define IRI_PERCEPTION_MSGS_MESSAGE_VOICERECOGNITIONANSWER_H
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
struct voiceRecognitionAnswer_ {
  typedef voiceRecognitionAnswer_<ContainerAllocator> Type;

  voiceRecognitionAnswer_()
  : code(0)
  , answer()
  {
  }

  voiceRecognitionAnswer_(const ContainerAllocator& _alloc)
  : code(0)
  , answer(_alloc)
  {
  }

  typedef uint32_t _code_type;
  uint32_t code;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _answer_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  answer;


  typedef boost::shared_ptr< ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct voiceRecognitionAnswer
typedef  ::iri_perception_msgs::voiceRecognitionAnswer_<std::allocator<void> > voiceRecognitionAnswer;

typedef boost::shared_ptr< ::iri_perception_msgs::voiceRecognitionAnswer> voiceRecognitionAnswerPtr;
typedef boost::shared_ptr< ::iri_perception_msgs::voiceRecognitionAnswer const> voiceRecognitionAnswerConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_perception_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> > {
  static const char* value() 
  {
    return "8af98cfda9adf4e1ce1333303c85eeb9";
  }

  static const char* value(const  ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x8af98cfda9adf4e1ULL;
  static const uint64_t static_value2 = 0xce1333303c85eeb9ULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_perception_msgs/voiceRecognitionAnswer";
  }

  static const char* value(const  ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> > {
  static const char* value() 
  {
    return "uint32 code\n\
string answer\n\
";
  }

  static const char* value(const  ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.code);
    stream.next(m.answer);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct voiceRecognitionAnswer_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_perception_msgs::voiceRecognitionAnswer_<ContainerAllocator> & v) 
  {
    s << indent << "code: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.code);
    s << indent << "answer: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.answer);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_PERCEPTION_MSGS_MESSAGE_VOICERECOGNITIONANSWER_H
