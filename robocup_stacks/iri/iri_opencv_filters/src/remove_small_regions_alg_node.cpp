#include "remove_small_regions_alg_node.h"

//#include <opencv2/highgui/highgui.hpp>
//static const char WINDOW[] = "Image window";

RemoveSmallRegionsAlgNode::RemoveSmallRegionsAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<RemoveSmallRegionsAlgorithm>()
{
	//init class attributes if necessary
	//this->loop_rate_ = 2;//in [Hz]
	
	// [init publishers]
	this->image_out_publisher_ = this->public_node_handle_.advertise<sensor_msgs::Image>("image_out", 1);
	
	// [init subscribers]
	this->image_in_subscriber_ = this->public_node_handle_.subscribe("image_in", 1, &RemoveSmallRegionsAlgNode::image_in_callback, this);
	
	// [init services]
	
	// [init clients]
	
	// [init action servers]
	
	// [init action clients]
	
	//cv::namedWindow(WINDOW);
}

RemoveSmallRegionsAlgNode::~RemoveSmallRegionsAlgNode(void)
{
	// [free dynamic memory]
	//cv::destroyWindow(WINDOW);
}

void RemoveSmallRegionsAlgNode::mainNodeThread(void)
{
	// [fill msg structures]
	//this->Image_msg_.data = my_var;
	
	// [fill srv structure and make request to the server]
	
	// [fill action structure and make request to the action server]

	// [publish messages]
	//this->remove_border_out_publisher_.publish(this->Image_msg_);
}

/*  [subscriber callbacks] */
void RemoveSmallRegionsAlgNode::image_in_callback(const sensor_msgs::Image::ConstPtr& msg) 
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
	
	ROS_DEBUG("Remove small regions publishing image");
	this->image_out_publisher_.publish(cv_ptr->toImageMsg());
	
	//use appropiate mutex to shared variables if necessary 
	//this->alg_.lock(); 
	//this->remove_border_in_mutex_.enter(); 

	//std::cout << msg->data << std::endl; 

	//unlock previously blocked shared variables 
	//this->alg_.unlock(); 
	//this->remove_border_in_mutex_.exit(); 
}

/*  [service callbacks] */

/*  [action callbacks] */

/*  [action requests] */


/* Other functions */
cv::Mat RemoveSmallRegionsAlgNode::processImage(cv::Mat image)
{
	Mat src_gray, res, threshold_output;
	vector<vector<Point> > contours;
	int thresh = 10;
	cvtColor( image, src_gray, CV_BGR2GRAY );
	
	/// Detect edges using Threshold
	threshold( src_gray, threshold_output, thresh, 255, THRESH_BINARY );
	
	/// Find contours  
	findContours( threshold_output, contours, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_NONE, Point(0, 0) );
	
	Mat mask = Mat::zeros( threshold_output.size(), CV_8UC3 );
	Scalar color_white = Scalar( 255, 255, 255 );
	for( size_t i = 0; i< contours.size(); i++ )
	{ 
		if (contours[i].size() < min_area_threshold) {
			drawContours( mask, contours, i, color_white, CV_FILLED); 
		}
	}
	
	bitwise_not(mask,mask);
	//cv::imshow(WINDOW, mask);
	//cv::waitKey(3);
	
	bitwise_and(image,mask,image);
	
	return image;
}

void RemoveSmallRegionsAlgNode::node_config_update(Config &config, uint32_t level)
{
	this->alg_.lock();
	
	this->min_area_threshold = config.min_area_threshold;
	
	// save the current configuration
	this->alg_.config_=config;
	
	this->alg_.unlock();
}

void RemoveSmallRegionsAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
	return algorithm_base::main<RemoveSmallRegionsAlgNode>(argc, argv, "remove_small_regions_alg_node");
}
