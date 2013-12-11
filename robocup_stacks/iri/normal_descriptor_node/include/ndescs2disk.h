#ifndef _ndescs2disk_h_
#define _ndescs2disk_h_

#include "ros/this_node.h"
#include "ros/names.h"
#include "ros/node_handle.h"
#include "ros/rate.h"

//#include "mutex.h"

#include "normal_descriptor_alg.h"
#include <normal_descriptor_node/ndesc_pc.h>
#include <normal_descriptor_node/ndesc.h>
#include <string>

class Ndescs2Disk
{
private:
  //CMutex execution_mutex;
  std::string prefix_out_;
  ros::NodeHandle node_handle_;
  int counter_;
  bool keep_nan_points_;
  //int max_frames_;
  void write_point(FILE *pf, const normal_descriptor_node::ndesc &point);

  // [publisher attributes]
  // [subscriber attributes]                               
  ros::Subscriber points_subscriber_;
  void points_callback(const normal_descriptor_node::ndesc_pc::ConstPtr& ndesc_pc_msg);
  // [service attributes]
  // [client attributes]
  // [action server attributes]
  // [action client attributes]
public:
  /**
   * \brief constructor
   *
   * This constructor mainly creates and initializes the WamActions topics
   * through the given NodeHandle object. CIriNode attributes may be also
   * modified to suit node specifications.
   *
   * All kind of ROS topics (publishers, subscribers, servers or clients) can
   * be easyly generated with the scripts in the iri_ros_scripts package. Refer
   * to ROS and IRI Wiki pages for more details:
   *
   * http://www.ros.org/wiki/ROS/Tutorials/WritingPublisherSubscriber(c++)
   * http://www.ros.org/wiki/ROS/Tutorials/WritingServiceClient(c++)
   * http://wikiri.upc.es/index.php/Robotics_Lab
   *
   * \param nh a reference to the node handle object to manage all ROS topics.
   */
  Ndescs2Disk(char *pref_out);//, int max_frames);
  /**
   * \brief main node thread
   *
   * This is the main thread node function. Code written here will be executed
   * in every node loop while the driver is on running state. Loop frequency
   * can be tuned my modifying loop_rate attribute.
   *
   * Here data related to the process loop or to ROS topics (mainly data structs
   * related to the MSG and SRV files) must be updated. ROS publisher objects
   * must publish their data in this process. ROS client servers may also
   * request data to the corresponding server topics.
   */

};
#endif



