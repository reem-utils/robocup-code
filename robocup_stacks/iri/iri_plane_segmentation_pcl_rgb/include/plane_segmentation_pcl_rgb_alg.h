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

#ifndef _plane_segmentation_pcl_rgb_alg_h_
#define _plane_segmentation_pcl_rgb_alg_h_

#include <iri_plane_segmentation_pcl_rgb/PlaneSegmentationPclRgbConfig.h>
#include "mutex.h"

//include plane_segmentation_pcl_rgb_alg main library
// Pointclouds
#include <pcl/point_cloud.h>

// segmentation
#include <pcl/io/pcd_io.h>
#include <pcl/ModelCoefficients.h>
#include <pcl/segmentation/sac_segmentation.h>
#include <pcl/sample_consensus/method_types.h>
#include <pcl/filters/project_inliers.h>
#include <pcl/filters/extract_indices.h>

// Segmentation
#include <pcl/segmentation/extract_polygonal_prism_data.h>
#include <pcl/surface/convex_hull.h>

// clustering
#include <pcl/segmentation/extract_clusters.h>
//#include <pcl/kdtree/kdtree_flann.h>

// downsampling
#include <pcl/filters/voxel_grid.h>

// crop
#include <pcl/filters/passthrough.h>


/**
 * \brief IRI ROS Specific Driver Class
 *
 *
 */
class PlaneSegmentationPclRgbAlgorithm
{
  protected:
   /**
    * \brief define config type
    *
    * Define a Config type with the PlaneSegmentationPclRgbConfig. All driver implementations
    * will then use the same variable type Config.
    */
    CMutex alg_mutex_;

    // private attributes and methods
  private:
    // downsampling
    bool pointcloud_downsample;
    double pointcloud_downsample_size;
    
    // distances
    bool choose_plane_by_distance;
    bool choose_nearest_plane;
    
    // segmentation values (in cm)
    double plane_size_thresh;
    double plane_min_height;
    double plane_max_height;
    int plane_segm_iterations;
    double plane_segm_probability;
    
    // clustering
    bool plane_clustering;
    int plane_min_cluster_size;
    double plane_min_cluster_distance;
    
    
    

  public:
   /**
    * \brief define config type
    *
    * Define a Config type with the PlaneSegmentationPclRgbConfig. All driver implementations
    * will then use the same variable type Config.
    */
    typedef iri_plane_segmentation_pcl_rgb::PlaneSegmentationPclRgbConfig Config;

   /**
    * \brief config variable
    *
    * This variable has all the driver parameters defined in the cfg config file.
    * Is updated everytime function config_update() is called.
    */
    Config config_;

   /**
    * \brief constructor
    *
    * In this constructor parameters related to the specific driver can be
    * initalized. Those parameters can be also set in the openDriver() function.
    * Attributes from the main node driver class IriBaseDriver such as loop_rate,
    * may be also overload here.
    */
    PlaneSegmentationPclRgbAlgorithm(void);

   /**
    * \brief Lock Algorithm
    *
    * Locks access to the Algorithm class
    */
    void lock(void) { alg_mutex_.enter(); };

   /**
    * \brief Unlock Algorithm
    *
    * Unlocks access to the Algorithm class
    */
    void unlock(void) { alg_mutex_.exit(); };

   /**
    * \brief Tries Access to Algorithm
    *
    * Tries access to Algorithm
    * 
    * \return true if the lock was adquired, false otherwise
    */
    bool try_enter(void) { return alg_mutex_.try_enter(); };

   /**
    * \brief config update
    *
    * In this function the driver parameters must be updated with the input
    * config variable. Then the new configuration state will be stored in the 
    * Config attribute.
    *
    * \param new_cfg the new driver configuration state
    *
    * \param level level in which the update is taken place
    */
    void config_update(Config& new_cfg, uint32_t level=0);

    // here define all plane_segmentation_pcl_rgb_alg interface methods to retrieve and set
    // the driver parameters

   /**
    * \brief Destructor
    *
    * This destructor is called when the object is about to be destroyed.
    *
    */
    ~PlaneSegmentationPclRgbAlgorithm(void);
    
    
    // Other methods
    
   /**
    * \brief get biggest plane pointcloud
    *
    * Sets to black all points not belonging to the plane
    */
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr segmentBiggestPlane (pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_rgb_orig, 
							    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_orig,
							    pcl::ModelCoefficients::Ptr coefficients);


   /**
    * \brief get biggest plane's inliers
    *
    * Gets the inliers of the points in biggest plane, and the plane coefficients.
    * It also downsamples the pointcloud to have better performance
    */ 
    void getBiggestPlaneInliersDownsampling(pcl::PointIndices::Ptr inliers,
					    pcl::ModelCoefficients::Ptr coefficients,
					    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud);

   /**
    * \brief get biggest plane's inliers
    *
    * Gets the inliers of the points in biggest plane, and the plane coefficients.
    */ 
    void getBiggestPlaneInliers(pcl::PointIndices::Ptr inliers,
				pcl::ModelCoefficients::Ptr coefficients,
				pcl::PointCloud<pcl::PointXYZ>::Ptr cloud);

    void getNearestBigPlaneInliers(pcl::PointIndices::Ptr inliers,
								 pcl::ModelCoefficients::Ptr coefficients,
								 pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_orig);
    
   /**
    * \brief get biggest cluster pointcloud
    *
    * Gets the biggest cluster pointcloud
    */ 
    pcl::PointCloud<pcl::PointXYZ>::Ptr getBiggestClusterPC (pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_orig);
    
   /**
    * \brief Makes the plane normal point at the camera direction
    *
    * Makes the plane normal point at the camera direction. 
    * If it was pointing in the opposite direction, it just inverts it.
    */ 
    void fixPlaneCoefficientsOrientation(pcl::ModelCoefficients::Ptr coefs);
    
    
    // WARNING copied from newer PCL libs. Remove when it's available
   inline double
   pointToPlaneDistance (const pcl::PointXYZ &p, const std::vector< float > &plane_coefficients)
   {
     return ( fabs (pointToPlaneDistanceSigned (p, plane_coefficients)) );
   }
   
   inline double
   pointToPlaneDistanceSigned (const pcl::PointXYZ &p, const std::vector< float > &plane_coefficients)
   {
     return ( plane_coefficients[0] * p.x + plane_coefficients[1] * p.y + plane_coefficients[2] * p.z + plane_coefficients[3] );
   }
};

#endif
