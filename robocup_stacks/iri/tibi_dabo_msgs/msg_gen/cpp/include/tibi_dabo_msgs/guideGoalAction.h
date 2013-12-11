/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/tibi_dabo_msgs/msg/guideGoalAction.msg */
#ifndef TIBI_DABO_MSGS_MESSAGE_GUIDEGOALACTION_H
#define TIBI_DABO_MSGS_MESSAGE_GUIDEGOALACTION_H
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

#include "tibi_dabo_msgs/guideGoalActionGoal.h"
#include "tibi_dabo_msgs/guideGoalActionResult.h"
#include "tibi_dabo_msgs/guideGoalActionFeedback.h"

namespace tibi_dabo_msgs
{
template <class ContainerAllocator>
struct guideGoalAction_ {
  typedef guideGoalAction_<ContainerAllocator> Type;

  guideGoalAction_()
  : action_goal()
  , action_result()
  , action_feedback()
  {
  }

  guideGoalAction_(const ContainerAllocator& _alloc)
  : action_goal(_alloc)
  , action_result(_alloc)
  , action_feedback(_alloc)
  {
  }

  typedef  ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator>  _action_goal_type;
   ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator>  action_goal;

  typedef  ::tibi_dabo_msgs::guideGoalActionResult_<ContainerAllocator>  _action_result_type;
   ::tibi_dabo_msgs::guideGoalActionResult_<ContainerAllocator>  action_result;

  typedef  ::tibi_dabo_msgs::guideGoalActionFeedback_<ContainerAllocator>  _action_feedback_type;
   ::tibi_dabo_msgs::guideGoalActionFeedback_<ContainerAllocator>  action_feedback;


  typedef boost::shared_ptr< ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct guideGoalAction
typedef  ::tibi_dabo_msgs::guideGoalAction_<std::allocator<void> > guideGoalAction;

typedef boost::shared_ptr< ::tibi_dabo_msgs::guideGoalAction> guideGoalActionPtr;
typedef boost::shared_ptr< ::tibi_dabo_msgs::guideGoalAction const> guideGoalActionConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace tibi_dabo_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "c4ad03327a4c5874a04413ed36029166";
  }

  static const char* value(const  ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xc4ad03327a4c5874ULL;
  static const uint64_t static_value2 = 0xa04413ed36029166ULL;
};

template<class ContainerAllocator>
struct DataType< ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "tibi_dabo_msgs/guideGoalAction";
  }

  static const char* value(const  ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
guideGoalActionGoal action_goal\n\
guideGoalActionResult action_result\n\
guideGoalActionFeedback action_feedback\n\
\n\
================================================================================\n\
MSG: tibi_dabo_msgs/guideGoalActionGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalID goal_id\n\
guideGoalGoal goal\n\
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
MSG: tibi_dabo_msgs/guideGoalGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#goal definition\n\
geometry_msgs/PoseStamped target_pose\n\
int32                     target_id  \n\
\n\
================================================================================\n\
MSG: geometry_msgs/PoseStamped\n\
# A Pose with reference coordinate frame and timestamp\n\
Header header\n\
Pose pose\n\
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
================================================================================\n\
MSG: tibi_dabo_msgs/guideGoalActionResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
guideGoalResult result\n\
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
MSG: tibi_dabo_msgs/guideGoalResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#result definition\n\
int32    result_code\n\
string   result_type\n\
\n\
================================================================================\n\
MSG: tibi_dabo_msgs/guideGoalActionFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
guideGoalFeedback feedback\n\
\n\
================================================================================\n\
MSG: tibi_dabo_msgs/guideGoalFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#feedback\n\
float32 distance\n\
\n\
\n\
\n\
";
  }

  static const char* value(const  ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.action_goal);
    stream.next(m.action_result);
    stream.next(m.action_feedback);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct guideGoalAction_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::tibi_dabo_msgs::guideGoalAction_<ContainerAllocator> & v) 
  {
    s << indent << "action_goal: ";
s << std::endl;
    Printer< ::tibi_dabo_msgs::guideGoalActionGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.action_goal);
    s << indent << "action_result: ";
s << std::endl;
    Printer< ::tibi_dabo_msgs::guideGoalActionResult_<ContainerAllocator> >::stream(s, indent + "  ", v.action_result);
    s << indent << "action_feedback: ";
s << std::endl;
    Printer< ::tibi_dabo_msgs::guideGoalActionFeedback_<ContainerAllocator> >::stream(s, indent + "  ", v.action_feedback);
  }
};


} // namespace message_operations
} // namespace ros

#endif // TIBI_DABO_MSGS_MESSAGE_GUIDEGOALACTION_H

