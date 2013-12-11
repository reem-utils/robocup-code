/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_wam_common_msgs/msg/LWPRTrajectoryReturningForceEstimationAction.msg */
#ifndef IRI_WAM_COMMON_MSGS_MESSAGE_LWPRTRAJECTORYRETURNINGFORCEESTIMATIONACTION_H
#define IRI_WAM_COMMON_MSGS_MESSAGE_LWPRTRAJECTORYRETURNINGFORCEESTIMATIONACTION_H
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

#include "iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionGoal.h"
#include "iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionResult.h"
#include "iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionFeedback.h"

namespace iri_wam_common_msgs
{
template <class ContainerAllocator>
struct LWPRTrajectoryReturningForceEstimationAction_ {
  typedef LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> Type;

  LWPRTrajectoryReturningForceEstimationAction_()
  : action_goal()
  , action_result()
  , action_feedback()
  {
  }

  LWPRTrajectoryReturningForceEstimationAction_(const ContainerAllocator& _alloc)
  : action_goal(_alloc)
  , action_result(_alloc)
  , action_feedback(_alloc)
  {
  }

  typedef  ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationActionGoal_<ContainerAllocator>  _action_goal_type;
   ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationActionGoal_<ContainerAllocator>  action_goal;

  typedef  ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationActionResult_<ContainerAllocator>  _action_result_type;
   ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationActionResult_<ContainerAllocator>  action_result;

  typedef  ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationActionFeedback_<ContainerAllocator>  _action_feedback_type;
   ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationActionFeedback_<ContainerAllocator>  action_feedback;


  typedef boost::shared_ptr< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct LWPRTrajectoryReturningForceEstimationAction
typedef  ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<std::allocator<void> > LWPRTrajectoryReturningForceEstimationAction;

typedef boost::shared_ptr< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction> LWPRTrajectoryReturningForceEstimationActionPtr;
typedef boost::shared_ptr< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction const> LWPRTrajectoryReturningForceEstimationActionConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_wam_common_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "0592c1ed5f73ef46d87caf22ed58f5eb";
  }

  static const char* value(const  ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x0592c1ed5f73ef46ULL;
  static const uint64_t static_value2 = 0xd87caf22ed58f5ebULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationAction";
  }

  static const char* value(const  ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
LWPRTrajectoryReturningForceEstimationActionGoal action_goal\n\
LWPRTrajectoryReturningForceEstimationActionResult action_result\n\
LWPRTrajectoryReturningForceEstimationActionFeedback action_feedback\n\
\n\
================================================================================\n\
MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalID goal_id\n\
LWPRTrajectoryReturningForceEstimationGoal goal\n\
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
MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# goal\n\
string model_filename\n\
string points_filename\n\
\n\
================================================================================\n\
MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
LWPRTrajectoryReturningForceEstimationResult result\n\
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
MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# result\n\
float32 force\n\
\n\
================================================================================\n\
MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
LWPRTrajectoryReturningForceEstimationFeedback feedback\n\
\n\
================================================================================\n\
MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# feedback\n\
\n\
\n\
";
  }

  static const char* value(const  ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.action_goal);
    stream.next(m.action_result);
    stream.next(m.action_feedback);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct LWPRTrajectoryReturningForceEstimationAction_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationAction_<ContainerAllocator> & v) 
  {
    s << indent << "action_goal: ";
s << std::endl;
    Printer< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationActionGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.action_goal);
    s << indent << "action_result: ";
s << std::endl;
    Printer< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationActionResult_<ContainerAllocator> >::stream(s, indent + "  ", v.action_result);
    s << indent << "action_feedback: ";
s << std::endl;
    Printer< ::iri_wam_common_msgs::LWPRTrajectoryReturningForceEstimationActionFeedback_<ContainerAllocator> >::stream(s, indent + "  ", v.action_feedback);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_WAM_COMMON_MSGS_MESSAGE_LWPRTRAJECTORYRETURNINGFORCEESTIMATIONACTION_H

