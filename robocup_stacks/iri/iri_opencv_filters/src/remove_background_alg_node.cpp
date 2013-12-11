#include "remove_background_alg_node.h"


using namespace cv;

RemoveBackgroundAlgNode::RemoveBackgroundAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<RemoveBackgroundAlgorithm>()
{
	//init class attributes if necessary
	//this->loop_rate_ = 2;//in [Hz]
// 	background_image_ = imread("/tmp/image_background.png");
	has_background_ = false;

	// [init publishers]
	this->image_out_publisher_ = this->public_node_handle_.advertise<sensor_msgs::Image>("image_out", 1);
	
	// [init subscribers]
	this->image_in_subscriber_ = this->public_node_handle_.subscribe("image_in", 1, &RemoveBackgroundAlgNode::image_in_callback, this);
	
	// [init services]
	this->set_background_image_server_ = this->public_node_handle_.advertiseService("set_background_image", &RemoveBackgroundAlgNode::set_background_imageCallback, this);
	
	// [init clients]
	
	// [init action servers]
	
	// [init action clients]
	
}

RemoveBackgroundAlgNode::~RemoveBackgroundAlgNode(void)
{
	// [free dynamic memory]
}

void RemoveBackgroundAlgNode::mainNodeThread(void)
{
	// [fill msg structures]
	//this->Image_msg_.data = my_var;
	
	// [fill srv structure and make request to the server]
	
	// [fill action structure and make request to the action server]

	// [publish messages]
	//this->image_out_publisher_.publish(this->Image_msg_);
}

/*  [subscriber callbacks] */
void RemoveBackgroundAlgNode::image_in_callback(const sensor_msgs::Image::ConstPtr& msg) 
{ 
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
	
	cv_ptr->image = processImage(cv_ptr->image);
	
	if (cv_ptr->image.cols != 0){
		ROS_DEBUG_STREAM("Publishing background substraction mask");
		this->image_out_publisher_.publish(cv_ptr->toImageMsg());
	}

	//use appropiate mutex to shared variables if necessary 
	//this->alg_.lock(); 
	//this->image_in_mutex_.enter(); 

	//unlock previously blocked shared variables 
	//this->alg_.unlock(); 
	//this->image_in_mutex_.exit(); 
}

/*  [service callbacks] */
bool RemoveBackgroundAlgNode::set_background_imageCallback(iri_perception_msgs::SetImage::Request &req, iri_perception_msgs::SetImage::Response &res) 
{ 
	ROS_DEBUG("RemoveBackgroundAlgNode::set_background_imageCallback: New Request Received!"); 
	
	cv_bridge::CvImagePtr cv_ptr;
	try
	{
		cv_ptr = cv_bridge::toCvCopy(req.image_in, sensor_msgs::image_encodings::BGR8);
	}
	catch (cv_bridge::Exception& e)
	{
		ROS_ERROR("cv_bridge exception: %s", e.what());
		res.success = false;
		return false;
	}
	
	//use appropiate mutex to shared variables if necessary 
	background_image_ = cv_ptr->image;
	has_background_ = true;
	
	res.success = true;
	
	return true; 
}

/*  [action callbacks] */

/*  [action requests] */

/* Other */
cv::Mat RemoveBackgroundAlgNode::processImage(cv::Mat image)
{
	Mat mask_bgr;
	
	// check if has background image
	if (!has_background_) {
		ROS_WARN("RemoveBackgroundAlgNode needs background image to be set.");
		mask_bgr = Mat::zeros(0, 0, 0);
	}
	else {
		cv::Mat differences, mask_gray;
		
		// differences
		cv::absdiff(image, background_image_, differences);
		
		// threshold
		cv::threshold(differences, differences, this->binarize_threshold_, 255, cv::THRESH_BINARY);
		cv::cvtColor(differences, mask_gray, CV_BGR2GRAY);
		cv::threshold(mask_gray, mask_gray, 10, 255, cv::THRESH_BINARY);
		cv::cvtColor(mask_gray, mask_bgr, CV_GRAY2BGR);
	}
	
	return mask_bgr;
}

void RemoveBackgroundAlgNode::node_config_update(Config &config, uint32_t level)
{
	this->alg_.lock();
	
	this->binarize_threshold_ = config.threshold;

	// save the current configuration
	this->alg_.config_=config;
	
	this->alg_.unlock();
}

void RemoveBackgroundAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
	return algorithm_base::main<RemoveBackgroundAlgNode>(argc, argv, "remove_background_alg_node");
}
