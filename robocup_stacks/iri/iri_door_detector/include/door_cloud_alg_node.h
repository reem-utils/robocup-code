// Copyright (C) 2010-2011 Institut de Robotica i Informatica Industrial, CSIC-UPC.
// Author 
// All rights reserved.
//
// This file is part of iri-ros-pkg
// iri-ros-pkg is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
// 
// IMPORTANT NOTE: This code has been generated through a script from the 
// iri_ros_scripts. Please do NOT delete any comments to guarantee the correctness
// of the scripts. ROS topics can be easly add by using those scripts. Please
// refer to the IRI wiki page for more information:
// http://wikiri.upc.es/index.php/Robotics_Lab

#ifndef _door_cloud_alg_node_h_
#define _door_cloud_alg_node_h_

#include <iri_base_algorithm/iri_base_algorithm.h>
#include "door_cloud_alg.h"
#include "boost/tuple/tuple.hpp"

// tf
#include <tf/transform_broadcaster.h>
#include <tf/transform_datatypes.h>

// PCL 
#include <pcl/ros/conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/ModelCoefficients.h>
#include <pcl/sample_consensus/method_types.h>
#include <pcl/sample_consensus/model_types.h>
#include <pcl/segmentation/sac_segmentation.h>
#include <pcl/filters/extract_indices.h>
#include <pcl/filters/passthrough.h>
#include <pcl/filters/voxel_grid.h>
//#include <pcl/common/transform.h>
#include <pcl/registration/transformation_estimation_svd.h>

// [publisher subscriber headers]
#include <std_msgs/Int8.h>
#include <visualization_msgs/Marker.h>
#include <sensor_msgs/PointCloud2.h>
#include <geometry_msgs/PoseStamped.h>

// [service client headers]

// [action server client headers]

/**
 * \brief IRI ROS Specific Algorithm Class
 *
 */
class DoorCloudAlgNode : public algorithm_base::IriBaseAlgorithm<DoorCloudAlgorithm>
{
  private:
    // [publisher attributes]
    ros::Publisher open_door_cloud_publisher_;
    sensor_msgs::PointCloud2 PointCloud2_msg_;
    ros::Publisher open_door_marker_publisher_;
    visualization_msgs::Marker Marker_msg_;
    ros::Publisher door_centroid_publisher_;
    geometry_msgs::PoseStamped PoseStamped_msg_;
    ros::Publisher closed_door_cloud_publisher_;
    //sensor_msgs::PointCloud2 PointCloud2_msg_;
    ros::Publisher closed_door_marker_publisher_;
    //visualization_msgs::Marker Marker_msg_;
    ros::Publisher door_handle_publisher_;
    //geometry_msgs::PoseStamped PoseStamped_msg_;
    

    // [subscriber attributes]
    ros::Subscriber door_action_start_subscriber_;
    void door_action_start_callback(const std_msgs::Int8::ConstPtr& msg);
    CMutex door_action_start_mutex_;
    ros::Subscriber points_subscriber_;
    void points_callback(const sensor_msgs::PointCloud2::ConstPtr& msg);
    CMutex points_mutex_;
    ros::Subscriber door_centroid_subscriber_;
    void door_centroid_callback(const geometry_msgs::PoseStamped::ConstPtr& msg);
    CMutex door_centroid_mutex_;
    ros::Subscriber handle_location_subscriber_;
    void handle_location_callback(const geometry_msgs::PoseStamped::ConstPtr& msg);
    CMutex handle_location_mutex_;

    // [service attributes]

    // [client attributes]

    // [action server attributes]

    // [action client attributes]

    // [reconfigurable variables]
    bool no_simulator;

    // [algorithm variables]
    int captured_open;
    int captured_closed;
    int start;
    float x_left;
    float x_right;
    float x_open;
    float y_top;
    float y_open;
    float z_open;
    float w_open;
    float x_closed;
    float y_closed; 
    float z_closed;
    float w_closed;
    float lower_x;
    float lower_y;
    float lower_z;
    float upper_x;
    float upper_y;
    float upper_z;
    std::string tf_original_frame;
    pcl::PointCloud<pcl::PointXYZ> cloud;
    pcl::PointCloud<pcl::PointXYZ> cloud_filtered;
    pcl::PointCloud<pcl::PointXYZ> cloud_filtered_left;
    pcl::PointCloud<pcl::PointXYZ> cloud_filtered_right;
    pcl::PointCloud<pcl::PointXYZ> cloud_filtered_top;
    pcl::PointCloud<pcl::PointXYZ> cloud_plane; 
    boost::tuple<pcl::PointCloud<pcl::PointXYZ>, pcl::PointIndices::Ptr, pcl::ModelCoefficients::Ptr> door_plane;
    geometry_msgs::PoseStamped poses;
    geometry_msgs::Quaternion orient;
    sensor_msgs::PointCloud2 open_door_cloud;
    sensor_msgs::PointCloud2 closed_door_cloud;
    visualization_msgs::Marker marker;

  public:
   /**
    * \brief Constructor
    * 
    * This constructor initializes specific class attributes and all ROS
    * communications variables to enable message exchange.
    */
    DoorCloudAlgNode(void);

   /**
    * \brief Destructor
    * 
    * This destructor frees all necessary dynamic memory allocated within this
    * this class.
    */
    ~DoorCloudAlgNode(void);

  protected:
   /**
    * \brief main node thread
    *
    * This is the main thread node function. Code written here will be executed
    * in every node loop while the algorithm is on running state. Loop frequency 
    * can be tuned by modifying loop_rate attribute.
    *
    * Here data related to the process loop or to ROS topics (mainly data structs
    * related to the MSG and SRV files) must be updated. ROS publisher objects 
    * must publish their data in this process. ROS client servers may also
    * request data to the corresponding server topics.
    */
    void mainNodeThread(void);

   /**
    * \brief dynamic reconfigure server callback
    * 
    * This method is called whenever a new configuration is received through
    * the dynamic reconfigure. The derivated generic algorithm class must 
    * implement it.
    *
    * \param config an object with new configuration from all algorithm 
    *               parameters defined in the config file.
    * \param level  integer referring the level in which the configuration
    *               has been changed.
    */
    void node_config_update(Config &config, uint32_t level);

   /**
    * \brief node add diagnostics
    *
    * In this abstract function additional ROS diagnostics applied to the 
    * specific algorithms may be added.
    */
    void addNodeDiagnostics(void);

   /**
    * \brief volume filter for a point cloud
    *
    * Removes points outisde x and z limits 
    */
    pcl::PointCloud<pcl::PointXYZ> filterCloud (pcl::PointCloud<pcl::PointXYZ> raw_cloud, float Lowx, float Uppx, float Lowy, float Uppy, float Lowz, float Uppz, bool negative_limits);

   /**
    * \brief RANSAC plane fit
    *
    * Returns plane coefficients, inliers and fitted plane point cloud in a tuple
    */
    boost::tuple<pcl::PointCloud<pcl::PointXYZ>, pcl::PointIndices::Ptr,pcl::ModelCoefficients::Ptr> planeFit (pcl::PointCloud<pcl::PointXYZ> raw_cloud);

   /**
    * \brief Quaterion from vectors
    *
    * Return rotation quaternion between two unit vectors
    */
    geometry_msgs::Quaternion quaternionFromVectors (tf::Vector3 vector_1, tf::Vector3 vector_2);

   /**
    * \brief Arrow Marker
    *
    * Construct an arrow marker for plane orientation visualization
    */
    visualization_msgs::Marker ArrowMarker(std_msgs::Header header, geometry_msgs::Pose pose, int alpha, int color,  const char arrow_tag []);

    // [diagnostic functions]
    
    // [test functions]
};

#endif
