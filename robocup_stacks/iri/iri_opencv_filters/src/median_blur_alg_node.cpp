#include "median_blur_alg_node.h"


using namespace cv;

MedianBlurAlgNode::MedianBlurAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<MedianBlurAlgorithm>()
{
	//init class attributes if necessary
	//this->loop_rate_ = 2;//in [Hz]

	// [init publishers]
	this->image_out_publisher_ = this->public_node_handle_.advertise<sensor_msgs::Image>("image_out", 1);
	
	// [init subscribers]
	this->image_in_subscriber_ = this->public_node_handle_.subscribe("image_in", 1, &MedianBlurAlgNode::image_in_callback, this);
	
	// [init services]
	
	// [init clients]
	
	// [init action servers]
	
	// [init action clients]
	
}

MedianBlurAlgNode::~MedianBlurAlgNode(void)
{
	// [free dynamic memory]
}

void MedianBlurAlgNode::mainNodeThread(void)
{
	// [fill msg structures]
	//this->Image_msg_.data = my_var;
	
	// [fill srv structure and make request to the server]
	
	// [fill action structure and make request to the action server]

	// [publish messages]
	//this->image_out_publisher_.publish(this->Image_msg_);
}

/*  [subscriber callbacks] */
void MedianBlurAlgNode::image_in_callback(const sensor_msgs::Image::ConstPtr& msg) 
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
	
	ROS_DEBUG_STREAM("Publishing median blur");
	
	this->image_out_publisher_.publish(cv_ptr->toImageMsg());

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

/*  [action requests] */

/* Other */
cv::Mat MedianBlurAlgNode::processImage(cv::Mat image)
{
	Mat dst;
	
	cv::medianBlur(image, dst, medianblur_size);
	
	return dst;
}

void MedianBlurAlgNode::node_config_update(Config &config, uint32_t level)
{
	this->alg_.lock();
	
	this->medianblur_size = config.medianblur_size;
	
	// save the current configuration
	this->alg_.config_=config;
	
	this->alg_.unlock();
}

void MedianBlurAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
	return algorithm_base::main<MedianBlurAlgNode>(argc, argv, "median_blur_alg_node");
}
