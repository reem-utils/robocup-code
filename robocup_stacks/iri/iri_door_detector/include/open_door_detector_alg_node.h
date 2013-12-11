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

#ifndef _open_door_detector_alg_node_h_
#define _open_door_detector_alg_node_h_

#include <iri_base_algorithm/iri_base_algorithm.h>
#include "open_door_detector_alg.h"
#include <cv_bridge/cv_bridge.h>
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <tf/transform_broadcaster.h>
#include <tf/transform_listener.h>
#include <tf/transform_datatypes.h>
#include <algorithm>

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
#include <std_msgs/Int32MultiArray.h>
#include <geometry_msgs/PoseStamped.h>
#include <sensor_msgs/Image.h>

// [service client headers]

// [action server client headers]

/**
 * \brief IRI ROS Specific Algorithm Class
 *
 */
class OpenDoorDetectorAlgNode : public algorithm_base::IriBaseAlgorithm<OpenDoorDetectorAlgorithm>
{
  private:
    // [publisher attributes]
    ros::Publisher door_centroid_publisher_;
    geometry_msgs::PoseStamped PoseStamped_msg_;
    ros::Publisher open_door_coordinates_publisher_;
    std_msgs::Int32MultiArray Int32MultiArray_msg_;

    // [subscriber attributes]
    ros::Subscriber door_action_start_subscriber_;
    void door_action_start_callback(const std_msgs::Int8::ConstPtr& msg);
    CMutex door_action_start_mutex_;
    ros::Subscriber image_color_subscriber_;
    void image_color_callback(const sensor_msgs::Image::ConstPtr& msg);
    CMutex image_color_mutex_;
    ros::Subscriber points_subscriber_;
    void points_callback(const sensor_msgs::PointCloud2::ConstPtr& msg);
    CMutex points_mutex_;

    // [service attributes]

    // [client attributes]

    // [action server attributes]

    // [action client attributes]

    // [reconfigurable parameters]
    int min_x;
    int max_x;
    int min_y;
    int max_y;
    int debugging_images;
    bool no_simulator;
    bool DSC;
    bool SVP;
    bool SVL;
    bool SFC;
    bool Range_filter;
    bool Persp_filter;
    bool Geom_filter;
    bool Aspect_filter;
    bool Size_filter;
    double security_distance;

    // [algorithm variables]
    int idx;
    int idx_left;
    int idx_right; 
    int idx_top;
    int point; 
    int count;
    int frame_x;
    int frame_y; 
    int cx_min; 
    int cx_max;
    int cy_min;
    int cy_max;
    int roi_x; 
    int roi_y; 
    int door_x; 
    int door_y; 
    int p_set; 
    int f_c1; 
    int f_c2;  
    int f_c3; 
    int f_c4; 
    int offset_l;
    int offset_r;
    int offset_u;
    int offset_d; 
    int check;
    int aspect;
    int perspective;
    int geometry;
    int size;
    int sensor_range;
    int start;
    int captured_depth;
    int support;
    int sill;
    int lintel;
    int room_frame_height;
    int jamb;
    int left_door_end;
    int right_door_end;
    int door_end;
    size_t vec_start;
    size_t vec_end;
    double step_x;
    double step_y; 
    double m1;
    double m2;
    double b1;
    double b2;
    double dx;
    double dy; 
    double dst_h;
    double dst_v;
    double min_dst_h;
    double min_dst_v;
    double max_dst_v;
    double max_dst_h;
    double dst_up;
    double dst_down;
    double dst_left;
    double dst_right;
    double theta; 
    double theta1;
    double theta2;
    double theta3;
    double theta4;
    double r;
    double dst;
    double min_range;
    double max_range;
    float area_ratio;
    float frame_left;
    float frame_right;
    float frame_up;
    float left_door_edge;
    float right_door_edge;
    float prev_depth;
    float min_depth;
    float max_depth;
    float meters;
    float side;
    float x_i;
    float x_left;
    float x_right;
    float y_i;
    float y_top;
    float z_i;
    float x_1;
    float x_2;
    float y_2;
    float y_1;
    float x;
    float y;
    float z;
    float distance_to_room;
    float room_door_ratio;	
    float left_depth;
    float right_depth; 
    float b_depth;
    float* Dii;
    float* Di;
    float* Da;
    char* Ii;
    cv::Point2d s_door_centroid;
    cv::Point2d c1;
    cv::Point2d c2;
    cv::Point2d c3;
    cv::Point2d c4;
    cv::Point2d c5;
    cv::Point2d c6;
    cv::Point2d c7;
    cv::Point2d c8;
    cv::Point2d b_door_centroid;
    cv::Point2d b_handle;
    cv::Point2d b_c1;
    cv::Point2d b_c2;
    cv::Point2d b_c3;
    cv::Point2d b_c4;
    cv::RNG rng;
    cv_bridge::CvImagePtr depth_raw; 
    cv_bridge::CvImagePtr original;
    std::vector<cv::Point2d> vec_left;
    std::vector<cv::Point2d> vec_right;
    std::vector<cv::Point2d> vec_up;
    std::vector<cv::Point2d> vec_down;
    std::vector<cv::Point2d> ss_door_centroid; 
    std::vector<float> ss_depth;
    std::vector<cv::Point2d> ss_c1;
    std::vector<cv::Point2d> ss_c2;
    std::vector<cv::Point2d> ss_c3;
    std::vector<cv::Point2d> ss_c4;
    std::vector<cv::Vec3b> colorTab;
    geometry_msgs::PoseStamped poses;
    std_msgs::Int32MultiArray door_coordinates;
    cv::Scalar white;
    cv::Scalar black;
    pcl::PointCloud<pcl::PointXYZ> cloud;
    pcl::PointXYZ point3D;
    

  public:
   /**
    * \brief Constructor
    * 
    * This constructor initializes specific class attributes and all ROS
    * communications variables to enable message exchange.
    */
    OpenDoorDetectorAlgNode(void);

   /**
    * \brief Destructor
    * 
    * This destructor frees all necessary dynamic memory allocated within this
    * this class.
    */
    ~OpenDoorDetectorAlgNode(void);

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
    * \brief Display door size limits
    *
    * Display current door limits in  inputImage in order
    * to modify these parameters based on visual feedback 
    */
    void DoorSizeCalibration (cv::Mat inputImage, double min_dst_h, double max_dst_h, double min_dst_v, double max_dst_v);
	
    /**
    * \brief Draw Quadrilateral 
    *
    * Draw a Quadrilateral shape on inputImage given 4 cvPoint coordinates in clockwise
    * order. If filled == 0 4 lines are drawn. If filled == 1 a filled quadrilateral is drawn
    */
    void DrawRect (cv::Mat inputImage, cv::Point q1, cv::Point q2, cv::Point q3, cv::Point q4, cv::Scalar color, int lineSize, int filled);

    /**
    * \brief Angle between two lines 
    *
    * Return minimum angle between two lines in radians
    */
    double AngleBetweenLines (cv::Point point1, cv::Point point2, cv::Point point3, cv::Point point4);

    // [diagnostic functions]
    
    // [test functions]
};

#endif
