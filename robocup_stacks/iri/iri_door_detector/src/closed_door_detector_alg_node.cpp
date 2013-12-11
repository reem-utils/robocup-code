#include "closed_door_detector_alg_node.h"

using namespace std;
namespace enc = sensor_msgs::image_encodings;

static const char WINDOW_1[] = "Closed Door Detector";

geometry_msgs::PoseStamped poses;

ClosedDoorDetectorAlgNode::ClosedDoorDetectorAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<ClosedDoorDetectorAlgorithm>()
{

  //<Added by Ruben>
   fx_d = 1.0 / 5.9421434211923247e+02;
   fy_d = 1.0 / 5.9104053696870778e+02;
   cx_d = 3.3930780975300314e+02;
   cy_d = 2.4273913761751615e+02;
   min_range = 0.5;
   max_range = 5.5;

  //</Added by Ruben>

  //init class attributes if necessary
  //this->loop_rate_ = 2;//in [Hz]

  // [init publishers]
  this->door_handle_publisher_ = this->public_node_handle_.advertise<geometry_msgs::PoseStamped>("door_handle", 1);
  this->closed_door_coordinates_publisher_ = this->public_node_handle_.advertise<std_msgs::Int32MultiArray>("closed_door_coordinates", 1);
  
  // [init subscribers]
  this->door_action_start_subscriber_ = this->public_node_handle_.subscribe("/iri_door_detector/door_detector_actions/door_action_start", 1, &ClosedDoorDetectorAlgNode::door_action_start_callback, this);

  // [init services]
  
  // [init clients]
  
  // [init action servers]
  
  // [init action clients]

  // [init algorithm variables]
 
  //variable declaration
  start=0;
  captured_depth = 0;	
  handle_x=0;
  handle_y=0;
  door_x=0;
  door_y=0;
  support=0;

  white = CV_RGB(255,255,255);
  black = CV_RGB(0,0,0);
}

ClosedDoorDetectorAlgNode::~ClosedDoorDetectorAlgNode(void)
{
  // [free dynamic memory]
}

void ClosedDoorDetectorAlgNode::mainNodeThread(void)
{
  // [fill msg structures]
  //this->Marker_msg_.data = my_var;
  //this->PointCloud2_msg_.data = my_var;
  //this->PoseStamped_msg_.data = my_var;
  
  // [fill srv structure and make request to the server]
  
  // [fill action structure and make request to the action server]

  // [publish messages]
  //this->door_handle_publisher_.publish(poses);
}

/*  [subscriber callbacks] */
void ClosedDoorDetectorAlgNode::door_action_start_callback(const std_msgs::Int8::ConstPtr& action_start) 
{ 
  ROS_INFO("ClosedDoorDetectorAlgNode::door_action_start_callback: New Message Received");

  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->door_action_start_mutex_.enter(); 

  start=action_start->data;

  if (start==0)
  {
  	points_subscriber_.shutdown();
	image_color_subscriber_.shutdown();
	//cvDestroyWindow("Closed Door Detector");
  }
  if (start==1)
  {
  	this->image_color_subscriber_ = this->public_node_handle_.subscribe("/camera/rgb/image_color", 1, &ClosedDoorDetectorAlgNode::image_color_callback, this);
	this->points_subscriber_ = this->public_node_handle_.subscribe("/camera/depth/points", 1, &ClosedDoorDetectorAlgNode::points_callback, this);
  }	

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->door_action_start_mutex_.exit(); 
}

void ClosedDoorDetectorAlgNode::points_callback(const sensor_msgs::PointCloud2::ConstPtr& points) 
{ 
  ROS_INFO("ClosedDoorDetectorAlgNode::image_depth_callback: New Message Received");

  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->points_mutex_.enter();  	

  if(captured_depth==0)
  {
	pcl::fromROSMsg (*points, cloud);
  }

  captured_depth = 1;  

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->points_mutex_.exit(); 
}

void ClosedDoorDetectorAlgNode::image_color_callback(const sensor_msgs::Image::ConstPtr& image_color) 
{ 
  ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: New Message Received");

  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->image_color_mutex_.enter(); 

  if(captured_depth==1)
  {
	try
	{
		canny = cv_bridge::toCvCopy(image_color, enc::MONO8);					
		blobs = cv_bridge::toCvCopy(image_color, enc::MONO8);
		original = cv_bridge::toCvCopy(image_color, enc::BGR8);
		gradient = cv_bridge::toCvCopy(image_color, enc::BGR8);
	}
	catch (cv_bridge::Exception& e)
	{
		//if there is an error during conversion, display it
		ROS_ERROR("Error while capturing color image: %s", e.what());
		return;
	}  
    //ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: New Message Received");

	//Image denoising
	cv::medianBlur(gradient->image, gradient->image, 3);	
	cv::GaussianBlur(gradient->image, gradient->image, cv::Size(5,5), 0, 0);
	//cv::boxFilter(gradient->image, gradient->image, -1, cv::Size(7,7));
	//cv::bilateralFilter(gradient->image, gradient->image, 5, 10.0, 10.0);
	//cv::pyrMeanShiftFiltering(gradient->image, gradient->image, 3.0, 150.0, 0);

	//Get image gradient
	cv::morphologyEx(gradient->image, gradient->image, cv::MORPH_GRADIENT, (getStructuringElement(cv::MORPH_RECT, cv::Size(3,3), cv::Point(-1, -1))), cv::Point(-1,-1), 1);	

	//Get image borders
	cv::cvtColor(gradient->image, canny->image, CV_BGR2GRAY);
	cv::medianBlur(canny->image, canny->image, 3);
	cv::GaussianBlur( canny->image, canny->image, cv::Size(5,5), 0, 0);
	cv::Canny(canny->image, canny->image, segment_fidelity, segment_size, 3, true);
 
	//Perform Watershed segmentation
	compCount = 0;
	vector<vector<cv::Point> > contours;
	vector<cv::Vec4i> hierarchy;

	findContours(canny->image, contours, hierarchy, CV_RETR_CCOMP, CV_CHAIN_APPROX_SIMPLE);

	cv::Mat markers(canny->image.size(), CV_32S);
	markers = cv::Scalar::all(0);

    ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: 1");

	if( !contours.empty() )
	{
		idx = 0;
		for( ; idx >= 0; idx = hierarchy[idx][0], compCount++ )
			drawContours(markers, contours, idx, cv::Scalar::all(compCount+1), -1, 8, hierarchy, INT_MAX);

		colorTab.clear();
		if( compCount != 0 )
		{
			for(int i = 0; i < compCount; i++ )
			{
				int b = rng.uniform(0, 255);
				int g = rng.uniform(0, 255);
				int r = rng.uniform(0, 255);

				colorTab.push_back(cv::Vec3b((uchar)b, (uchar)g, (uchar)r));
			}
		}
	}	
	
	//Use gradient image as input for the watershed segmentation
	watershed( gradient->image, markers );

	cv::Mat wshed(markers.size(), CV_8UC3);
	wshed = cv::Scalar::all(0);

    ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: 2");

	// paint the watershed image
	for(int i = 0; i < markers.rows; i++ )
	{
		for(int j = 0; j < markers.cols; j++ )
		{
		    idx = markers.at<int>(i,j);
		    if( idx == -1 )
		    {
			wshed.at<cv::Vec3b>(i,j) = cv::Vec3b(255,255,255);
		    }
		    else if( idx <= 0 || idx > compCount )
			wshed.at<cv::Vec3b>(i,j) = cv::Vec3b(0,0,0);
		    else
		    {
			wshed.at<cv::Vec3b>(i,j) = colorTab[idx - 1];
		    }
		}
	}
	
	cv::GaussianBlur( blobs->image, blobs->image,cv::Size(7,7), 0, 0);

	//Prepare blobs extraction
	cv::Sobel(blobs->image, blobs->image, -1, 0, 1, 3, 1, 0); 
	cv::Canny(blobs->image, blobs->image, allowed_blobs, allowed_blobs, 3, true);
	cv::dilate(blobs->image, blobs->image, (getStructuringElement(cv::MORPH_ELLIPSE, cv::Size(3,3), cv::Point(-1, -1))), cv::Point(-1, -1), 2);

	/*for(int i = 1; i < blobs->image.rows; i++)
	{
		for(int j = 1; j < blobs->image.cols; j++ )
		{
			if (wshed.at<cv::Vec3b>(i,j) == cv::Vec3b(255,255,255))
				blobs->image.data[i*blobs->image.cols+j]=0;
		}	
	}*/
	
	cv::erode(blobs->image, blobs->image, (getStructuringElement(cv::MORPH_RECT, cv::Size(3,3), cv::Point(-1, -1))), cv::Point(-1, -1), 1);
	cv::dilate(blobs->image, blobs->image, (getStructuringElement(cv::MORPH_RECT, cv::Size(5,5), cv::Point(-1, -1))), cv::Point(-1, -1), 3);
	cv::erode(blobs->image, blobs->image, (getStructuringElement(cv::MORPH_ELLIPSE, cv::Size(5,5), cv::Point(-1, -1))), cv::Point(-1, -1), 3);

    ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: 3");

    cv::Mat blob_mat;
	blob_mat = cv::Mat::zeros(blobs->image.rows, blobs->image.cols, CV_8UC3);
	
	//Convert images to match cvBlob format
	IplImage ipl_1 = blobs->image;

	//Declare cvBlob output variables
	IplImage *labelImg = cvCreateImage(cv::Size(blobs->image.cols,blobs->image.rows), IPL_DEPTH_LABEL, 1);
	IplImage *blobsDst = cvCreateImage(cv::Size(blobs->image.cols,blobs->image.rows), IPL_DEPTH_8U, 3);
	cvZero(blobsDst);
	cvb::CvBlobs CVblobs;

	//Label Blobs and render 
	cvb::cvLabel(&ipl_1, labelImg, CVblobs);
	//cvFilterByArea(blobs, 1000, 50000);
	cvb::cvRenderBlobs(labelImg, CVblobs, blobsDst, blobsDst, CV_BLOB_RENDER_COLOR);

	//Convert back to general format
  	blob_mat= cv::Mat(blobsDst,true);
		
	cvReleaseImage(&labelImg);
	cvReleaseImage(&blobsDst);
	//ROS_ERROR("blobs size: %i, pixels: %i", blobs.size(), result);	

	vec_up.clear();
	vec_down.clear();
	vec_left.clear();
	vec_right.clear();
	ss_door_centroid.clear();
	ss_handle.clear();
	ss_handle_x.clear();
	ss_handle_y.clear();
	ss_handle_z.clear();
	ss_c1.clear();
	ss_c2.clear();
	ss_c3.clear();
	ss_c4.clear();

	step_x=canny->image.cols/(24);
	step_y=canny->image.rows/(18);


    ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: 4");

	CvPoint p_right, p_left;
	// watershed horizontal scan
	for(int i = 1; i < wshed.rows; i=i+step_y)
	{
		point=0;
		original_color = wshed.at<cv::Vec3b>(i,1);
		color = wshed.at<cv::Vec3b>(i,1);
		p_left = cvPoint(0,i);
		p_right = cvPoint(0,0);

		for(int j = 1; j < wshed.cols; j++ )
		{
			//Seed condition to allow skipping NaN depth readings
			min_dst_h=1;
			max_dst_h=0;
			if( wshed.at<cv::Vec3b>(i,j) != color && (wshed.at<cv::Vec3b>(i,j) != cv::Vec3b(255,255,255) || j==wshed.cols-1))
			{
				p_right=cvPoint(j,i);	
				if(j<wshed.cols-1)
				{	
					repeated_color=0;
					for(int n=j; n<wshed.cols; n++)
					{
						if(wshed.at<cv::Vec3b>(i,n) == color && wshed.at<cv::Vec3b>(i,n) != cv::Vec3b(255,255,255))
						{
							repeated_color=1;
							p_right = cvPoint(n,i);
						}
					}
				}
				point3D = cloud.at((int)((p_left.x+p_right.x)/2),i);
				sensor_range=(!std::isnan(point3D.z) && point3D.z>0.0 && point3D.z<5.0);
				if(sensor_range)
				{
					min_dst_h=(min_door_width/point3D.z);
					max_dst_h=(max_door_width/point3D.z);
				
					if(p_left.x<=10 || p_right.x>=wshed.cols-10)
						min_dst_h=min_dst_h/2;
					if(abs(p_left.x-p_right.x)>min_dst_h && abs(p_left.x-p_right.x)<max_dst_h)
					{
						vec_left.push_back(p_left);
						vec_right.push_back(p_right);
						if(SVP)
						{cv::line(original->image, p_left,p_left, CV_RGB(0,0,0), 10, 8, 0);
						cv::line(original->image, p_right, p_right, CV_RGB(255,255,255), 10, 8, 0);}
						point=1;
					}
				}
				p_left = cvPoint(j,i);					
			}
			if(j==wshed.cols-3 && point==0 && wshed.at<cv::Vec3b>(i,j) == original_color)
			{
				vec_left.push_back(cvPoint(0,i));
				vec_right.push_back(cvPoint(j+2,i));
				if(SVP)
				{cv::line(original->image, cvPoint(0,i) , cvPoint(0,i), CV_RGB(0,0,0), 10, 8, 0);
				cv::line(original->image, cvPoint(j,i), cvPoint(j,i), CV_RGB(255,255,255), 10, 8, 0);}
			}
			if(wshed.at<cv::Vec3b>(i,j) != cv::Vec3b(255,255,255))
				color = wshed.at<cv::Vec3b>(i,j);
		}
	}

    ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: 5");

	CvPoint p_up, p_down;
	// watershed vertical scan
	for(int j = 1; j < wshed.cols; j=j+step_x)
	{
	
		point=0;
		original_color=wshed.at<cv::Vec3b>(1,j);
		color = wshed.at<cv::Vec3b>(1,j);
		p_up = cvPoint(j,0);
		p_down = cvPoint(0,0);

		for(int i = 1; i < wshed.rows; i++ )
		{
			if( wshed.at<cv::Vec3b>(i,j) != color && (wshed.at<cv::Vec3b>(i,j) != cv::Vec3b(255,255,255) || i==wshed.rows-1))
			{
				//Seed condition to allow skipping NaN depth readings
				min_dst_v=1;
				max_dst_v=0;
				p_down=cvPoint(j,i);
				if(i<wshed.rows-1)
				{	
					repeated_color=0;
					for(int n=i; n<wshed.rows; n++)
					{
						if(wshed.at<cv::Vec3b>(n,j) == color && wshed.at<cv::Vec3b>(n,j) != cv::Vec3b(255,255,255))
							repeated_color=1;
						if(wshed.at<cv::Vec3b>(n,j) != color && wshed.at<cv::Vec3b>(n,j) != cv::Vec3b(255,255,255) && repeated_color==1)
						{
							p_down = cvPoint(j,n);
							repeated_color=0;
							i=n;
						}
						if(n==wshed.rows-3 && repeated_color==1)
						{
							p_down = cvPoint(j,n+2);
							repeated_color=0;
							i=n+2;
						}
						if(n==wshed.rows-3 && point==0 && wshed.at<cv::Vec3b>(n,j) == original_color)
						{
							vec_up.push_back(cvPoint(j,0));
							vec_down.push_back(cvPoint(j,n+2));
							if(SVP)
							{cv::line(original->image, cvPoint(j,0), cvPoint(j,0), CV_RGB(0,0,0), 10, 8, 0);
							cv::line(original->image, cvPoint(j,n), cvPoint(j,n), CV_RGB(255,255,255), 10, 8, 0);}
						}
						
					}
				}
				
				point3D = cloud.at(j,(int)((p_up.y+p_down.y)/2));

				sensor_range=(!std::isnan(point3D.z) && point3D.z>0 && point3D.z<5.0);
				if(sensor_range)
				{
					min_dst_v=(min_door_height/point3D.z);
					max_dst_v=(max_door_height/point3D.z);
	
					if(p_up.y<=10 || p_down.y>=wshed.rows-10)
						min_dst_v=min_dst_v/2;
					if(abs(p_up.y-p_down.y)>min_dst_v && abs(p_up.y-p_down.y)<max_dst_v && sensor_range)
					{
						vec_up.push_back(p_up);
						vec_down.push_back(p_down);
						if(SVP)
						{cv::line(original->image, p_up,p_up, CV_RGB(0,0,0), 10, 8, 0);
						cv::line(original->image, p_down, p_down, CV_RGB(255,255,255), 10, 8, 0);}
						point=1;
					}
				}
				p_up = cvPoint(j,i);				
			}
			if(i==wshed.rows-3 && point==0 && wshed.at<cv::Vec3b>(i,j) == original_color)
			{
				vec_up.push_back(cvPoint(j,0));
				vec_down.push_back(cvPoint(j,i+2));
				if(SVP)
				{cv::line(original->image, cvPoint(j,0), cvPoint(j,0), CV_RGB(0,0,0), 10, 8, 0);
				cv::line(original->image, cvPoint(j,i), cvPoint(j,i), CV_RGB(255,255,255), 10, 8, 0);}
			}
			if(wshed.at<cv::Vec3b>(i,j) != cv::Vec3b(255,255,255))
				color = wshed.at<cv::Vec3b>(i,j);
		}
	}		

	frames_size=min(min(vec_left.size(),vec_right.size()),min(vec_up.size(),vec_down.size()));

     ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: 6");

	if(frames_size>1)
	{	
         ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: if(frames_size>1) is >1");
         ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: vec_up.size(): " << std::to_string ( vec_up.size() ));
         ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: vec_left.size(): " << std::to_string ( vec_left.size() ));
		for(size_t j=0;j<vec_up.size()-1;j++)
		{	
			for(size_t i=0;i<vec_left.size()-1;i++)
			{	
				f_c1=0;
				f_c2=0;
				f_c3=0;
				f_c4=0;
				
				//look for the next left marker which is nearest to left marker i
				check=0;
				offset_l=0;
				dst=canny->image.cols*2;
				while(check==0)
				{
					while(vec_left.at(i+1+offset_l).y==vec_left.at(i).y)
					{
						offset_l++;
						if(i+1+offset_l>vec_left.size()-2)
						{
							offset_l--;
							break;
						}
					}
					if(i+1+offset_l>vec_left.size()-2)
					{
						offset_l--;
						break;
					}
					dst=min(dst,abs(vec_left.at(i+1+offset_l).x-vec_left.at(i).x));
					if(i+2+offset_l<vec_left.size()-1)
					{		
						if(vec_left.at(i+2+offset_l).y>vec_left.at(i+1+offset_l).y)
						{
							check=1;
						}		
					}
					if(check==0)
						offset_l++;
				}
				if(offset_l>0)
				{
					for(int k=0; k<=offset_l; k++)
					{
						if(abs(vec_left.at(i+1+k).x-vec_left.at(i).x)==dst)
							offset_l=k;
					}
				}
					
                ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: look for the next up marker which is nearest to up marker " << std::to_string(i));

				//look for the next up marker which is nearest to up marker i
				check=0;
				offset_u=0;
				dst=canny->image.cols*2;
				while(check==0)
				{
					while(vec_up.at(j+1+offset_u).x==vec_up.at(j).x)
					{
						offset_u++;
						if(j+1+offset_u>vec_up.size()-2)
						{
							offset_u--;
							break;
						}
					}
					if(j+1+offset_u>vec_up.size()-2)
					{
						offset_u--;
						break;
					}
					dst=min(dst,abs(vec_up.at(j+1+offset_u).y-vec_up.at(j).y));
					if(j+2+offset_u<vec_up.size()-1)
					{		
						if(vec_up.at(j+2+offset_u).x>vec_up.at(j+1+offset_u).x)
						{
							check=1;
						}
					}
					if(check==0)
						offset_u++;		
				}
				if(offset_u>0)
				{
					for(int k=0; k<=offset_u; k++)
					{
						if(abs(vec_up.at(j+1+k).y-vec_up.at(j).y)==dst)
							offset_u=k;
					}
				}

                ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: look for the next right marker which is nearest to right marker " << std::to_string(i));
				//look for the next right marker which is nearest to right marker i
				check=0;
				offset_r=0;
				dst=canny->image.cols*2;
				while(check==0)
				{
					while(vec_right.at(i+1+offset_r).y==vec_right.at(i).y)
					{
						offset_r++;
						if(i+1+offset_r>vec_right.size()-2)
						{
							offset_r--;
							break;
						}
					}
					if(i+1+offset_r>vec_right.size()-2)
					{
						offset_r--;
						break;
					}
					dst=min(dst,abs(vec_right.at(i+1+offset_r).x-vec_right.at(i).x));
					if(i+2+offset_r<vec_right.size()-1)
					{		
						if(vec_right.at(i+2+offset_r).y>vec_right.at(i+1+offset_r).y)
						{
							check=1;
						}		
					}
					if(check==0)
						offset_r++;
				}
				if(offset_r>0)
				{
					for(int k=0; k<=offset_r; k++)
					{
						if(abs(vec_right.at(i+1+k).x-vec_right.at(i).x)==dst)
							offset_r=k;
					}
				}

                ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: look for the next left marker which is nearest to down marker " << std::to_string(i));
				//look for the next left marker which is nearest to down marker i					
				check=0;
				offset_d=0;
				dst=canny->image.cols*2;
				while(check==0)
				{
					while(vec_down.at(j+1+offset_d).x==vec_down.at(j).x)
					{
						offset_d++;
						if(j+1+offset_d>vec_down.size()-2)
						{
							offset_d--;
							break;
						}
					}
					if(j+1+offset_d>vec_down.size()-2)
					{
						offset_d--;
						break;
					}
					dst=min(dst,abs(vec_down.at(j+1+offset_d).y-vec_down.at(j).y));
					if(j+2+offset_d<vec_down.size()-1)
					{		
						if(vec_down.at(j+2+offset_d).x>vec_down.at(j+1+offset_d).x)
						{
							check=1;
						}
					}
					if(check==0)
						offset_d++;		
				}
				if(offset_d>0)
				{
					for(int k=0; k<=offset_d; k++)
					{
						if(abs(vec_down.at(j+1+k).y-vec_down.at(j).y)==dst)
							offset_d=k;
					}
				}

				if(vec_up.at(j).x>=vec_left.at(i).x+step_x && vec_up.at(j).y+step_y<=vec_left.at(i).y)
				{
                    ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: in if(vec_up.at(j).x>=vec_left.at(i).x+step_x && vec_up.at(j).y+step_y<=vec_left.at(i).y)");
					//get c1
					dy=(vec_left.at(i+1+offset_l).y-vec_left.at(i).y);
					dx=(vec_left.at(i+1+offset_l).x-vec_left.at(i).x);
					m1=dy/(dx+0.0001);
					b1=(vec_left.at(i+1+offset_l).y-m1*vec_left.at(i+1+offset_l).x);

					dy=(vec_up.at(j+1+offset_u).y-vec_up.at(j).y);
					dx=(vec_up.at(j+1+offset_u).x-vec_up.at(j).x);
					m2=dy/(dx+0.0001);
					b2=(vec_up.at(j+1+offset_u).y-m2*vec_up.at(j+1+offset_u).x);

					x = (b2 - b1)/(m1 - m2 + 0.0001);
					y = (m1*x)+b1;

					if(x<0)
						x=0;
					if(y<0)
						y=0;
					if(x>=canny->image.cols)	
						x=canny->image.cols-1;
					if(y>=canny->image.rows)	
						y=canny->image.rows-1;

					f_c1=1;
					c1= cvPoint((int)x,(int)y);
					//if(SVP)
						//cv::line(original->image, cvPoint(vec_up.at(j).x,vec_up.at(j).y), cvPoint(vec_up.at(j+1+offset_u).x,vec_up.at(j+1+offset_u).y), CV_RGB(255,255,255), 2, 8, 0);	
				}

				if(vec_up.at(j+1+offset_u).x+step_x<=vec_right.at(i).x && vec_up.at(j+1+offset_u).y+step_y<=vec_right.at(i).y)
				{
                    ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: in if(vec_up.at(j+1+offset_u).x+step_x<=vec_right.at(i).x && vec_up.at(j+1+offset_u).y+step_y<=vec_right.at(i).y)");

					//get c2
					dy=(vec_right.at(i+1+offset_r).y-vec_right.at(i).y);
					dx=(vec_right.at(i+1+offset_r).x-vec_right.at(i).x);
					m1=dy/(dx+0.0001);
					b1=(vec_right.at(i+1+offset_r).y-m1*vec_right.at(i+1+offset_r).x);

					dy=(vec_up.at(j+1+offset_u).y-vec_up.at(j).y);
					dx=(vec_up.at(j+1+offset_u).x-vec_up.at(j).x);
					m2=dy/(dx+0.0001);
					b2=(vec_up.at(j+1+offset_u).y-m2*vec_up.at(j+1+offset_u).x);

					x = (b2 - b1)/(m1 - m2 + 0.0001);
					y = (m1*x)+b1;
	
					if(x<0)
						x=0;
					if(y<0)
						y=0;
					if(x>=canny->image.cols)	
						x=canny->image.cols-1;
					if(y>=canny->image.rows)	
						y=canny->image.rows-1;

					f_c2=1;
					c2= cvPoint((int)x,(int)y);
					//if(SVP)
						//cv::line(original->image, cvPoint(vec_left.at(i).x,vec_left.at(i).y), cvPoint(vec_left.at(i+1+offset_l).x,vec_left.at(i+1+offset_l).y), CV_RGB(255,255,255), 2, 8, 0);	
				}				

				if(vec_down.at(j+1+offset_d).x+step_x<=vec_right.at(i+1+offset_r).x && vec_down.at(j+1+offset_d).y>=vec_right.at(i+1+offset_r).y+step_y)
				{
                    ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: in if(vec_down.at(j+1+offset_d).x+step_x<=vec_right.at(i+1+offset_r).x && vec_down.at(j+1+offset_d).y>=vec_right.at(i+1+offset_r).y+step_y)");

					//get c3
					dy=(vec_right.at(i+1+offset_r).y-vec_right.at(i).y);
					dx=(vec_right.at(i+1+offset_r).x-vec_right.at(i).x);
					m1=dy/(dx+0.0001);
					b1=(vec_right.at(i+1+offset_r).y-m1*vec_right.at(i+1+offset_r).x);

					dy=(vec_down.at(j+1+offset_d).y-vec_down.at(j).y);
					dx=(vec_down.at(j+1+offset_d).x-vec_down.at(j).x);
					m2=dy/(dx+0.0001);
					b2=(vec_down.at(j+1+offset_d).y-m2*vec_down.at(j+1+offset_d).x);

					x = (b2 - b1)/(m1 - m2 + 0.0001);
					y = (m1*x)+b1;

					if(x<0)
						x=0;
					if(y<0)
						y=0;
					if(x>=canny->image.cols)	
						x=canny->image.cols-1;
					if(y>=canny->image.rows)	
						y=canny->image.rows-1;

					f_c3=1;
					c3= cvPoint((int)x,(int)y);
					//if(SVP)
						//cv::line(original->image, cvPoint(vec_down.at(j).x,vec_down.at(j).y), cvPoint(vec_down.at(j+1+offset_d).x,vec_down.at(j+1+offset_d).y), CV_RGB(255,255,255), 2, 8, 0);		
				}
				
				if(vec_down.at(j).x>=vec_left.at(i+1+offset_l).x+step_x && vec_down.at(j).y>=vec_left.at(i+1+offset_l).y+step_y)
				{
                    ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: in if(vec_down.at(j).x>=vec_left.at(i+1+offset_l).x+step_x && vec_down.at(j).y>=vec_left.at(i+1+offset_l).y+step_y)");

					//get c4
					dy=(vec_left.at(i+1+offset_l).y-vec_left.at(i).y);
					dx=(vec_left.at(i+1+offset_l).x-vec_left.at(i).x);
					m1=dy/(dx+0.0001);
					b1=(vec_left.at(i+1+offset_l).y-m1*vec_left.at(i+1+offset_l).x);

					dy=(vec_down.at(j+1+offset_d).y-vec_down.at(j).y);
					dx=(vec_down.at(j+1+offset_d).x-vec_down.at(j).x);
					m2=dy/(dx+0.0001);
					b2=(vec_down.at(j+1+offset_d).y-m2*vec_down.at(j+1+offset_d).x);

					x = (b2 - b1)/(m1 - m2 + 0.0001);
					y = (m1*x)+b1;

					if(x<0)
						x=0;
					if(y<0)
						y=0;
					if(x>=canny->image.cols)	
						x=canny->image.cols-1;
					if(y>=canny->image.rows)	
						y=canny->image.rows-1;

					c4= cvPoint((int)x,(int)y);
					f_c4=1;
					//if(SVP)
						//cv::line(original->image, cvPoint(vec_right.at(i).x,vec_right.at(i).y), cvPoint(vec_right.at(i+1+offset_r).x,vec_right.at(i+1+offset_r).y), CV_RGB(255,255,255), 2, 8, 0);	
				}
				
				if(f_c1*f_c2*f_c3*f_c4>0)
				{
                    ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: in if(f_c1*f_c2*f_c3*f_c4>0)");

					//distance between corners
					dst_up=sqrt((c2.x-c1.x)*(c2.x-c1.x)+(c2.y-c1.y)*(c2.y-c1.y));
					dst_right=sqrt((c3.x-c2.x)*(c3.x-c2.x)+(c3.y-c2.y)*(c3.y-c2.y));
					dst_down=sqrt((c4.x-c3.x)*(c4.x-c3.x)+(c4.y-c3.y)*(c4.y-c3.y));
					dst_left=sqrt((c4.x-c1.x)*(c4.x-c1.x)+(c4.y-c1.y)*(c4.y-c1.y));

					//compute angles between line pairs
					theta1 = AngleBetweenLines (c1, c2, c2, c3);
					theta2 = AngleBetweenLines (c2, c3, c4, c3);
					theta3 = AngleBetweenLines (c4, c3, c1, c4);
					theta4 = AngleBetweenLines (c1, c2, c1, c4);
		
					theta=min(min(theta1,theta2),min(theta3,theta4));
					dst_h=(dst_down+dst_up)/2;
					dst_v=(dst_left+dst_right)/2;

					cx_min=min(min(c1.x,c2.x),min(c3.x,c4.x));
					cx_max=max(max(c1.x,c2.x),max(c3.x,c4.x));
					cy_min=min(min(c1.y,c2.y),min(c3.y,c4.y));
					cy_max=max(max(c1.y,c2.y),max(c3.y,c4.y));

					if (cx_min<0)						
						cx_min=0;			if (cx_max<4)
											cx_max=4;
					if (cy_min<0)						
						cy_min=0;			if (cy_max<4)
											cy_max=4;
					if (cx_min>blobs->image.cols-5)						
						cx_min=blobs->image.cols-5;	if (cx_max>blobs->image.cols-1)
											cx_max=blobs->image.cols-1;
					if (cy_min>blobs->image.rows-5)						
						cy_min=blobs->image.rows-5;	if (cy_max>blobs->image.rows-1)
											cy_max=blobs->image.rows-1;
					roi_x=abs(cx_max-cx_min);
					roi_y=abs(cy_max-cy_min);
					door_x=(int)(cx_min+cx_max)/2;
					door_y=(int)(cy_min+cy_max)/2;

					if(door_x<0)
						door_x=0;
					if(door_y<0)
						door_y=0;
					if(door_x>=original->image.cols)	
						door_x=original->image.cols-1;
					if(door_y>=original->image.rows)	
						door_y=original->image.rows-1;
					
					point3D = cloud.at(door_x,door_y);
					meters = point3D.z;

					if(std::isnan(meters) || meters < 0.0 || meters > 5.0)
					{
                        ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: in if(std::isnan(meters) || meters < 0.0 || meters > 5.0)");
						meters=0;
						idx=0;
						if(roi_x>5 && roi_y>5)
						{
							for(int k = cx_min; k < cx_max; k++)
							{
								point3D = cloud.at(k,door_y);
								if(!std::isnan(point3D.z) && point3D.z>0.0 && point3D.z<5.0)
								{
									meters=meters+point3D.z;
									idx++;
								}
							}
							for(int k = cy_min; k < cy_max; k++)
							{
								point3D = cloud.at(door_x,k);							
								if(!std::isnan(point3D.z) && point3D.z>0.0 && point3D.z<5.0)
								{
									meters=meters+point3D.z;
									idx++;
								}
							}
						}

						if(idx==0)
							idx=1;
					
						meters=meters/idx;
					}
					
					//Check for sensor saturation
					sensor_range = meters>0.0 && !std::isnan(meters) && meters<5.0;

					if(!Range_filter)
						sensor_range =1;
			
					if(sensor_range)
					{
                        ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: in if(sensor_range)");

						min_dst_h=(min_door_width/meters);
						max_dst_h=(max_door_width/meters);
						min_dst_v=(min_door_height/meters);
						max_dst_v=(max_door_height/meters);

						r=roi_x/(roi_y+0.0001);

						if(cx_min <= 10 || cx_max >= blobs->image.cols-10)
						{
							min_dst_h=min_dst_h/2;
							aspect = (r>=0.4 && r<=0.8);	
						}
						if(cy_min <= 10 || cy_max >= blobs->image.rows-10)
						{
							min_dst_v=min_dst_v/3;
							aspect = (r>=0.4 && r<=1.5);
						}
						if(cx_min >= 10 && cx_max <= blobs->image.cols-10 && cy_min >= 10 && cy_max <= blobs->image.rows-10)
							aspect = (r>=0.4 && r<=0.8);
						if((cx_min <= 10 || cx_max >= blobs->image.cols-10) && (cy_min <= 10 || cy_max >= blobs->image.rows-10))
							aspect = (r>=0.4 && r<=1.5);
					
						//ROS_ERROR("vmin: %f, hmin: %f, hr: %f ",min_dst_h, dst_h, h_r);
					
						//filter false doors using physical constraints
						perspective = (abs(dst_up-dst_down)<roi_x/2 && abs(dst_left-dst_right)<roi_y/2 && theta>0.45);
						geometry = (c4.x<c3.x && c1.x<c2.x && c4.y>c1.y && c3.y>c2.y);
						size = (dst_h>min_dst_h && dst_h<max_dst_h && dst_v>min_dst_v && dst_v<max_dst_v && roi_x>5 && roi_y>5);
	 
						if(!Persp_filter)
							perspective=1; 
						if(!Geom_filter)
							geometry=1; 
						if(!Size_filter)
							size=1; 
						if(!Aspect_filter)
							aspect=1;
					
                        ROS_INFO_STREAM("!!!!!!!! ClosedDoorDetectorAlgNode::image_color_callback: checking if(aspect && perspective && geometry && size)");
						if(aspect && perspective && geometry && size)
						{	
                            ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: in if(aspect && perspective && geometry && size)");
							//cv::line(original->image, cvPoint(door_x,door_y), cvPoint(door_x,door_y), CV_RGB(255,0,0), 10, 8, 0);		
							//Initialize mask matrices with ROI dimensions
							cv::Mat area_mask, blobs_roi;
							area_mask = cv::Mat::zeros(blobs->image.rows, blobs->image.cols, CV_8UC1);

							//handle mask			
							c5=cvPoint((int)(c1.x+(c4.x-c1.x)*0.1),(int)(c1.y+(c4.y-c1.y)*0.1));
							c6=cvPoint((int)(c2.x+(c3.x-c2.x)*0.1),(int)(c2.y+(c3.y-c2.y)*0.1));
							c7=cvPoint((int)(c1.x+(c4.x-c1.x)*0.9),(int)(c1.y+(c4.y-c1.y)*0.9));
							c8=cvPoint((int)(c2.x+(c3.x-c2.x)*0.9),(int)(c2.y+(c3.y-c2.y)*0.9));
						
							//Horiztonal location of handle mask 
							c9=cvPoint((int)(c5.x+(c6.x-c5.x)*((float)handle_location/100)),(int)(c5.y+(c6.y-c5.y)*((float)handle_location/100)));
							c10=cvPoint((int)(c7.x+(c8.x-c7.x)*((float)handle_location/100)),(int)(c7.y+(c8.y-c7.y)*((float)handle_location/100)));
							c11=cvPoint((int)(c5.x+(c6.x-c5.x)*(1-((float)handle_location/100))),(int)(c5.y+(c6.y-c5.y)*(1-((float)handle_location/100))));
							c12=cvPoint((int)(c7.x+(c8.x-c7.x)*(1-((float)handle_location/100))),(int)(c7.y+(c8.y-c7.y)*(1-((float)handle_location/100))));
				
							h_r=max_dst_h*handle_width/100;
							v_r=max_dst_h*handle_height/100;
							handle_mask_width=max_dst_h/10;

							if(handle_mask_width < 1.0)
								handle_mask_width=1.0;

							//Draw handle mask
							if(c1.x > 10 || c4.x > 10)
						   		cv::line(area_mask, c9, c10, white, (int)handle_mask_width, 8, 0);
							if(c2.x < area_mask.cols-10 || c3.x < area_mask.cols-10)
						  		cv::line(area_mask, c11, c12, white, (int)handle_mask_width, 8, 0);
						
							if(SHM)
							{
								if(c1.x > 10 || c4.x > 10)
						   			cv::line(original->image, c9, c10, white, (int)handle_mask_width, 8, 0);
								if(c2.x < area_mask.cols-10 || c3.x < area_mask.cols-10)
						  			cv::line(original->image, c11, c12, white, (int)handle_mask_width, 8, 0);
							}


							handle_x=0;
							handle_y=0;
							area=100000;
                            int blobnum = 0;
							// "blobs" is the list of blobs, result of the "cvLabel" call at the beginning of the algorithm.
							for (cvb::CvBlobs::const_iterator it=CVblobs.begin(); it!=CVblobs.end(); ++it)
							{
                                blobnum++;
                                //ROS_INFO_STREAM(" WOOOOHAAA DOING BLOBS STUFF!!   blob: " << blobnum);
								cvb::CvBlob *blob=it->second;
								blob->area=(blob->maxx-blob->minx)*(blob->maxy-blob->miny);
                                ROS_INFO_STREAM(" WOOOOHAAA DOING BLOBS STUFF!!   blob: " << blobnum << " with area: " << blob->area << " that should be bigger than " << (v_r*h_r*0.2) << " and shorter than " << (v_r*h_r*2.0) << " with v_r= " << v_r << " and h_r=" << h_r << " and max_dst_h=" << max_dst_h );
								if (blob->area < (v_r*h_r*2.0) && blob->area > (v_r*h_r*0.2) && blob->maxx-blob->minx < h_r*1.4 && blob->maxx-blob->minx > h_r*0.3 && blob->maxy-blob->miny < v_r*1.4 && blob->maxy-blob->miny > v_r*0.3 && area_mask.data[(int)blob->centroid.y*area_mask.cols+(int)blob->centroid.x]>0)
								{
                                    ROS_INFO_STREAM(" WOOOOHAAA DOING BLOBS STUFF!!   this blob is awesome, lets see if we use it");
									//ROS_ERROR("x: %d",(int)blob->centroid.x);
									if(abs(blob->area-v_r*h_r) < area)
									{
                                        ROS_INFO_STREAM(" WOOOOHAAA DOING BLOBS STUFF!!  BEST BLOB EVER!!!!! ONE OENEOENEJE");
										handle_x=(int)(blob->centroid.x);
										handle_y=(int)(blob->centroid.y);
										handle_minx=blob->minx;
										handle_maxx=blob->maxx;
										handle_miny=blob->miny;
										handle_maxy=blob->maxy;
										area=abs(blob->area-v_r*h_r);
										cv::rectangle(blob_mat, cvPoint(blob->minx,blob->miny), cvPoint(blob->maxx,blob->maxy), CV_RGB(150,150,150), 2, 8, 0);
									}
								}
							}

                            ROS_INFO_STREAM("?????? ClosedDoorDetectorAlgNode::image_color_callback: if(handle_x>30 && handle_y>30 && handle_x<original->image.cols-30 && handle_y<original->image.rows-30) ");
                            ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: handle_x= " << handle_x << " handle_y= " << handle_y << " original->image.cols= " << original->image.cols << " original->image.rows= " << original->image.rows);
                            if(handle_x>30 && handle_y>30 && handle_x<original->image.cols-30 && handle_y<original->image.rows-30)
							{								
								cv::line(area_mask, cvPoint(handle_x,handle_y), cvPoint(handle_x,handle_y), CV_RGB(100,100,100), h_r*1.3, 8, 0);		
								flat=1;
								//horizontal flatness test
								i_min=cy_min; i_max=cy_max; k_min=cx_min; k_max=cx_max;

								//if(i_max > i_min+(int)(roi_x/5))
								for (int i = i_min; i < i_max; i=i+(int)((i_max-i_min)/5))
							    	{  
									point=0;
									for(int k = k_min; k < k_max; k=k+3)
									{   	
										if (k>(int)(cx_min+cx_max)/2 && area_mask.data[i*area_mask.cols+k]!=255)
											point=0;

										if(area_mask.data[i*area_mask.cols+k]==255)
										{
											if(!std::isnan(cloud.at(k,i).z) && cloud.at(k,i).z>0.0 && cloud.at(k,i).z<5.0)
											{
												if(point==1)
												{
													point3D = cloud.at(k,i);

													if(SFT)
													cv::line(original->image, cvPoint(k,i), cvPoint(k,i), black, 1, 8, 0);
													if(abs(point3D.z-offsetPoint3D.z)>0.15)
													{
														flat=0;
														cv::line(original->image, cvPoint(k,i), cvPoint(k,i), CV_RGB(0,255,0), 5, 8, 0);
													}
												}
												offsetPoint3D = cloud.at(k,i);
												point=1;
											}
										}
									}   
							    	}
							
								//vertical flatness test
								i_min=cy_min; i_max=cy_max; k_min=cx_min; k_max=cx_max;

								//if(i_max > i_min+(int)(roi_x/5))
								for (int k = k_min; k < k_max; k=k+(int)((k_max-k_min)/10))
							    	{  
									point=0;
									for(int i = i_min; i < i_max; i=i+3)
									{   	
										if (area_mask.data[i*area_mask.cols+k]!=255)
											point=0;

										if(area_mask.data[i*area_mask.cols+k]==255)
										{
											if(!std::isnan(cloud.at(k,i).z) && cloud.at(k,i).z>0.0 && cloud.at(k,i).z<5.0)
											{
												if(point==1)
												{
													point3D = cloud.at(k,i);

													if(SFT)
													cv::line(original->image, cvPoint(k,i), cvPoint(k,i), black, 1, 8, 0);
													if(abs(point3D.z-offsetPoint3D.z)>0.15)
													{
														flat=0;
														cv::line(original->image, cvPoint(k,i), cvPoint(k,i), CV_RGB(0,255,0), 5, 8, 0);
													}
												}
												offsetPoint3D = cloud.at(k,i);
												point=1;
											}
										}
									}   
							    	}

                                ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: flat is: " << std::to_string( flat ));
								if(flat==1)
								{
									//cv::line(original->image, cvPoint(handle_x,handle_y), cvPoint(handle_x,handle_y), CV_RGB(255,0,0), 10);
									if(debugging_images==1)
									DrawRect (blob_mat, c1, c2, c3, c4, CV_RGB(150,150,150), 2, 0);	
									if(debugging_images==1)
									cv::rectangle(original->image, cvPoint(handle_minx,handle_miny), cvPoint(handle_maxx,handle_maxy), CV_RGB(150,150,150), 2, 8, 0);
										
									x_i=0;
									y_i=0;
									z_i=0;
									compCount=0;

									for(int k = handle_miny; k < handle_maxy; k++)
									{
										for(int i = handle_minx; i < handle_maxx; i++)
										{
											point3D = cloud.at(i,k);
											if(!std::isnan(point3D.z) && point3D.z>0.0 && point3D.z<5.0)
											{
												x_i=point3D.x+x_i;
												y_i=point3D.y+y_i;
												z_i=point3D.z+z_i;
												compCount++;
											}
										}
									}
									
									x_i=x_i/(float)compCount;
									y_i=y_i/(float)compCount;
									z_i=z_i/(float)compCount;

									//prepare locations of the selected door frames	for the output message	
                                    ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: _____  ss_door_centroid pushed point");
									ss_door_centroid.push_back(cvPoint(door_x,door_y));
									ss_handle.push_back(cvPoint(handle_x,handle_y));
									ss_handle_x.push_back(x_i);
									ss_handle_y.push_back(y_i);
									ss_handle_z.push_back(z_i);
									ss_c1.push_back(c1);
									ss_c2.push_back(c2);
									ss_c3.push_back(c3);
									ss_c4.push_back(c4);
								}
							}
							
							handle_y=0;
							handle_x=0;						
						}
					}	
				}
			}
		}
	}

    ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: 7");

	if (ss_door_centroid.size()>0)
	{
        ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: ss_door_centroid.size() > 0 !");

		b_door_centroid=cvPoint(0,0);
		b_handle=cvPoint(0,0);
		b_handle_x=0;
		b_handle_y=0;
		b_handle_z=0;
		b_c1=cvPoint(0,0);
		b_c2=cvPoint(0,0);
		b_c3=cvPoint(0,0);
		b_c4=cvPoint(0,0);

		for (size_t i=0; i<ss_door_centroid.size(); i++)
		{
			b_door_centroid.x=(int)(b_door_centroid.x+ss_door_centroid.at(i).x);
			b_door_centroid.y=(int)(b_door_centroid.y+ss_door_centroid.at(i).y);
			b_handle.x=(int)(b_handle.x+ss_handle.at(i).x);
			b_handle.y=(int)(b_handle.y+ss_handle.at(i).y);
			b_handle_x=(b_handle_x+ss_handle_x.at(i));
			b_handle_y=(b_handle_y+ss_handle_y.at(i));
			b_handle_z=(b_handle_z+ss_handle_z.at(i));
			b_c1.x=(int)(b_c1.x+ss_c1.at(i).x);
			b_c1.y=(int)(b_c1.y+ss_c1.at(i).y);
			b_c2.x=(int)(b_c2.x+ss_c2.at(i).x);
			b_c2.y=(int)(b_c2.y+ss_c2.at(i).y);
			b_c3.x=(int)(b_c3.x+ss_c3.at(i).x);
			b_c3.y=(int)(b_c3.y+ss_c3.at(i).y);
			b_c4.x=(int)(b_c4.x+ss_c4.at(i).x);
			b_c4.y=(int)(b_c4.y+ss_c4.at(i).y);
		}
		b_door_centroid.x=(int)(b_door_centroid.x/ss_door_centroid.size());
		b_door_centroid.y=(int)(b_door_centroid.y/ss_door_centroid.size());
		b_handle.x=(int)(b_handle.x/ss_door_centroid.size());
		b_handle.y=(int)(b_handle.y/ss_door_centroid.size());
		b_handle_x=(b_handle_x/ss_door_centroid.size());
		b_handle_y=(b_handle_y/ss_door_centroid.size());
		b_handle_z=(b_handle_z/ss_door_centroid.size());
		b_c1.x=(int)(b_c1.x/ss_door_centroid.size());
		b_c1.y=(int)(b_c1.y/ss_door_centroid.size());
		b_c2.x=(int)(b_c2.x/ss_door_centroid.size());
		b_c2.y=(int)(b_c2.y/ss_door_centroid.size());
		b_c3.x=(int)(b_c3.x/ss_door_centroid.size());
		b_c3.y=(int)(b_c3.y/ss_door_centroid.size());
		b_c4.x=(int)(b_c4.x/ss_door_centroid.size());
		b_c4.y=(int)(b_c4.y/ss_door_centroid.size());

		if(s_handle.x>0 && s_handle.y>0)
		{
			dx=abs(b_handle.x-s_handle.x);
			dy=abs(b_handle.y-s_handle.y);
			dst=sqrt(dx*dx+dy*dy);
		
			if(dst<min_dst_h/4)
				support++;
		}
		if(s_handle.x==0 && s_handle.y==0)
			dst=max_dst_h/4;
		
		s_handle.x=b_handle.x;
		s_handle.y=b_handle.y;
	}
	
	if(ss_door_centroid.size()==0)
		support--;
	if(support < 0)
	{
		support=0;
		s_handle.x=0;
		s_handle.y=0;
	}

	if(support >10)
		support=10;	

    ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: ss_door_centroid.size()>0: " << std::to_string( ss_door_centroid.size()>0) );
    ROS_INFO_STREAM("ClosedDoorDetectorAlgNode::image_color_callback: dst<max_dst_h/4: " << std::to_string( dst<max_dst_h/4) );
	if(ss_door_centroid.size()>0 && dst<max_dst_h/4)
	{
        ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: inside if(ss_door_centroid.size()>0 && dst<max_dst_h/4)");
		x=b_handle_x;
		y=b_handle_y;
		z=b_handle_z;

		//ROS_ERROR("boundaries loop!");
		
		if(!std::isnan(z) && z > 0.0 && z < 5.0)
		{
            ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: inside if(!std::isnan(z) && z > 0.0 && z < 5.0)");
			if(debugging_images==1)
			DrawRect (original->image, b_c1, b_c2, b_c3, b_c4, CV_RGB(255,255,0), 2, 0);

			std::ostringstream zd;
			zd << b_handle_z ;
		
			if(debugging_images==1)
			cv::line(original->image, b_handle, b_handle, CV_RGB(0,0,255), 10, 8, 0);

			if(b_handle.x+10>0 && b_handle.y+25>0 && b_handle.x+10<original->image.cols-50 && b_handle.y+25<original->image.rows-25)
			{
				if(debugging_images==1)
				putText(original->image, zd.str(), cvPoint(b_handle.x+10,b_handle.y+25), cv::FONT_HERSHEY_SIMPLEX, 0.7, white,3);
			}


			poses.pose.position.x = x;
			poses.pose.position.y = y;
			poses.pose.position.z = z;

			poses.pose.orientation.w = 0.0;

			if(b_door_centroid.x > b_handle.x)
				poses.pose.orientation.w = -1.0; //left handle
			if(b_door_centroid.x < b_handle.x)
				poses.pose.orientation.w = 1.0; //right handle

			door_handle_publisher_.publish(poses);
			b_handle_z=b_handle_z*1000;
			
			door_coordinates.data.clear();
			door_coordinates.data.push_back(b_c1.x);
			door_coordinates.data.push_back(b_c1.y);
			door_coordinates.data.push_back(b_c2.x);
			door_coordinates.data.push_back(b_c2.y);
			door_coordinates.data.push_back(b_c3.x);
			door_coordinates.data.push_back(b_c3.y);
			door_coordinates.data.push_back(b_c4.x);
			door_coordinates.data.push_back(b_c4.y);	
			door_coordinates.data.push_back(b_handle.x);
			door_coordinates.data.push_back(b_handle.y);
			door_coordinates.data.push_back((int)b_handle_z);
			door_coordinates.data.push_back(poses.pose.orientation.w);

			closed_door_coordinates_publisher_.publish(door_coordinates);
		}
	}

    ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: 8");

	point3D = cloud.at((int)(original->image.cols/2),(int)(original->image.rows/2));
	sensor_range= !std::isnan(point3D.z) && point3D.z>0.0 && point3D.z<5.0;
	if(sensor_range)
	{
		min_dst_h=(min_door_width/point3D.z);
		max_dst_h=(max_door_width/point3D.z);
		min_dst_v=(min_door_height/point3D.z);
		max_dst_v=(max_door_height/point3D.z);
	}

	if(DSC)
 		DoorSizeCalibration (original->image, min_dst_h, max_dst_h, min_dst_v, max_dst_v, handle_width, handle_height);	
	if(debugging_images==2)
		original->image = blob_mat*0.5 + original->image*0.5;	
	if(debugging_images==3)
		original->image = canny->image;
	if(debugging_images==4)
		original->image = wshed;
	if(debugging_images==5)
		original->image = gradient->image;

	if(debugging_images!=0)
	{
		cv::imshow(WINDOW_1, original->image);
		//cvMoveWindow(WINDOW_1, 0, 0);
		cv::waitKey(3);
	}
  }

  ROS_INFO("ClosedDoorDetectorAlgNode::image_color_callback: 9");

  captured_depth = 0;

  //unlock previously blocked shared variables 
  //this->alg_.unlock();
  this->image_color_mutex_.exit(); 
}

/*  [service callbacks] */

/*  [action callbacks] */

/*  [action requests] */

void ClosedDoorDetectorAlgNode::node_config_update(Config &config, uint32_t level)
{
  this->alg_.lock();

	this->allowed_blobs = config.allowed_blobs;
	this->segment_fidelity = config.segment_fidelity;
	this->segment_size = config.segment_size;
	this->min_door_width = config.min_door_width;
	this->max_door_width = config.max_door_width;
	this->min_door_height = config.min_door_height;
	this->max_door_height = config.max_door_height;
	this->handle_width = config.handle_width;
	this->handle_height = config.handle_height;
	this->handle_location = config.handle_location;
	this->debugging_images = config.debugging_images;
	this->no_simulator = config.no_simulator;
	this->DSC = config.DSC;
	this->SHM = config.SHM;
	this->SVP = config.SVP;
	this->SFT = config.SFT;
	this->Range_filter = config.Range_filter;
	this->Persp_filter = config.Persp_filter;
	this->Geom_filter = config.Geom_filter ;
	this->Size_filter = config.Size_filter ;
	this->Aspect_filter = config.Aspect_filter;

  this->alg_.unlock();
}

void ClosedDoorDetectorAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<ClosedDoorDetectorAlgNode>(argc, argv, "closed_door_detector_alg_node");
}

/* algorithm functions */
void ClosedDoorDetectorAlgNode::DoorSizeCalibration (cv::Mat inputImage, double min_dst_h, double max_dst_h, double min_dst_v, double max_dst_v, int handle_width, int handle_height)
{	

	//Smallest door frame allowed
	c1= cvPoint((inputImage.cols/2)-(min_dst_h/2), (inputImage.rows/2)-(min_dst_v/2));
	c2= cvPoint((inputImage.cols/2)+(min_dst_h/2), (inputImage.rows/2)-(min_dst_v/2));
	c3= cvPoint((inputImage.cols/2)+(min_dst_h/2), (inputImage.rows/2)+(min_dst_v/2));
	c4= cvPoint((inputImage.cols/2)-(min_dst_h/2), (inputImage.rows/2)+(min_dst_v/2));
	
	DrawRect (inputImage, c1, c2, c3, c4, CV_RGB(255,0,0), 2, 0);

	//Biggest door frame allowed
	c1= cvPoint((inputImage.cols/2)-(max_dst_h/2), (inputImage.rows/2)-(max_dst_v/2));
	c2= cvPoint((inputImage.cols/2)+(max_dst_h/2), (inputImage.rows/2)-(max_dst_v/2));
	c3= cvPoint((inputImage.cols/2)+(max_dst_h/2), (inputImage.rows/2)+(max_dst_v/2));
	c4= cvPoint((inputImage.cols/2)-(max_dst_h/2), (inputImage.rows/2)+(max_dst_v/2));
	
	DrawRect (inputImage, c1, c2, c3, c4, CV_RGB(255,0,0), 2, 0);
	
	//Expected handle size
	c1= cvPoint((inputImage.cols/2)-(max_dst_h*handle_width)/200, (inputImage.rows/2)-(max_dst_h*handle_height)/200);
	c2= cvPoint((inputImage.cols/2)+(max_dst_h*handle_width)/200, (inputImage.rows/2)-(max_dst_h*handle_height)/200);
	c3= cvPoint((inputImage.cols/2)+(max_dst_h*handle_width)/200, (inputImage.rows/2)+(max_dst_h*handle_height)/200);
	c4= cvPoint((inputImage.cols/2)-(max_dst_h*handle_width)/200, (inputImage.rows/2)+(max_dst_h*handle_height)/200);

	DrawRect (inputImage, c1, c2, c3, c4, CV_RGB(0,255,0), 2, 0);
}

void ClosedDoorDetectorAlgNode::DrawRect (cv::Mat inputImage, cv::Point q1, cv::Point q2, cv::Point q3, cv::Point q4, cv::Scalar color, int lineSize, int filled)
{	
	if(filled==0)
	{
		cv::line(inputImage, q1, q2, color, lineSize);
		cv::line(inputImage, q2, q3, color, lineSize);
		cv::line(inputImage, q3, q4, color, lineSize);
		cv::line(inputImage, q4, q1, color, lineSize);
	}

	if(filled==1)
	{
		std::vector<cv::Point> pts;
		pts.push_back(q1);
		pts.push_back(q2);
		pts.push_back(q3);
		pts.push_back(q4);
	
		cv::Point *pP = new cv::Point[pts.size()];
		std::copy(pts.begin(), pts.end(), pP);
		fillConvexPoly(inputImage, pP, 4, color);
	}
}

double ClosedDoorDetectorAlgNode::AngleBetweenLines (cv::Point point1, cv::Point point2, cv::Point point3, cv::Point point4)
{	
	double m1, m2, dx, dy;

	dy=point2.y-point1.y;
	dx=point2.y-point1.y;
	m1=dy/(dx+0.0001);
	dy=point4.y-point3.y;
	dx=point4.x-point3.x;
	m2=dy/(dx+0.0001);

	double theta=abs(atan((m2-m1)/(1.0001+m1*m2)));
	
	return theta;
}

