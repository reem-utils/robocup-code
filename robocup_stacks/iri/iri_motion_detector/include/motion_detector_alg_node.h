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

#ifndef _motion_detector_alg_node_h_
#define _motion_detector_alg_node_h_

#include <iri_base_algorithm/iri_base_algorithm.h>
#include "motion_detector_alg.h"

// [publisher subscriber headers]
#include <sensor_msgs/PointCloud2.h>
#include <sensor_msgs/Image.h>

// [service client headers]

// [action server client headers]
#include <iri_action_server/iri_action_server.h>
#include <iri_motion_detector/MotionDetectorActionAction.h>

#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <pcl/point_cloud.h>
#include <pcl/ModelCoefficients.h>
#include <pcl/io/pcd_io.h>

#include <pcl/ModelCoefficients.h>
#include <pcl/segmentation/sac_segmentation.h>
#include <pcl/sample_consensus/method_types.h>
#include <pcl/filters/project_inliers.h>
#include <pcl/filters/extract_indices.h>

// events
#include "eventexceptions.h"
#include "event.h"

// Use sqrt and pow to calculate the differente between two points
#include <math.h>
#include <queue>

float MAXIMUM_DISTANCE = 4.00;     //FIXME: Adjust MAXIMUM_VALUE after see the "dimensions" of cocktail_party room.


/**
 * \brief IRI ROS Specific Algorithm Class
 *
 */
class MotionDetectorAlgNode : public algorithm_base::IriBaseAlgorithm<MotionDetectorAlgorithm>
{
  private:
    // [publisher attributes]

    // [subscriber attributes]
    ros::Subscriber pointcloud_in_subscriber_;
    void pointcloud_in_callback(const sensor_msgs::PointCloud2::ConstPtr& msg);
    CMutex pointcloud_in_mutex_;
    ros::Subscriber image_in_subscriber_;
    void image_in_callback(const sensor_msgs::Image::ConstPtr& msg);
    CMutex image_in_mutex_;

    // [service attributes]

    // [client attributes]

    // [action server attributes]
    IriActionServer<iri_motion_detector::MotionDetectorActionAction> getMotionPosition_aserver_;
    void getMotionPositionStartCallback(const iri_motion_detector::MotionDetectorActionGoalConstPtr& goal);
    void getMotionPositionStopCallback(void);
    bool getMotionPositionIsFinishedCallback(void);
    bool getMotionPositionHasSucceedCallback(void);
    void getMotionPositionGetResultCallback(iri_motion_detector::MotionDetectorActionResultPtr& result);
    void getMotionPositionGetFeedbackCallback(iri_motion_detector::MotionDetectorActionFeedbackPtr& feedback);

    // [action client attributes]
    
    bool first, processing, waiting_for_pointcloud;
    cv::Mat frameOld;
    cv::Mat resultat;
    geometry_msgs::PoseStamped motionPose;
    pcl::PointCloud<pcl::PointXYZ> cloud;
    CEvent EventInfoReady;
    double  m00, m10, m01;
    pcl::PointXYZ previous_gravity_center;
    std::deque<cv::Point> _average;
    float distance;

  public:
   /**
    * \brief Constructor
    * 
    * This constructor initializes specific class attributes and all ROS
    * communications variables to enable message exchange.
    */
    MotionDetectorAlgNode(void);

   /**
    * \brief Destructor
    * 
    * This destructor frees all necessary dynamic memory allocated within this
    * this class.
    */
    ~MotionDetectorAlgNode(void);

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
