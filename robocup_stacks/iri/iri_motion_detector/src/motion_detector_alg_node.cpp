#include "motion_detector_alg_node.h"

using namespace cv;

MotionDetectorAlgNode::MotionDetectorAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<MotionDetectorAlgorithm>(),
  getMotionPosition_aserver_(public_node_handle_, "getMotionPosition"),
  EventInfoReady("Info ready")
{
  //init class attributes if necessary
  //this->loop_rate_ = 2;//in [Hz]

  // [init publishers]
  
  // [init subscribers]
  this->pointcloud_in_subscriber_ = this->public_node_handle_.subscribe("/pointcloud_in", 1, &MotionDetectorAlgNode::pointcloud_in_callback, this);
  this->image_in_subscriber_ = this->public_node_handle_.subscribe("/image_in", 1, &MotionDetectorAlgNode::image_in_callback, this);
  
  // [init services]
  
  // [init clients]
  
  // [init action servers]
  getMotionPosition_aserver_.registerStartCallback(boost::bind(&MotionDetectorAlgNode::getMotionPositionStartCallback, this, _1)); 
  getMotionPosition_aserver_.registerStopCallback(boost::bind(&MotionDetectorAlgNode::getMotionPositionStopCallback, this)); 
  getMotionPosition_aserver_.registerIsFinishedCallback(boost::bind(&MotionDetectorAlgNode::getMotionPositionIsFinishedCallback, this)); 
  getMotionPosition_aserver_.registerHasSucceedCallback(boost::bind(&MotionDetectorAlgNode::getMotionPositionHasSucceedCallback, this)); 
  getMotionPosition_aserver_.registerGetResultCallback(boost::bind(&MotionDetectorAlgNode::getMotionPositionGetResultCallback, this, _1)); 
  getMotionPosition_aserver_.registerGetFeedbackCallback(boost::bind(&MotionDetectorAlgNode::getMotionPositionGetFeedbackCallback, this, _1)); 
  getMotionPosition_aserver_.start();
  
  // [init action clients]
  
  first = true;
  //namedWindow("edges",1);
}

MotionDetectorAlgNode::~MotionDetectorAlgNode(void)
{
  // [free dynamic memory]
}

void MotionDetectorAlgNode::mainNodeThread(void)
{
  // [fill msg structures]
  
  // [fill srv structure and make request to the server]
  
  // [fill action structure and make request to the action server]

  // [publish messages]
}

/*  [subscriber callbacks] */
void MotionDetectorAlgNode::pointcloud_in_callback(const sensor_msgs::PointCloud2::ConstPtr& msg) 
{ 
 // ROS_INFO("MotionDetectorAlgNode::pointcloud_in_callback: New Message Received"); //FIXME: Uncomment this line
  
  pcl::fromROSMsg (*msg, cloud);
  waiting_for_pointcloud = false;
  EventInfoReady.set();

  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  //this->pointcloud_in_mutex_.enter(); 

  //std::cout << msg->data << std::endl; 

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  //this->pointcloud_in_mutex_.exit(); 
}
void MotionDetectorAlgNode::image_in_callback(const sensor_msgs::Image::ConstPtr& msg) 
{ 
	//ROS_INFO("MotionDetectorAlgNode::image_in_callback: New Message Received");  //FIXME: Uncomment this line
	
	cv_bridge::CvImagePtr cv_ptr;
	
	try
	{
		cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
	}
	catch (cv_bridge::Exception& e)
	{
		ROS_ERROR("cv_bridge exception: %s", e.what());
		return;
	}
	
	Mat edges;
	
	if (first) {
		       
		
		
		cvtColor(cv_ptr->image, edges, CV_BGR2GRAY);
		frameOld = edges.clone();
		first = false;
	}
	else {

		// Ruben
		Moments my_moments =  moments(frameOld);
		previous_gravity_center.x = my_moments.m10/my_moments.m00;
		previous_gravity_center.y = my_moments.m01/my_moments.m00;
		// /Ruben

		cvtColor(cv_ptr->image, edges, CV_BGR2GRAY);
		GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);
		//Canny(edges, edges, 0, 30, 3);
		absdiff(edges, frameOld,resultat);
		erode(resultat,resultat,Mat());
		//imshow("edges", resultat);
		//waitKey(3);
		frameOld = edges.clone();
		//frameOld = edges;
	}

	//use appropiate mutex to shared variables if necessary 
	//this->alg_.lock(); 
	//this->image_in_mutex_.enter(); 

	//std::cout << msg->data << std::endl; 

	//unlock previously blocked shared variables 
	//this->alg_.unlock(); 
	//this->image_in_mutex_.exit(); 
}

/*  [service callbacks] */

/*  [action callbacks] */
void MotionDetectorAlgNode::getMotionPositionStartCallback(const iri_motion_detector::MotionDetectorActionGoalConstPtr& goal)
{ 
	alg_.lock(); 
	//check goal 
	ROS_INFO_STREAM("Start action server");
	
	processing = true;
	waiting_for_pointcloud = true;

  Point gravity_center;
  pcl::PointXYZ point ;
  double meanX = 0, meanY = 0;  
	
	/*result
	sacar centro gravedad
	wait for kinect
	sacar poseSTamped
	return poseStamped
	*/
//  do{

//    do{

    	this->pointcloud_in_subscriber_ = this->public_node_handle_.subscribe("/pointcloud_in", 1, &MotionDetectorAlgNode::pointcloud_in_callback, this);
    	
    do{

    	//ROS_INFO_STREAM("before event");
    	while (waiting_for_pointcloud) {
    		//ROS_INFO_STREAM("event");
    		try {
    			EventInfoReady.wait(5000000); // 5 sec
    		}catch(CEventTimeoutException& e){
          ROS_ERROR_STREAM("PointCloud Timeout!");
    		}catch(CException& e){
    			ROS_ERROR("Exception no timeout");
    			return;
    		}
    	}
    	
    	//this->pointcloud_in_subscriber_.shutdown();
    	
    	// gravity_center = algo(resultat);
    	Moments my_moments =  moments(resultat);
    	gravity_center.x = my_moments.m10/my_moments.m00;
    	gravity_center.y = my_moments.m01/my_moments.m00;

      /// Sometimes the moments computation fails for unknown reason. Then it returns a large negative number
      /// To bypass this error, we set the gravity center to the center of the image
    	if(gravity_center.x < 0 || gravity_center.y < 0){
        gravity_center.x = 309;
        gravity_center.y = 260;
    	}

        //ROS_INFO_STREAM("Gravity center " << gravity_center);
        /*
        if(_average.size() > 10){
          _average.pop_front();
        }
        _average.push_back(gravity_center);
          
        
    	  for(std::deque<cv::Point>::iterator it = _average.begin(); it != _average.end(); ++it){
            meanX += it->x;
            meanY += it->y;
        }
            
        meanX /= _average.size();
        meanY /= _average.size();
        */
        /*
        FIXME: After test, remove the 7 lines below
    	float distance = sqrt( 
    		pow(gravity_center.x - previous_gravity_center.x, 2) + 
    		pow(gravity_center.y - previous_gravity_center.y, 2)
    		 );	
    	
        ROS_INFO_STREAM("\nPrevious gravity center " << previous_gravity_center);
        ROS_INFO_STREAM("Difference between      " << distance);
        */

    //FIXME: Make adjustment of the parameters below.    
	//  }while(meanX > 290 && meanX < 320 && meanY > 215 && meanY < 260);

    //ROS_INFO_STREAM ("gravity center (" << gravity_center.x << "," << gravity_center.y <<")");
    //ROS_INFO_STREAM ("Cloud size ("<< cloud.width <<","<< cloud.height <<")");

    // get pose from cloud and resultat
    point = cloud.at(gravity_center.x,gravity_center.y);
    
  }while(isnan(point.x) || isnan(point.y) || isnan(point.z) || (distance = sqrtf(point.x * point.x + point.y * point.y + point.z * point.z)) > MAXIMUM_DISTANCE );

    
    this->pointcloud_in_subscriber_.shutdown();
      

    distance = sqrtf(point.x * point.x + point.y * point.y + point.z * point.z);

    //ROS_INFO_STREAM("POINT: "<< point);
    printf("\nPoint(%.2f, %.2f, %.2f)): ", point.x, point.y, point.z);
    

    ROS_INFO_STREAM("\n\nDistance: "<< distance);

  //}while(distance > MAXIMUM_DISTANCE);

  motionPose.pose.position.x = point.x;
  motionPose.pose.position.y = point.y;
  motionPose.pose.position.z = point.z;
  motionPose.pose.orientation.x = 0;
  motionPose.pose.orientation.y = 0;
  motionPose.pose.orientation.z = 0;
  motionPose.pose.orientation.w = 1;
  motionPose.header.stamp = ros::Time::now();
  motionPose.header.frame_id = "/head_mount_xtion_ir_optical_frame" ; // "/camera_depth_frame";

  processing = false;
	//execute goal 
	alg_.unlock(); 
} 

void MotionDetectorAlgNode::getMotionPositionStopCallback(void) 
{ 
  alg_.lock(); 
    //stop action 
  alg_.unlock(); 
} 

bool MotionDetectorAlgNode::getMotionPositionIsFinishedCallback(void) 
{ 
  bool ret = false; 

  alg_.lock(); 
    //if action has finish for any reason 
    //ret = true; 
  if (not processing)
	  ret = true;
  alg_.unlock(); 
  
  

  return ret; 
} 

bool MotionDetectorAlgNode::getMotionPositionHasSucceedCallback(void) 
{ 
  bool ret = false; 

  alg_.lock(); 
    //if goal was accomplished 
    //ret = true 
  if (not processing)
	  ret = true;
  alg_.unlock(); 
  
  

  return ret; 
} 

void MotionDetectorAlgNode::getMotionPositionGetResultCallback(iri_motion_detector::MotionDetectorActionResultPtr& result) 
{ 
  alg_.lock(); 
    //update result data to be sent to client 
    result->pose = motionPose; 
  alg_.unlock(); 
} 

void MotionDetectorAlgNode::getMotionPositionGetFeedbackCallback(iri_motion_detector::MotionDetectorActionFeedbackPtr& feedback) 
{ 
  alg_.lock(); 
    //keep track of feedback 
    //ROS_INFO("feedback: %s", feedback->data.c_str()); 
  alg_.unlock(); 
}

/*  [action requests] */

void MotionDetectorAlgNode::node_config_update(Config &config, uint32_t level)
{
  this->alg_.lock();

  this->alg_.unlock();
}

void MotionDetectorAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<MotionDetectorAlgNode>(argc, argv, "motion_detector_alg_node");
}
