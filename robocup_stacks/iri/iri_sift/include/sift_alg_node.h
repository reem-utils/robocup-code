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

#ifndef _sift_alg_node_h_
#define _sift_alg_node_h_

#include <iri_base_algorithm/iri_base_algorithm.h>
#include "sift_alg.h"

// [publisher subscriber headers]
#include <iri_publish_params/classifier_update.h>
#include <iri_perception_msgs/GeoVwSet.h>
#include <sensor_msgs/Image.h>

// [service client headers]
#include <iri_sift/DescriptorsFromImage.h>
#include <iri_publish_params/classifier_update_service.h>
#include <iri_sift/GeoVwSetSrv.h>

// [action server client headers]

// OpenCV
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>

/**
 * \brief IRI ROS Specific Algorithm Class
 *
 */
class SiftAlgNode : public algorithm_base::IriBaseAlgorithm<SiftAlgorithm>
{
  private:
    // [publisher attributes]
    ros::Publisher geo_vw_set_publisher_;
    iri_perception_msgs::GeoVwSet GeoVwSet_msg_;

    // [subscriber attributes]
    ros::Subscriber image_in_subscriber_;
    void image_in_callback(const sensor_msgs::Image::ConstPtr& msg);
    CMutex image_in_mutex_;

    // [service attributes]
    ros::ServiceServer descriptors_from_image_server_;
    bool descriptors_from_imageCallback(iri_sift::DescriptorsFromImage::Request &req, iri_sift::DescriptorsFromImage::Response &res);
    CMutex descriptors_from_image_mutex_;
    ros::ServiceServer set_sift_centroids_server_;
    bool set_sift_centroidsCallback(iri_publish_params::classifier_update_service::Request &req, iri_publish_params::classifier_update_service::Response &res);
    CMutex set_sift_centroids_mutex_;
    ros::ServiceServer get_geo_vw_set_server_;
    bool get_geo_vw_setCallback(iri_sift::GeoVwSetSrv::Request &req, iri_sift::GeoVwSetSrv::Response &res);
    CMutex get_geo_vw_set_mutex_;

    // [client attributes]

    // [action server attributes]

    // [action client attributes]

  public:
   /**
    * \brief Constructor
    * 
    * This constructor initializes specific class attributes and all ROS
    * communications variables to enable message exchange.
    */
    SiftAlgNode(void);

   /**
    * \brief Destructor
    * 
    * This destructor frees all necessary dynamic memory allocated within this
    * this class.
    */
    ~SiftAlgNode(void);

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
