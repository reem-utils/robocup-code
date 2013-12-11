#include "sift_alg_node.h"

SiftAlgNode::SiftAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<SiftAlgorithm>()
{
  //init class attributes if necessary
  //this->loop_rate_ = 2;//in [Hz]
  ROS_INFO("Enterning iri_sift.");
  // [init publishers]
  this->geo_vw_set_publisher_ = this->public_node_handle_.advertise<iri_perception_msgs::GeoVwSet>("geo_vw_set", 1);
  
  // [init subscribers]
  this->image_in_subscriber_ = this->public_node_handle_.subscribe("image_in", 1, &SiftAlgNode::image_in_callback, this);
  
  // [init services]
  this->descriptors_from_image_server_ = this->public_node_handle_.advertiseService("descriptors_from_image", &SiftAlgNode::descriptors_from_imageCallback, this);
  this->set_sift_centroids_server_ = this->public_node_handle_.advertiseService("set_sift_centroids", &SiftAlgNode::set_sift_centroidsCallback, this);
  this->get_geo_vw_set_server_ = this->public_node_handle_.advertiseService("get_geo_vw_set", &SiftAlgNode::get_geo_vw_setCallback, this);
  
  // [init clients]
  
  // [init action servers]
  
  // [init action clients]
}

SiftAlgNode::~SiftAlgNode(void)
{
	// [free dynamic memory]
}

void SiftAlgNode::mainNodeThread(void)
{
	// [fill msg structures]
	//this->BagVisualWords_msg_.data = my_var;
	
	// [fill srv structure and make request to the server]
	
	// [fill action structure and make request to the action server]

	// [publish messages]
// 	this->geo_vw_set_publisher_.publish(this->BagVisualWords_msg_);
}

/*  [subscriber callbacks] */
void SiftAlgNode::image_in_callback(const sensor_msgs::Image::ConstPtr& msg) 
{ 
	cv_bridge::CvImagePtr cv_ptr;
	
	try
	{
		cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::RGB8);
	}
	catch (cv_bridge::Exception& e)
	{
		ROS_ERROR("cv_bridge exception: %s", e.what());
		return;
	}
	
	ROS_INFO("SiftAlgNode::image_in_callback: Processing image."); 
	
// 	cv::Mat descriptors;
// 	std::vector<cv::KeyPoint> keypoints;
// 	this->alg_.get_sift_descriptors(cv_ptr->image, descriptors, keypoints);
	
// 	ROS_INFO_STREAM("Tipo es " << descriptors.type());
// 	ROS_INFO_STREAM("Size es " << descriptors.size().width << "," << descriptors.size().height);
	
// 	this->alg_.save_descriptors(descriptors);
	
	if (this->alg_.centroids_ready_) {
		ROS_DEBUG("Getting geo_vw.");
		this->GeoVwSet_msg_ = this->alg_.get_geovw_from_image(cv_ptr->image);
		this->geo_vw_set_publisher_.publish(this->GeoVwSet_msg_);
	}
	else
		ROS_ERROR("iri_sift: Need centroids!");
}

/*  [service callbacks] */
bool SiftAlgNode::descriptors_from_imageCallback(iri_sift::DescriptorsFromImage::Request &req, iri_sift::DescriptorsFromImage::Response &res) 
{ 
        ROS_INFO("SiftAlgNode::descriptors_from_imageCallback: New Request Received!"); 

        // checks and get image
        if (not this->alg_.centroids_ready_) {
                ROS_ERROR("iri_sift: Need centroids!");
                return false;
        }
        
        cv_bridge::CvImagePtr cv_ptr;
        try
        {
                cv_ptr = cv_bridge::toCvCopy(req.image, sensor_msgs::image_encodings::RGB8);
        }
        catch (cv_bridge::Exception& e)
        {
                ROS_ERROR("cv_bridge exception: %s", e.what());
                return false;
        }

        // actual processing
        res.descriptor_set = this->alg_.get_descriptors_from_image(cv_ptr->image);

        return true; 
}
bool SiftAlgNode::set_sift_centroidsCallback(iri_publish_params::classifier_update_service::Request &req, iri_publish_params::classifier_update_service::Response &res) 
{ 
        ROS_INFO("SiftAlgNode::set_sift_centroidsCallback: New Request Received!"); 
        
        //use appropiate mutex to shared variables if necessary 
        this->alg_.lock(); 
        
        // If something fails maybe size is incorrect
        ROS_INFO_STREAM("Size " << req.params.update_params.size() << " y "  << req.params.update_params[0].params.size());
        
        // each row is a descriptor
        this->alg_.sift_centroids_ = cv::Mat::zeros(req.params.update_params.size(), req.params.update_params[0].params.size(), CV_32FC1); // (rows, cols)
        for(size_t i=0; i < req.params.update_params.size(); i++) {
                for(size_t j=0; j< req.params.update_params[i].params.size(); j++) {
                        this->alg_.sift_centroids_.at<float>(i,j) = (float)req.params.update_params[i].params[j];
                }
        }
        
        this->alg_.centroids_ready_ = true;
        
        //unlock previously blocked shared variables 
        this->alg_.unlock(); 
        
        res.result = true;
        return true; 
}
bool SiftAlgNode::get_geo_vw_setCallback(iri_sift::GeoVwSetSrv::Request &req, iri_sift::GeoVwSetSrv::Response &res) 
{ 
	ROS_INFO("SiftAlgNode::get_geo_vw_setCallback: New Request Received!"); 
        
        // checks and get image
        if (not this->alg_.centroids_ready_) {
                ROS_ERROR("iri_sift: Need centroids!");
                return false;
        }
        
        cv_bridge::CvImagePtr cv_ptr;
        try
        {
                cv_ptr = cv_bridge::toCvCopy(req.image, sensor_msgs::image_encodings::RGB8);
        }
        catch (cv_bridge::Exception& e)
        {
                ROS_ERROR("cv_bridge exception: %s", e.what());
                return false;
        }
        
        res.geo_vw_set = this->alg_.get_geovw_from_image(cv_ptr->image);

        return true; 
}

/*  [action callbacks] */

/*  [action requests] */

void SiftAlgNode::node_config_update(Config &config, uint32_t level)
{
  this->alg_.lock();
  
  this->alg_.unlock();
}

void SiftAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<SiftAlgNode>(argc, argv, "sift_alg_node");
}
