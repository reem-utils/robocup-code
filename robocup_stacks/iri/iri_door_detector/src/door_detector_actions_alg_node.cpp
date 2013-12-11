#include "door_detector_actions_alg_node.h"


DoorDetectorActionsAlgNode::DoorDetectorActionsAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<DoorDetectorActionsAlgorithm>(),
  find_a_door_aserver_(public_node_handle_, "find_a_door")
{
  //init class attributes if necessary
  //this->loop_rate_ = 2;//in [Hz]

  // [init publishers]
  this->arm_poses_marker_publisher_ = this->public_node_handle_.advertise<visualization_msgs::Marker>("arm_poses_marker", 1);
  this->door_action_start_publisher_ = this->public_node_handle_.advertise<std_msgs::Int8>("door_action_start", 1);
  
  // [init subscribers]
  this->door_handle_subscriber_ = this->public_node_handle_.subscribe("/iri_door_detector/door_cloud/door_handle", 1, &DoorDetectorActionsAlgNode::door_handle_callback, this);
  this->door_centroid_subscriber_ = this->public_node_handle_.subscribe("/iri_door_detector/door_cloud/door_centroid", 1, &DoorDetectorActionsAlgNode::door_centroid_callback, this);
  
  // [init services]
  
  // [init clients]
  
  // [init action servers]
  find_a_door_aserver_.registerStartCallback(boost::bind(&DoorDetectorActionsAlgNode::find_a_doorStartCallback, this, _1)); 
  find_a_door_aserver_.registerStopCallback(boost::bind(&DoorDetectorActionsAlgNode::find_a_doorStopCallback, this)); 
  find_a_door_aserver_.registerIsFinishedCallback(boost::bind(&DoorDetectorActionsAlgNode::find_a_doorIsFinishedCallback, this)); 
  find_a_door_aserver_.registerHasSucceedCallback(boost::bind(&DoorDetectorActionsAlgNode::find_a_doorHasSucceedCallback, this)); 
  find_a_door_aserver_.registerGetResultCallback(boost::bind(&DoorDetectorActionsAlgNode::find_a_doorGetResultCallback, this, _1)); 
  find_a_door_aserver_.registerGetFeedbackCallback(boost::bind(&DoorDetectorActionsAlgNode::find_a_doorGetFeedbackCallback, this, _1)); 
  find_a_door_aserver_.start();
  
  // [init action clients]

  // [init variables]
  // --- tf_original_frame = "/kinect_depth_optical_frame";
  tf_target_frame = "/base_link";
  tf_target_frame_2 = "/right_hand_base_link";
  current_planner = "ompl_planning/plan_kinematic_path";
  closed_door=0;
  open_door=0;
  start=0;
  side_open=0.0;
  side_closed=0.0;
  voting_rule_approval=3;
}

DoorDetectorActionsAlgNode::~DoorDetectorActionsAlgNode(void)
{
  // [free dynamic memory]
}

void DoorDetectorActionsAlgNode::mainNodeThread(void)
{
  // [fill msg structures]
  //this->Marker_msg_.data = my_var;
  //this->Int8_msg_.data = my_var;
  
  // [fill srv structure and make request to the server]
  
  // [fill action structure and make request to the action server]

  // [publish messages]
}

/*  [subscriber callbacks] */
void DoorDetectorActionsAlgNode::door_handle_callback(const geometry_msgs::PoseStamped::ConstPtr& handle_location) 
{ 
  ROS_INFO("DoorDetectorActionsAlgNode::door_handle_callback: New Message Received"); 

  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->door_handle_mutex_.enter(); 

  bool tf_exists = false;
  bool tf_2_exists = false;

  if((start==1 || no_simulator) && closed_door<voting_rule_approval)
  {
	  closed_door++; 
		ROS_ERROR("closed door counter: %d", closed_door);

	  if(closed_door==voting_rule_approval)
	  {
		  side_closed=handle_location->pose.orientation.w;
		  if (side_closed < 0)
			ROS_ERROR("Result: handle located on the left side, the door is closed!");
		  if (side_closed > 0)
			ROS_ERROR("Result: handle located on the right side, the door is closed!");
		
		  //Re-start counter, or send commands to robot	
		  if(no_simulator)
				closed_door=0;
 
		  if(!no_simulator)
		  {
			  tf_exists = tf_listener.waitForTransform(tf_target_frame, 
				handle_location->header.frame_id, handle_location->header.stamp, ros::Duration(100));
			  tf_2_exists = tf_listener.waitForTransform(tf_target_frame_2, 
				handle_location->header.frame_id, handle_location->header.stamp, ros::Duration(100));

			  if(tf_exists)
			  {
			  	base_door_handle=transformGoalBase(*handle_location, tf_target_frame);

				  if(tf_2_exists)
				  {
					if(side_closed > 0)
					{
						arm_door_handle=transformGoalArm(*handle_location, tf_target_frame_2);
						marker.header.frame_id=tf_target_frame_2;
					}
					if(side_closed < 0)
					{
						arm_door_handle=transformGoalArm(*handle_location, tf_target_frame);
						marker.header.frame_id=tf_target_frame;
					}

					marker.pose.position = arm_door_handle.goal_constraints.position_constraints[0].position;
					marker.pose.orientation = arm_door_handle.goal_constraints.orientation_constraints[0].orientation;
					marker = ArrowMarker(handle_location->header, marker.pose, 1, 1, "arm_poses_marker");
					arm_poses_marker_publisher_.publish(marker);
				  }
		          }
		  }
	  }
  }

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->door_handle_mutex_.exit(); 
}
void DoorDetectorActionsAlgNode::door_centroid_callback(const geometry_msgs::PoseStamped::ConstPtr& door_centroid) 
{ 
  ROS_INFO("DoorDetectorActionsAlgNode::door_centroid_callback: New Message Received"); 

  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->door_centroid_mutex_.enter(); 

  bool tf_exists = false;
  bool tf_2_exists = false;

  if((start==1 || no_simulator) && open_door<voting_rule_approval)
  {
	  open_door++; 
	  ROS_ERROR("open door counter: %d", open_door);

	  if(open_door==voting_rule_approval)
	  {
		  side_open=door_centroid->pose.orientation.w;
		  //Print result
	  	  if (side_open == 0)
			ROS_ERROR("Result: the door is fully open!");
		  if (side_open < 0)
			ROS_ERROR("Result: door ajar on the left side!");
		  if (side_open > 0)
			ROS_ERROR("Result: door ajar on the right side!");

		  //Re-start counter, or send commands to robot
		  if(no_simulator)
				open_door=0;

		  if(!no_simulator)
		  {
		  	  tf_exists = tf_listener.waitForTransform(tf_target_frame, 
				door_centroid->header.frame_id, door_centroid->header.stamp, ros::Duration(100));
		  	  tf_2_exists = tf_listener.waitForTransform(tf_target_frame_2, 
				door_centroid->header.frame_id, door_centroid->header.stamp, ros::Duration(100));

			  if(tf_exists)
			  {
				base_door_centroid=transformGoalBase(*door_centroid, tf_target_frame);
			  
				  if(tf_2_exists)
				  {
					if (side_open > 0)
					{
						arm_door_centroid=liftArm(*door_centroid, tf_target_frame_2);
						marker.header.frame_id=tf_target_frame_2;
					}
					if (side_open < 0)
					{
						arm_door_centroid=liftArm(*door_centroid, tf_target_frame);
						marker.header.frame_id=tf_target_frame;	
					}
					if (side_open != 0)
					{
						marker.pose.position = arm_door_centroid.goal_constraints.position_constraints[0].position;
						marker.pose.orientation = arm_door_centroid.goal_constraints.orientation_constraints[0].orientation;
						marker = ArrowMarker(door_centroid->header, marker.pose, 1, 1, "arm_poses_marker");

						arm_poses_marker_publisher_.publish(marker);
					}
				  }
			  }
		  }
	  }
  }

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->door_centroid_mutex_.exit(); 
}

/*  [service callbacks] */

/*  [action callbacks] */
void DoorDetectorActionsAlgNode::find_a_doorStartCallback(const iri_door_detector::FindADoorGoalConstPtr& goal)
{ 
  alg_.lock(); 
    start=goal->start;
    if (start==1)
    {
    action_start.data=1;
        ROS_ERROR("Goal acknowledged, currently looking for a door!");
    closed_door=0;
    open_door=0;
    this->door_action_start_publisher_.publish(action_start);
    }
  alg_.unlock(); 
} 

void DoorDetectorActionsAlgNode::find_a_doorStopCallback(void) 
{ 
  alg_.lock(); 
    if(open_door==voting_rule_approval || closed_door==voting_rule_approval)
    {
    	start = 0;
	action_start.data=0;
    } 
  alg_.unlock(); 
} 

bool DoorDetectorActionsAlgNode::find_a_doorIsFinishedCallback(void) 
{ 
  bool ret = false; 

  alg_.lock(); 
    if(open_door==voting_rule_approval || closed_door==voting_rule_approval)
    {
    	ret = true;
	start = 0;
	action_start.data=0;
    }
  alg_.unlock(); 

  return ret; 
} 

bool DoorDetectorActionsAlgNode::find_a_doorHasSucceedCallback(void) 
{ 
  bool ret = false; 

  alg_.lock(); 
    if(open_door==voting_rule_approval || closed_door==voting_rule_approval)
    {
    	ret = true;
	start = 0;
	action_start.data=0;
	this->door_action_start_publisher_.publish(action_start);
    }
  alg_.unlock(); 

  return ret; 
} 

void DoorDetectorActionsAlgNode::find_a_doorGetResultCallback(iri_door_detector::FindADoorResultPtr& result) 
{ 
  alg_.lock(); 
    //update result data to be sent to client 
    if(open_door==voting_rule_approval)
    {
    	result->base_poses = base_door_centroid;
	result->arm_poses = arm_door_centroid;
	result->planner_service_name = current_planner;
	if(side_open>0)
		result->state = "open_right"; 
	if(side_open<0)
		result->state = "open_left";
	if(side_open==0)
		result->state = "fully_open";
	start=0;
	action_start.data=0;
    }
    if(closed_door==voting_rule_approval)
    {
    	result->base_poses = base_door_handle;
	result->arm_poses = arm_door_handle;
	result->planner_service_name = current_planner; 
	if(side_closed>0)
		result->state = "closed_right";
	if(side_closed<0)
		result->state = "closed_left";
	start=0;
	action_start.data=0;
    } 
  alg_.unlock(); 
} 

void DoorDetectorActionsAlgNode::find_a_doorGetFeedbackCallback(iri_door_detector::FindADoorFeedbackPtr& feedback) 
{ 
  alg_.lock(); 
    //keep track of feedback 
    //ROS_INFO("feedback: %s", feedback->data.c_str()); 
  alg_.unlock(); 
}

/*  [action requests] */

void DoorDetectorActionsAlgNode::node_config_update(Config &config, uint32_t level)
{
  this->alg_.lock();
	
	this->base_distance_before_closed_door = config.base_distance_before_closed_door;
	this->base_distance_after_open_door = config.base_distance_after_open_door;
	this->arm_distance_before_closed_door = config.arm_distance_before_closed_door;
	this->z_arm_offset = config.z_arm_offset;
	this->y_offset = config.y_offset;
	this->no_simulator = config.no_simulator;

  this->alg_.unlock();
}

void DoorDetectorActionsAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<DoorDetectorActionsAlgNode>(argc, argv, "door_detector_alg_node");
}

/* algorithm functions */
geometry_msgs::PoseStamped DoorDetectorActionsAlgNode::transformGoalBase (geometry_msgs::PoseStamped pose, std::string target_frame)
{	
    ROS_INFO("DoorDetectorActionsAlgNode::transformGoalBase");
	geometry_msgs::PoseStamped target_pose;
	geometry_msgs::PoseStamped p1;
	geometry_msgs::PoseStamped p2;
	geometry_msgs::Quaternion orient;
	float side = pose.pose.orientation.w;
	
	pose.pose.orientation.w=0;	

	if(side==1.0 || side==-1.0)
	{
		//send base 0.5m before the door to avoid collision
		pose.pose.position.x -= (base_distance_before_closed_door * pose.pose.orientation.x);
		pose.pose.position.y -= (base_distance_before_closed_door * pose.pose.orientation.y);
		pose.pose.position.z -= (base_distance_before_closed_door * pose.pose.orientation.z);
	}

	if(side==0.0 || side==-2.0 || side==2.0)
	{
		//if the door is fully open, send base 0.5m beyond the door
		pose.pose.position.x += (base_distance_after_open_door * pose.pose.orientation.x);
		pose.pose.position.y += (base_distance_after_open_door * pose.pose.orientation.y);
		pose.pose.position.z += (base_distance_after_open_door * pose.pose.orientation.z);
	}

	tf_listener.transformPose(target_frame, pose, target_pose);

	//transform orientation vector origin
        tf_listener.transformPose(target_frame, pose, p1); 
	
	//compute orientation vector end
	pose.pose.position.x=pose.pose.position.x+pose.pose.orientation.x;
	pose.pose.position.y=pose.pose.position.y+pose.pose.orientation.y;
	pose.pose.position.z=pose.pose.position.z+pose.pose.orientation.z;

	//transform orientation vector end
	tf_listener.transformPose(target_frame, pose, p2);

	tf::Vector3 initial_position = tf::Vector3(1.0,0.0,0.0);//align to x axis
	tf::Vector3 plane_norm = tf::Vector3(p2.pose.position.x-p1.pose.position.x, 
					     p2.pose.position.y-p1.pose.position.y, 
					     0);
	initial_position = initial_position.normalize();
	plane_norm = plane_norm.normalize();
	float rot_ang = acos(initial_position.dot(plane_norm));
	tf::Vector3 rot_axis = initial_position.cross(plane_norm);
	//orient = tf::createQuaternionMsgFromYaw(rot_ang);
	tf::Quaternion q = tf::Quaternion(rot_axis,rot_ang);
	tf::quaternionTFToMsg (q, orient);

	target_pose.pose.position.z=0;
	if(side_closed == 1.0)
		target_pose.pose.position.y=target_pose.pose.position.y+y_offset+0.2;
	if(side_closed == -1.0)
		target_pose.pose.position.y=target_pose.pose.position.y+y_offset-0.2;
	target_pose.pose.orientation=orient;
	
    ROS_INFO("DoorDetectorActionsAlgNode::transformGoalBase finished");
	return target_pose;
}

arm_navigation_msgs::MotionPlanRequest DoorDetectorActionsAlgNode::transformGoalArm (geometry_msgs::PoseStamped pose, std::string target_frame)
{	

    ROS_INFO("DoorDetectorActionsAlgNode::transformGoalArm");
	geometry_msgs::PoseStamped target_pose;
	geometry_msgs::PoseStamped p1;
	geometry_msgs::PoseStamped p2;
	geometry_msgs::Quaternion orient;
	std::string group_name;
	std::string link_name;
	tf::Vector3 plane_norm;
	tf::Vector3 initial_position;
	float side = pose.pose.orientation.w;

	//send arm 0.1m before the door to avoid collision
	pose.pose.position.x -= (arm_distance_before_closed_door * pose.pose.orientation.x);
	pose.pose.position.y -= (arm_distance_before_closed_door * pose.pose.orientation.y);
	pose.pose.position.z -= (arm_distance_before_closed_door * pose.pose.orientation.z);

	
	
	pose.pose.orientation.w=0;	

	tf_listener.transformPose(target_frame, pose, target_pose);

	//transform orientation vector origin
        tf_listener.transformPose(target_frame, pose, p1); 

	//compute orientation vector end
	pose.pose.position.x=pose.pose.position.x+pose.pose.orientation.x;
	pose.pose.position.y=pose.pose.position.y+pose.pose.orientation.y;
	pose.pose.position.z=pose.pose.position.z+pose.pose.orientation.z;

	//transform orientation vector end
	tf_listener.transformPose(target_frame, pose, p2);

	if (side > 0)
	{
		initial_position = tf::Vector3(0.2,0.0,1.0);
		initial_position = initial_position.normalize();
		//target_pose.pose.position.x=target_pose.pose.position.x-0.37;
		//target_pose.pose.position.y=target_pose.pose.position.y+0.1;
		//target_pose.pose.position.z=target_pose.pose.position.z+0.15;
		group_name = "right_arm_torso";
		link_name = "arm_right_7_link";
		plane_norm = tf::Vector3(p2.pose.position.x-p1.pose.position.x, 
					 p2.pose.position.y-p1.pose.position.y, 
					 p2.pose.position.z-p1.pose.position.z);
		plane_norm = plane_norm.normalize();
	}

	if (side < 0)
	{
		initial_position = tf::Vector3(-0.2,0.0,1.0);
		initial_position = initial_position.normalize();
		//target_pose.pose.position.x=target_pose.pose.position.x+0.37;
		//target_pose.pose.position.y=target_pose.pose.position.y-0.1;
		//target_pose.pose.position.z=target_pose.pose.position.z+0.15;
		group_name = "left_arm";
		link_name = "arm_left_7_link";
		plane_norm = tf::Vector3(-p2.pose.position.x+p1.pose.position.x, 
					 -p2.pose.position.y+p1.pose.position.y, 
					 -p2.pose.position.z+p1.pose.position.z);
		plane_norm = plane_norm.normalize();
	}

	float rot_ang = acos(initial_position.dot(plane_norm));
	tf::Vector3 rot_axis = initial_position.cross(plane_norm);	
	tf::Quaternion q = tf::Quaternion(rot_axis,rot_ang);
	tf::quaternionTFToMsg (q, orient);


	target_pose.pose.orientation=orient;
	target_pose.pose.position.z=target_pose.pose.position.z+z_arm_offset;
	target_pose.pose.position.y=target_pose.pose.position.y+y_offset;

	arm_navigation_msgs::MotionPlanRequest motion_plan_request;

	motion_plan_request.group_name = group_name;
	motion_plan_request.num_planning_attempts = 10;
	motion_plan_request.planner_id = std::string("");
	motion_plan_request.allowed_planning_time = ros::Duration(10.0);
	//goalA.motion_plan_request.expected_path_dt = ros::Duration(3.0);

	motion_plan_request.goal_constraints.position_constraints.resize(1);
	motion_plan_request.goal_constraints.position_constraints[0].header.frame_id = target_frame;
	motion_plan_request.goal_constraints.position_constraints[0].link_name = link_name;
	motion_plan_request.goal_constraints.position_constraints[0].position=target_pose.pose.position;

	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.type = arm_navigation_msgs::Shape::BOX;
  	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions.push_back(0.1);
  	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions.push_back(0.1);
 	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions.push_back(0.1);
	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_orientation.x = 0.0;
	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_orientation.y = 0.0;
	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_orientation.z = 0.0;
	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_orientation.w = 1.0;
 	motion_plan_request.goal_constraints.position_constraints[0].weight = 1.0; 

	motion_plan_request.goal_constraints.orientation_constraints.resize(1);
	motion_plan_request.goal_constraints.orientation_constraints[0].header.frame_id = target_frame;
	motion_plan_request.goal_constraints.orientation_constraints[0].link_name = link_name;
	motion_plan_request.goal_constraints.orientation_constraints[0].orientation=target_pose.pose.orientation;

	motion_plan_request.goal_constraints.orientation_constraints[0].absolute_roll_tolerance = 2.0;
	motion_plan_request.goal_constraints.orientation_constraints[0].absolute_pitch_tolerance = 2.0;
	motion_plan_request.goal_constraints.orientation_constraints[0].absolute_yaw_tolerance = 2.0;

	motion_plan_request.goal_constraints.position_constraints[0].position.z=target_pose.pose.position.z + 0.05;

    ROS_INFO("DoorDetectorActionsAlgNode::transformGoalArm finished");

	return motion_plan_request;
}

arm_navigation_msgs::MotionPlanRequest DoorDetectorActionsAlgNode::liftArm (geometry_msgs::PoseStamped pose, std::string target_frame)
{	

    ROS_INFO("DoorDetectorActionsAlgNode::liftArm");
	geometry_msgs::PoseStamped target_pose;
	geometry_msgs::PoseStamped p1;
	geometry_msgs::PoseStamped p2;
	geometry_msgs::Quaternion orient;
	std::string group_name;
	std::string link_name;
	tf::Vector3 plane_norm;
	tf::Vector3 initial_position;
	float side = pose.pose.orientation.w;

	arm_navigation_msgs::MotionPlanRequest motion_plan_request;
	motion_plan_request.goal_constraints.position_constraints.resize(1);
	motion_plan_request.goal_constraints.orientation_constraints.resize(1);
	
	if (side > 0)
	{
		group_name = "right_arm_torso";
		link_name = "arm_right_7_link";	
		motion_plan_request.goal_constraints.position_constraints[0].position.x=-0.3;
		motion_plan_request.goal_constraints.position_constraints[0].position.y=0.191835;
		motion_plan_request.goal_constraints.position_constraints[0].position.z=1.094355;

		motion_plan_request.goal_constraints.orientation_constraints[0].orientation.x=-0.436727;
		motion_plan_request.goal_constraints.orientation_constraints[0].orientation.y=-0.526269;
		motion_plan_request.goal_constraints.orientation_constraints[0].orientation.z=0.377467;
		motion_plan_request.goal_constraints.orientation_constraints[0].orientation.w=0.624364;
	}

	if (side < 0)
	{
		group_name = "left_arm";
		link_name = "arm_left_7_link";
		motion_plan_request.goal_constraints.position_constraints[0].position.x=0.318141;
		motion_plan_request.goal_constraints.position_constraints[0].position.y=0.313599;
		motion_plan_request.goal_constraints.position_constraints[0].position.z=1.205298;

		motion_plan_request.goal_constraints.orientation_constraints[0].orientation.x=-0.264641;
		motion_plan_request.goal_constraints.orientation_constraints[0].orientation.y=-0.714832;
		motion_plan_request.goal_constraints.orientation_constraints[0].orientation.z=0.057748;
		motion_plan_request.goal_constraints.orientation_constraints[0].orientation.w=0.644705;
	}

	motion_plan_request.group_name = group_name;
	motion_plan_request.num_planning_attempts = 10;
	motion_plan_request.planner_id = std::string("");
	motion_plan_request.allowed_planning_time = ros::Duration(10.0);
	//goalA.motion_plan_request.expected_path_dt = ros::Duration(3.0);

	motion_plan_request.goal_constraints.position_constraints[0].header.frame_id = target_frame;
	motion_plan_request.goal_constraints.position_constraints[0].link_name = link_name;

	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.type = arm_navigation_msgs::Shape::BOX;
  	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions.push_back(0.1);
  	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions.push_back(0.1);
 	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_shape.dimensions.push_back(0.1);
	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_orientation.x = 0.0;
	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_orientation.y = 0.0;
	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_orientation.z = 0.0;
	motion_plan_request.goal_constraints.position_constraints[0].constraint_region_orientation.w = 1.0;
 	motion_plan_request.goal_constraints.position_constraints[0].weight = 1.0; 

	motion_plan_request.goal_constraints.orientation_constraints[0].header.frame_id = target_frame;
	motion_plan_request.goal_constraints.orientation_constraints[0].link_name = link_name;

	motion_plan_request.goal_constraints.orientation_constraints[0].absolute_roll_tolerance = 2.0;
	motion_plan_request.goal_constraints.orientation_constraints[0].absolute_pitch_tolerance = 2.0;
	motion_plan_request.goal_constraints.orientation_constraints[0].absolute_yaw_tolerance = 2.0;

    ROS_INFO("DoorDetectorActionsAlgNode::liftArm finished");

	return motion_plan_request;
}

visualization_msgs::Marker DoorDetectorActionsAlgNode::ArrowMarker(std_msgs::Header header, geometry_msgs::Pose pose, int alpha, int color,  const char arrow_tag[])
{	

	marker.header.stamp = header.stamp;
	marker.ns = arrow_tag;
	marker.id = 0;
	marker.type = visualization_msgs::Marker::ARROW;
	marker.action = visualization_msgs::Marker::ADD;
	marker.pose = pose;

	// scale
	marker.scale.x = 0.7;
	marker.scale.y = 0.7;
	marker.scale.z = 0.7;

	// color
	marker.color.a = alpha;
	marker.color.r = 0.0;
	marker.color.g = 0.0;
	marker.color.b = 0.0;

	if(color==1)
		marker.color.r = 1.0;
	if(color==2)
 		marker.color.g = 1.0;
	if(color==3)
		marker.color.b = 1.0;

	return marker;
}
