#include "normal_descriptor_alg_node.h"

NormalDescriptorAlgNode::NormalDescriptorAlgNode(void)
{
  //init class attributes if necessary
  //this->loop_rate_ = 2;//in [Hz]

  // [init publishers]
  this->descriptor_publisher_ = this->public_node_handle_.advertise<normal_descriptor_node::ndesc_pc>("ndesc", 1); 
  // [init subscribers]
  this->points_subscriber_ = this->public_node_handle_.subscribe("points", 1, &NormalDescriptorAlgNode::points_callback, this);
  
  // [init services]
  this->point_desc_service_ = this->public_node_handle_.advertiseService("nornal_descriptor_service", &NormalDescriptorAlgNode::points_service_callback, this);
  
  // [init clients]
  
  // [init action servers]
  
  // [init action clients]
}

NormalDescriptorAlgNode::~NormalDescriptorAlgNode(void)
{
  // [free dynamic memory]
}

void NormalDescriptorAlgNode::mainNodeThread(void)
{
  // [fill msg structures]
  
  // [fill srv structure and make request to the server]
  
  // [fill action structure and make request to the action server]

  // [publish messages]
  
}

/*  [subscriber callbacks] */

/*  [service callbacks] */

/*  [action callbacks] */

/*  [action requests] */

void NormalDescriptorAlgNode::node_config_update(Config &config, uint32_t level)
{
  ROS_INFO("Config update");
}


void NormalDescriptorAlgNode::compute_and_publish_descs(pcl::PointCloud<pcl::PointXYZ> &cloud, normal_descriptor_node::ndesc_pc &ndesc_pc_msg)
{
  //Function just in case more processing was needed...

  this->alg_.compute_ndescs_integral_spatial(cloud, ndesc_pc_msg);
  //testing oriented version
  //this->alg_.compute_descriptor_spatial_rot_inv(cloud, ndesc_pc_msg);



  ndesc_pc_msg.header = cloud.header;
  //deprecated
  //ndesc_pc_msg = this->alg_.compute_ndescs(cloud);
  //ndesc_pc_msg = this->alg_.compute_ndescs_integral(cloud);  
}


void NormalDescriptorAlgNode::points_callback(const sensor_msgs::PointCloud2::ConstPtr& msg)
{
  ROS_INFO("Received pointcloud in subscriber");
  pcl::PointCloud<pcl::PointXYZ> cloud;
  pcl::fromROSMsg(*msg, cloud);  
  normal_descriptor_node::ndesc_pc ndesc_pc_msg;
  this->compute_and_publish_descs(cloud, ndesc_pc_msg);
  this->descriptor_publisher_.publish(ndesc_pc_msg);
}


bool NormalDescriptorAlgNode::points_service_callback(normal_descriptor_node::ndesc_pc_service::Request &req, normal_descriptor_node::ndesc_pc_service::Response &res)
{
  //ROS_INFO("disabled for now.");
  //return false;
  ROS_INFO("received ndesc_pc_service call");
  pcl::PointCloud<pcl::PointXYZ> cloud;
  pcl::fromROSMsg(req.cloth_cloud, cloud);

  this->compute_and_publish_descs(cloud, res.ndesc_pc_msg);
  return true; 
}

void NormalDescriptorAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<NormalDescriptorAlgNode>(argc, argv, "normal_descriptor_node");
}

