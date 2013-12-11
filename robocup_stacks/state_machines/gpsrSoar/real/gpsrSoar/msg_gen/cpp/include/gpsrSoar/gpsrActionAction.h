/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/state_machines/gpsrSoar/real/gpsrSoar/msg/gpsrActionAction.msg */
#ifndef GPSRSOAR_MESSAGE_GPSRACTIONACTION_H
#define GPSRSOAR_MESSAGE_GPSRACTIONACTION_H
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

#include "gpsrSoar/gpsrActionActionGoal.h"
#include "gpsrSoar/gpsrActionActionResult.h"
#include "gpsrSoar/gpsrActionActionFeedback.h"

namespace gpsrSoar
{
template <class ContainerAllocator>
struct gpsrActionAction_ {
  typedef gpsrActionAction_<ContainerAllocator> Type;

  gpsrActionAction_()
  : action_goal()
  , action_result()
  , action_feedback()
  {
  }

  gpsrActionAction_(const ContainerAllocator& _alloc)
  : action_goal(_alloc)
  , action_result(_alloc)
  , action_feedback(_alloc)
  {
  }

  typedef  ::gpsrSoar::gpsrActionActionGoal_<ContainerAllocator>  _action_goal_type;
   ::gpsrSoar::gpsrActionActionGoal_<ContainerAllocator>  action_goal;

  typedef  ::gpsrSoar::gpsrActionActionResult_<ContainerAllocator>  _action_result_type;
   ::gpsrSoar::gpsrActionActionResult_<ContainerAllocator>  action_result;

  typedef  ::gpsrSoar::gpsrActionActionFeedback_<ContainerAllocator>  _action_feedback_type;
   ::gpsrSoar::gpsrActionActionFeedback_<ContainerAllocator>  action_feedback;


  typedef boost::shared_ptr< ::gpsrSoar::gpsrActionAction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::gpsrSoar::gpsrActionAction_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct gpsrActionAction
typedef  ::gpsrSoar::gpsrActionAction_<std::allocator<void> > gpsrActionAction;

typedef boost::shared_ptr< ::gpsrSoar::gpsrActionAction> gpsrActionActionPtr;
typedef boost::shared_ptr< ::gpsrSoar::gpsrActionAction const> gpsrActionActionConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::gpsrSoar::gpsrActionAction_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::gpsrSoar::gpsrActionAction_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace gpsrSoar

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::gpsrSoar::gpsrActionAction_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::gpsrSoar::gpsrActionAction_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::gpsrSoar::gpsrActionAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "5bb9b72ee77a378288b662aa160ce69c";
  }

  static const char* value(const  ::gpsrSoar::gpsrActionAction_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x5bb9b72ee77a3782ULL;
  static const uint64_t static_value2 = 0x88b662aa160ce69cULL;
};

template<class ContainerAllocator>
struct DataType< ::gpsrSoar::gpsrActionAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "gpsrSoar/gpsrActionAction";
  }

  static const char* value(const  ::gpsrSoar::gpsrActionAction_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::gpsrSoar::gpsrActionAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
gpsrActionActionGoal action_goal\n\
gpsrActionActionResult action_result\n\
gpsrActionActionFeedback action_feedback\n\
\n\
================================================================================\n\
MSG: gpsrSoar/gpsrActionActionGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalID goal_id\n\
gpsrActionGoal goal\n\
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
MSG: actionlib_msgs/GoalID\n\
# The stamp should store the time at which this goal was requested.\n\
# It is used by an action server when it tries to preempt all\n\
# goals that were requested before a certain time\n\
time stamp\n\
\n\
# The id provides a way to associate feedback and\n\
# result message with specific goal requests. The id\n\
# specified must be unique.\n\
string id\n\
\n\
\n\
================================================================================\n\
MSG: gpsrSoar/gpsrActionGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#goal definition\n\
order[] orderList\n\
\n\
================================================================================\n\
MSG: gpsrSoar/order\n\
string action\n\
string person\n\
string location\n\
string item\n\
\n\
================================================================================\n\
MSG: gpsrSoar/gpsrActionActionResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
gpsrActionResult result\n\
\n\
================================================================================\n\
MSG: actionlib_msgs/GoalStatus\n\
GoalID goal_id\n\
uint8 status\n\
uint8 PENDING         = 0   # The goal has yet to be processed by the action server\n\
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server\n\
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing\n\
                            #   and has since completed its execution (Terminal State)\n\
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)\n\
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due\n\
                            #    to some failure (Terminal State)\n\
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,\n\
                            #    because the goal was unattainable or invalid (Terminal State)\n\
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing\n\
                            #    and has not yet completed execution\n\
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,\n\
                            #    but the action server has not yet confirmed that the goal is canceled\n\
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing\n\
                            #    and was successfully cancelled (Terminal State)\n\
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be\n\
                            #    sent over the wire by an action server\n\
\n\
#Allow for the user to associate a string with GoalStatus for debugging\n\
string text\n\
\n\
\n\
================================================================================\n\
MSG: gpsrSoar/gpsrActionResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#result definition\n\
string   outcome\n\
\n\
================================================================================\n\
MSG: gpsrSoar/gpsrActionActionFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
gpsrActionFeedback feedback\n\
\n\
================================================================================\n\
MSG: gpsrSoar/gpsrActionFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#feedback\n\
uint8   order_id\n\
\n\
\n\
\n\
";
  }

  static const char* value(const  ::gpsrSoar::gpsrActionAction_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::gpsrSoar::gpsrActionAction_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.action_goal);
    stream.next(m.action_result);
    stream.next(m.action_feedback);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct gpsrActionAction_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::gpsrSoar::gpsrActionAction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::gpsrSoar::gpsrActionAction_<ContainerAllocator> & v) 
  {
    s << indent << "action_goal: ";
s << std::endl;
    Printer< ::gpsrSoar::gpsrActionActionGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.action_goal);
    s << indent << "action_result: ";
s << std::endl;
    Printer< ::gpsrSoar::gpsrActionActionResult_<ContainerAllocator> >::stream(s, indent + "  ", v.action_result);
    s << indent << "action_feedback: ";
s << std::endl;
    Printer< ::gpsrSoar::gpsrActionActionFeedback_<ContainerAllocator> >::stream(s, indent + "  ", v.action_feedback);
  }
};


} // namespace message_operations
} // namespace ros

#endif // GPSRSOAR_MESSAGE_GPSRACTIONACTION_H

