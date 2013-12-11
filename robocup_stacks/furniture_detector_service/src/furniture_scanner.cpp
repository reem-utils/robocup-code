#include "ros/ros.h"
#include <iostream>
#include <boost/filesystem.hpp>
#include "std_srvs/Empty.h"
#include "furniture_scanner.h"

using namespace std;

const string POINTCLOUD_TOPIC = "/head_mount_xtion/depth_registered/points_snapshot";
const string SNAPSHOTTER_SRV = "/xtion_snapshotter/snapshot";
const string OUT_DIR = "/home/gerard/Robocup2013/fuerte_workspace/sandbox/furniture_recognition/furn_test/scans/";

FurnitureScanner::FurnitureScanner(ros::ServiceClient& client, string out) {
    snapshotter = client;
    out_dir = out;
    last_pointcloud = sensor_msgs::PointCloud2::ConstPtr();
    pointcloud_received = false;
    last_modelName = "";
    last_modelId = 0;
}
FurnitureScanner::~FurnitureScanner() {}

void FurnitureScanner::pointcloud_snapshot_cb(const sensor_msgs::PointCloud2::ConstPtr& pc) {
    last_pointcloud = pc;
    pointcloud_received = true;
    ROS_INFO("Received a snapshot");
}

void FurnitureScanner::capture(string className, string modelName) {
    string dir = out_dir + className + "/" + modelName;
    // Check if output directory for this model exists. If not create
    boost::filesystem::path dirpath(dir);
    if (!boost::filesystem::exists(dirpath)) {
        if (!boost::filesystem::create_directories(dirpath)) {
            ROS_FATAL("Error creating directory %s.\n", dir.c_str ());
            exit(-1);
        }
    }

    //Call the snapshotter
    std_srvs::Empty srv;
    if (!snapshotter.call(srv)){
        ROS_FATAL("Call to the snapshotter failed!");
        exit(-1);
    }
    do { // Wait until the pointcloud is received
        ros::spinOnce(); // To get the snapshot callback called.
        ros::Duration(0.3).sleep();
    } while (!pointcloud_received);
    pointcloud_received = false;
    pcl17::PointCloud<pcl17::PointXYZ>::Ptr cloud(new pcl17::PointCloud<pcl17::PointXYZ>());
    pcl17::fromROSMsg (*last_pointcloud, *cloud); //Convert the pointCloud to a saving one
    
    //ROS_INFO("cloud_size before removeNaN: %d", cloud->points.size());
    vector< int > index;
    pcl17::removeNaNFromPointCloud(*cloud, *cloud, index);
    //cloud->is_dense = false; //from http://www.pcl-users.org/descriptor-extraction-Assertion-failed-td3704969.html
    //ROS_INFO("cloud_size after: %d, indx_size: %d", cloud->points.size(), index.size());

    if (modelName == last_modelName) {
        stringstream sstm;
        sstm << modelName << "_" << last_modelId;
        pcl17::io::savePCDFile(dir + "/" + sstm.str() +".pcd", *cloud);
        last_modelId++;
    }
    else {
        last_modelId = 0;
        pcl17::io::savePCDFile(dir + "/" + "full.pcd", *cloud); // We must have a full model!
    }

    last_modelName = modelName;
}


void capture(FurnitureScanner& fs) {
    string className, modelName;
    cout << "Insert object's class name: ";
    cin >> className;
    cout << "Insert object model's name: ";
    cin >> modelName;
    string out = "y";
    int model_id = 0;
    while (ros::ok() && out == "y") {
        stringstream sstm;
        sstm << modelName << model_id;
        fs.capture(className, sstm.str());
        cout << "Done!\nDo you want to capture another view of the same object model? [y/n] ";
        cin >> out;
        if (out == "n") {
            cout << "Do you want to capture another object model of the same class? [y/n] ";
            cin >> out;
            if (out == "y") {
                /*cout << "Do you want to change the model name? [y/n] ";
                cin >> out;
                if (out == "y") {*/
                    cout << "Insert the new name: ";
                    cin >> modelName;
                    model_id = 0;
                /*}
                else model_id++;
                out = "y";*/
            }
        }
    }

}

void print_menu() {
    cout << "Insert one option of the following:" << endl;
    cout << "\tcapture - Capture snapshots of an object to generate a model." << endl;
    cout << "\texit - Exit the program." << endl;
    cout << "Your option: ";
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "furniture_scanner");
    ros::NodeHandle n;

    string output_dir = OUT_DIR;
    if (argc < 2) ROS_WARN("No output dir set. Using %s", OUT_DIR.c_str());
    else output_dir = argv[1];

    // Check if output directory exists and if not, create it.
    boost::filesystem::path output_path(output_dir);
    if (!boost::filesystem::exists(output_path) || !boost::filesystem::is_directory(output_path)) {
        if (!boost::filesystem::create_directories(output_path)) {
          ROS_FATAL("Error creating directory %s.\n", output_path.c_str ());
          return -1;
        }
    }

    ros::ServiceClient client = n.serviceClient<std_srvs::Empty>(SNAPSHOTTER_SRV);
    FurnitureScanner fs(client, output_dir);
    ros::Subscriber sub = n.subscribe(POINTCLOUD_TOPIC, 10, &FurnitureScanner::pointcloud_snapshot_cb, &fs);

    //main loop
    string opt = "";
    do {
        if (opt == "capture") capture(fs);
        else if (opt == "exit") break;
        print_menu();
    } while (ros::ok() && cin >> opt);
    return 1;
}