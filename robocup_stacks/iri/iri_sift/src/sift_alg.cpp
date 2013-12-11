#include "sift_alg.h"

extern "C" {
#include "dsift.h"
}

using namespace cv;

SiftAlgorithm::SiftAlgorithm(void)
{
        centroids_ready_ = false;
//      sift_centroids_ = Mat(128, 128, CV_32FC1);
}

SiftAlgorithm::~SiftAlgorithm(void)
{
}

void SiftAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
        this->lock();

        this->descriptors_file_ = new_cfg.descriptors_file;
        // save the current configuration
        this->config_=new_cfg;
        
        this->unlock();
}

// SiftAlgorithm Public API

iri_perception_msgs::DescriptorSet SiftAlgorithm::get_descriptors_from_image(cv::Mat &image)
{
        iri_perception_msgs::DescriptorSet result;
        cv::Mat descriptors;
        std::vector<cv::KeyPoint> keypoints;
        
        get_sift_descriptors(image, descriptors, keypoints);
        for (int i=0; i < descriptors.rows; i++) {
                iri_perception_msgs::Descriptor descriptor;
                for (int j=0; j < descriptors.cols; j++) {
                        descriptor.descriptor.push_back(descriptors.at<float>(i,j));
                }
                descriptor.u = keypoints[i].pt.x;
                descriptor.v = keypoints[i].pt.y;
                result.descriptors.push_back(descriptor);
        }
        
        result.num = descriptors.rows;
        result.len = descriptors.cols;
        result.width = 640;
        result.height = 480;
        //result.num_orient_bins = ; TODO ARNAU
        //result.num_spa_bins = ; TODO ARNAU
        
        return result;
}


iri_perception_msgs::GeoVwSet SiftAlgorithm::get_geovw_from_image(cv::Mat &image)
{
        cv::Mat descriptors;
        std::vector<cv::KeyPoint> keypoints;
        
        get_sift_descriptors(image, descriptors, keypoints);
        
        return get_geo_vw_from_descriptors(descriptors, keypoints);
}

iri_perception_msgs::GeoVwSet SiftAlgorithm::get_geo_vw_from_descriptors(cv::Mat descriptors, std::vector<cv::KeyPoint> keypoints)
{
        std::vector<DMatch> matches;
        
        ROS_INFO("MATCHING! %d, %d", descriptors.rows, sift_centroids_.rows);
        
        cv::Ptr<cv::DescriptorMatcher> matcher = cv::DescriptorMatcher::create("BruteForce");
        matcher->match( descriptors, sift_centroids_, matches);
        
        iri_perception_msgs::GeoVwSet geo_vw_set;
        vector<DMatch>::iterator it;
        for ( it=matches.begin() ; it < matches.end(); it++ ) {
                iri_perception_msgs::GeoVw geo_vw;
                geo_vw.x = keypoints[it->queryIdx].pt.x;
                geo_vw.y = keypoints[it->queryIdx].pt.y;
                geo_vw.word = it->trainIdx;
                geo_vw_set.geo_vws.push_back(geo_vw);
        }
        
        return geo_vw_set;
}

void SiftAlgorithm::get_sift_descriptors(cv::Mat const& image, cv::Mat& descriptors, std::vector<cv::KeyPoint>& keypoints)
{
        cv::Mat image_gray;
        
        //cv::DenseFeatureDetector::Params(1.f,1,0.1f,6));
        //cv::Ptr<FeatureDetector> feature_detector = new DenseFeatureDetector();
        //cv::Ptr<DescriptorExtractor> descriptor_extractor = DescriptorExtractor::create("SIFT");

        cvtColor(image, image_gray, CV_RGB2GRAY);
        cv::Mat ima;
        image_gray.convertTo(ima, CV_32F);

        
        ROS_DEBUG("SiftAlgNode::get_sift_descriptors: Getting keypoints..."); 
        
        float* img=ima.ptr<float>(0);
        int width = ima.cols; 
        int height = ima.rows;

        VlDsiftFilter* dsift_data = vl_dsift_new (width, height);
        VlDsiftDescriptorGeometry dsift_geo;
        dsift_geo.binSizeX=8;
        dsift_geo.binSizeY=8;
        dsift_geo.numBinT=8;
        dsift_geo.numBinX=4;
        dsift_geo.numBinY=4;
        
        int descsize = dsift_geo.numBinT*dsift_geo.numBinX*dsift_geo.numBinY;
        
        vl_dsift_set_geometry(dsift_data, &dsift_geo);
        vl_dsift_set_steps (dsift_data,6,6);
        vl_dsift_process(dsift_data, img);
        
        int npoints = vl_dsift_get_keypoint_num (dsift_data);
        
        float const* descs = vl_dsift_get_descriptors (dsift_data);
        VlDsiftKeypoint const * kpoints = vl_dsift_get_keypoints (dsift_data);
        
        ROS_DEBUG("SiftAlgNode::get_sift_descriptors: Getting descriptors..."); 

        for(int i=0; i<npoints; i++)
                keypoints.push_back(cv::KeyPoint(kpoints[i].x, kpoints[i].y, kpoints[i].s, 0, kpoints[i].norm));

        cv::Mat fdescs(npoints, 128, CV_32FC1);
        if(!fdescs.isContinuous())
        {
                std::cout<<"Matrix not continuous!"<<std::endl;
                exit (-1);
        }
        memcpy(fdescs.ptr<float>(0), descs, sizeof(float)*npoints*128);
        descriptors = cv::Mat(npoints, 128, CV_32FC1);
        fdescs.convertTo(descriptors, CV_32F, 256); // 07/08/12 Arnau: Originally though to converting it to uchar (less space faster to match). Turns out cv::Matcher can only work wit floats, apparently. 
        //std::cout<<descriptors<<std::endl;
        vl_dsift_delete(dsift_data);
        //descriptor_extractor->compute( image_gray, keypoints, descriptors );
}

cv::Mat SiftAlgorithm::read_trained_descriptors()
{
        FileStorage fs; 
        fs.open(this->descriptors_file_, FileStorage::READ);
        
        Mat trained_desc;
        fs["descriptors"] >> trained_desc;
        
        fs.release();
        return trained_desc;
}

bool SiftAlgorithm::save_descriptors(Mat descriptors)
{
        ROS_INFO("SiftAlgNode::save_descriptors: Saving descriptors"); 
        
        FileStorage fs(this->descriptors_file_, FileStorage::WRITE);
        
        fs << "descriptors" << descriptors;
        
        fs.release();
        
        ROS_INFO("SiftAlgNode::save_descriptors: Finished"); 
        
        return true;
}
