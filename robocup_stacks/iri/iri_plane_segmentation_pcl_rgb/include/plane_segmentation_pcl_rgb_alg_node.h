// Copyright (C) 2010-2011 Institut de Robotica i Informatica Industrial, CSIC-UPC.
// Author David Martínez
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

#ifndef _plane_segmentation_pcl_rgb_alg_node_h_
#define _plane_segmentation_pcl_rgb_alg_node_h_

#include <iri_base_algorithm/iri_base_algorithm.h>
#include "plane_segmentation_pcl_rgb_alg.h"

// [publisher subscriber headers]
#include <sensor_msgs/Image.h>
#include <pcl/ModelCoefficients.h>
#include <sensor_msgs/PointCloud2.h>

// [service client headers]
//#include <iri_plane_segmentation_pcl_rgb/segment.h> UNUSED

// [action server client headers]

// other
// Pointclouds
#include <pcl/point_cloud.h>

// opencv
#include <opencv2/imgproc/imgproc.hpp>

// cvmat to rosmsg
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>

/**
 * \brief IRI ROS Specific Algorithm Class
 *
 */
class PlaneSegmentationPclRgbAlgNode : public algorithm_base::IriBaseAlgorithm<PlaneSegmentationPclRgbAlgorithm>
{
  private:
    // [publisher attributes]
    ros::Publisher segmented_image_publisher_;
    sensor_msgs::Image Image_msg_;
    ros::Publisher plane_coefficients_publisher_;
    pcl::ModelCoefficients ModelCoefficients_msg_;
    ros::Publisher pointcloud_out_publisher_;
    sensor_msgs::PointCloud2 PointCloud2_msg_;

    // [subscriber attributes]
    ros::Subscriber pointcloud_in_subscriber_;
    void pointcloud_in_callback(const sensor_msgs::PointCloud2::ConstPtr& msg);
    CMutex pointcloud_in_mutex_;

    // [service attributes]
    //ros::ServiceServer segment_server_; UNUSED
    //bool segmentCallback(iri_plane_segmentation_pcl_rgb::segment::Request &req, iri_plane_segmentation_pcl_rgb::segment::Response &res); UNUSED
    CMutex segment_mutex_;

    // [client attributes]

    // [action server attributes]

    // [action client attributes]
    
    // Other methods
    
   /**
    * \brief Registered pointcloud to image
    *
    * Gets the image shown by a pointcloud
    */
    cv::Mat pointcloud_to_image(pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud);
    
   /**
    * \brief Registered pointcloud to image
    *
    * Gets the image shown by a pointcloud
    */
    sensor_msgs::ImagePtr cvimage_to_rosimage(cv::Mat cvimage, std_msgs::Header header);
    

  public:
   /**
    * \brief Constructor
    * 
    * This constructor initializes specific class attributes and all ROS
    * communications variables to enable message exchange.
    */
    PlaneSegmentationPclRgbAlgNode(void);

   /**
    * \brief Destructor
    * 
    * This destructor frees all necessary dynamic memory allocated within this
    * this class.
    */
    ~PlaneSegmentationPclRgbAlgNode(void);

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

    // [diagnostic functions]
    
    // [test functions]
};

#endif
