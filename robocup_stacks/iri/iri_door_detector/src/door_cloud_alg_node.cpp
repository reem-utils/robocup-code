#include "door_cloud_alg_node.h"

DoorCloudAlgNode::DoorCloudAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<DoorCloudAlgorithm>()
{
  //init class attributes if necessary
  //this->loop_rate_ = 2;//in [Hz]

  // [init publishers]
  this->open_door_cloud_publisher_ = this->public_node_handle_.advertise<sensor_msgs::PointCloud2>("open_door_cloud", 1);
  this->open_door_marker_publisher_ = this->public_node_handle_.advertise<visualization_msgs::Marker>("open_door_marker", 1);
  this->door_centroid_publisher_ = this->public_node_handle_.advertise<geometry_msgs::PoseStamped>("door_centroid", 1);

  this->closed_door_cloud_publisher_ = this->public_node_handle_.advertise<sensor_msgs::PointCloud2>("closed_door_cloud", 1);
  this->closed_door_marker_publisher_ = this->public_node_handle_.advertise<visualization_msgs::Marker>("closed_door_marker", 1, true);
  this->door_handle_publisher_ = this->public_node_handle_.advertise<geometry_msgs::PoseStamped>("door_handle", 1);
  
  // [init subscribers]
  if (!no_simulator)
  	this->door_action_start_subscriber_ = this->public_node_handle_.subscribe("/iri_door_detector/door_detector_actions/door_action_start", 1, &DoorCloudAlgNode::door_action_start_callback, this);

  if (no_simulator)
  {
	this->points_subscriber_ = this->public_node_handle_.subscribe("/camera/depth/points", 1, &DoorCloudAlgNode::points_callback, this);
	this->door_centroid_subscriber_ = this->public_node_handle_.subscribe("/iri_door_detector/open_door_detector/door_centroid", 1, &DoorCloudAlgNode::door_centroid_callback, this);
  	this->handle_location_subscriber_ = this->public_node_handle_.subscribe("/iri_door_detector/closed_door_detector/door_handle", 1, &DoorCloudAlgNode::handle_location_callback, this);
  }
  
  // [init services]
  
  // [init clients]
  
  // [init action servers]
  
  // [init action clients]

  // [init variables]
  captured_open = 0;
  captured_closed = 0;
  start = 0;
  tf_original_frame = "/kinect_depth_optical_frame";
}

DoorCloudAlgNode::~DoorCloudAlgNode(void)
{
  // [free dynamic memory]
}

void DoorCloudAlgNode::mainNodeThread(void)
{
  // [fill msg structures]
  //this->PointCloud2_msg_.data = my_var;
  //this->Marker_msg_.data = my_var;
  //this->PoseStamped_msg_.data = my_var;
  
  // [fill srv structure and make request to the server]
  
  // [fill action structure and make request to the action server]

  // [publish messages]
  //this->open_door_cloud_publisher_.publish(this->PointCloud2_msg_);
  //this->open_door_marker_publisher_.publish(this->Marker_msg_);
  //this->door_centroid_publisher_.publish(this->PoseStamped_msg_);
}

/*  [subscriber callbacks] */
void DoorCloudAlgNode::door_action_start_callback(const std_msgs::Int8::ConstPtr& action_start) 
{ 
  //ROS_INFO("DoorCloudAlgNode::door_action_start_callback: New Message Received"); 

  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->door_action_start_mutex_.enter(); 

  start=action_start->data;
  
  if (start==0)
  {
  	points_subscriber_.shutdown();
	door_centroid_subscriber_.shutdown();
	handle_location_subscriber_.shutdown();
  }
  if (start==1)
  {
	this->points_subscriber_ = this->public_node_handle_.subscribe("/camera/depth/points", 1, &DoorCloudAlgNode::points_callback, this);
	this->door_centroid_subscriber_ = this->public_node_handle_.subscribe("/iri_door_detector/open_door_detector/door_centroid", 1, &DoorCloudAlgNode::door_centroid_callback, this);
  	this->handle_location_subscriber_ = this->public_node_handle_.subscribe("/iri_door_detector/closed_door_detector/door_handle", 1, &DoorCloudAlgNode::handle_location_callback, this);
  }

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->door_action_start_mutex_.exit(); 
}
void DoorCloudAlgNode::door_centroid_callback(const geometry_msgs::PoseStamped::ConstPtr& door_centroid) 
{ 
  //use appropiate mutex to shared variables if necessary   
  //this->alg_.lock(); 
  this->door_centroid_mutex_.enter(); 

  if (captured_open==0)
  {
  	y_open=door_centroid->pose.position.y;
  	z_open=door_centroid->pose.position.z;
  	w_open=door_centroid->pose.orientation.w;

	x_left = door_centroid->pose.position.x;
	x_right = door_centroid->pose.orientation.x;
	y_top = door_centroid->pose.orientation.y;

	x_open=(x_left+x_right)/2;

	//ROS_INFO("DoorCloudAlgNode::door_centroid_callback: New Message Received"); 
	captured_open=1;
  }

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->door_centroid_mutex_.exit(); 
}
void DoorCloudAlgNode::handle_location_callback(const geometry_msgs::PoseStamped::ConstPtr& handle_location) 
{ 
  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->handle_location_mutex_.enter(); 
  
  //ROS_INFO("DoorCloudAlgNode::handle_location_callback: New Message Received"); 

  if (captured_closed==0)
  {

	x_closed=handle_location->pose.position.x;
  	y_closed=handle_location->pose.position.y;
 	z_closed=handle_location->pose.position.z;
  	w_closed=handle_location->pose.orientation.w;

	captured_closed=1;
  }

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->handle_location_mutex_.exit(); 
}

void DoorCloudAlgNode::points_callback(const sensor_msgs::PointCloud2::ConstPtr& input_cloud) 
{ 
  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->points_mutex_.enter(); 

  if(captured_open==1 || captured_closed==1)
  {
	  //ROS_INFO("DoorCloudAlgNode::points_callback: New Message Received"); 
	  pcl::fromROSMsg (*input_cloud,cloud);
 	  pcl::ModelCoefficients::Ptr cloud_coeffs (new pcl::ModelCoefficients ());
	  pcl::PointIndices::Ptr cloud_inliers (new pcl::PointIndices);

	  pcl::VoxelGrid<pcl::PointXYZ> sor;
	  sor.setInputCloud (cloud.makeShared());
	  sor.setLeafSize (0.01f, 0.01f, 0.01f);
	  sor.filter (cloud);
  
	  if(captured_open==1)
	  {
		//---OPEN DOOR STAGE
		
		cloud_filtered.clear();
		cloud_filtered_left.clear();
		cloud_filtered_right.clear();
		cloud_filtered_top.clear();

		cloud_filtered.header=cloud.header;

		//ROS_ERROR("%f, %f, %f, %f", y_open, z_open, x_left, x_right);

		//Bounding volume where a door may exist
		//lower_x and upper_x defined in open door callback
		lower_x = x_left-0.3;
		upper_x = x_left;
		lower_y = y_open-5.0;
		upper_y = y_open;
		lower_z = z_open-0.25;
		upper_z = z_open+0.25;

		//Filter cloud by bounding volume: x, y, z
		cloud_filtered_left=filterCloud(cloud, lower_x, upper_x, lower_y, upper_y, lower_z, upper_z, false);
		cloud_filtered_left.header=cloud.header;
		cloud_filtered+=cloud_filtered_left;

		//Bounding volume where a door may exist
		lower_x = x_right;
		upper_x = x_right+0.3;

		//Filter cloud by bounding volume: x, y, z
		cloud_filtered_right=filterCloud(cloud, lower_x, upper_x, lower_y, upper_y, lower_z, upper_z, false);
		cloud_filtered_right.header=cloud.header;
		cloud_filtered+=cloud_filtered_right;

		//Bounding volume where a door may exist
		lower_x = x_left-0.3;
		upper_x = x_right+0.3;
		lower_y = y_open-5.0;
		upper_y = y_top;

		//Filter cloud by bounding volume: x, y, z
		cloud_filtered_top=filterCloud(cloud, lower_x, upper_x, lower_y, upper_y, lower_z, upper_z, false);
		cloud_filtered_top.header.frame_id=input_cloud->header.frame_id;
		//cloud_filtered+=cloud_filtered_top;

		//Fit cloud to plane and get properties
		door_plane = planeFit(cloud_filtered);

		cloud_plane= boost::tuples::get<0>(door_plane);
		cloud_inliers= boost::tuples::get<1>(door_plane);
		cloud_coeffs= boost::tuples::get<2>(door_plane);

		if (cloud_inliers->indices.size () == 0)
		{
			ROS_WARN("Open Door Detector: Could not compute plane! maybe there are too few points");
		}
	
		//prepare data for advertising
		if (cloud_inliers->indices.size () > 0)
		{
			//Adjust vector to point forward 
			if(cloud_coeffs->values[2]<0)
			{
				cloud_coeffs->values[0]= -cloud_coeffs->values[0];	
				cloud_coeffs->values[1]= -cloud_coeffs->values[1];
				cloud_coeffs->values[2]= -cloud_coeffs->values[2];
				cloud_coeffs->values[3]= -cloud_coeffs->values[3];
			}

		
			//ROS_ERROR("%s, %f", input_cloud->header.frame_id, input_cloud->header.stamp);

			poses.header.frame_id=input_cloud->header.frame_id;
			poses.header.stamp=input_cloud->header.stamp;

			poses.pose.position.x = x_open;
			poses.pose.position.y = y_open;
			poses.pose.position.z = z_open;//-(x_open*cloud_coeffs->values[0]+y_open*cloud_coeffs->values[1]+cloud_coeffs->values[3])/cloud_coeffs->values[2];

			poses.pose.orientation.x = cloud_coeffs->values[0];
			poses.pose.orientation.y = cloud_coeffs->values[1];
			poses.pose.orientation.z = cloud_coeffs->values[2];
			poses.pose.orientation.w = w_open;
			
			door_centroid_publisher_.publish(poses);

			tf::Vector3 initial_position = tf::Vector3(1.0,0.0,0.0);//align to z axis
			tf::Vector3 plane_norm = tf::Vector3(poses.pose.orientation.x, 
							     poses.pose.orientation.y, 
							     poses.pose.orientation.z);

			orient=quaternionFromVectors(initial_position, plane_norm);
			poses.pose.orientation=orient;

			pcl::toROSMsg(cloud_plane, open_door_cloud);
			open_door_cloud.header.frame_id=input_cloud->header.frame_id;
			open_door_cloud.header.stamp=input_cloud->header.stamp;
			open_door_cloud_publisher_.publish(open_door_cloud);

			cloud_plane.points.clear();
			cloud_plane.width=1;
			cloud_plane.height=1;
			cloud_plane.points.resize (1);
			pcl::toROSMsg(cloud_plane, closed_door_cloud);
			closed_door_cloud.header=input_cloud->header;
			closed_door_cloud_publisher_.publish(closed_door_cloud);

 			marker = ArrowMarker(input_cloud->header, poses.pose, 1, 2, "door_centroid_vector");
			open_door_marker_publisher_.publish(marker);

			marker.ns = "door_handle_vector";
			marker.color.a = 0.0;
			closed_door_marker_publisher_.publish(marker);
		}
	  }

	  if(captured_closed==1)
	  {
		//---CLOSED DOOR STAGE

		//Bounding volume where a door may exist
		lower_x = x_closed-0.4;		
		upper_x = x_closed+0.4;
		lower_y = y_closed-5.0;		
		upper_y = y_closed;
		lower_z = z_closed-0.3;
		upper_z = z_closed+0.3;
		
		if(w_closed==-1)
		{
			lower_x = x_closed-0.1;		
			upper_x = x_closed+0.6;
		}
		if(w_closed==1)
		{
			lower_x = x_closed-0.6;
			upper_x = x_closed+0.1;
		}

		//Filter cloud by bounding volume: x, y, z
		cloud_filtered=filterCloud(cloud, lower_x, upper_x, lower_y, upper_y, lower_z, upper_z, false);

		//Fit cloud to plane and get propertiers
		door_plane = planeFit(cloud_filtered);
		cloud_plane= boost::tuples::get<0>(door_plane);
		cloud_inliers= boost::tuples::get<1>(door_plane);
		cloud_coeffs= boost::tuples::get<2>(door_plane);

		if (cloud_inliers->indices.size () == 0)
		{
			ROS_WARN("Closed Door Detector: Could not compute plane! maybe there are too few points");
		
		}

		//prepare data for advertising
		if (cloud_inliers->indices.size () > 0)
		{

			if(cloud_coeffs->values[2]<0)
			{
				cloud_coeffs->values[3]=cloud_coeffs->values[3]-0.04;
			}
			if(cloud_coeffs->values[2]>0)
			{
				cloud_coeffs->values[3]=cloud_coeffs->values[3]+0.04;
			}
			

			//Adjust vector to point forward
			if(cloud_coeffs->values[2]<0)
			{
				cloud_coeffs->values[0]= -cloud_coeffs->values[0];	
				cloud_coeffs->values[1]= -cloud_coeffs->values[1];
				cloud_coeffs->values[2]= -cloud_coeffs->values[2];
				cloud_coeffs->values[3]= -cloud_coeffs->values[3];
			}

			//ROS_ERROR("%s, %f", input_cloud->header.frame_id, input_cloud->header.stamp);

			poses.header.frame_id=input_cloud->header.frame_id;
			poses.header.stamp=input_cloud->header.stamp;

			poses.pose.position.x = x_closed;
			poses.pose.position.y = y_closed;
			poses.pose.position.z = z_closed;//-(x_closed*cloud_coeffs->values[0]+y_closed*cloud_coeffs->values[1]+cloud_coeffs->values[3])/cloud_coeffs->values[2];

			poses.pose.orientation.x=cloud_coeffs->values[0];
			poses.pose.orientation.y=cloud_coeffs->values[1];
			poses.pose.orientation.z=cloud_coeffs->values[2];
			poses.pose.orientation.w = w_closed;

			door_handle_publisher_.publish(poses);

			tf::Vector3 initial_position = tf::Vector3(-1.0,0.0,0.0);//align to z axis
			tf::Vector3 plane_norm = tf::Vector3(poses.pose.orientation.x, 
							     poses.pose.orientation.y, 
							     poses.pose.orientation.z);

			orient=quaternionFromVectors(initial_position, plane_norm);
			poses.pose.orientation=orient;

			pcl::toROSMsg(cloud_plane, closed_door_cloud);
			closed_door_cloud.header.frame_id=input_cloud->header.frame_id;
			closed_door_cloud.header.stamp=input_cloud->header.stamp;

			closed_door_cloud_publisher_.publish(closed_door_cloud);

			cloud_plane.points.clear();
			cloud_plane.width=1;
			cloud_plane.height=1;
			cloud_plane.points.resize (1);
			pcl::toROSMsg(cloud_plane, open_door_cloud);
			open_door_cloud.header=input_cloud->header;
			open_door_cloud_publisher_.publish(open_door_cloud);

			marker = ArrowMarker(input_cloud->header, poses.pose, 1, 2, "door_handle_vector");
			closed_door_marker_publisher_.publish(marker);
		
			marker.ns = "door_centroid_vector";
			marker.color.a = 0.0;
			open_door_marker_publisher_.publish(marker);
		}
	  }

  	  captured_open=0;
  	  captured_closed=0;
  } 

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->points_mutex_.exit(); 
}

/*  [service callbacks] */

/*  [action callbacks] */

/*  [action requests] */

void DoorCloudAlgNode::node_config_update(Config &config, uint32_t level)
{
  this->alg_.lock();

	this->no_simulator = config.no_simulator;

  this->alg_.unlock();
}

void DoorCloudAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<DoorCloudAlgNode>(argc, argv, "door_cloud_alg_node");
}

/* algorithm functions */
pcl::PointCloud<pcl::PointXYZ> DoorCloudAlgNode::filterCloud (pcl::PointCloud<pcl::PointXYZ> raw_cloud, float Lowx, float Uppx, float Lowy, float Uppy, float Lowz, float Uppz, bool negative_limits)
{	
	//Filter points to door location
	pcl::PointCloud<pcl::PointXYZ> cloud_filtered_x;
	pcl::PointCloud<pcl::PointXYZ> cloud_filtered_z;
	pcl::PointCloud<pcl::PointXYZ> cloud_filtered_y;

	pcl::PassThrough<pcl::PointXYZ> pass;
	pass.setInputCloud (raw_cloud.makeShared());
	pass.setFilterFieldName ("x");
	pass.setFilterLimits (Lowx, Uppx);
	pass.setFilterLimitsNegative (negative_limits); 
	pass.filter (cloud_filtered_x);
	
	if (cloud_filtered_x.points.size()>0)
	{
		pcl::PassThrough<pcl::PointXYZ> pass2;
		pass2.setInputCloud (cloud_filtered_x.makeShared());
		pass2.setFilterFieldName ("y");
		pass2.setFilterLimits (Lowy, Uppy);
		pass2.filter (cloud_filtered_y);

		if (cloud_filtered_y.points.size()>0)
		{
			pcl::PassThrough<pcl::PointXYZ> pass3;
			pass3.setInputCloud (cloud_filtered_y.makeShared());
			pass3.setFilterFieldName ("z");
			pass3.setFilterLimits (Lowz, Uppz);
			pass3.filter (cloud_filtered_z);
		}
	}

	return cloud_filtered_z;
}

boost::tuple<pcl::PointCloud<pcl::PointXYZ>, pcl::PointIndices::Ptr,pcl::ModelCoefficients::Ptr> DoorCloudAlgNode::planeFit (pcl::PointCloud<pcl::PointXYZ> raw_cloud)
{

	pcl::ModelCoefficients::Ptr coefficients (new pcl::ModelCoefficients ());
	pcl::PointIndices::Ptr inliers (new pcl::PointIndices);
	pcl::PointCloud<pcl::PointXYZ> planecloud;

	// Create the segmentation object
	pcl::SACSegmentation<pcl::PointXYZ> seg;
	// Optional
	seg.setOptimizeCoefficients (true);
	// Mandatory
	seg.setModelType (pcl::SACMODEL_PLANE);
	seg.setMethodType (pcl::SAC_RANSAC);
	seg.setDistanceThreshold (0.05);

	if (raw_cloud.points.size()>0)
	{
		seg.setInputCloud (raw_cloud.makeShared ());
		seg.segment (*inliers, *coefficients);

		pcl::ExtractIndices<pcl::PointXYZ> extract;
		extract.setInputCloud(raw_cloud.makeShared ());
		extract.setIndices (inliers);
		extract.setNegative(false);
		extract.filter(planecloud);
	}

	boost::tuple<pcl::PointCloud<pcl::PointXYZ>, pcl::PointIndices::Ptr, pcl::ModelCoefficients::Ptr> planeFit (planecloud, inliers, coefficients);

	return planeFit;
}

geometry_msgs::Quaternion DoorCloudAlgNode::quaternionFromVectors (tf::Vector3 vector_1, tf::Vector3 vector_2)
{	

	vector_1 = vector_1.normalize();
	vector_2 = vector_2.normalize();
	float rot_ang = acos(vector_1.dot(vector_2));
	tf::Vector3 rot_axis = vector_1.cross(vector_2);
	tf::Quaternion q = tf::Quaternion(rot_axis,rot_ang);
	q.normalize();
	tf::quaternionTFToMsg(q, orient);
	//ROS_ERROR("%f, %f, %f",poses.pose.orientation.x,poses.pose.orientation.y,poses.pose.orientation.z);
	//ROS_ERROR("%f, %f, %f, %f",orient.x,orient.y,orient.z,orient.w);

	return orient;
}

visualization_msgs::Marker DoorCloudAlgNode::ArrowMarker(std_msgs::Header header, geometry_msgs::Pose pose, int alpha, int color,  const char arrow_tag[])
{	

	marker.header = header;
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
