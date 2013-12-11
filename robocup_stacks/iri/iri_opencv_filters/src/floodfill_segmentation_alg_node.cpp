#include "floodfill_segmentation_alg_node.h"

using namespace cv;

FloodfillSegmentationAlgNode::FloodfillSegmentationAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<FloodfillSegmentationAlgorithm>()
{
	//init class attributes if necessary
	//this->loop_rate_ = 2;//in [Hz]

	// [init publishers]
	this->image_out_publisher_ = this->public_node_handle_.advertise<sensor_msgs::Image>("image_out", 1);
	
	// [init subscribers]
	this->image_in_subscriber_ = this->public_node_handle_.subscribe("image_in", 1, &FloodfillSegmentationAlgNode::image_in_callback, this);
	
	// [init services]
	
	// [init clients]
	
	// [init action servers]
	
	// [init action clients]
	
}

FloodfillSegmentationAlgNode::~FloodfillSegmentationAlgNode(void)
{
	// [free dynamic memory]
}

void FloodfillSegmentationAlgNode::mainNodeThread(void)
{
	// [fill msg structures]
	//this->Image_msg_.data = my_var;
	
	// [fill srv structure and make request to the server]
	
	// [fill action structure and make request to the action server]
	
	// [publish messages]
	//this->image_out_publisher_.publish(this->Image_msg_);
}

/*  [subscriber callbacks] */
void FloodfillSegmentationAlgNode::image_in_callback(const sensor_msgs::Image::ConstPtr& msg) 
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
	
	cv_ptr->image = floodfillRemoval(cv_ptr->image);
	
	ROS_DEBUG_STREAM("Publishing floodfill");
	
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
cv::Mat FloodfillSegmentationAlgNode::floodfillRemoval(cv::Mat image)
{
	// WARNING Mask is bigger than image!!!!!!
	Mat dst, newMask, image_lab;
	int connectivity = 4;
	int newMaskVal = 0;
	int flags = connectivity + (newMaskVal << 8);
	Rect ccomp;
	int area = 0;
	int areaThreshold = floodfill_min_area;
	int x, y;
	int maxSeedSearchTries = 20;
	Vec3b ignoredColor;
	Scalar newVal;
	Scalar ffthresh;
	
	Point seed;
	//mask.create(image.rows+2, image.cols+2, CV_8UC1);
	
	if (colorspace_lab) {
		cvtColor(image, image, CV_BGR2Lab);
		ffthresh = Scalar(floodfill_threshold*3, floodfill_threshold, floodfill_threshold);
		ignoredColor = Vec3b(0,128,128); // black in l*a*b*
		newVal = Scalar(0,128,128); // black in l*a*b*
	}
	else { // BGR8
		ffthresh = Scalar(floodfill_threshold, floodfill_threshold, floodfill_threshold);
		ignoredColor = Vec3b(0,0,0); // black in BGR
		newVal = Scalar(0,0,0); // black in BGR
	}
	
	Vec3b color;
	for (int i = 0; i < floodfill_seed_num; i++) {
		// Find a non-black seed
		int iter_num = 0;
		do {
			x = floor(theRNG().next() % image.rows);
			y = floor(theRNG().next() % image.cols);
			seed = Point(y,x);
			color = image.at<cv::Vec3b>(x,y);
		} while ((image.at<cv::Vec3b>(x,y) == ignoredColor) && (iter_num++ < maxSeedSearchTries));
		
		if (image.at<cv::Vec3b>(x,y) != ignoredColor) { // if found a non-black seed
			newMask = Scalar::all(0);
			dst = image.clone();
			area = floodFill(dst, newMask, seed, newVal, 0, ffthresh, ffthresh, flags);
			ROS_DEBUG_STREAM("Area removed "<<area);
			if (area > areaThreshold)
				image = dst;
		}
	}
	
	if (colorspace_lab)
		cvtColor(image, image, CV_Lab2BGR);
	
	threshold( image, image, 10, 255, THRESH_BINARY );
	return image;
}

void FloodfillSegmentationAlgNode::node_config_update(Config &config, uint32_t level)
{
	this->alg_.lock();
	
	this->floodfill_threshold = config.floodfill_threshold;
	this->floodfill_min_area  = config.floodfill_min_area;
	this->floodfill_seed_num  = config.floodfill_seed_num;
	this->colorspace_lab      = config.colorspace_lab;
	
	// save the current configuration
	this->alg_.config_=config;
	
	this->alg_.unlock();
}

void FloodfillSegmentationAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
	return algorithm_base::main<FloodfillSegmentationAlgNode>(argc, argv, "floodfill_segmentation_alg_node");
}
