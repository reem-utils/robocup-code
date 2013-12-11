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

#ifndef _moped_handler_alg_h_
#define _moped_handler_alg_h_

#include <iri_moped_handler/MopedHandlerConfig.h>
#include "mutex.h"

// C++ includes
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Publisher subscriber headers
#include <pr_msgs/ObjectPoseList.h>

// PCL specific includes
#include <pcl/ros/conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>

//include moped_handler_alg main library

/**
 * \brief IRI ROS Specific Driver Class
 *
 *
 */
class MopedHandlerAlgorithm
{
  protected:
   /**
    * \brief define config type
    *
    * Define a Config type with the MopedHandlerConfig. All driver implementations
    * will then use the same variable type Config.
    */
    CMutex alg_mutex_;

    // private attributes and methods

  public:
   /**
    * \brief define config type
    *
    * Define a Config type with the MopedHandlerConfig. All driver implementations
    * will then use the same variable type Config.
    */
    typedef iri_moped_handler::MopedHandlerConfig Config;

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
    MopedHandlerAlgorithm(void);

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

    // here define all moped_handler_alg interface methods to retrieve and set
    // the driver parameters

   /**
    * \brief Destructor
    *
    * This destructor is called when the object is about to be destroyed.
    *
    */
    ~MopedHandlerAlgorithm(void);

};

#endif


// DEAD CODE

/*
	// Struct for position
	typedef struct
	{
		float x, y, z;
	} pos_t;

	// Struct for orientation
	typedef struct
	{
		float x, y, z, w;
	} ori_t;

	// Struct for object pose.
	typedef struct
	{
		pos_t pos2D;
		pos_t pos3D;
		ori_t ori;
	} Op_t;

	// Attributes
	vector<Op_t> inputOpl; // Object Position List
	vector<Op_t> outputOpl; // Object Position List
	pcl::PointCloud<pcl::PointXYZ> pcl_;

	// Main functions

	//   Set data to @attribute opl from a ROS message.
	void setObjectDataFromRosMsg(pr_msgs::ObjectPoseList input);

	//   Starts to compute the input data and fills the output data.
	void compute();

	//   Creates and returns a ROS msg from the output OPL.
	pr_msgs::ObjectPoseList getRosMsgWithObjectData();

	// Other functions
	//   Given a position wrt the camera, gives the pixel showing that position.
	void getPose2Pixel(float x, float y, float z, int& xPixel, int& yPixel, pcl::PointCloud<pcl::PointXYZ> pcl);
	//   Given a pixel position (x, y) returns the distance to that pixel in the @param pcl.
//	float getDepthPixel(int x, int y, pcl::PointCloud<pcl::PointXYZ> pcl);
	//   Given a pixel, return the point in that pixel (wrt the camera), according to the input pcl.
	MopedHandlerAlgorithm::pos_t getPixel2Pose(float xPixel, float yPixel, pcl::PointCloud<pcl::PointXYZ> pcl);

*/
