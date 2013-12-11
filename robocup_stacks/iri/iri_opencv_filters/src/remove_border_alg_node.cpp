#include "remove_border_alg_node.h"


RemoveBorderAlgNode::RemoveBorderAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<RemoveBorderAlgorithm>()
{
	//init class attributes if necessary
	//this->loop_rate_ = 2;//in [Hz]
	
	// [init publishers]
	this->image_out_publisher_ = this->public_node_handle_.advertise<sensor_msgs::Image>("image_out", 1);
	
	// [init subscribers]
	this->image_in_subscriber_ = this->public_node_handle_.subscribe("image_in", 1, &RemoveBorderAlgNode::image_in_callback, this);
	
	// [init services]
	
	// [init clients]
	
	// [init action servers]
	
	// [init action clients]
	
}

RemoveBorderAlgNode::~RemoveBorderAlgNode(void)
{
	// [free dynamic memory]
}

void RemoveBorderAlgNode::mainNodeThread(void)
{
	// [fill msg structures]
	//this->Image_msg_.data = my_var;
	
	// [fill srv structure and make request to the server]
	
	// [fill action structure and make request to the action server]

	// [publish messages]
	//this->image_out_publisher_.publish(this->Image_msg_);
}

/*  [subscriber callbacks] */
void RemoveBorderAlgNode::image_in_callback(const sensor_msgs::Image::ConstPtr& msg) 
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
	
	ROS_DEBUG("Remove border publishing image");
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


/* Other functions */
cv::Mat RemoveBorderAlgNode::processImage(cv::Mat image)
{
	Mat src_gray, res;
	Mat threshold_output;
	vector<vector<Point> > contours;
	vector<Vec4i> hierarchy;
	int thresh = 10;
	cvtColor( image, src_gray, CV_BGR2GRAY );
	blur( src_gray, src_gray, Size(3,3) );
	
	/// Detect edges using Threshold
	threshold( src_gray, threshold_output, thresh, 255, THRESH_BINARY );

	/// Find contours  
	findContours( threshold_output, contours, hierarchy, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );

	/// Find the convex hull object for each contour
	vector<vector<Point> >hull( contours.size() );
	if (remove_border_convex) {
		for( size_t i = 0; i < contours.size(); i++ ) {
			convexHull( Mat(contours[i]), hull[i], false );
		}
	}
	
	/// Draw contours + hull results
	Mat drawing = Mat::zeros( threshold_output.size(), CV_8UC3 );
	for( size_t i = 0; i< contours.size(); i++ )
	{ 
		Scalar color = Scalar( 255, 255, 255 );
		if (remove_border_convex)
			drawContours( drawing, hull, i, color, 1, 8, vector<Vec4i>(), 0, Point() );
		else
			drawContours( drawing, contours, i, color, 1, 8, vector<Vec4i>(), 0, Point() ); 
		
	}
	
	dilate(drawing, drawing, Mat::ones(remove_border_size, remove_border_size,1));
	subtract(image, drawing, res);
	
	return res;
}

void RemoveBorderAlgNode::node_config_update(Config &config, uint32_t level)
{
	this->alg_.lock();
	
	this->remove_border_size= config.remove_border_size;
	this->remove_border_convex = config.remove_border_convex;
	
	// save the current configuration
	this->alg_.config_=config;
	
	this->alg_.unlock();
}

void RemoveBorderAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
	return algorithm_base::main<RemoveBorderAlgNode>(argc, argv, "remove_border_alg_node");
}
