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

#ifndef _door_detector_actions_alg_node_h_
#define _door_detector_actions_alg_node_h_

#include <iri_base_algorithm/iri_base_algorithm.h>
#include "door_detector_actions_alg.h"

// [publisher subscriber headers]
#include <visualization_msgs/Marker.h>
#include <std_msgs/Int8.h>
#include <geometry_msgs/PoseStamped.h>
#include <arm_navigation_msgs/MoveArmAction.h>
#include <arm_navigation_msgs/utils.h>
#include <tf/transform_listener.h>
#include <tf/transform_datatypes.h>

// [service client headers]

// [action server client headers]
#include <iri_action_server/iri_action_server.h>
#include <iri_door_detector/FindADoorAction.h>

/**
 * \brief IRI ROS Specific Algorithm Class
 *
 */
class DoorDetectorActionsAlgNode : public algorithm_base::IriBaseAlgorithm<DoorDetectorActionsAlgorithm>
{
  private:
    // [publisher attributes]
    ros::Publisher arm_poses_marker_publisher_;
    visualization_msgs::Marker Marker_msg_;
    ros::Publisher door_action_start_publisher_;
    std_msgs::Int8 Int8_msg_;

    // [subscriber attributes]
    CMutex arm_poses_marker_mutex_;
    ros::Subscriber door_handle_subscriber_;
    void door_handle_callback(const geometry_msgs::PoseStamped::ConstPtr& msg);
    CMutex door_handle_mutex_;
    ros::Subscriber door_centroid_subscriber_;
    void door_centroid_callback(const geometry_msgs::PoseStamped::ConstPtr& msg);
    CMutex door_centroid_mutex_;

    // [algorithm variables]
    int closed_door;
    int open_door;
    int start;
    int voting_rule_approval;
    float side_open;
    float side_closed;
    std::string tf_original_frame;
    std::string tf_base_frame;
    std::string tf_arm_frame;
    std::string tf_target_frame;
    std::string tf_target_frame_2;
    std::string current_planner;
    tf::TransformListener tf_listener;
    std_msgs::Int8 action_start;
    visualization_msgs::Marker marker;
    geometry_msgs::PoseStamped base_door_centroid;
    geometry_msgs::PoseStamped base_door_handle;
    geometry_msgs::PoseStamped marker_pose;
    arm_navigation_msgs::MotionPlanRequest arm_door_centroid;
    arm_navigation_msgs::MotionPlanRequest arm_door_handle;

    // [service attributes]

    // [client attributes]

    // [action server attributes]
    IriActionServer<iri_door_detector::FindADoorAction> find_a_door_aserver_;
    void find_a_doorStartCallback(const iri_door_detector::FindADoorGoalConstPtr& goal);
    void find_a_doorStopCallback(void);
    bool find_a_doorIsFinishedCallback(void);
    bool find_a_doorHasSucceedCallback(void);
    void find_a_doorGetResultCallback(iri_door_detector::FindADoorResultPtr& result);
    void find_a_doorGetFeedbackCallback(iri_door_detector::FindADoorFeedbackPtr& feedback);

    // [action client attributes]

    // [reconfigurable parameters]
    double base_distance_before_closed_door;
    double base_distance_after_open_door;
    double arm_distance_before_closed_door;
    double z_arm_offset;
    double y_offset;
    bool no_simulator;

  public:
   /**
    * \brief Constructor
    * 
    * This constructor initializes specific class attributes and all ROS
    * communications variables to enable message exchange.
    */
    DoorDetectorActionsAlgNode(void);

   /**
    * \brief Destructor
    * 
    * This destructor frees all necessary dynamic memory allocated within this
    * this class.
    */
    ~DoorDetectorActionsAlgNode(void);

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
    * \brief transform pose for to base frame
    *
    * Transform a 3D pose into a 2D projection in the /base_link frame
    */
    geometry_msgs::PoseStamped transformGoalBase (geometry_msgs::PoseStamped pose, std::string traget_frame);

   /**
    * \brief transform pose to arm frame
    *
    * Transform a 3D pose to a pose form arm navigation
    */
    arm_navigation_msgs::MotionPlanRequest transformGoalArm (geometry_msgs::PoseStamped pose, std::string traget_frame);

   /**
    * \brief lift arm
    *
    * Simple arm pose to traverse partially open doors
    */
    arm_navigation_msgs::MotionPlanRequest liftArm (geometry_msgs::PoseStamped pose, std::string target_frame);
	
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
