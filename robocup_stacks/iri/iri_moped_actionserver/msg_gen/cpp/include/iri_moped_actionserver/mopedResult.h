/* Auto-generated by genmsg_cpp for file /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_actionserver/msg/mopedResult.msg */
#ifndef IRI_MOPED_ACTIONSERVER_MESSAGE_MOPEDRESULT_H
#define IRI_MOPED_ACTIONSERVER_MESSAGE_MOPEDRESULT_H
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

#include "pr_msgs/ObjectPoseList.h"

namespace iri_moped_actionserver
{
template <class ContainerAllocator>
struct mopedResult_ {
  typedef mopedResult_<ContainerAllocator> Type;

  mopedResult_()
  : pose()
  {
  }

  mopedResult_(const ContainerAllocator& _alloc)
  : pose(_alloc)
  {
  }

  typedef  ::pr_msgs::ObjectPoseList_<ContainerAllocator>  _pose_type;
   ::pr_msgs::ObjectPoseList_<ContainerAllocator>  pose;


  typedef boost::shared_ptr< ::iri_moped_actionserver::mopedResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iri_moped_actionserver::mopedResult_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct mopedResult
typedef  ::iri_moped_actionserver::mopedResult_<std::allocator<void> > mopedResult;

typedef boost::shared_ptr< ::iri_moped_actionserver::mopedResult> mopedResultPtr;
typedef boost::shared_ptr< ::iri_moped_actionserver::mopedResult const> mopedResultConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::iri_moped_actionserver::mopedResult_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::iri_moped_actionserver::mopedResult_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace iri_moped_actionserver

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::iri_moped_actionserver::mopedResult_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::iri_moped_actionserver::mopedResult_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::iri_moped_actionserver::mopedResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "67229d53dfde046d6f32029a9eed81cb";
  }

  static const char* value(const  ::iri_moped_actionserver::mopedResult_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x67229d53dfde046dULL;
  static const uint64_t static_value2 = 0x6f32029a9eed81cbULL;
};

template<class ContainerAllocator>
struct DataType< ::iri_moped_actionserver::mopedResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "iri_moped_actionserver/mopedResult";
  }

  static const char* value(const  ::iri_moped_actionserver::mopedResult_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::iri_moped_actionserver::mopedResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#result definition\n\
pr_msgs/ObjectPoseList pose\n\
\n\
================================================================================\n\
MSG: pr_msgs/ObjectPoseList\n\
Header header\n\
\n\
ObjectPose[] object_list\n\
\n\
time originalTimeStamp\n\
\n\
time requestTimeStamp\n\
\n\
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
MSG: pr_msgs/ObjectPose\n\
string name\n\
\n\
geometry_msgs/Pose pose\n\
geometry_msgs/Point32 pose2D\n\
\n\
int16[] convex_hull_x\n\
int16[] convex_hull_y\n\
\n\
float32 mean_quality\n\
int16 used_points\n\
\n\
NameTypeValue[] properties\n\
\n\
geometry_msgs/Pose[] pose_uncertainty_list\n\
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
MSG: geometry_msgs/Point32\n\
# This contains the position of a point in free space(with 32 bits of precision).\n\
# It is recommeded to use Point wherever possible instead of Point32.  \n\
# \n\
# This recommendation is to promote interoperability.  \n\
#\n\
# This message is designed to take up less space when sending\n\
# lots of points at once, as in the case of a PointCloud.  \n\
\n\
float32 x\n\
float32 y\n\
float32 z\n\
================================================================================\n\
MSG: pr_msgs/NameTypeValue\n\
string name\n\
string type\n\
string value\n\
\n\
";
  }

  static const char* value(const  ::iri_moped_actionserver::mopedResult_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::iri_moped_actionserver::mopedResult_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.pose);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct mopedResult_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iri_moped_actionserver::mopedResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::iri_moped_actionserver::mopedResult_<ContainerAllocator> & v) 
  {
    s << indent << "pose: ";
s << std::endl;
    Printer< ::pr_msgs::ObjectPoseList_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
  }
};


} // namespace message_operations
} // namespace ros

#endif // IRI_MOPED_ACTIONSERVER_MESSAGE_MOPEDRESULT_H

