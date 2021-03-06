/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/msg/NameTypeValue.msg */
#ifndef PR_MSGS_MESSAGE_NAMETYPEVALUE_H
#define PR_MSGS_MESSAGE_NAMETYPEVALUE_H
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


namespace pr_msgs
{
template <class ContainerAllocator>
struct NameTypeValue_ {
  typedef NameTypeValue_<ContainerAllocator> Type;

  NameTypeValue_()
  : name()
  , type()
  , value()
  {
  }

  NameTypeValue_(const ContainerAllocator& _alloc)
  : name(_alloc)
  , type(_alloc)
  , value(_alloc)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  name;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _type_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  type;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _value_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  value;


  typedef boost::shared_ptr< ::pr_msgs::NameTypeValue_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr_msgs::NameTypeValue_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct NameTypeValue
typedef  ::pr_msgs::NameTypeValue_<std::allocator<void> > NameTypeValue;

typedef boost::shared_ptr< ::pr_msgs::NameTypeValue> NameTypeValuePtr;
typedef boost::shared_ptr< ::pr_msgs::NameTypeValue const> NameTypeValueConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::pr_msgs::NameTypeValue_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::pr_msgs::NameTypeValue_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace pr_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::NameTypeValue_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::pr_msgs::NameTypeValue_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::pr_msgs::NameTypeValue_<ContainerAllocator> > {
  static const char* value() 
  {
    return "2a06900160ca5ec95f57a5ec28eaaa33";
  }

  static const char* value(const  ::pr_msgs::NameTypeValue_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x2a06900160ca5ec9ULL;
  static const uint64_t static_value2 = 0x5f57a5ec28eaaa33ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr_msgs::NameTypeValue_<ContainerAllocator> > {
  static const char* value() 
  {
    return "pr_msgs/NameTypeValue";
  }

  static const char* value(const  ::pr_msgs::NameTypeValue_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::pr_msgs::NameTypeValue_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string name\n\
string type\n\
string value\n\
\n\
";
  }

  static const char* value(const  ::pr_msgs::NameTypeValue_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::pr_msgs::NameTypeValue_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.name);
    stream.next(m.type);
    stream.next(m.value);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct NameTypeValue_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pr_msgs::NameTypeValue_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::pr_msgs::NameTypeValue_<ContainerAllocator> & v) 
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "type: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.type);
    s << indent << "value: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.value);
  }
};


} // namespace message_operations
} // namespace ros

#endif // PR_MSGS_MESSAGE_NAMETYPEVALUE_H

