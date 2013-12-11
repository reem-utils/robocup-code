#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <iri_motion_detector/MotionDetectorActionGoal.h>
#include <iri_motion_detector/MotionDetectorActionResult.h>
#include <iri_motion_detector/MotionDetectorActionAction.h>
#include <iri_motion_detector/MotionDetectorActionFeedback.h>
#include <visualization_msgs/Marker.h>

typedef actionlib::SimpleActionClient<iri_motion_detector::MotionDetectorActionAction> Client;

/**
  This class allows a visual debug.
  Publish a Marker in the /visualization_marker topic indicating the detected moviment location.
  You can view the result in rviz adding a Marker and PointCloud2 Display types in the topics /visualization_marker and /camera/depth/points 
  respectively in the /openni_depth_optical_frame frame.
*/

class IriMotionDetectorMarkerDebug{

protected:  
  Client client;
  ros::NodeHandle node_handle;
  ros::Publisher *vis_pub;
  visualization_msgs::Marker marker;
  iri_motion_detector::MotionDetectorActionGoal goal;

  void publishMarker(const iri_motion_detector::MotionDetectorActionResultConstPtr& result);
  void actionClientSendGoal();
  void done_cb(const actionlib::SimpleClientGoalState& state, const iri_motion_detector::MotionDetectorActionResultConstPtr& result);

public:
  IriMotionDetectorMarkerDebug();
  
};

IriMotionDetectorMarkerDebug::IriMotionDetectorMarkerDebug() : client("/iri_motion_detector/getMotionPosition", true ){// true -> don't need ros::spin()
    //marker.header.frame_id = "/head_mount_xtion_ir_optical_frame";
    marker.header.frame_id = "/base_link";
    marker.header.stamp = ros::Time();
    marker.ns = "iri_motion_detector_marker";
    marker.id = 0;
    marker.type = visualization_msgs::Marker::SPHERE;
    marker.action = visualization_msgs::Marker::ADD;
    marker.scale.x = 0.2;
    marker.scale.y = 0.2;
    marker.scale.z = 0.2;
    marker.color.a = 1.0;
    marker.color.r = 0;
    marker.color.g = 255;
    marker.color.b = 0;

    ros::Publisher pub = node_handle.advertise<visualization_msgs::Marker>( "/motion_detector_marker", 0 );
    this->vis_pub = &pub;

    ROS_INFO("Waiting for action server to start.");
    client.waitForServer();
    ROS_INFO("Action server started, sending goal.");
    this->actionClientSendGoal();
}

void IriMotionDetectorMarkerDebug::publishMarker(const iri_motion_detector::MotionDetectorActionResultConstPtr& result){
    
    marker.pose.position.x = result->pose.pose.position.x;
    marker.pose.position.y = result->pose.pose.position.y;
    marker.pose.position.z = result->pose.pose.position.z;
    marker.pose.orientation.x = 0.0;
    marker.pose.orientation.y = 0.0;
    marker.pose.orientation.z = 0.0;
    marker.pose.orientation.w = 1.0;
    
    vis_pub->publish( marker );
    ROS_INFO("Marker published");
}

void IriMotionDetectorMarkerDebug::actionClientSendGoal(){
    while(ros::ok()){
      this->client.sendGoal(
        this->goal,
        boost::bind(&IriMotionDetectorMarkerDebug::done_cb, this, _1, _2),
        Client::SimpleActiveCallback(),
        Client::SimpleFeedbackCallback());

      this->client.waitForResult(ros::Duration(30.0));
      ROS_INFO("Sending IriMotionDetectionActionGoal again.");
    }
}

void IriMotionDetectorMarkerDebug::done_cb(const actionlib::SimpleClientGoalState& state, const iri_motion_detector::MotionDetectorActionResultConstPtr& result){
    //ROS_INFO("------------------->> Finished in state [%s]", state.toString().c_str());
    
    if(isnan(result->pose.pose.position.x) || isnan(result->pose.pose.position.y) || isnan(result->pose.pose.position.z))
      return;

    this->publishMarker(result);
}


int main(int argc, char **argv){
    
    ros::init(argc, argv, "iri_motion_detector_marker_debug");

    IriMotionDetectorMarkerDebug IriMotionDetectorMarkerDebug;

    return 0;
}
