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

#ifndef _normal_descriptor_alg_node_h_
#define _normal_descriptor_alg_node_h_

#include <iri_base_algorithm/iri_base_algorithm.h>
#include "normal_descriptor_alg.h"
//aramisa 2/12/11 #include "normal_descriptor_node/wrinkle.h"
#include "normal_descriptor_node/ndesc_pc_service.h"
#include <vector>

// [publisher subscriber headers]

// [service client headers]

// [action server client headers]

/**
 * \brief IRI ROS Specific Driver Class
 *
 */
class NormalDescriptorAlgNode : public algorithm_base::IriBaseAlgorithm<NormalDescriptorAlgorithm>
{
  private:
    // [publisher attributes]
    ros::Publisher descriptor_publisher_;

    // [subscriber attributes]
    ros::Subscriber points_subscriber_;
    void points_callback(const sensor_msgs::PointCloud2::ConstPtr& msg);

    // [service attributes]
    ros::ServiceServer point_desc_service_;
    bool points_service_callback(normal_descriptor_node::ndesc_pc_service::Request &req, normal_descriptor_node::ndesc_pc_service::Response &res);

    // [client attributes]
    void compute_and_publish_descs(pcl::PointCloud<pcl::PointXYZ> &cloud, normal_descriptor_node::ndesc_pc &ndesc_pc_msg);


    // [action server attributes]

    // [action client attributes]

  public:
   /**
    * \brief Constructor
    * 
    * This constructor initializes specific class attributes and all ROS
    * communications variables to enable message exchange.
    */
    NormalDescriptorAlgNode(void);

   /**
    * \brief Destructor
    * 
    * This destructor frees all necessary dynamic memory allocated within this
    * this class.
    */
    ~NormalDescriptorAlgNode(void);

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
