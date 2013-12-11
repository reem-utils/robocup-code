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

#ifndef _normal_descriptor_alg_h_
#define _normal_descriptor_alg_h_

#include <normal_descriptor_node/NormalDescriptorConfig.h>
#include "mutex.h"
#include <sensor_msgs/PointCloud2.h>
#include <normal_descriptor_node/ndesc_pc.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/ros/conversions.h>
#include <pcl/features/normal_3d.h>
#include <cmath>
#include <vector>
#include <sstream>

template <class T>
inline std::string to_string (const T& t)
{
  std::stringstream ss;
  ss << t;
  return ss.str();
}


//include normal_descriptor_alg main library

/**
 * \brief IRI ROS Specific Driver Class
 *
 *
 */
class NormalDescriptorAlgorithm
{
  protected:
   /**
    * \brief define config type
    *
    * Define a Config type with the NormalDescriptorConfig. All driver implementations
    * will then use the same variable type Config.
    */
    CMutex alg_mutex_;

    // private attributes and methods
    // [num threads]
    uint nt_;

    // [descriptor attributes]
    uint desc_num_orient_bins_;
    std::vector<float> orient_bin_boundsX_;
    std::vector<float> orient_bin_boundsY_;
    uint desc_num_side_spatial_bins_;
    uint desc_num_total_bins_;
    uint desc_patch_radius_;
    
    // [descriptor sampling attributes]
    uint sample_each_;
    uint margin_;


    /* /\** */
    /*  * \brief compute descriptor */
    /*  * */
    /*  * Main descriptor computation function. Computes descriptor at */
    /*  * position (u,v) with parameters from the object instance. */
    /*  *\/ */
    /* normal_descriptor_node::ndesc */
    /*   compute_descriptor(const pcl::PointCloud<pcl::PointXYZ> &cloud,  */
    /* 			 pcl::PointCloud<pcl::PointXY> &pcl_spherical,  */
    /* 			 uint u, uint v); */
    
    /* /\** */
    /*  * \brief compute descriptor with spatial bins */
    /*  * */
    /*  * Main descriptor computation function using spatial */
    /*  * bins. Computes descriptor at position (u,v) with parameters */
    /*  * from the object instance. */
    /*  *\/ */
    /* normal_descriptor_node::ndesc */
    /*   compute_descriptor_spatial(pcl::PointCloud<pcl::PointXYZ> &cloud, */
    /* 				 pcl::PointCloud<pcl::PointXY> &pcl_spherical,  */
    /* 				 uint u, uint v); */

    /**
     * \brief compute spherical coordinates
     *
     * Takes a "normals" point cloud and computes the azimuth and
     * inclination angles of the spherical coordinates (magnitude not
     * possible since the normal is normalized). The angles are passed
     * as a PointXY point cloud, being X the azimuth and Y the
     * inclination (check!).
     */
    void
      compute_spherical_coords(pcl::PointCloud<pcl::Normal> &pcl_normal, 
			       pcl::PointCloud<pcl::PointXY> &pcl_spherical);

  public:
   /**
    * \brief define config type
    *
    * Define a Config type with the NormalDescriptorConfig. All driver implementations
    * will then use the same variable type Config.
    */
    typedef normal_descriptor_node::NormalDescriptorConfig Config;

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
    NormalDescriptorAlgorithm();

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
    void config_update(const Config& new_cfg, uint32_t level=0);

    // here define all normal_descriptor_alg interface methods to retrieve and set
    // the driver parameters
    /**
     * \brief Set total descriptor bins
     * 
     * Given the current parameters, this function computes the total
     * number of bins of the descriptor.
     *
     */
    inline int compute_total_bins()
    {
      this->desc_num_total_bins_ = this->desc_num_orient_bins_ * this->desc_num_orient_bins_ * 
	this->desc_num_side_spatial_bins_ * this->desc_num_side_spatial_bins_;
      return this->desc_num_total_bins_;
    }

    /**
     * \brief Set number of spatial bins (side)
     * 
     * This function allows to change the number of spatial bins of
     * the descriptor, and triggers all actions dependant on them.
     *
     */
    inline int set_num_side_spatial_bins(int nb)
    {
      this->desc_num_side_spatial_bins_ = nb;
      this->compute_total_bins();
      return this->desc_num_side_spatial_bins_;
    }

    /**
     * \brief Set number of orientation bins
     * 
     * This function allows to change the number of orientation bins
     * of the descriptor, and triggers all actions dependant on them.
     *
     */
    inline uint set_num_orientation_bins(uint nb)
    {
      this->desc_num_orient_bins_ = nb;
      this->orient_bin_boundsX_.resize(this->desc_num_orient_bins_);
      this->orient_bin_boundsY_.resize(this->desc_num_orient_bins_);
      //angle Y (phi)
      float increment_bound  = 2*M_PI/this->desc_num_orient_bins_;
      this->orient_bin_boundsY_[0]   = -M_PI + increment_bound;
      for(uint i=1; i<this->desc_num_orient_bins_; i++)
      {
          this->orient_bin_boundsY_[i] = this->orient_bin_boundsY_[i-1]+increment_bound;
      }
      //angle X (theta)
      increment_bound  = M_PI/(2*this->desc_num_orient_bins_);  //we are only concerned with things above 45deg
      this->orient_bin_boundsX_[0]   = M_PI/2.0+increment_bound;
      for(uint i=1; i<this->desc_num_orient_bins_; i++)
      {
          this->orient_bin_boundsX_[i] = this->orient_bin_boundsX_[i-1]+increment_bound;
      }

      this->compute_total_bins();
      return this->desc_num_orient_bins_;
    }

    /**
     * \brief Set patch radius
     * 
     * This function allows to change the patch radius of the
     * descriptor, and triggers all actions dependant on them.
     *
     */
    inline int set_desc_patch_radius(int r)
    {
      this->desc_patch_radius_ = r;
      this->margin_ = this->desc_patch_radius_;
      return this->desc_patch_radius_;
    }

    /**
     * \brief Set sample each
     * 
     * Function used to change the spacing between each sampled
     * position of the grid for descriptor computation.
     *
     */
    inline int set_sample_each(int s)
    {
      this->sample_each_ = s;
      return this->sample_each_;
    }

    // [descriptor computation]

/*     /\** */
/*      * \brief compute all descriptors of image */
/*      * */
/*      * Main interface to compute normal descriptors from a point cloud */
/*      *\/ */
/* //    normal_descriptor_node::ndesc_pc compute_ndescs(const sensor_msgs::PointCloud2::ConstPtr& msg); */
/*     normal_descriptor_node::ndesc_pc compute_ndescs(pcl::PointCloud<pcl::PointXYZ>& pcl_xyzrgb); */

    /* /\** */
    /*  * \brief compute all descriptors of image using an integral image */
    /*  * */
    /*  * Main interface to compute normal descriptors from a point cloud */
    /*  * (DEPREACTED) */
    /*  * */
    /*  *\/ */
    /* normal_descriptor_node::ndesc_pc compute_ndescs_integral(pcl::PointCloud<pcl::PointXYZ>& cloud); */

    /**
     * \brief compute all descriptors with spatial bin support of image using an integral image
     *
     * Main interface to compute normal descriptors with spatial support from a point cloud
     */
    void compute_ndescs_integral_spatial(pcl::PointCloud<pcl::PointXYZ>& cloud, normal_descriptor_node::ndesc_pc &ndesc_pc_msg);

    //Needs to be adapted for rotation invariant!!
    normal_descriptor_node::ndesc compute_descriptor_one_spatial_rot_inv(pcl::PointCloud<pcl::PointXYZ> &cloud, pcl::PointCloud<pcl::PointXY> &pcl_spherical, uint u, uint v);
    void compute_descriptor_spatial_rot_inv(pcl::PointCloud<pcl::PointXYZ> &cloud, normal_descriptor_node::ndesc_pc &ndesc_pc_msg);

    /**
     * \brief compute heat/wrinkledness map
     *
     * Compute a wrinkledness map from the entropy descriptors
     */
    //normal_descriptor_node::heat_map compute_wrinkled_map(const normal_descriptor_node::ndesc_pc &ndesc_pc_msg);

   /**
    * \brief Destructor
    *
    * This destructor is called when the object is about to be destroyed.
    *
    */
    ~NormalDescriptorAlgorithm();
};

#endif
