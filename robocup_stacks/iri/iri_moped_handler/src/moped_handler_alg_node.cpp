#include "moped_handler_alg_node.h"

MopedHandlerAlgNode::MopedHandlerAlgNode(void) :
	algorithm_base::IriBaseAlgorithm<MopedHandlerAlgorithm>(),
	moped_client_("moped", true)
{
	//init class attributes if necessary
	this->working = false;

	//ROS_INFO("MopedHandlerAlgNode [init publishers]"); 
	// [init publishers]
	this->outputOPL_publisher_ = this->public_node_handle_.advertise<pr_msgs::ObjectPoseList>("outputOPL", 10);
	
	//ROS_INFO("MopedHandlerAlgNode [init subscribers]"); 
	// [init subscribers]
	this->subImage_.subscribe(this->public_node_handle_, "/camera/rgb/image_mono", 1);
	this->subPointCloud_.subscribe(this->public_node_handle_, "/camera/depth_registered/points", 1);

	typedef message_filters::sync_policies::ApproximateTime<sensor_msgs::Image, sensor_msgs::PointCloud2> MySyncPolicy;
	this->sync_ = new message_filters::Synchronizer<MySyncPolicy>(MySyncPolicy(10), subImage_, subPointCloud_);
	//ROS_INFO("MopedHandlerAlgNode [attaching callback]"); 
	sync_->registerCallback(boost::bind(&MopedHandlerAlgNode::callback, this, _1, _2));

	//ROS_INFO("MopedHandlerAlgNode [init services]"); 
	// [init services]
  this->enable_server_ = this->public_node_handle_.advertiseService("enable", &MopedHandlerAlgNode::enableCallback, this);

  	ROS_INFO("MopedHandlerAlgNode Initiated."); 
	
	// [init clients]
	
	// [init action servers]
	
	// [init action clients]
}

MopedHandlerAlgNode::~MopedHandlerAlgNode(void)
{
	// [free dynamic memory]
}

void MopedHandlerAlgNode::mainNodeThread(void)
{
	// [fill msg structures]
  //this->ObjectPoseList_msg_.data = my_var;
	
	// [fill srv structure and make request to the server]
	
	// [fill action structure and make request to the action server]
//	mopedMakeActionRequest(); // Not used here, first we have to receive image data from camera.

	// [publish messages]
//  this->outputOPL_publisher_.publish(this->ObjectPoseList_msg_);
}

/*	[subscriber callbacks] */

/*	[service callbacks] */
bool MopedHandlerAlgNode::enableCallback(iri_moped_handler::enable::Request &req, iri_moped_handler::enable::Response &res) 
{ 
	ROS_INFO("MopedHandlerAlgNode::enableCallback: New Request Received!"); 

	if(req.enable)
	{
		this->subImage_.subscribe(this->public_node_handle_, "/camera/rgb/image_mono", 1);
		this->subPointCloud_.subscribe(this->public_node_handle_, "/camera/depth_registered/points", 1);
		ROS_INFO("MopedHandlerAlgNode::enableCallback: subscribed to topics [/camera/rgb/image_mono /camera/depth_registered/points]!"); 

		typedef message_filters::sync_policies::ApproximateTime<sensor_msgs::Image, sensor_msgs::PointCloud2> MySyncPolicy;
		this->sync_ = new message_filters::Synchronizer<MySyncPolicy>(MySyncPolicy(10), subImage_, subPointCloud_);
		sync_->registerCallback(boost::bind(&MopedHandlerAlgNode::callback, this, _1, _2));
	}
	else
	{
		this->subImage_.subscribe(this->public_node_handle_, "falseTopic", 1);
		this->subPointCloud_.subscribe(this->public_node_handle_, "falseTopic2", 1);
		ROS_INFO("MopedHandlerAlgNode::enableCallback: UNsubscribed from topics [/camera/rgb/image_mono /camera/depth_registered/points]!"); 
	}

	//use appropiate mutex to shared variables if necessary 
	//this->alg_.lock(); 
	//this->enable_mutex_.enter(); 

	//if(this->alg_.isRunning()) 
	//{ 
	//ROS_INFO("MopedHandlerAlgNode::enableCallback: Processin New Request!"); 
	//do operations with req and output on res 
	//res.data2 = req.data1 + my_var; 
	//} 
	//else 
	//{ 
	//ROS_INFO("MopedHandlerAlgNode::enableCallback: ERROR: alg is not on run mode yet."); 
	//} 

	//unlock previously blocked shared variables 
	//this->alg_.unlock(); 
	//this->enable_mutex_.exit(); 

	return true; 
}

/*	[action callbacks] */
void MopedHandlerAlgNode::mopedDone(const actionlib::SimpleClientGoalState& state,	const iri_moped_actionserver::mopedResultConstPtr& result) 
{ 
	if( state.toString().compare("SUCCEEDED") == 0 ) 
		ROS_INFO("MopedHandlerAlgNode::mopedDone: Goal Achieved!"); 
	else 
	{
		ROS_INFO("MopedHandlerAlgNode::mopedDone: %s", state.toString().c_str()); 
		return;
	}

	// Convert the sensor_msgs/PointCloud2 data to pcl/PointCloud
	pcl::fromROSMsg(this->inputPointCloud, this->pcl_);

	// Create result message.
	pr_msgs::ObjectPoseList outputMsg = result->pose;
    outputMsg.header.frame_id = "/base_link";



	// Delete bad objects from result message
	vector<pr_msgs::ObjectPose> objects = outputMsg.object_list;
    ROS_INFO("Got %i objects.", objects.size());
	vector<int> bad; // Indices containing bad objects.
	for(size_t i=0; i<objects.size(); ++i)
	{
		float col = objects[i].pose2D.x;
		float row = objects[i].pose2D.y;

		// Check bounds
        if( col < 0 or col >= 640 or row < 0 or row >= 480 ){
            ROS_INFO("Object %d has col=%f row=%f, will be discarted", i, col, row);
			bad.push_back(i);
        }
	}

	// Delete objects in inverse order.
	for(int i=bad.size()-1; i>=0; --i)
		outputMsg.object_list.erase( outputMsg.object_list.begin() + bad[i] );

    ROS_INFO("From them, %i are good objects.", outputMsg.object_list.size());

	bad.clear();
	// For every good object detected...
	for(size_t i=0; i < outputMsg.object_list.size(); ++i)
	{
        ROS_INFO("Object num %i:", i);
		// Get 2D position
		float col = outputMsg.object_list[i].pose2D.x;
		float row = outputMsg.object_list[i].pose2D.y;

		// Get 3D position according to pcl.
		pcl::PointXYZ p = this->pcl_.at(col, row);

		// Check p correctness.
		// TODO: Complete.
		if(isnan(p.x) || isnan(p.y) || isnan(p.z)){
            ROS_INFO("Found NaN values!!");
            ROS_INFO("Aborting this object: %s", outputMsg.object_list[i].name.c_str()); //seg fault here i dont know why it happens
			bad.push_back(i);
		}
		else {
			// Set 3D position to output message.
			outputMsg.object_list[i].pose.position.x = p.x;
			outputMsg.object_list[i].pose.position.y = p.y;
			outputMsg.object_list[i].pose.position.z = p.z;

			// Feedback TODO: Comment.
            if(outputMsg.object_list[i].name != ""){
                ROS_INFO("Pixel (%f, %f) is at position (%f, %f, %f) for object found \"%s\".", col, row, p.x, p.y, p.z, outputMsg.object_list[i].name.c_str());
            }
            else
                ROS_INFO("Pixel (%f, %f) is at position (%f, %f, %f)", col, row, p.x, p.y, p.z);
		}
	}

	// Delete objects which had NaN position in inverse order.
	for(int i=bad.size()-1; i>=0; --i)
		outputMsg.object_list.erase( outputMsg.object_list.begin() + bad[i] );

	// Publish data to output topic
	this->outputOPL_publisher_.publish(outputMsg);

	ROS_INFO("Sent final result to topic");

	this->working = false;
} 

void MopedHandlerAlgNode::mopedActive() 
{ 
	//ROS_INFO("MopedHandlerAlgNode::mopedActive: Goal just went active!"); 
} 

void MopedHandlerAlgNode::mopedFeedback(const iri_moped_actionserver::mopedFeedbackConstPtr& feedback) 
{ 
	//ROS_INFO("MopedHandlerAlgNode::mopedFeedback: Got Feedback!"); 

	bool feedback_is_ok = true; 

	//analyze feedback 
	//my_var = feedback->var; 

	//if feedback is not what expected, cancel requested goal 
	if( !feedback_is_ok ) 
	{ 
		moped_client_.cancelGoal(); 
		//ROS_INFO("MopedHandlerAlgNode::mopedFeedback: Cancelling Action!"); 
	} 
}

/*	[action requests] */
void MopedHandlerAlgNode::mopedMakeActionRequest() 
{ 
	ROS_INFO("MopedHandlerAlgNode::mopedMakeActionRequest: Starting New Request!"); 

	//wait for the action server to start 
	//will wait for infinite time 
	moped_client_.waitForServer();	
	ROS_INFO("MopedHandlerAlgNode::mopedMakeActionRequest: Server is Available!"); 

	//send a goal to the action 
	moped_goal_.image = this->inputImage; 
	moped_client_.sendGoal(moped_goal_, 
							boost::bind(&MopedHandlerAlgNode::mopedDone,		 this, _1, _2), 
							boost::bind(&MopedHandlerAlgNode::mopedActive,	 this), 
							boost::bind(&MopedHandlerAlgNode::mopedFeedback, this, _1)); 
	ROS_INFO("MopedHandlerAlgNode::mopedMakeActionRequest: Goal Sent. Wait for Result!"); 
}

void MopedHandlerAlgNode::node_config_update(Config &config, uint32_t level)
{
	this->alg_.lock();

	this->alg_.unlock();
}

void MopedHandlerAlgNode::callback(const ImageConstPtr& image, const PointCloud2ConstPtr& pcl)
{
	//ROS_INFO("MopedHandlerAlgNode::callback received!");
	if( this->working )
		return;
	else
		this->working = true;

	ROS_INFO("Received image and PCL with the same timestamp!");

	// Save image and PCL to attributes in order to work with them later.
	this->inputImage = *image;
	this->inputPointCloud = *pcl;

	// Send Image to Moped to process it and get the result.
	mopedMakeActionRequest();
}

void MopedHandlerAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
	return algorithm_base::main<MopedHandlerAlgNode>(argc, argv, "moped_handler_alg_node");
}
