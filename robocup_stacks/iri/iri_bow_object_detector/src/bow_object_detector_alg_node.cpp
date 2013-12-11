#include "bow_object_detector_alg_node.h"

BowObjectDetectorAlgNode::BowObjectDetectorAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<BowObjectDetectorAlgorithm>(),
  get_grasping_point_aserver_(public_node_handle_, "get_grasping_point"),
  EventPointCloudReady("PointCloud ready"),
  EventImageMaskReady("Image mask ready"),
  EventWrinkledMapReady("Wrinkled map ready")
{
        //init class attributes if necessary
        //this->loop_rate_ = 2;//in [Hz]
        first_pointcloud_ = true;
        
        // [init publishers]
        this->image_out_publisher_ = this->public_node_handle_.advertise<sensor_msgs::Image>("image_out", 1);
        this->pointcloud_out_publisher_ = this->public_node_handle_.advertise<sensor_msgs::PointCloud2>("pointcloud_out", 1);
        
        // [init subscribers]
        this->mask_image_in_subscriber_ = this->public_node_handle_.subscribe("mask_image_in", 1, &BowObjectDetectorAlgNode::mask_image_in_callback, this);
        this->pointcloud_in_subscriber_ = this->public_node_handle_.subscribe("pointcloud_in", 1, &BowObjectDetectorAlgNode::pointcloud_in_callback, this);
        
        // [init services]
        
        // [init clients]
        pointcloud_to_descriptorset_client_ = this->public_node_handle_.serviceClient<iri_perception_msgs::PclToDescriptorSet>("pointcloud_to_descriptorset");
        get_vws_client_ = this->public_node_handle_.serviceClient<iri_perception_msgs::DescriptorsToVws>("get_vws");
        get_sift_descriptors_client_ = this->public_node_handle_.serviceClient<iri_sift::DescriptorsFromImage>("get_sift_descriptors");
        set_background_image_client_ = this->public_node_handle_.serviceClient<iri_perception_msgs::SetImage>("set_background_image");
        select_grasp_point_client_ = this->public_node_handle_.serviceClient<iri_bow_object_detector::RefineGraspPoint>("select_grasp_point");
        detectObjects_client_ = this->public_node_handle_.serviceClient<iri_bow_object_detector::GeoVwDetection>("detectObjects");
        getVwSet_client_ = this->public_node_handle_.serviceClient<iri_sift::GeoVwSetSrv>("getVwSet");
        
        // [init action servers]
        get_grasping_point_aserver_.registerStartCallback(boost::bind(&BowObjectDetectorAlgNode::get_grasping_pointStartCallback, this, _1)); 
        get_grasping_point_aserver_.registerStopCallback(boost::bind(&BowObjectDetectorAlgNode::get_grasping_pointStopCallback, this)); 
        get_grasping_point_aserver_.registerIsFinishedCallback(boost::bind(&BowObjectDetectorAlgNode::get_grasping_pointIsFinishedCallback, this)); 
        get_grasping_point_aserver_.registerHasSucceedCallback(boost::bind(&BowObjectDetectorAlgNode::get_grasping_pointHasSucceedCallback, this)); 
        get_grasping_point_aserver_.registerGetResultCallback(boost::bind(&BowObjectDetectorAlgNode::get_grasping_pointGetResultCallback, this, _1)); 
        get_grasping_point_aserver_.registerGetFeedbackCallback(boost::bind(&BowObjectDetectorAlgNode::get_grasping_pointGetFeedbackCallback, this, _1)); 
        get_grasping_point_aserver_.start();
        
        // [init action clients]
}

BowObjectDetectorAlgNode::~BowObjectDetectorAlgNode(void)
{
        // [free dynamic memory]
}

void BowObjectDetectorAlgNode::mainNodeThread(void)
{
        pointcloud_ready_ = false;
        image_mask_ready_ = false;
        wrinkled_map_ready_ = false;
        
        // If true it grabs its own pointclouds
        // If false it grabs pointclouds from actions
        if (false) {
                // subscribe pointcloud
                this->pointcloud_in_subscriber_ = this->public_node_handle_.subscribe("pointcloud_in", 1, &BowObjectDetectorAlgNode::pointcloud_in_callback, this);
        }
        // else action server will do it
        
        // wait for pointcloud
        while (not pointcloud_ready_) {
                try {
                        EventPointCloudReady.wait(1000000); // 1 secs
                }catch(CEventTimeoutException& e){
                        ROS_INFO("Waiting for pointcloud...");
                }catch(CException& e){
                        ROS_ERROR_STREAM("get_board_info -> main_thread: Exception found waiting" << e.what());
                        return;
                }
        }
        
        // pointcloud -> image
        last_image_ = ros_pointcloud_to_ros_image(last_pointcloud_);
        

        // Get sift descriptors
        get_sift_descriptors_srv_.request.image = last_image_; 
        ROS_INFO("BowObjectDetectorAlgNode:: Sending New Request!"); 
        if (get_sift_descriptors_client_.call(get_sift_descriptors_srv_)) 
        { 
                ROS_INFO("BowObjectDetectorAlgNode:: Service called successfully!");
                last_sift_descriptors_ = get_sift_descriptors_srv_.response.descriptor_set;
        } 
        else 
        { 
                ROS_ERROR("BowObjectDetectorAlgNode:: Failed to Call Server on topic get_sift_descriptors "); 
        }
        
        // Get sift visual words
        get_vws_srv_.request.descriptor_set = last_sift_descriptors_; 
        ROS_INFO("BowObjectDetectorAlgNode:: Sending New Request!"); 
        if (get_vws_client_.call(get_vws_srv_)) 
        { 
                ROS_INFO("BowObjectDetectorAlgNode::  Service called successfully!");
                last_sift_vw_set_ = get_vws_srv_.response.geo_vw_set;
        } 
        else 
        { 
                ROS_ERROR("BowObjectDetectorAlgNode:: Failed to Call Server on topic get_vws "); 
        }
        
        
        // wait for mask
        while (not image_mask_ready_) {
                try {
                        EventImageMaskReady.wait(1000000); // 1 secs
                }catch(CEventTimeoutException& e){
                        ROS_INFO("Waiting for image mask...");
                }catch(CException& e){
                        ROS_ERROR_STREAM("get_board_info -> main_thread: Exception found waiting" << e.what());
                        return;
                }
        }
        
        
        detectGraspPoint();
        
        training();
        
        // [fill srv structure and make request to the server]
        
        // [fill msg structures]
        
        // [fill action structure and make request to the action server]

        // [publish messages]
}

/*  [subscriber callbacks] */
void BowObjectDetectorAlgNode::mask_image_in_callback(const sensor_msgs::Image::ConstPtr& msg) 
{ 
	ROS_INFO("BowObjectDetectorAlgNode::mask_image_in_callback: New Message Received"); 
	
	last_image_mask_ = *msg;
	image_mask_ready_ = true;
	EventImageMaskReady.set();
	
	//use appropiate mutex to shared variables if necessary 
	//this->alg_.lock(); 
	//this->mask_image_in_mutex_.enter(); 

	//std::cout << msg->data << std::endl; 

	//unlock previously blocked shared variables 
	//this->alg_.unlock(); 
	//this->mask_image_in_mutex_.exit(); 
}

void BowObjectDetectorAlgNode::pointcloud_in_callback(const sensor_msgs::PointCloud2::ConstPtr& msg) 
{ 
	ROS_INFO("BowObjectDetectorAlgNode::pointcloud_in_callback: New Message Received"); 
	
	if (first_pointcloud_) {
		first_pointcloud_ = false;
		set_background_image_srv_.request.image_in = ros_pointcloud_to_ros_image(*msg); 
		ROS_DEBUG("BowObjectDetectorAlgNode:: Sending New Request!"); 
		if (set_background_image_client_.call(set_background_image_srv_)) 
		{ 
			ROS_DEBUG_STREAM("BowObjectDetectorAlgNode:: Response: " << set_background_image_srv_.response.success); 
		} 
		else 
		{ 
			ROS_WARN("BowObjectDetectorAlgNode:: Failed to Call Server on topic set_background_image "); 
		}
	}
	else {
		last_pointcloud_ = *msg;
		pointcloud_ready_ = true;
		solution_ready_ = false;
		this->pointcloud_out_publisher_.publish(msg);
		this->image_out_publisher_.publish(ros_pointcloud_to_ros_image(*msg));
		EventPointCloudReady.set();
	}
	
	// unsubscribe
	this->pointcloud_in_subscriber_.shutdown();
}

/*  [service callbacks] */

/*  [action callbacks] */
void BowObjectDetectorAlgNode::get_grasping_pointStartCallback(const iri_bow_object_detector::GetGraspingPointGoalConstPtr& goal)
{ 
	alg_.lock(); 
	
	solution_ready_ = false;
	
	last_pointcloud_ = goal->pointcloud;
	this->pointcloud_out_publisher_.publish(goal->pointcloud);
	this->image_out_publisher_.publish(ros_pointcloud_to_ros_image(goal->pointcloud));
	
	pointcloud_ready_ = true;
	EventPointCloudReady.set();
	
	alg_.unlock(); 
} 

void BowObjectDetectorAlgNode::get_grasping_pointStopCallback(void) 
{ 
	alg_.lock(); 
	//stop action 
	alg_.unlock(); 
} 

bool BowObjectDetectorAlgNode::get_grasping_pointIsFinishedCallback(void) 
{ 
	bool ret = false; 

	alg_.lock(); 
	if (solution_ready_)
		ret = true;
	alg_.unlock(); 

	return ret; 
} 

bool BowObjectDetectorAlgNode::get_grasping_pointHasSucceedCallback(void) 
{ 
	bool ret = false; 

	alg_.lock(); 
	if (solution_ready_)
		ret = true;
	alg_.unlock(); 

	return ret; 
} 

void BowObjectDetectorAlgNode::get_grasping_pointGetResultCallback(iri_bow_object_detector::GetGraspingPointResultPtr& result) 
{ 
	pcl::PointCloud<pcl::PointXYZRGB> cloud;
	pcl::PointXYZRGB pixel;
	
	alg_.lock(); 
	//update result data to be sent to client 
	pcl::fromROSMsg (last_pointcloud_, cloud);
	pixel = cloud.at(select_grasp_point_srv_.response.grasp_point.x, select_grasp_point_srv_.response.grasp_point.y); 
	
	result->grasping_point.x = pixel.x;
	result->grasping_point.y = pixel.y;
	result->grasping_point.z = pixel.z;
	alg_.unlock(); 
} 

void BowObjectDetectorAlgNode::get_grasping_pointGetFeedbackCallback(iri_bow_object_detector::GetGraspingPointFeedbackPtr& feedback) 
{ 
	alg_.lock(); 
	//keep track of feedback 
	//ROS_INFO("feedback: %s", feedback->data.c_str()); 
	alg_.unlock(); 
}

/*  [action requests] */

void BowObjectDetectorAlgNode::node_config_update(Config &config, uint32_t level)
{
	this->alg_.lock();

	this->alg_.unlock();
}

void BowObjectDetectorAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
	return algorithm_base::main<BowObjectDetectorAlgNode>(argc, argv, "bow_object_detector_alg_node");
}


/* Other functions */
sensor_msgs::Image BowObjectDetectorAlgNode::ros_pointcloud_to_ros_image(sensor_msgs::PointCloud2 ros_cloud)
{
	pcl::PointCloud<pcl::PointXYZRGB> pcl_cloud;
	pcl::fromROSMsg (ros_cloud, pcl_cloud);
	
	cv::Mat cv_image = pcl_pointcloud_to_cv_image(pcl_cloud.makeShared());
	
// 	cv_image = crop_and_resize(cv_image);
	
	return *cv_image_to_ros_image(cv_image, ros_cloud.header);
}



cv::Mat BowObjectDetectorAlgNode::pcl_pointcloud_to_cv_image(pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud)
{
	pcl::PointXYZRGB pixel;
	cv::Mat cvimage;
	uint32_t rgb;
	uint8_t r;
	uint8_t g;
	uint8_t b;

	
	cvimage = cv::Mat::zeros(cloud->height, cloud->width, CV_8UC3);//a black image 
	for (int i = 0; i < cvimage.rows; i++) {
		//double* Mi = cvimage.ptr<double>(i);
		
		for (int j = 0; j< cvimage.cols; j++) {
			pixel = cloud->at(j,i);
			
			rgb = *reinterpret_cast<int*>(&pixel.rgb);
			r = (rgb >> 16) & 0x0000ff;
			g = (rgb >> 8)  & 0x0000ff;
			b = (rgb)       & 0x0000ff;
			//ROS_INFO_STREAM("Color: " << rgb );
			//if (pixel.x == pixel.x) { // if x != NaN
			if(! isnan(pixel.x))  { //Changed the line above by this, because we get erors when compiling.
				//Mi[j] = rgb;
                                // Change order bgr -> rgb 29/08/2012
				cvimage.at<cv::Vec3b>(i,j)[0] = b;
				cvimage.at<cv::Vec3b>(i,j)[1] = g;
				cvimage.at<cv::Vec3b>(i,j)[2] = r;
			}
		}
	}
	return cvimage;
}

cv::Mat BowObjectDetectorAlgNode::crop_and_resize(cv::Mat& image)
{
	cv::Mat newima = image.colRange(30,image.cols - 30).rowRange(20,image.rows - 20);
	cv::resize(newima,newima, cv::Size(640,480));
	
	return newima;
}

sensor_msgs::ImagePtr BowObjectDetectorAlgNode::cv_image_to_ros_image(cv::Mat cvimage, std_msgs::Header header)
{
	cv_bridge::CvImage out_msg;
	out_msg.encoding = sensor_msgs::image_encodings::BGR8;
	out_msg.image    = cvimage;
	out_msg.header.stamp = header.stamp; // This fails.
	return out_msg.toImageMsg();
}

void BowObjectDetectorAlgNode::detectGraspPoint()
{
        detectObjects_srv_.request.geo_vw_sets.clear();
        detectObjects_srv_.request.geo_vw_sets.push_back(last_sift_vw_set_); 
        detectObjects_srv_.request.image = last_image_; 
        detectObjects_srv_.request.mask = last_image_mask_; 
        ROS_INFO("BowObjectDetectorAlgNode:: Sending New Request!"); 
        if (detectObjects_client_.call(detectObjects_srv_)) 
        {  
                ROS_INFO("BowObjectDetectorAlgNode:: Service call successful!");
        } 
        else 
        { 
                ROS_INFO("BowObjectDetectorAlgNode:: Failed to Call service detectObjects on: %s", detectObjects_client_.getService().c_str());
                return;
        }
        
        pointcloud_to_descriptorset_srv_.request.pointcloud = last_pointcloud_; 
        ROS_INFO("BowObjectDetectorAlgNode:: Sending New Request!"); 
        if (pointcloud_to_descriptorset_client_.call(pointcloud_to_descriptorset_srv_)) 
        { 
                ROS_INFO("BowObjectDetectorAlgNode:: Response: OK"); 
        } 
        else 
        { 
                ROS_INFO("BowObjectDetectorAlgNode:: Failed to Call Server on topic pointcloud_to_descriptorset "); 
        }
        
        select_grasp_point_srv_.request.posible_solutions = detectObjects_srv_.response.posible_solutions; 
        select_grasp_point_srv_.request.descriptor_set = pointcloud_to_descriptorset_srv_.response.descriptor_set;
        select_grasp_point_srv_.request.image = last_image_; 
        ROS_INFO("BowObjectDetectorAlgNode:: Sending New Request!"); 
        if (select_grasp_point_client_.call(select_grasp_point_srv_)) 
        { 
//      ROS_INFO("BowObjectDetectorAlgNode:: Response: %s", select_grasp_point_srv_.response.result); 
                ROS_INFO("BowObjectDetectorAlgNode:: Service call successful!");
        } 
        else 
        { 
                ROS_INFO("BowObjectDetectorAlgNode:: Failed to Call service select_grasp_point on: %s ", select_grasp_point_client_.getService().c_str());
                return;
        }
        
        ROS_INFO_STREAM("Solution is " << select_grasp_point_srv_.response.grasp_point);
        
        solution_ready_ = true;
}

void BowObjectDetectorAlgNode::training()
{
    
}

