#include "moped_actionserver_alg_node.h"

MopedActionserverAlgNode::MopedActionserverAlgNode(void) :
	algorithm_base::IriBaseAlgorithm<MopedActionserverAlgorithm>(),
	moped_aserver_(public_node_handle_, "moped")
{
	//init class attributes if necessary
	this->image_sent = false;

	// [init publishers]
  this->Image_publisher_ = this->public_node_handle_.advertise<sensor_msgs::Image>("/moped/image", 10);
	
	// [init subscribers]
  this->object_poses_subscriber_ = this->public_node_handle_.subscribe("object_poses", 10, &MopedActionserverAlgNode::object_poses_callback, this);
	
	// [init services]
	
	// [init clients]
	
	// [init action servers]
	moped_aserver_.registerStartCallback(boost::bind(&MopedActionserverAlgNode::mopedStartCallback, this, _1)); 
	moped_aserver_.registerStopCallback(boost::bind(&MopedActionserverAlgNode::mopedStopCallback, this)); 
	moped_aserver_.registerIsFinishedCallback(boost::bind(&MopedActionserverAlgNode::mopedIsFinishedCallback, this)); 
	moped_aserver_.registerHasSucceedCallback(boost::bind(&MopedActionserverAlgNode::mopedHasSucceedCallback, this)); 
	moped_aserver_.registerGetResultCallback(boost::bind(&MopedActionserverAlgNode::mopedGetResultCallback, this, _1)); 
	moped_aserver_.registerGetFeedbackCallback(boost::bind(&MopedActionserverAlgNode::mopedGetFeedbackCallback, this, _1)); 
	moped_aserver_.start();
	
	// [init action clients]
}

MopedActionserverAlgNode::~MopedActionserverAlgNode(void)
{
	// [free dynamic memory]
}

void MopedActionserverAlgNode::mainNodeThread(void)
{
	// [fill msg structures]
  //this->Image_msg_.data = my_var;
	
	// [fill srv structure and make request to the server]
	
	// [fill action structure and make request to the action server]

	// [publish messages]
//  this->Image_publisher_.publish(this->Image_msg_);
}

/*	[subscriber callbacks] */
void MopedActionserverAlgNode::object_poses_callback(const pr_msgs::ObjectPoseList::ConstPtr& msg) 
{ 
  ROS_INFO("MopedActionserverAlgNode::object_poses_callback: New Message Received"); 

  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  //this->object_poses_mutex_.enter(); 

	// Check if we were waiting for a result.
	if( not this->image_sent )
	{
		ROS_ERROR("New moped result received but wasn't requested.");
		return;
	}

	this->image_sent = false;
	this->result = (*msg);

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  //this->object_poses_mutex_.exit(); 
}

/*	[service callbacks] */

/*	[action callbacks] */
void MopedActionserverAlgNode::mopedStartCallback(const iri_moped_actionserver::mopedGoalConstPtr& goal)
{ 
	ROS_INFO("MopedActionserverAlgNode::mopedStartCallback got a callback of a goal"); 
	alg_.lock();

	// Check if node is currently processing an image.
	if( this->image_sent )
	{
		ROS_ERROR("Still processing last image.");
		alg_.unlock();
		return;
	}
 
	// Save received image to attribute.
	this->Image_msg_ = goal->image;

	// Publish image to /Image topic.
	this->Image_publisher_.publish(this->Image_msg_);

	// Set control variable to indicate an image has been sent.
	this->image_sent = true;

	//execute goal 
	alg_.unlock(); 
} 

void MopedActionserverAlgNode::mopedStopCallback(void) 
{ 
	alg_.lock(); 

	// Check if was running
	if( this->image_sent == false )
	{
		ROS_ERROR("Received a stop request but Moped wasn't running.");
		alg_.unlock(); 
		return;		
	}

	//stop action
	this->image_sent = false;

	alg_.unlock(); 
} 

bool MopedActionserverAlgNode::mopedIsFinishedCallback(void) 
{ 
	bool ret = false; 

	alg_.lock();

	ret = not this->image_sent;

	alg_.unlock(); 

	return ret; 
} 

bool MopedActionserverAlgNode::mopedHasSucceedCallback(void) 
{ 
	bool ret = false; 

	alg_.lock();

	ret = not this->image_sent;

	alg_.unlock(); 

	return ret; 
} 

void MopedActionserverAlgNode::mopedGetResultCallback(iri_moped_actionserver::mopedResultPtr& result) 
{ 
	alg_.lock(); 

	//update result data to be sent to client 
	result->pose = this->result;

	alg_.unlock(); 
} 

void MopedActionserverAlgNode::mopedGetFeedbackCallback(iri_moped_actionserver::mopedFeedbackPtr& feedback) 
{ 
	alg_.lock(); 
	//keep track of feedback 
	//ROS_INFO("feedback: %s", feedback->data.c_str()); 
	alg_.unlock(); 
}

/*	[action requests] */

void MopedActionserverAlgNode::node_config_update(Config &config, uint32_t level)
{
	this->alg_.lock();

	this->alg_.unlock();
}

void MopedActionserverAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
	return algorithm_base::main<MopedActionserverAlgNode>(argc, argv, "moped_actionserver_alg_node");
}
