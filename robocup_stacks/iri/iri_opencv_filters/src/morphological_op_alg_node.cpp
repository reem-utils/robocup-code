#include "morphological_op_alg_node.h"

using namespace cv;

MorphologicalOpAlgNode::MorphologicalOpAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<MorphologicalOpAlgorithm>()
{
  //init class attributes if necessary
  //this->loop_rate_ = 2;//in [Hz]

  // [init publishers]
  this->image_out_publisher_ = this->public_node_handle_.advertise<sensor_msgs::Image>("image_out", 1);
  
  // [init subscribers]
  this->image_in_subscriber_ = this->public_node_handle_.subscribe("image_in", 1, &MorphologicalOpAlgNode::image_in_callback, this);
  
  // [init services]
  
  // [init clients]
  
  // [init action servers]
  
  // [init action clients]
}

MorphologicalOpAlgNode::~MorphologicalOpAlgNode(void)
{
  // [free dynamic memory]
}

void MorphologicalOpAlgNode::mainNodeThread(void)
{
  // [fill msg structures]
  //this->Image_msg_.data = my_var;
  
  // [fill srv structure and make request to the server]
  
  // [fill action structure and make request to the action server]

  // [publish messages]
  //this->image_out_publisher_.publish(this->Image_msg_);
}

/*  [subscriber callbacks] */
void MorphologicalOpAlgNode::image_in_callback(const sensor_msgs::Image::ConstPtr& msg) 
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
	
	ROS_DEBUG("Publishing morphological operation");
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
cv::Mat MorphologicalOpAlgNode::processImage(cv::Mat image)
{
	cv::Mat dst;
	cv::Mat element;
	//cvtColor(image, image, CV_BGR2Lab);
	if (!structuring_element_shape.compare("ellipse"))
		element = cv::getStructuringElement(MORPH_ELLIPSE, cv::Size(morph_element_size, morph_element_size));
	else if (!structuring_element_shape.compare("rect"))
		element = cv::getStructuringElement(MORPH_RECT, cv::Size(morph_element_size, morph_element_size));
	else if (!structuring_element_shape.compare("cross"))
		element = cv::getStructuringElement(MORPH_CROSS, cv::Size(morph_element_size, morph_element_size));
	else {
		ROS_WARN("Morphological element shape not recognized");
		return image;
	}
	
	if (!morph_operation.compare("open")) {
		cv::morphologyEx(image, dst, cv::MORPH_OPEN, element);
	}
	else if (!morph_operation.compare("close")){
		cv::morphologyEx(image, dst, cv::MORPH_CLOSE, element);
	}
	else if (!morph_operation.compare("gradient")) {
		cv::morphologyEx(image, dst, cv::MORPH_GRADIENT, element, Point(-1,-1), 1);
	}
	else if (!morph_operation.compare("tophat")) {
		cv::medianBlur(image, image, 5);
		cv::morphologyEx(image, dst, cv::MORPH_TOPHAT, element);
	}
	else if (!morph_operation.compare("blackhat")) {
		cv::morphologyEx(image, dst, cv::MORPH_BLACKHAT, element, Point(-1,-1), 1);
	}
	else if (!morph_operation.compare("addgradient")) {
		dst = add_gradient_to_image(image, element);
	}
	else if (!morph_operation.compare("addblackhat")) {
		cv::morphologyEx(image, dst, cv::MORPH_BLACKHAT, element);
		//threshold(dst, dst, 13, 50, THRESH_BINARY);
		subtract(dst, morph_val_reduction, dst);
		subtract(image, dst, dst);
	}
	else if (!morph_operation.compare("dilate")) {
		cv::dilate(image, dst, element);
	}
	else if (!morph_operation.compare("erode")) {
		cv::erode(image, dst, element);
	}
	else {
		ROS_WARN("Morphological operation not recognized");
		return image;
	}
	
	//cvtColor(dst, dst, CV_Lab2BGR);
	return dst;
}


cv::Mat MorphologicalOpAlgNode::add_gradient_to_image(cv::Mat image, cv::Mat element)
{
	Mat dst;
	Mat src_gray, threshold_output, drawing;
	vector<vector<Point> > contours;
	vector<Vec4i> hierarchy;
	int thresh = 10;
	
	cv::morphologyEx(image, dst, cv::MORPH_GRADIENT, element, Point(-1,-1), 1);
	
	/**
	Remove border
	*/
	cvtColor( dst, src_gray, CV_BGR2GRAY );
	blur( src_gray, src_gray, Size(3,3) );
	
	/// Detect edges using Threshold
	threshold( src_gray, threshold_output, thresh, 255, THRESH_BINARY );

	/// Find contours  
	findContours( threshold_output, contours, hierarchy, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );

	/// Find the convex hull object for each contour
	vector<vector<Point> >hull( contours.size() );
	for( size_t i = 0; i < contours.size(); i++ ) {
		convexHull( Mat(contours[i]), hull[i], false );
	}
	
	/// Draw contours + hull results
	drawing = Mat::zeros( threshold_output.size(), CV_8UC3 );
	for( size_t i = 0; i< contours.size(); i++ )
	{ 
		Scalar color = Scalar( 255, 255, 255 );
		drawContours( drawing, hull, i, color, 1, 8, vector<Vec4i>(), 0, Point() );
	}
	dilate(drawing, drawing, Mat::ones(morph_element_size * 2 + 1, morph_element_size * 2 + 1, 1));
	subtract(dst, drawing, dst);
	
	/**
	dst now is gradient without external border
	*/
	
	//threshold(dst, dst, morph_val_reduction, 50, THRESH_BINARY);
	subtract(dst, morph_val_reduction, dst);
	
	subtract(image, dst, dst);
	
	return dst;
}


void MorphologicalOpAlgNode::node_config_update(Config &config, uint32_t level)
{
  this->alg_.lock();
  
  this->morph_element_size = config.morph_element_size;
  this->morph_operation = config.morph_operation;
  this->morph_val_reduction = config.morph_val_reduction;
  this->structuring_element_shape = config.structuring_element_shape;

  // save the current configuration
  //this->alg_.config_=config;

  this->alg_.unlock();
}

void MorphologicalOpAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<MorphologicalOpAlgNode>(argc, argv, "morphological_op_alg_node");
}
