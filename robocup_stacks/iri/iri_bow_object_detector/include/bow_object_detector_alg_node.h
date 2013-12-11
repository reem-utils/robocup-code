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

#ifndef _bow_object_detector_alg_node_h_
#define _bow_object_detector_alg_node_h_

#include <iri_base_algorithm/iri_base_algorithm.h>
#include "bow_object_detector_alg.h"

// [publisher subscriber headers]
#include <normal_descriptor_node/ndesc_pc.h>
#include <iri_bow_object_detector/WrinkledMap.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/PointCloud2.h>

// [service client headers]
#include <iri_perception_msgs/PclToDescriptorSet.h>
#include <iri_perception_msgs/DescriptorsToVws.h>
#include <iri_sift/DescriptorsFromImage.h>
#include <iri_perception_msgs/SetImage.h>
#include <iri_bow_object_detector/RefineGraspPoint.h>
#include <iri_bow_object_detector/GeoVwDetection.h>
#include <iri_sift/GeoVwSetSrv.h>

// [action server client headers]
#include <iri_action_server/iri_action_server.h>
#include <iri_bow_object_detector/GetGraspingPointAction.h>

//OpenCV
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h> 
#include <opencv2/imgproc/imgproc.hpp>


// PCL
#include <pcl/point_cloud.h>
#include <pcl/io/pcd_io.h>
#include <pcl/filters/passthrough.h>
#include <pcl/segmentation/extract_clusters.h>

// events
#include "eventexceptions.h"
#include "event.h"

/**
 * \brief IRI ROS Specific Algorithm Class
 *
 */
class BowObjectDetectorAlgNode : public algorithm_base::IriBaseAlgorithm<BowObjectDetectorAlgorithm>
{
  private:
    // [publisher attributes]
    ros::Publisher image_out_publisher_;
    sensor_msgs::Image Image_msg_;
    ros::Publisher pointcloud_out_publisher_;
    sensor_msgs::PointCloud2 PointCloud2_msg_;

    // [subscriber attributes]
    ros::Subscriber mask_image_in_subscriber_;
    void mask_image_in_callback(const sensor_msgs::Image::ConstPtr& msg);
    CMutex mask_image_in_mutex_;
    ros::Subscriber pointcloud_in_subscriber_;
    void pointcloud_in_callback(const sensor_msgs::PointCloud2::ConstPtr& msg);
    CMutex pointcloud_in_mutex_;

    // [service attributes]

    // [client attributes]
    ros::ServiceClient pointcloud_to_descriptorset_client_;
    iri_perception_msgs::PclToDescriptorSet pointcloud_to_descriptorset_srv_;
    ros::ServiceClient get_vws_client_;
    iri_perception_msgs::DescriptorsToVws get_vws_srv_;
    ros::ServiceClient get_sift_descriptors_client_;
    iri_sift::DescriptorsFromImage get_sift_descriptors_srv_;
    ros::ServiceClient set_background_image_client_;
    iri_perception_msgs::SetImage set_background_image_srv_;
    ros::ServiceClient select_grasp_point_client_;
    iri_bow_object_detector::RefineGraspPoint select_grasp_point_srv_;
    ros::ServiceClient detectObjects_client_;
    iri_bow_object_detector::GeoVwDetection detectObjects_srv_;
    ros::ServiceClient getVwSet_client_;
    iri_sift::GeoVwSetSrv getVwSet_srv_;

    // [action server attributes]
    IriActionServer<iri_bow_object_detector::GetGraspingPointAction> get_grasping_point_aserver_;
    void get_grasping_pointStartCallback(const iri_bow_object_detector::GetGraspingPointGoalConstPtr& goal);
    void get_grasping_pointStopCallback(void);
    bool get_grasping_pointIsFinishedCallback(void);
    bool get_grasping_pointHasSucceedCallback(void);
    void get_grasping_pointGetResultCallback(iri_bow_object_detector::GetGraspingPointResultPtr& result);
    void get_grasping_pointGetFeedbackCallback(iri_bow_object_detector::GetGraspingPointFeedbackPtr& feedback);

    // [action client attributes]
    
    // other
    CEvent EventPointCloudReady, EventImageMaskReady, EventWrinkledMapReady;
    
    iri_perception_msgs::DescriptorSet last_sift_descriptors_;
    iri_perception_msgs::GeoVwSet last_sift_vw_set_;
    sensor_msgs::PointCloud2 last_pointcloud_;
    sensor_msgs::Image last_image_mask_;
    sensor_msgs::Image last_image_;
    //iri_bow_object_detector::WrinkledMap last_wrinkled_map_;
    sensor_msgs::PointCloud2::ConstPtr last_wrinkled_map_;
    normal_descriptor_node::ndesc_pc::ConstPtr last_normal_descriptor_;
    
    bool first_pointcloud_;
    bool pointcloud_ready_;
    bool image_mask_ready_;
    bool wrinkled_map_ready_;
    bool solution_ready_;
    
    sensor_msgs::Image ros_pointcloud_to_ros_image(sensor_msgs::PointCloud2 ros_cloud);
    cv::Mat pcl_pointcloud_to_cv_image(pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud);
    sensor_msgs::ImagePtr cv_image_to_ros_image(cv::Mat cvimage, std_msgs::Header header);
    cv::Mat crop_and_resize(cv::Mat& image);
    
    void detectGraspPoint();
    void training();
    

  public:
   /**
    * \brief Constructor
    * 
    * This constructor initializes specific class attributes and all ROS
    * communications variables to enable message exchange.
    */
    BowObjectDetectorAlgNode(void);

   /**
    * \brief Destructor
    * 
    * This destructor frees all necessary dynamic memory allocated within this
    * this class.
    */
    ~BowObjectDetectorAlgNode(void);

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
