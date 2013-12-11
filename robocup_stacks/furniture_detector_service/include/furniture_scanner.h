#ifndef FURNITURE_SCAN_H
#define FURNITURE_SCAN_H

#include "ros/ros.h"
#include "sensor_msgs/PointCloud2.h"
#include "std_srvs/Empty.h"
#include <boost/filesystem.hpp>
#include <pcl17/io/pcd_io.h>
#include <pcl17/filters/filter.h>
#include <string>

using namespace std;

class FurnitureScanner {
    public:
        FurnitureScanner(ros::ServiceClient&, string);
        ~FurnitureScanner();

        void pointcloud_snapshot_cb(const sensor_msgs::PointCloud2::ConstPtr&);
        void capture(string className, string modelName);
    private:
        bool pointcloud_received;
        sensor_msgs::PointCloud2::ConstPtr last_pointcloud;
        ros::ServiceClient snapshotter;
        string out_dir;
        string last_modelName;
        int last_modelId;

};

#endif