#ifndef FURNITURE_DETECTOR_SERVICE_H
#define FURNITURE_DETECTOR_SERVICE_H

#include "ros/ros.h"
#include "sensor_msgs/PointCloud2.h"
#include "std_srvs/Empty.h"
#include <pcl17/classification/PHVObjectClassifier.h>
#include <pcl17/point_types.h>
#include <pcl17/features/sgfall.h>
#include <furniture_detector_service/FurnitureDetection.h>
#include <geometry_msgs/PoseStamped.h>

#include <string>


class FurnitureDetectorService {
    typedef pcl17::Histogram<pcl17::SGFALL_SIZE> FeatureType;
    typedef pcl17::SGFALLEstimation<pcl17::PointNormal, pcl17::Histogram< pcl17::SGFALL_SIZE> > FeatureEstimatorType;

    public:
        FurnitureDetectorService(std::string, ros::Publisher);
        ~FurnitureDetectorService();

        void pointcloud_snapshot_cb(const sensor_msgs::PointCloud2::ConstPtr&);
        bool classify_cb(furniture_detector_service::FurnitureDetection::Request  &req,
                         furniture_detector_service::FurnitureDetection::Response &res);

    private:
        sensor_msgs::PointCloud2::ConstPtr last_pointcloud;
        bool pointcloud_initialized;
        bool classification_running;
        std::string database_dir;
        ros::Publisher result_pub; //Publisher for the received classification pointcloud
        bool publish; //Says if the result must be published or not.

        //Created in the classify_cb function everytime
        //pcl17::PHVObjectClassifier<pcl17::PointXYZ, pcl17::PointNormal, FeatureType> oc;
        

};

#endif