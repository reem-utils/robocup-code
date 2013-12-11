#include <iostream>
#include "ros/ros.h"
#include "pcl_ros/io/bag_io.h"
#include "pcl/point_types.h"
#include "pcl/io/pcd_io.h"
#include <pcl/features/normal_3d.h>
#include <pcl/ros/conversions.h>
#include <sensor_msgs/Image.h>
#include <pcl/features/integral_image_normal.h>

using pcl::PointCloud;
using pcl::PointXYZRGB;
using pcl::Normal;
using pcl::PointXYZRGBNormal;
using pcl::NormalEstimation;
using pcl::KdTreeFLANN;


/* ---[ */
class normals_computer
{
  ros::Publisher pub;
  ros::Publisher pub2;
  ros::NodeHandle *nh;
  //ros::NodeHandle m;
  ros::Subscriber sub;
  sensor_msgs::Image ima;

  //NormalEstimation<PointXYZRGB, Normal> ne;
  pcl::IntegralImageNormalEstimation<pcl::PointXYZRGB, pcl::Normal> ne;
  
  PointCloud<PointXYZRGBNormal> cloud_normals;
  PointCloud<Normal> normals;

public:
  normals_computer(ros::NodeHandle *nn):nh(nn){
    sub = nh->subscribe("/get_normals/input_pointcloud", 1, &normals_computer::normals_callback, this);
    pub = nh->advertise<sensor_msgs::PointCloud2>("/camera/rgb/points/normals", 1);
    pub2 = nh->advertise<sensor_msgs::Image>("/camera/gray/image", 1);
    cloud_normals=PointCloud<PointXYZRGBNormal> ();
    cloud_normals.header.frame_id = std::string ("/myframe");
    ima = sensor_msgs::Image();
    ima.header.frame_id = std::string ("/myframe");
    ima.width  = 640;
    ima.height = 480;
    ima.data.resize(ima.width*ima.height);
    ima.encoding="8UC1";
    ROS_INFO("Normals computer node started");
  }
  
  ~normals_computer(){}
  
  void normals_callback(const sensor_msgs::PointCloud2ConstPtr& msg){

    ROS_INFO("callback!");

    //Compute Normals
    PointCloud<PointXYZRGB>::Ptr cloud (new PointCloud<PointXYZRGB> ());
    //PointCloud<PointXYZRGB> cloud ();
    pcl::fromROSMsg(*msg, *cloud);
    ne.setInputCloud (boost::make_shared<PointCloud<PointXYZRGB> > (*cloud));
    //ne.setKSearch (20);
    //KdTreeFLANN<PointXYZRGB>::Ptr tree = boost::make_shared<KdTreeFLANN<PointXYZRGB> > ();
    //ne.setSearchMethod (tree);
    ne.setNormalEstimationMethod (ne.AVERAGE_3D_GRADIENT);
    ne.setMaxDepthChangeFactor(0.02f);
    ne.setNormalSmoothingSize(10.0f);
    ne.compute (normals);
    std::cout<<normals.width<<std::endl;
    pcl::concatenateFields (*cloud, normals, cloud_normals);
    cloud_normals.header.stamp=msg->header.stamp;

    pcl::PointCloud<pcl::PointXYZRGB>::iterator pt_iter = cloud->begin (); 
    if(cloud->width!=ima.width || cloud->height!=ima.width){
      ima.width  = cloud->width;
      ima.height = cloud->height;
      ima.data.resize(ima.width*ima.height);
    }
    ima.header.stamp=msg->header.stamp;
    for(uint i=0; i<cloud->width*cloud->height; i++, pt_iter++){
      int red = (*reinterpret_cast<int*>(&(pt_iter->rgb)) & 0xff0000) >> 16;
      int green = (*reinterpret_cast<int*>(&(pt_iter->rgb)) & 0xff00) >> 8;
      int blue = *reinterpret_cast<int*>(&(pt_iter->rgb)) & 0xff;
      ima.data[i]= (uint8_t) ((float)red*0.30+(float)green*0.59+(float)blue*0.11);
    }
    //publish pointcloud w/ normals
    pub2.publish(ima);
    pub.publish(cloud_normals);
  }

};


int
main (int argc, char** argv)
{
  ros::init(argc, argv, "get_normals");
  ros::NodeHandle n;
  normals_computer nc(&n);
  ros::spin();
  
  return 0;
}




