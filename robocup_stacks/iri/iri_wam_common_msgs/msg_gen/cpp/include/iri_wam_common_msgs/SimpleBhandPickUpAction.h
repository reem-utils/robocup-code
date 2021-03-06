/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_wam_common_msgs/msg/SimpleBhandPickUpAction.msg */
#ifndef IRI_WAM_COMMON_MSGS_MESSAGE_SIMPLEBHANDPICKUPACTION_H
#define IRI_WAM_COMMON_MSGS_MESSAGE_SIMPLEBHANDPICKUPACTION_H
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

#include "iri_wam_common_msgs/SimpleBhandPickUpActionGoal.h"
#include "iri_wam_common_msgs/SimpleBhandPickUpActionResult.h"
#include "iri_wam_common_msgs/SimpleBhandPickUpActionFeedback.h"

namespace iri_wam_common_msgs
{
template <class ContainerAllocator>
struct SimpleBhandPickUpAction_ {
  typedef SimpleBhandPickUpAction_<ContainerAllocator> Type;

  SimpleBhandPickUpAction_()
  : action_goal()
  , action_result()
  , action_feedback()
  {
  }

  SimpleBhandPickUpAction_(const ContainerAllocator& _alloc)
  : action_goal(_alloc)
  , action_result(_alloc)
  , action_feedback(_alloc)
  {
  }

  typedef  ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator>  _action_goal_type;
   ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator>  action_goal;

  typedef  ::iri_wam_common_msgs::SimpleBhandPickUpActionResult_<ContainerAllocator>  _action_result_type;
   ::iri_wam_common_msgs::SimpleBhandPickUpActionResult_<ContainerAllocator>  action_result;

  typedef  ::iri_wam_common_msgs::SimpleBhandPickUpActionFeedback_<ContainerAllocator>  _action_feedback_type;
   ::iri_wam_common_msgs::SimpleBhandPickUpActionFeedback_<ContainerAllocator>  action_feedback;


  typedef boost::shared_ptr< ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct SimpleBhandPickUpAction
typedef  ::iri_wam_common_msgs::SimpleBhandPickUpAction_<std::allocator<void> > SimpleBhandPickUpAction;

typedef boost::shared_ptr< ::iri_wam_common_msgs::SimpleBhandPickUpAction> SimpleBhandPickUpActionPtr;
typedef boost::shared_ptr< ::iri_wam_common_msgs::SimpleBhandPickUpAction const> SimpleBhandPickUpActionConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_wam_common_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "370e75ccee11eea7e64a9d4adf8f292a";
  }

  static const char* value(const  ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x370e75ccee11eea7ULL;
  static const uint64_t static_value2 = 0xe64a9d4adf8f292aULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_wam_common_msgs/SimpleBhandPickUpAction";
  }

  static const char* value(const  ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
SimpleBhandPickUpActionGoal action_goal\n\
SimpleBhandPickUpActionResult action_result\n\
SimpleBhandPickUpActionFeedback action_feedback\n\
\n\
================================================================================\n\
MSG: iri_wam_common_msgs/SimpleBhandPickUpActionGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalID goal_id\n\
SimpleBhandPickUpGoal goal\n\
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
MSG: iri_wam_common_msgs/SimpleBhandPickUpGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# October 2012 - J.L Rivero, G. Alenya, D. Martinez\n\
#\n\
# This action was built after analyze previously the \"standard\" ROS message\n\
# PickUp. The ROS message involve a lot of action we were not consider at\n\
# the moment of writing and adapt that huge input for our needs was over-\n\
# engineer a solution.\n\
#\n\
# A translator PickUp -> SimpleBhandPickUp could be done, if needed\n\
\n\
# SimpleBhandPickUp is composed by the following phases:\n\
#\n\
# 1. Move the ARM from current to pre-grasp (planned if requested)\n\
# 2. Put the fingers into the pre-grasp position\n\
# 3. Move the ARM from pre-grasp to grasp (planned if requested)\n\
# 4. Put the fingers into the grasp position\n\
# 5. Perform the lift movement\n\
\n\
# goal\n\
# A vector of different GCL bhand commands\n\
string[] fingers_position_for_grasp\n\
string[] fingers_position_for_pre_grasp\n\
# Grasp pose is defined in the Stamped \n\
geometry_msgs/PoseStamped grasp_pose\n\
# pre movement relative to the grasp_pose\n\
geometry_msgs/Pose pre_grasp_modifier\n\
# Direction and distance to lift from the grasp_pose\n\
object_manipulation_msgs/GripperTranslation lift\n\
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
MSG: object_manipulation_msgs/GripperTranslation\n\
# defines a translation for the gripper, used in pickup or place tasks\n\
# for example for lifting an object off a table or approaching the table for placing\n\
\n\
# the direction of the translation\n\
geometry_msgs/Vector3Stamped direction\n\
\n\
# the desired translation distance\n\
float32 desired_distance\n\
\n\
# the min distance that must be considered feasible before the\n\
# grasp is even attempted\n\
float32 min_distance\n\
================================================================================\n\
MSG: geometry_msgs/Vector3Stamped\n\
# This represents a Vector3 with reference coordinate frame and timestamp\n\
Header header\n\
Vector3 vector\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
================================================================================\n\
MSG: iri_wam_common_msgs/SimpleBhandPickUpActionResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
SimpleBhandPickUpResult result\n\
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
MSG: iri_wam_common_msgs/SimpleBhandPickUpResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# result\n\
object_manipulation_msgs/GraspResult grasp_result\n\
\n\
\n\
================================================================================\n\
MSG: object_manipulation_msgs/GraspResult\n\
int32 SUCCESS = 1\n\
int32 GRASP_OUT_OF_REACH = 2\n\
int32 GRASP_IN_COLLISION = 3\n\
int32 GRASP_UNFEASIBLE = 4\n\
int32 PREGRASP_OUT_OF_REACH = 5\n\
int32 PREGRASP_IN_COLLISION = 6\n\
int32 PREGRASP_UNFEASIBLE = 7\n\
int32 LIFT_OUT_OF_REACH = 8\n\
int32 LIFT_IN_COLLISION = 9\n\
int32 LIFT_UNFEASIBLE = 10\n\
int32 MOVE_ARM_FAILED = 11\n\
int32 GRASP_FAILED = 12\n\
int32 LIFT_FAILED = 13\n\
int32 RETREAT_FAILED = 14\n\
int32 result_code\n\
\n\
# whether the state of the world was disturbed by this attempt. generally, this flag\n\
# shows if another task can be attempted, or a new sensed world model is recommeded\n\
# before proceeding\n\
bool continuation_possible\n\
\n\
================================================================================\n\
MSG: iri_wam_common_msgs/SimpleBhandPickUpActionFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
SimpleBhandPickUpFeedback feedback\n\
\n\
================================================================================\n\
MSG: iri_wam_common_msgs/SimpleBhandPickUpFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# feedback\n\
\n\
\n\
";
  }

  static const char* value(const  ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.action_goal);
    stream.next(m.action_result);
    stream.next(m.action_feedback);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct SimpleBhandPickUpAction_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_wam_common_msgs::SimpleBhandPickUpAction_<ContainerAllocator> & v) 
  {
    s << indent << "action_goal: ";
s << std::endl;
    Printer< ::iri_wam_common_msgs::SimpleBhandPickUpActionGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.action_goal);
    s << indent << "action_result: ";
s << std::endl;
    Printer< ::iri_wam_common_msgs::SimpleBhandPickUpActionResult_<ContainerAllocator> >::stream(s, indent + "  ", v.action_result);
    s << indent << "action_feedback: ";
s << std::endl;
    Printer< ::iri_wam_common_msgs::SimpleBhandPickUpActionFeedback_<ContainerAllocator> >::stream(s, indent + "  ", v.action_feedback);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_WAM_COMMON_MSGS_MESSAGE_SIMPLEBHANDPICKUPACTION_H

