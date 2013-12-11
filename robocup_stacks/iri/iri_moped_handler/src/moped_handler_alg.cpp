#include "moped_handler_alg.h"

MopedHandlerAlgorithm::MopedHandlerAlgorithm(void)
{
}

MopedHandlerAlgorithm::~MopedHandlerAlgorithm(void)
{
}

void MopedHandlerAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// MopedHandlerAlgorithm Public API




// DEAD CODE

/*
void MopedHandlerAlgorithm::setObjectDataFromRosMsg(pr_msgs::ObjectPoseList input)
{
	// Clear previous data
	this->inputOpl.clear();

	// For every object pose in the input msg...
	for(size_t i=0; i<input.object_list.size(); ++i)
	{
		// Fill attributes with data.
		Op_t current;

		current.pos3D.x = input.object_list[i].pose.position.x;
		current.pos3D.y = input.object_list[i].pose.position.y;
		current.pos3D.z = input.object_list[i].pose.position.z;

		current.pos2D.x = input.object_list[i].pose2D.x;
		current.pos2D.y = input.object_list[i].pose2D.y;

		current.ori.x = input.object_list[i].pose.orientation.x;
		current.ori.y = input.object_list[i].pose.orientation.y;
		current.ori.z = input.object_list[i].pose.orientation.z;
		current.ori.w = input.object_list[i].pose.orientation.w;

		this->inputOpl.push_back(current);
	}
}

//   Starts to compute the input data and fills the output data.
void MopedHandlerAlgorithm::compute()
{
	// For every object...
	for(int i=0; i < this->inputOpl.size(); ++i)
	{
		// Get object
		Op_t objectPose = this->inputOpl[i];

		// Get pixels of object position
		int xPixel, yPixel;
		getPose2Pixel(objectPose.pos3D.x, objectPose3D.pos.y, objectPose3D.pos.z, xPixel, yPixel, this->pcl_);

		// Get position of point with new depth.
		pos_t refinedPosition = getPixel2Pose(xPixel, yPixel);
		Op_t refinedOp(objectPose);
		refinedOp.pos = refinedPosition;

		// Save refined object position to the attribute.
		this->outputOpl.push_back(refinedOp);
	}
}

//   Creates and returns a ROS msg from the output OPL.
pr_msgs::ObjectPoseList MopedHandlerAlgorithm::getRosMsgWithObjectData()
{
	size_t n = this->outputOpl.size();

	pr_msgs::ObjectPoseList result;
	result.object_list.resize(n);

	// For every object pose in the output attribute...
	for(size_t i=0; i<n; ++i)
	{
		result.object_list[i].pose.position.x = this->outputOpl[i].pos.x;
		result.object_list[i].pose.position.y = this->outputOpl[i].pos.y;
		result.object_list[i].pose.position.z = this->outputOpl[i].pos.z;

		result.object_list[i].pose.orientation.x = this->outputOpl[i].ori.x;
		result.object_list[i].pose.orientation.y = this->outputOpl[i].ori.y;
		result.object_list[i].pose.orientation.z = this->outputOpl[i].ori.z;
		result.object_list[i].pose.orientation.w = this->outputOpl[i].ori.w;
	}

	return result;
}

void MopedHandlerAlgorithm::getPose2Pixel(float x, float y, float z, int& xPixel, int& yPixel, pcl::PointCloud<pcl::PointXYZ> pcl)
{
	for(int col=0; col<640; ++col)
	for(int row=0; row<480; ++row)
	{
		pcl::PointXYZ p;
		p = pcl.at(col, row);

		if( p.x == x and p.y == y and p.z == z)
		{
			xPixel = row;
			yPixel = col;
			return;
		}
	}

	cout << "MopedHandlerAlgorithm::getPose2Pixel: Error! Point not found." << endl;
}

//float MopedHandlerAlgorithm::getDepthPixel(int x, int y, pcl::PointCloud<pcl::PointXYZ> pcl)
//{
//	pcl::PointXYZ p = pcl.at(x, y);

//	float aux1 = p.x * p.x;
//	float aux2 = p.y * p.y;
//	float aux3 = p.z * p.z;

//	return sqrt(aux1 + aux2 + aux3);
//}

MopedHandlerAlgorithm::pos_t MopedHandlerAlgorithm::getPixel2Pose(float xPixel, float yPixel, pcl::PointCloud<pcl::PointXYZ> pcl);
{
	pcl::PointXYZ p = pcl.at(x, y);

	// Check p correctness.
	// TODO: Complete.

	MopedHandlerAlgorithm::pos_t result;
	result.x = p.x;
	result.y = p.y;
	result.z = p.z;
	return result;
}

*/

