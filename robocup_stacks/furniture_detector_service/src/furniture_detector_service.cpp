#include "ros/ros.h"
#include "furniture_detector_service.h"
#include "std_srvs/Empty.h"
#include "string"

const std::string POINTCLOUD_TOPIC = "/head_mount_xtion/depth_registered/points_snapshot";
const std::string DB_DIR = "/home/gerard/Robocup2013/fuerte_workspace/sandbox/furniture_recognition/furn_test_original/database/";

//Note: Line 1241 and 1242 of the PHVObjectClassifier.hpp should look like this in order to improve the results:
//    if ((vote_x >= 0) && (vote_y >= 0) && (vote_x < image_x_width)
//                && (vote_y < image_y_width) /*&& (model_centers.points[i].z >= 0)*/)  //Commented by Gerard Canal GCC
//After line 762 aprox:
//    grid.filter(*cloud_downsampled);
//
//    cloud_downsampled->is_dense = false;
//    std::vector<int> idx;
//    pcl17::removeNaNFromPointCloud(*cloud_downsampled, *cloud_downsampled, idx);

FurnitureDetectorService::FurnitureDetectorService(std::string db_dir, ros::Publisher pub) {
    last_pointcloud = sensor_msgs::PointCloud2::ConstPtr();
    pointcloud_initialized = false;
    classification_running = false;
    database_dir = db_dir;
    result_pub = pub;
    publish = true;

    //Initialize furniture classificator things
    /*typename pcl17::Feature<pcl17::PointNormal, FeatureType>::Ptr feature_estimator(new FeatureEstimatorType);
    oc.setFeatureEstimator(feature_estimator);

    oc.setDatabaseDir(database_dir);
    oc.loadFromFile();

    oc.setDebug(false);*/
}
FurnitureDetectorService::~FurnitureDetectorService() {}

void FurnitureDetectorService::pointcloud_snapshot_cb(const sensor_msgs::PointCloud2::ConstPtr& pc) {
    last_pointcloud = pc;
    pointcloud_initialized = true;
    ROS_INFO("Furniture detector service: Recieved a pointcloud");
}


bool FurnitureDetectorService::classify_cb(furniture_detector_service::FurnitureDetection::Request  &req,
                                           furniture_detector_service::FurnitureDetection::Response &res) {
    if (!pointcloud_initialized) {
        ROS_FATAL("No pointcloud has been received!");
        return false;
    }
    if (classification_running) {
        ROS_FATAL("A classification is already running!");
        return false;
    }

    classification_running = true;
    
    pcl17::PointCloud<pcl17::PointXYZ>::Ptr cloud(new pcl17::PointCloud<pcl17::PointXYZ>);
    pcl17::fromROSMsg (*last_pointcloud, *cloud);


    ///Shouldn't be necessary here... but if not it crashes
    pcl17::PHVObjectClassifier<pcl17::PointXYZ, pcl17::PointNormal, FeatureType> oc;
    typename pcl17::Feature<pcl17::PointNormal, FeatureType>::Ptr feature_estimator(new FeatureEstimatorType);
    oc.setFeatureEstimator(feature_estimator);

    oc.setDatabaseDir(database_dir);
    oc.loadFromFile();

    oc.setDebug(false);
    ///

    /*Convert piece...
    pcl17::PointCloud<pcl17::PointXYZ>::Ptr cloud_transformed = convert(cloud, 30);

    pcl17::PointCloud<pcl17::PointXYZ>::Ptr scene(new pcl17::PointCloud<pcl17::PointXYZ>);

    pcl17::copyPointCloud(*cloud_transformed, *scene);

    scene->sensor_origin_ = cloud_transformed->sensor_origin_;
    scene->sensor_orientation_ = cloud_transformed->sensor_orientation_;

    oc.setScene(scene);
    // End of convert piece.*/
    oc.setScene(cloud); // Uncomment if convert piece commented!!!
    //oc.setLocalMaximaThreshold(0.0); //Big testing things...
    ROS_INFO("Classifying...");
    oc.classify();

    map<string, vector<pcl17::PointCloud<pcl17::PointNormal>::Ptr> > objects = oc.getFoundObjects();

    typedef typename map<string, vector<pcl17::PointCloud<pcl17::PointNormal>::Ptr> >::value_type vt;

    res.status = res.NO_RESULT;
    BOOST_FOREACH(vt &v, objects)
    {
        ROS_INFO("Name of recognized thing: %s\n", v.first.c_str());
        if (v.second.size() > 0) {
            res.status = res.SUCCESS;
            res.furn_names.push_back(v.first);
            //ROS_INFO("Size: %d", v.second.size());
            pcl17::PointNormal min, max;
            pcl17::getMinMax3D(*v.second[0], min, max);
            geometry_msgs::PoseStamped ps;
            //ps.header.frame_id = v.second[0]->header.frame_id; // It's not filled!!
            ps.header.frame_id = last_pointcloud->header.frame_id; // It should be that one because of the snapshotter...
            ps.pose.position.x = min.x;
            ps.pose.position.y = min.y;
            ps.pose.position.z = min.z;
            res.poses.push_back(ps);

            if (publish) {
                sensor_msgs::PointCloud2 pc2; // remove
                pcl17::toROSMsg(*v.second[0], pc2); //remove
                pc2.header.frame_id = last_pointcloud->header.frame_id; //"/head_mount_xtion_rgb_optical_frame"; //remove
                result_pub.publish(pc2); //remove
            }
        }
    }

    classification_running = false;
    return true;
}


int main(int argc, char **argv) {
    ros::init(argc, argv, "furniture_recognition_service");
    ros::NodeHandle n;
    std::string db_dir = DB_DIR;
    if (argc < 2) {
        ROS_WARN("No database dir set. Using %s", DB_DIR.c_str());
    }
    else {
        db_dir = argv[1];
    }
    ros::Publisher pub = n.advertise<sensor_msgs::PointCloud2>("/furniture_detection_service", 1000, true);
    FurnitureDetectorService fds(db_dir, pub);
    ros::Subscriber sub = n.subscribe(POINTCLOUD_TOPIC, 10, &FurnitureDetectorService::pointcloud_snapshot_cb, &fds);
    ros::ServiceServer service = n.advertiseService("furniture_classification", 
                                                    &FurnitureDetectorService::classify_cb, &fds);
    ros::spin();
}
