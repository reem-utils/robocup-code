#include "plane_segmentation_pcl_rgb_alg_node.h"

PlaneSegmentationPclRgbAlgNode::PlaneSegmentationPclRgbAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<PlaneSegmentationPclRgbAlgorithm>()
{
	//init class attributes if necessary
	//this->loop_rate_ = 2;//in [Hz]

	// [init publishers]
	this->segmented_image_publisher_ = this->public_node_handle_.advertise<sensor_msgs::Image>("segmented_image", 1);
	this->plane_coefficients_publisher_ = this->public_node_handle_.advertise<pcl::ModelCoefficients>("plane_coefficients", 1);
	this->pointcloud_out_publisher_ = this->public_node_handle_.advertise<sensor_msgs::PointCloud2>("pointcloud_out", 1);
	
	// [init subscribers]
	this->pointcloud_in_subscriber_ = this->public_node_handle_.subscribe("pointcloud_in", 1, &PlaneSegmentationPclRgbAlgNode::pointcloud_in_callback, this);
	
	// [init services]
  //this->segment_server_ = this->public_node_handle_.advertiseService("segment", &PlaneSegmentationPclRgbAlgNode::segmentCallback, this); UNUSED
	
	// [init clients]
	
	// [init action servers]
	
	// [init action clients]
	
}

PlaneSegmentationPclRgbAlgNode::~PlaneSegmentationPclRgbAlgNode(void)
{
	// [free dynamic memory]
}

void PlaneSegmentationPclRgbAlgNode::mainNodeThread(void)
{
	// [fill msg structures]
	//this->Image_msg_.data = my_var;
	//this->ModelCoefficients_msg_.data = my_var;
	//this->PointCloud2_msg_.data = my_var;
	
	// [fill srv structure and make request to the server]
	
	// [fill action structure and make request to the action server]

	// [publish messages]
	//this->segmented_image_publisher_.publish(this->Image_msg_);
	//this->plane_coefficients_publisher_.publish(this->ModelCoefficients_msg_);
	//this->pointcloud_out_publisher_.publish(this->PointCloud2_msg_);
}

/*  [subscriber callbacks] */
void PlaneSegmentationPclRgbAlgNode::pointcloud_in_callback(const sensor_msgs::PointCloud2::ConstPtr& msg) 
{ 
	
	pcl::PointCloud<pcl::PointXYZRGB> cloud_rgb;
	pcl::PointCloud<pcl::PointXYZ> cloud;
	pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_rgb_segmented;
	pcl::ModelCoefficients::Ptr coefficients (new pcl::ModelCoefficients);
	cv::Mat boardImage;
	
	pcl::fromROSMsg (*msg, cloud_rgb);
	pcl::fromROSMsg (*msg, cloud);
	
	ROS_DEBUG_STREAM("Segmenting plane");
	// Get segmented pointcloud
	cloud_rgb_segmented = this->alg_.segmentBiggestPlane(cloud_rgb.makeShared(), cloud.makeShared(), coefficients);
	boardImage = pointcloud_to_image(cloud_rgb_segmented);
	
	// PCL and image to ROS msg
	pcl::toROSMsg(*cloud_rgb_segmented, this->PointCloud2_msg_);
	std_msgs::Header header = this->PointCloud2_msg_.header;
	this->Image_msg_ = *cvimage_to_rosimage(boardImage, header);
	this->ModelCoefficients_msg_ = *coefficients;
	
	
	ROS_DEBUG_STREAM("Publishing segmented plane");
	// Publish
	
	
	if (this->pointcloud_out_publisher_.getNumSubscribers())
		this->pointcloud_out_publisher_.publish(this->PointCloud2_msg_);
	this->segmented_image_publisher_.publish(this->Image_msg_);
	this->plane_coefficients_publisher_.publish(this->ModelCoefficients_msg_);

	//use appropiate mutex to shared variables if necessary 
	//this->alg_.lock(); 
	//this->pointcloud_in_mutex_.enter(); 

	//std::cout << msg->data << std::endl; 

	//unlock previously blocked shared variables 
	//this->alg_.unlock(); 
	//this->pointcloud_in_mutex_.exit(); 
}

/*  [service callbacks] */
/* To recover replace "$$n" for "\n".
bool PlaneSegmentationPclRgbAlgNode::segmentCallback(iri_plane_segmentation_pcl_rgb::segment::Request &req, iri_plane_segmentation_pcl_rgb::segment::Response &res) $$n{ $$n	ROS_INFO("PlaneSegmentationPclRgbAlgNode::segmentCallback: New Request Received!"); $$n$$n	// Define data to be used.$$n	pcl::PointCloud<pcl::PointXYZRGB> cloud_rgb;$$n	pcl::PointCloud<pcl::PointXYZ> cloud;$$n	pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_rgb_segmented;$$n	pcl::ModelCoefficients::Ptr coefficients (new pcl::ModelCoefficients);$$n$$n	// From ROS msg to pcl.$$n	pcl::fromROSMsg(req.inputPCL, cloud_rgb);$$n	pcl::fromROSMsg(req.inputPCL, cloud);$$n$$n	ROS_INFO("PlaneSegmentationPclRgbAlgNode::segmentCallback: Processing New Request!"); $$n$$n	// Call algorithm function: segmentBiggestPlane.$$n	cloud_rgb_segmented = this->alg_.segmentBiggestPlane(cloud_rgb.makeShared(), cloud.makeShared(), coefficients);$$n	cv::Mat segmented_img = pointcloud_to_image(cloud_rgb_segmented);$$n$$n	// From image to ROS msg.$$n	res.segmentedImg = *cvimage_to_rosimage(segmented_img);$$n$$n	return true; $$n}
*/

/*  [action callbacks] */

/*  [action requests] */

void PlaneSegmentationPclRgbAlgNode::node_config_update(Config &config, uint32_t level)
{
	this->alg_.lock();

	this->alg_.unlock();
}

void PlaneSegmentationPclRgbAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<PlaneSegmentationPclRgbAlgNode>(argc, argv, "plane_segmentation_pcl_rgb_alg_node");
}


/* Other functions */
cv::Mat PlaneSegmentationPclRgbAlgNode::pointcloud_to_image(pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud)
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
			if(! isnan(pixel.x)){ //Changed the line above because we got error when compiling.
				//Mi[j] = rgb;
				cvimage.at<cv::Vec3b>(i,j)[0] = b;
				cvimage.at<cv::Vec3b>(i,j)[1] = g;
				cvimage.at<cv::Vec3b>(i,j)[2] = r;
			}
		}
	}
	
	return cvimage;
}

sensor_msgs::ImagePtr PlaneSegmentationPclRgbAlgNode::cvimage_to_rosimage(cv::Mat cvimage, std_msgs::Header header)
{
	cv_bridge::CvImage out_msg;
	out_msg.encoding = sensor_msgs::image_encodings::BGR8;
	out_msg.image    = cvimage;
	out_msg.header.stamp = header.stamp; // This fails.
	return out_msg.toImageMsg();
}
