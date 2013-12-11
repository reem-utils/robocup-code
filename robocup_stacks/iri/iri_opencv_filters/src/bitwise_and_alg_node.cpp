#include "bitwise_and_alg_node.h"


using namespace cv;

BitwiseAndAlgNode::BitwiseAndAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<BitwiseAndAlgorithm>()
{
	//init class attributes if necessary
	this->loop_rate_ = 2;//in [Hz]
	has_image1_ = false;
	has_image2_ = false;

	// [init publishers]
	this->image_out_publisher_ = this->public_node_handle_.advertise<sensor_msgs::Image>("image_out", 1);
	
	// [init subscribers]
	this->image_in1_subscriber_ = this->public_node_handle_.subscribe("image_in1", 1, &BitwiseAndAlgNode::image_in1_callback, this);
	this->image_in2_subscriber_ = this->public_node_handle_.subscribe("image_in2", 1, &BitwiseAndAlgNode::image_in2_callback, this);
	
	// [init services]
	
	// [init clients]
	
	// [init action servers]
	
	// [init action clients]
	
}

BitwiseAndAlgNode::~BitwiseAndAlgNode(void)
{
	// [free dynamic memory]
}

void BitwiseAndAlgNode::mainNodeThread(void)
{
	// [fill msg structures]
	//this->Image_msg_.data = my_var;
	
	// [fill srv structure and make request to the server]
	
	// [fill action structure and make request to the action server]

	// [publish messages]
// 	this->image_out_publisher_.publish( cvimage_to_rosimage( bitwise_and_last_images() ) );
}

/*  [subscriber callbacks] */
void BitwiseAndAlgNode::image_in1_callback(const sensor_msgs::Image::ConstPtr& msg) 
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
	last_image1_ = cv_ptr->image;
	has_image1_ = true; 
	
	publish_bitwise_and_last_images();
}

void BitwiseAndAlgNode::image_in2_callback(const sensor_msgs::Image::ConstPtr& msg) 
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
	last_image2_ = cv_ptr->image;
	has_image2_ = true; 
	
	publish_bitwise_and_last_images();
}

/*  [service callbacks] */

/*  [action callbacks] */

/*  [action requests] */

/* Other */
void BitwiseAndAlgNode::publish_bitwise_and_last_images()
{
	Mat dst;
	
	// check if already has images
	if (has_image1_ && has_image2_) {
		cv::bitwise_and(last_image1_, last_image2_, dst);
		has_image1_ = false;
		has_image2_ = false;
		this->image_out_publisher_.publish( cvimage_to_rosimage(dst));
	}
	else {
		ROS_WARN("BitwiseAndAlgNode: Input images aren't ready!");
	}
}

void BitwiseAndAlgNode::node_config_update(Config &config, uint32_t level)
{
	this->alg_.lock();

	// save the current configuration
	this->alg_.config_=config;
	
	this->alg_.unlock();
}

void BitwiseAndAlgNode::addNodeDiagnostics(void)
{
}

sensor_msgs::ImagePtr BitwiseAndAlgNode::cvimage_to_rosimage(cv::Mat cvimage)
{
	cv_bridge::CvImage out_msg;
	out_msg.encoding = sensor_msgs::image_encodings::BGR8;
	out_msg.image    = cvimage;
	out_msg.header.stamp = ros::Time::now();
	//out_msg.header.stamp = header.stamp; // This fails.
	return out_msg.toImageMsg();
}

/* main function */
int main(int argc,char *argv[])
{
	return algorithm_base::main<BitwiseAndAlgNode>(argc, argv, "bitwise_and_alg_node");
}
