/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/state_machines/gpsr/msg/action.msg */
#ifndef GPSR_MESSAGE_ACTION_H
#define GPSR_MESSAGE_ACTION_H
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


namespace gpsr
{
template <class ContainerAllocator>
struct action_ {
  typedef action_<ContainerAllocator> Type;

  action_()
  : action()
  , person()
  , location()
  , item()
  {
  }

  action_(const ContainerAllocator& _alloc)
  : action(_alloc)
  , person(_alloc)
  , location(_alloc)
  , item(_alloc)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _action_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  action;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _person_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  person;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _location_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  location;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _item_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  item;


  typedef boost::shared_ptr< ::gpsr::action_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::gpsr::action_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct action
typedef  ::gpsr::action_<std::allocator<void> > action;

typedef boost::shared_ptr< ::gpsr::action> actionPtr;
typedef boost::shared_ptr< ::gpsr::action const> actionConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::gpsr::action_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::gpsr::action_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace gpsr

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::gpsr::action_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::gpsr::action_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::gpsr::action_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d87e5d751f9c8a39144689baeaab19fe";
  }

  static const char* value(const  ::gpsr::action_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd87e5d751f9c8a39ULL;
  static const uint64_t static_value2 = 0x144689baeaab19feULL;
};

template<class ContainerAllocator>
struct DataType< ::gpsr::action_<ContainerAllocator> > {
  static const char* value() 
  {
    return "gpsr/action";
  }

  static const char* value(const  ::gpsr::action_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::gpsr::action_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string action\n\
string person\n\
string location\n\
string item\n\
\n\
";
  }

  static const char* value(const  ::gpsr::action_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::gpsr::action_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.action);
    stream.next(m.person);
    stream.next(m.location);
    stream.next(m.item);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct action_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::gpsr::action_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::gpsr::action_<ContainerAllocator> & v) 
  {
    s << indent << "action: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.action);
    s << indent << "person: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.person);
    s << indent << "location: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.location);
    s << indent << "item: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.item);
  }
};


} // namespace message_operations
} // namespace ros

#endif // GPSR_MESSAGE_ACTION_H

