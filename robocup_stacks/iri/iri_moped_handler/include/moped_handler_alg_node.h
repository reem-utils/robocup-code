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

#ifndef _moped_handler_alg_node_h_
#define _moped_handler_alg_node_h_

#include <iri_base_algorithm/iri_base_algorithm.h>
#include "moped_handler_alg.h"

// [publisher subscriber headers]
#include <pr_msgs/ObjectPoseList.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/PointCloud2.h>

// [service client headers]
#include <iri_moped_handler/enable.h>

// [action server client headers]
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <iri_moped_actionserver/mopedAction.h>

// Time synchronizer libs
#include <message_filters/subscriber.h>
#include <message_filters/synchronizer.h>
#include <message_filters/sync_policies/approximate_time.h>
#include <message_filters/time_synchronizer.h>

using namespace sensor_msgs;
using namespace message_filters;

// PCL specific includes
#include <pcl/ros/conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>

/**
 * \brief IRI ROS Specific Algorithm Class
 *
 */
class MopedHandlerAlgNode : public algorithm_base::IriBaseAlgorithm<MopedHandlerAlgorithm>
{
  private:
    // [publisher attributes]
    ros::Publisher outputOPL_publisher_;
    pr_msgs::ObjectPoseList ObjectPoseList_msg_;

    // [subscriber attributes]
	message_filters::Subscriber<sensor_msgs::Image> subImage_;
	message_filters::Subscriber<sensor_msgs::PointCloud2> subPointCloud_;

	// NOTE: When using "ApproximateTime" getting images from different moments may happen.
	typedef message_filters::sync_policies::ApproximateTime<sensor_msgs::Image, sensor_msgs::PointCloud2> MySyncPolicy;
	message_filters::Synchronizer<MySyncPolicy> *sync_;

    // [service attributes]
    ros::ServiceServer enable_server_;
    bool enableCallback(iri_moped_handler::enable::Request &req, iri_moped_handler::enable::Response &res);
    CMutex enable_mutex_;

    // [client attributes]

    // [action server attributes]

    // [action client attributes]
    actionlib::SimpleActionClient<iri_moped_actionserver::mopedAction> moped_client_;
    iri_moped_actionserver::mopedGoal moped_goal_;
    void mopedMakeActionRequest();
    void mopedDone(const actionlib::SimpleClientGoalState& state,  const iri_moped_actionserver::mopedResultConstPtr& result);
    void mopedActive();
    void mopedFeedback(const iri_moped_actionserver::mopedFeedbackConstPtr& feedback);


  public:
   /**
    * \brief Constructor
    * 
    * This constructor initializes specific class attributes and all ROS
    * communications variables to enable message exchange.
    */
    MopedHandlerAlgNode(void);

   /**
    * \brief Destructor
    * 
    * This destructor frees all necessary dynamic memory allocated within this
    * this class.
    */
    ~MopedHandlerAlgNode(void);

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

	// Other functions
	void callback(const ImageConstPtr& image, const PointCloud2ConstPtr& pcl);

	// Attributes
	sensor_msgs::Image inputImage;
	sensor_msgs::PointCloud2 inputPointCloud;
	pcl::PointCloud<pcl::PointXYZ> pcl_;

	// Control variables.
	bool working;
};

#endif
