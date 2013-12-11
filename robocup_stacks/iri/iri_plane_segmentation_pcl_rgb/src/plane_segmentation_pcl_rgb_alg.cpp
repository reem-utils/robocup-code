#include "plane_segmentation_pcl_rgb_alg.h"

PlaneSegmentationPclRgbAlgorithm::PlaneSegmentationPclRgbAlgorithm(void)
{
}

PlaneSegmentationPclRgbAlgorithm::~PlaneSegmentationPclRgbAlgorithm(void)
{
}

void PlaneSegmentationPclRgbAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
	this->lock();
	
	this->pointcloud_downsample      = new_cfg.pointcloud_downsample;
	this->pointcloud_downsample_size = new_cfg.pointcloud_downsample_size;
	this->choose_plane_by_distance   = new_cfg.choose_plane_by_distance;
	this->choose_nearest_plane       = new_cfg.choose_nearest_plane;
	this->plane_size_thresh          = new_cfg.plane_size_thresh;
	this->plane_min_height           = new_cfg.plane_min_height;
	this->plane_max_height           = new_cfg.plane_max_height;
	this->plane_segm_iterations      = new_cfg.plane_segm_iterations;
	this->plane_clustering           = new_cfg.plane_clustering;
	this->plane_min_cluster_size     = new_cfg.plane_min_cluster_size;
	this->plane_min_cluster_distance = new_cfg.plane_min_cluster_distance;
	this->plane_segm_probability     = new_cfg.plane_segm_probability;
	
	// save the current configuration
	this->config_=new_cfg;
	
	this->unlock();
}

// PlaneSegmentationPclRgbAlgorithm Public API
pcl::PointCloud<pcl::PointXYZRGB>::Ptr PlaneSegmentationPclRgbAlgorithm::segmentBiggestPlane (pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_rgb_orig, 
											      pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_orig, 
											      pcl::ModelCoefficients::Ptr coefficients)
{
	pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_rgb_dst (new pcl::PointCloud<pcl::PointXYZRGB>);
	
	// we will need a copy of the pointcloud
	*cloud_rgb_dst = *cloud_rgb_orig; 
	
	// Plane segmentation indices
	pcl::PointIndices::Ptr inliers (new pcl::PointIndices ());
	
	// Downsample to improve performance
	if (pointcloud_downsample)
		getBiggestPlaneInliersDownsampling(inliers, coefficients, cloud_orig);
	else
		getBiggestPlaneInliers(inliers, coefficients, cloud_orig);
	
	
	// set all points but inliers to black
	for (size_t i = 0; i < cloud_rgb_dst->size(); ++i)
	{
		cloud_rgb_dst->at(i).rgb = 0;
	}
	
	for (size_t i = 0; i < inliers->indices.size(); ++i)
	{
		cloud_rgb_dst->at(inliers->indices[i]).rgb = cloud_rgb_orig->at(inliers->indices[i]).rgb;
	}
	
	// coefficients should be always pointing to the camera. If they are not, they will be inverted
	fixPlaneCoefficientsOrientation(coefficients);
	
	return cloud_rgb_dst;
}


void PlaneSegmentationPclRgbAlgorithm::getBiggestPlaneInliersDownsampling(pcl::PointIndices::Ptr inliers,
									  pcl::ModelCoefficients::Ptr coefficients,
									  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud)
{
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_downsampled (new pcl::PointCloud<pcl::PointXYZ>);
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_seg (new pcl::PointCloud<pcl::PointXYZ>);
	pcl::PointCloud<pcl::PointXYZ>::Ptr ground_hull (new pcl::PointCloud<pcl::PointXYZ>);
	
	// downsampling
	pcl::VoxelGrid<pcl::PointXYZ> grid_objects_;
	grid_objects_.setLeafSize (pointcloud_downsample_size, pointcloud_downsample_size, pointcloud_downsample_size);
	grid_objects_.setDownsampleAllData (false);
	
	grid_objects_.setInputCloud (cloud);
	grid_objects_.filter (*cloud_downsampled);
	
	// segment plane
	if (choose_plane_by_distance)
		getNearestBigPlaneInliers(inliers, coefficients, cloud_downsampled);
	else
		getBiggestPlaneInliers(inliers, coefficients, cloud_downsampled);
	
	// check if the plane exists
	if (inliers->indices.size() == 0) {
		// if plane doesn't exist a black image will be returned
		ROS_WARN_STREAM("Plane segmentation: couldn't find plane.");
		return;
	}
	
	// copy inliers
	pcl::ProjectInliers<pcl::PointXYZ> proj;
	proj.setModelType(pcl::SACMODEL_PLANE);
	proj.setInputCloud(cloud_downsampled);
	proj.setModelCoefficients(coefficients);
	proj.setIndices (inliers);
	proj.filter(*cloud_seg);
	
	// remove NaN
	pcl::PassThrough<pcl::PointXYZ> pass;
	pass.setInputCloud (cloud_seg);
	pass.filter (*cloud_seg);
	
	// get biggest cluster
	if (plane_clustering)
		cloud_seg = getBiggestClusterPC(cloud_seg);
	
	// Create a Convex Hull representation of the projected inliers
	pcl::ConvexHull<pcl::PointXYZ> chull;
	chull.setInputCloud(cloud_seg);
	chull.setDimension(2);
	chull.reconstruct(*ground_hull);
	
	
	// Extract only those outliers that lie inside the ground plane's convex hull
	pcl::PointIndices::Ptr object_indices (new pcl::PointIndices);
	pcl::ExtractPolygonalPrismData<pcl::PointXYZ> hull_limiter;
	hull_limiter.setInputCloud(cloud);
	hull_limiter.setInputPlanarHull(ground_hull);
	hull_limiter.setHeightLimits(plane_min_height, plane_max_height);
	hull_limiter.segment(*object_indices);
	
	*inliers = *object_indices;
}


void PlaneSegmentationPclRgbAlgorithm::getNearestBigPlaneInliers(pcl::PointIndices::Ptr inliers,
								 pcl::ModelCoefficients::Ptr coefficients,
								 pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_orig)
{
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_seg (new pcl::PointCloud<pcl::PointXYZ>);
	pcl::PointIndices::Ptr inliers_first (new pcl::PointIndices ());
	pcl::PointIndices::Ptr inliers_second (new pcl::PointIndices ());
	pcl::ModelCoefficients::Ptr coefficients_first (new pcl::ModelCoefficients);
	pcl::ModelCoefficients::Ptr coefficients_second (new pcl::ModelCoefficients);
	pcl::ExtractIndices<pcl::PointXYZ> extract;
	float dist1, dist2;
	pcl::PointXYZ p_orig = pcl::PointXYZ(0,0,0);
	ROS_DEBUG("Get nearest big plane.");
	
	// Get biggest plane
	getBiggestPlaneInliers(inliers_first, coefficients_first, cloud_orig);
	
	// check if first plane exists
	if (inliers_first->indices.size () == 0) // no plane
		return;
	
	//dist1 = euclideanDistance(cloud_orig->at(inliers_first->indices[0]), p_orig);
	dist1 = pointToPlaneDistance(p_orig, coefficients_first->values);
	
	// Remove plane from pointcloud
	extract.setInputCloud (cloud_orig);
	extract.setIndices (inliers_first);
	extract.setNegative (true);
	extract.filter (*cloud_seg);
	
	// Get second biggest plane
	getBiggestPlaneInliers(inliers_second, coefficients_second, cloud_seg);
	
	// check if the second plane exists
	if (inliers_second->indices.size () == 0) {
		ROS_INFO_STREAM("Plane segmentation: couldn't find a second plane. Choosing biggest one.");
		*inliers = *inliers_first;
		*coefficients = *coefficients_first;
		return;
	}
	
	//dist2 = euclideanDistance(cloud_seg->at(inliers_second->indices[0]), p_orig);
	dist2 = pointToPlaneDistance(p_orig, coefficients_second->values);
	
	ROS_DEBUG_STREAM("Dist 1 is "<<dist1);
	ROS_DEBUG_STREAM("Dist 2 is "<<dist2);
	
	// if first is nearest get its inliers 
	if ( ( (dist1 < dist2) && choose_nearest_plane ) || ( (dist1 > dist2) && !choose_nearest_plane ) ) {
		ROS_DEBUG("Chose biggest plane.");
		*inliers = *inliers_first;
		*coefficients = *coefficients_first;
	}
	else { // else inliers would be of the second plane
		ROS_DEBUG("Chose second biggest plane.");
		*inliers = *inliers_second;
		*coefficients = *coefficients_second;
		*cloud_orig = *cloud_seg;
	}
	
	
}


void PlaneSegmentationPclRgbAlgorithm::getBiggestPlaneInliers(pcl::PointIndices::Ptr inliers,
							      pcl::ModelCoefficients::Ptr coefficients,
							      pcl::PointCloud<pcl::PointXYZ>::Ptr cloud)
{
	// Create the segmentation object
	pcl::SACSegmentation<pcl::PointXYZ> seg;
	// Optional
	seg.setOptimizeCoefficients (true);
	// Iterations
	seg.setMaxIterations (plane_segm_iterations);
	// Probability
	seg.setProbability (plane_segm_probability);
	// Mandatory
	seg.setModelType (pcl::SACMODEL_PLANE);
	seg.setMethodType (pcl::SAC_RANSAC);
	seg.setDistanceThreshold (plane_size_thresh); // centimeters | from param server
	
	// segment
	seg.setInputCloud (cloud);
	seg.segment (*inliers, *coefficients);
}


void PlaneSegmentationPclRgbAlgorithm::fixPlaneCoefficientsOrientation(pcl::ModelCoefficients::Ptr coefs)
{
	if (coefs->values.size() == 0) { // plane extraction failed
		coefs->values.resize(4);
		coefs->values[0] = 0;
		coefs->values[1] = 0;
		coefs->values[2] = 0;
		coefs->values[3] = 0;
	}
	else if (coefs->values[2] < 0) {
		coefs->values[0] = -coefs->values[0];
		coefs->values[1] = -coefs->values[1];
		coefs->values[2] = -coefs->values[2];
		coefs->values[3] = -coefs->values[3];
	}
}


pcl::PointCloud<pcl::PointXYZ>::Ptr PlaneSegmentationPclRgbAlgorithm::getBiggestClusterPC (pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_orig)
{
	pcl::EuclideanClusterExtraction<pcl::PointXYZ> pcl_cluster;
	// Min distance between two clusters
	pcl_cluster.setClusterTolerance (plane_min_cluster_distance);
	// Min number of points for a cluster
	pcl_cluster.setMinClusterSize (plane_min_cluster_size);
	
	ROS_DEBUG("Clustering");
	
	ROS_DEBUG_STREAM("Original pointcloud size is" << cloud_orig->points.size());
	
	std::vector<pcl::PointIndices> clusters;
	pcl_cluster.setInputCloud (cloud_orig);
	pcl_cluster.extract (clusters);

	//converts clusters into the PointCloud message
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_cluster (new pcl::PointCloud<pcl::PointXYZ>);
	
	ROS_DEBUG_STREAM("Number of clusters is " << clusters.size());
	
	if ((int)clusters.size () > 0 ) {
		// get biggest cluster
		size_t biggest_cluster = 0;
		for (size_t j = 1; j < clusters.size (); ++j) {
			if (clusters[biggest_cluster].indices.size () < clusters[j].indices.size ())
				biggest_cluster = j;
		}
		
		ROS_DEBUG_STREAM("Biggest cluster is " << clusters[biggest_cluster].indices.size());
		cloud_cluster->points.resize (clusters[biggest_cluster].indices.size ());
		for (size_t j = 0; j < cloud_cluster->points.size (); ++j)
		{
			cloud_cluster->points[j].x = cloud_orig->points[clusters[biggest_cluster].indices[j]].x;
			cloud_cluster->points[j].y = cloud_orig->points[clusters[biggest_cluster].indices[j]].y;
			cloud_cluster->points[j].z = cloud_orig->points[clusters[biggest_cluster].indices[j]].z;
		}
	}
	else
		*cloud_cluster = *cloud_orig;
	
	return cloud_cluster;
}