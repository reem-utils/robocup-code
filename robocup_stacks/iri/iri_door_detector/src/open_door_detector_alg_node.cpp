#include "open_door_detector_alg_node.h"

using namespace std;
namespace enc = sensor_msgs::image_encodings;

static const char WINDOW_1[] = "Depth Image";
static const char WINDOW_2[] = "Open Door Detector";

OpenDoorDetectorAlgNode::OpenDoorDetectorAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<OpenDoorDetectorAlgorithm>()
{
  //init class attributes if necessary
  //this->loop_rate_ = 2;//in [Hz]

  // [init publishers]
  this->door_centroid_publisher_ = this->public_node_handle_.advertise<geometry_msgs::PoseStamped>("door_centroid", 1);
  this->open_door_coordinates_publisher_ = this->public_node_handle_.advertise<std_msgs::Int32MultiArray>("open_door_coordinates", 1);
  
  // [init subscribers]
  //if (!no_simulator)
  this->door_action_start_subscriber_ = this->public_node_handle_.subscribe("/iri_door_detector/door_detector_actions/door_action_start", 1, &OpenDoorDetectorAlgNode::door_action_start_callback, this);


  // [init services]
  
  // [init clients]
  
  // [init action servers]
  
  // [init action clients]

  // [init algorithm variables]
  min_range = 0.5;
  max_range = 5.5;

  frame_left=0;
  frame_right=0;
  frame_up=0;

  start=0;
  captured_depth = 0;
  support=15;
  distance_to_room=0.7;

  white = CV_RGB(255,255,255);
  black = CV_RGB(0,0,0);
}

OpenDoorDetectorAlgNode::~OpenDoorDetectorAlgNode(void)
{
  // [free dynamic memory]
}

void OpenDoorDetectorAlgNode::mainNodeThread(void)
{
  // [fill msg structures]
  //this->Marker_msg_.data = my_var;
  //this->PoseStamped_msg_.data = my_var;
  
  // [fill srv structure and make request to the server]
  
  // [fill action structure and make request to the action server]

  // [publish messages]
  //this->door_centroid_publisher_.publish(poses);
}

/*  [subscriber callbacks] */
void OpenDoorDetectorAlgNode::door_action_start_callback(const std_msgs::Int8::ConstPtr& action_start) 
{ 
  //ROS_INFO("OpenDoorDetectorAlgNode::door_action_start_callback: New Message Received"); 

  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->door_action_start_mutex_.enter(); 

  start=action_start->data;

  if (start==0)
  {
  	image_color_subscriber_.shutdown();
	points_subscriber_.shutdown();
	//cvDestroyWindow("Open Door Detector");
  }
  if (start==1)
  {  
	  this->points_subscriber_ = this->public_node_handle_.subscribe("/camera/depth/points", 1, &OpenDoorDetectorAlgNode::points_callback, this);
	  this->image_color_subscriber_ = this->public_node_handle_.subscribe("/camera/rgb/image_color", 1, &OpenDoorDetectorAlgNode::image_color_callback, this);
  }

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->door_action_start_mutex_.exit(); 
}
void OpenDoorDetectorAlgNode::image_color_callback(const sensor_msgs::Image::ConstPtr& image_color) 
{ 
  //ROS_INFO("OpenDoorDetectorAlgNode::image_color_callback: New Message Received"); 
 
  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->image_color_mutex_.enter(); 
  
  if(captured_depth==0)
  {
	  try
	  {
		//Always copy, returning a mutable CvImage. OpenCV expects color images to use BGR channel order.
		original = cv_bridge::toCvCopy(image_color, enc::BGR8);					
	  }
	  catch (cv_bridge::Exception& e)
	  {
		//if there is an error during conversion, display it
		ROS_ERROR("Error while capturing color image: %s", e.what());
		return;
	  } 
  }

  captured_depth=1; 

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->image_color_mutex_.exit(); 
}
void OpenDoorDetectorAlgNode::points_callback(const sensor_msgs::PointCloud2::ConstPtr& points) 
{ 
  //ROS_INFO("OpenDoorDetectorAlgNode::depth_image_callback: New Message Received"); 

  //use appropiate mutex to shared variables if necessary 
  //this->alg_.lock(); 
  this->points_mutex_.enter(); 

  if(captured_depth==1)
  {	      
	pcl::fromROSMsg (*points, cloud);

	cv:: Mat depth (original->image.rows, original->image.cols, CV_8UC1);	
	
    	// convert to something visible
    	for(int i = 0; i < original->image.rows; i++)
    	{
        	Ii = depth.ptr<char>(i);
        	for(int j = 0; j < original->image.cols; j++)
        	{   
			point3D = cloud.at(j,i);
            		Ii[j] = (char) (255*((point3D.z-min_range)/(max_range-min_range)));
        	}   
    	}
	//cv::Canny(depth, depth, 50, 50, 3, true);

	step_x=original->image.cols/20;
	step_y=original->image.rows/20;

	vec_up.clear();
	vec_down.clear();
	vec_left.clear();
	vec_right.clear();
	vec_start=0;
	vec_end=0;
	
	//look for vertical door frames (left to right)
	for(int i = 1; i < original->image.rows; i=i+step_y)
    	{
		p_set=0;
		point=0; 
        	for(int j = 1; j < original->image.cols; j++)
        	{
			//cv::line(depth, cvPoint(j,i), cvPoint(j,i), CV_RGB(0,0,0), 3, 8, 0); 
			if(point==-1 && cloud.at(j,i).z>=left_depth+distance_to_room && !std::isnan(cloud.at(j,i).z) && cloud.at(j,i).z>0.0 && cloud.at(j,i).z<5.0)
			{							
				for(int k = 1; k < j; k++)
				{ 
					if(!std::isnan(cloud.at(k,i).z) && cloud.at(k,i).z>0.0 && cloud.at(k,i).z<5.0)
					{
						if(k<=j-50)
						{
							x_left=cloud.at(k,i).x;
							frame_left=cloud.at(k,i).z;
						}
						if(k<=j-30)
						{
							x_right=cloud.at(k,i).x;
							frame_right=cloud.at(k,i).z;
						}
					}
				}
				dy=frame_right-frame_left;
				dx=x_right-x_left;
				if(dx!=0)
				{
					m1=dy/dx;
					b1=frame_left-m1*x_left;

					for(int k=j; k<original->image.cols-1; k++)
					{
						if(!std::isnan(cloud.at(k,i).z) && cloud.at(k,i).z>0.0 && cloud.at(k,i).z<5.0)
						{
							dst=abs(m1*cloud.at(k,i).x-cloud.at(k,i).z+b1)/sqrt(m1*m1+1);
							meters= (left_depth+cloud.at(k,i).z)/2;
							max_dst_h=max_x/meters;
							min_dst_h=min_x/meters;
							if(dst<0.1 && abs(k-frame_x)<max_dst_h && abs(k-frame_x)>min_dst_h && abs(left_depth-cloud.at(k,i).z)<0.8) 
							{
								if(SVP)
								{cv::line(depth, cvPoint(frame_x,i), cvPoint(frame_x,i), white, 10, 8, 0);
								cv::line(depth, cvPoint(k,i), cvPoint(k,i), black, 10, 8, 0);}
								vec_right.push_back(cvPoint(k,i));
								vec_left.push_back(cvPoint(frame_x,i));
								vec_end++;
								point=0;
								break;
							}
							if(point==1 && cloud.at(k,i).z<prev_depth-distance_to_room && abs(left_depth-cloud.at(k,i).z)<0.8)
							{
								if(SVP)
								{cv::line(depth, cvPoint(frame_x,i), cvPoint(frame_x,i), white, 10, 8, 0);
								cv::line(depth, cvPoint(k,i), cvPoint(k,i), black, 10, 8, 0);}
								vec_right.push_back(cvPoint(k,i));
								vec_left.push_back(cvPoint(frame_x,i));
								vec_end++;
								point=0;
								break;
							}
							prev_depth=cloud.at(k,i).z;
							point=1;
						}
					}
				}
			}
			if(point!=1 && !std::isnan(cloud.at(j,i).z) && cloud.at(j,i).z>0.0 && cloud.at(j,i).z<5.0)
			{
				//cv::line(depth, cvPoint(j,i), cvPoint(j,i), CV_RGB(0,0,0), 10, 8, 0);
				frame_x=j;
				left_depth=cloud.at(j,i).z;
				point=-1;
			}
			/*if(j==original->image.cols-1 && p_set==0)
			{
				if(SVP)
				{cv::line(depth, cvPoint(original->image.cols-1,i), cvPoint(original->image.cols-1,i), white, 10, 8, 0);
				cv::line(depth, cvPoint(1,i), cvPoint(1,i), black, 10, 8, 0);}
				vec_left.push_back(cvPoint(original->image.cols-1,i));
				vec_right.push_back(cvPoint(1,i));
				vec_end++;
			}*/
        	}   
    	}
	

	//look for vertical door frames (right to left)
	for(int i = 1; i < original->image.rows; i=i+step_y)
    	{
		p_set=0;
		point=0; 
        	for(int j = original->image.cols-1; j > 1; j--)
        	{
			//cv::line(depth, cvPoint(j,i), cvPoint(j,i), CV_RGB(0,0,0), 3, 8, 0); 
			if(point==-1 && cloud.at(j,i).z>=right_depth+distance_to_room && !std::isnan(cloud.at(j,i).z) && cloud.at(j,i).z>0.0 && cloud.at(j,i).z<5.0)
			{							
				for(int k = original->image.cols-1; k > j; k--)
				{ 
					if(!std::isnan(cloud.at(k,i).z) && cloud.at(k,i).z>0.0 && cloud.at(k,i).z<5.0)
					{
						if(k>=j+50)
						{
							x_right=cloud.at(k,i).x;
							frame_right=cloud.at(k,i).z;
						}
						if(k>=j+30)
						{
							x_left=cloud.at(k,i).x;
							frame_left=cloud.at(k,i).z;
						}
					}
				}
				dy=frame_right-frame_left;
				dx=x_right-x_left;
				if(dx!=0)
				{
					m1=dy/dx;
					b1=frame_right-m1*x_right;

					for(int k=j; k>1; k--)
					{
						if(!std::isnan(cloud.at(k,i).z) && cloud.at(k,i).z>0.0 && cloud.at(k,i).z<5.0)
						{
							dst=abs(m1*cloud.at(k,i).x-cloud.at(k,i).z+b1)/sqrt(m1*m1+1);
							meters= (right_depth+cloud.at(k,i).z)/2;
							max_dst_h=max_x/meters;
							min_dst_h=min_x/meters;
							if(dst<0.1 && abs(k-frame_x)<max_dst_h && abs(k-frame_x)>min_dst_h && abs(right_depth-cloud.at(k,i).z)<0.8) 
							{
								if(SVP)
								{cv::line(depth, cvPoint(frame_x,i), cvPoint(frame_x,i), black, 10, 8, 0);
								cv::line(depth, cvPoint(k,i), cvPoint(k,i), white, 10, 8, 0);}
								vec_left.push_back(cvPoint(k,i));
								vec_right.push_back(cvPoint(frame_x,i));
								point=0;
								break;
							}
							if (point==1 && cloud.at(k,i).z<prev_depth-distance_to_room && abs(right_depth-cloud.at(k,i).z)<0.8)
							{
								if(SVP)
								{cv::line(depth, cvPoint(frame_x,i), cvPoint(frame_x,i), black, 10, 8, 0);
								cv::line(depth, cvPoint(k,i), cvPoint(k,i), white, 10, 8, 0);}
								vec_left.push_back(cvPoint(k,i));
								vec_right.push_back(cvPoint(frame_x,i));
								point=0;
								break;
							}
							prev_depth=cloud.at(k,i).z;
							point=1;
						}
					}
				}
			}
			if(point!=1 && !std::isnan(cloud.at(j,i).z) && cloud.at(j,i).z>0.0 && cloud.at(j,i).z<5.0)
			{
				//cv::line(depth, cvPoint(j,i), cvPoint(j,i), CV_RGB(0,0,0), 10, 8, 0);
				frame_x=j;
				right_depth=cloud.at(j,i).z;
				point=-1;
			}
			/*if(j==original->image.cols-1 && p_set==0)
			{
				if(SVP)
				{cv::line(depth, cvPoint(original->image.cols-1,i), cvPoint(original->image.cols-1,i), white, 10, 8, 0);
				cv::line(depth, cvPoint(1,i), cvPoint(1,i), black, 10, 8, 0);}
				vec_left.push_back(cvPoint(original->image.cols-1,i));
				vec_right.push_back(cvPoint(1,i));
				vec_end++;
			}*/
        	}   
    	}
	
	//look for horizontal door frames
	for(int j = 1; j < original->image.cols; j=j+step_x)
    	{  
		p_set=0;
		point=0;
                frame_y=10;
        	for(int i = 10; i < original->image.rows; i++)
        	{   

			meters= (cloud.at(j,(int)frame_y).z+cloud.at(j,i).z)/2;
			min_dst_v=(min_y/meters);

			//cv::line(depth, cvPoint(j,i), cvPoint(j,i), CV_RGB(0,0,0), 3, 8, 0);
			if((abs(cloud.at(j,i).z-frame_up)<0.1 && point==1 && !std::isnan(cloud.at(j,i).z) && abs(i-frame_y)>min_dst_v) || (i==original->image.rows-1 && point==1))
			{
				if(SVP)
				{cv::line(depth, cvPoint(j,frame_y), cvPoint(j,frame_y), white, 10, 8, 0);
				cv::line(depth, cvPoint(j,i), cvPoint(j,i), black, 10, 8, 0);}
				vec_up.push_back(cvPoint(j,frame_y));
				vec_down.push_back(cvPoint(j,i));
				frame_up=0;
				point=0;
				p_set=1;
			}
			if(cloud.at(j,i).z>=cloud.at(j,i-10).z+distance_to_room && point==0 && !std::isnan(cloud.at(j,i).z) && !std::isnan(cloud.at(j,i-10).z))
			{
				//cv::line(depth, cvPoint(j,i), cvPoint(j,i), CV_RGB(255,255,255), 10, 8, 0);
				frame_up=cloud.at(j,i-10).z;
				frame_y=i;
				point=1;
			}
			if(i==original->image.rows-1 && p_set==0)
			{
				if(SVP)
				{cv::line(depth, cvPoint(j,0), cvPoint(j,0), white, 10, 8, 0);
				cv::line(depth, cvPoint(j,original->image.rows-1), cvPoint(j,original->image.rows-1), black, 10, 8, 0);}
				vec_up.push_back(cvPoint(j,0));
				vec_down.push_back(cvPoint(j,original->image.rows-1));
			}
        	}
    	}
	
	ss_door_centroid.clear();
	ss_depth.clear();
	ss_c1.clear();
	ss_c2.clear();
	ss_c3.clear();
	ss_c4.clear();
	if(vec_end==0)
		vec_end=vec_left.size();

	if(min(min(vec_left.size(),vec_right.size()),min(vec_up.size(),vec_down.size()))>0)
	{
		for (size_t i=0; i<vec_end-1; i++)
		{
			//after left to right sweep, analyze right to left sweep
			if(i==vec_end-2 && i < vec_left.size()-1)
			{
				vec_end=vec_left.size();
				if(i+2<vec_end-1)
					i=i+2;		
			}
			for (size_t j=0; j<min(vec_up.size(),vec_down.size())-1; j++)
			{
				f_c1=0;
				f_c2=0;
				f_c3=0;
				f_c4=0;
				
				//look for the next left marker which is nearest to left marker i
				check=0;
				offset_l=0;
				dst=original->image.cols*2;
				while(check==0)
				{
					while(vec_left.at(i+1+offset_l).y==vec_left.at(i).y)
					{
						offset_l++;
						if(i+1+offset_l>vec_end-2)
						{
							offset_l--;
							break;
						}
					}
					if(i+1+offset_l>vec_end-2)
					{
						offset_l--;
						break;
					}
					dst=min(dst,abs(vec_left.at(i+1+offset_l).x-vec_left.at(i).x));
					if(i+2+offset_l<vec_end-1)
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
						{
							offset_l=k;
						}
					}
				}
					
				//look for the next up marker which is nearest to up marker i
				check=0;
				offset_u=0;
				dst=original->image.cols*2;
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
						{
							offset_u=k;
						}
					}
				}

				//look for the next right marker which is nearest to right marker i
				check=0;
				offset_r=0;
				dst=original->image.cols*2;
				while(check==0)
				{
					while(vec_right.at(i+1+offset_r).y==vec_right.at(i).y)
					{
						offset_r++;
						if(i+1+offset_r>vec_end-2)
						{
							offset_r--;
							break;
						}
					}
					if(i+1+offset_r>vec_end-2)
					{
						offset_r--;
						break;
					}
					dst=min(dst,abs(vec_right.at(i+1+offset_r).x-vec_right.at(i).x));
					if(i+2+offset_r<vec_end-1)
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
						{
							offset_r=k;
						}
					}
				}

				//look for the next down marker which is nearest to down marker i			
				check=0;
				offset_d=0;
				dst=original->image.cols*2;
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
						{
							offset_d=k;	
						}
					}
				}

				if(SVL)
				{
					cv::line(depth, cvPoint(vec_left.at(i).x,vec_left.at(i).y), cvPoint(vec_left.at(i+1+offset_l).x,vec_left.at(i+1+offset_l).y), CV_RGB(255,255,255), 2, 8, 0);
					cv::line(depth, cvPoint(vec_up.at(j).x,vec_up.at(j).y), cvPoint(vec_up.at(j+1+offset_u).x,vec_up.at(j+1+offset_u).y), CV_RGB(255,255,255), 2, 8, 0);	
					cv::line(depth, cvPoint(vec_right.at(i).x,vec_right.at(i).y), cvPoint(vec_right.at(i+1+offset_r).x,vec_right.at(i+1+offset_r).y), CV_RGB(255,255,255), 2, 8, 0);	
					cv::line(depth, cvPoint(vec_down.at(j).x,vec_down.at(j).y), cvPoint(vec_down.at(j+1+offset_d).x,vec_down.at(j+1+offset_d).y), CV_RGB(255,255,255), 2, 8, 0);
				}

				//if(vec_up.at(j).x>=vec_left.at(i).x && vec_up.at(j).y<=vec_left.at(i).y)
				//{
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
					if(x>=original->image.cols)	
						x=original->image.cols-1;
					if(y>=original->image.rows)	
						y=original->image.rows-1;

					f_c1=1;
					c1= cvPoint((int)x,(int)y);
				//}

				//if(vec_up.at(j+1+offset_u).x<=vec_right.at(i).x && vec_up.at(j+1+offset_u).y<=vec_right.at(i).y)
				//{
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
					if(x>=original->image.cols)	
						x=original->image.cols-1;
					if(y>=original->image.rows)	
						y=original->image.rows-1;

					f_c2=1;
					c2= cvPoint((int)x,(int)y);	
				//}				

				//if(vec_down.at(j+1+offset_d).x<=vec_right.at(i+1+offset_r).x && vec_down.at(j+1+offset_d).y>=vec_right.at(i+1+offset_r).y)
				//{
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
					if(x>=original->image.cols)	
						x=original->image.cols-1;
					if(y>=original->image.rows)	
						y=original->image.rows-1;

					f_c3=1;
					c3= cvPoint((int)x,(int)y);	
				//}
				
				//if(vec_down.at(j).x>=vec_left.at(i+1+offset_l).x && vec_down.at(j).y>=vec_left.at(i+1+offset_l).y)
				//{
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
					if(x>=original->image.cols)	
						x=original->image.cols-1;
					if(y>=original->image.rows)	
						y=original->image.rows-1;

					c4= cvPoint((int)x,(int)y);
					f_c4=1;
				//}	
	
				if(f_c1*f_c2*f_c3*f_c4>0)
				{
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
					if (cx_min>original->image.cols-5)						
						cx_min=original->image.cols-5;	if (cx_max>original->image.cols-1)
											cx_max=original->image.cols-1;
					if (cy_min>original->image.rows-5)						
						cy_min=original->image.rows-5;	if (cy_max>original->image.rows-1)
											cy_max=original->image.rows-1;
					roi_x=abs(cx_max-cx_min);
					roi_y=abs(cy_max-cy_min);

					//Look for door frame depth
					x_1=(int)((c1.x+c4.x)/2);
					x_2=(int)((c2.x+c3.x)/2);
					meters=0;
					right_depth=1000;
					left_depth=1000;
					for (int i=cy_min+roi_y/2; i<cy_min+roi_y*2/3; i++)
					{
		
						if(!std::isnan(cloud.at(x_1,i).z) && cloud.at(x_1,i).z>0.0 && cloud.at(x_1,i).z<5.0)
						{
							left_depth=min(left_depth,cloud.at(x_1,i).z);
						}
						if(!std::isnan(cloud.at(x_2,i).z) && cloud.at(x_2,i).z>0.0 && cloud.at(x_2,i).z<5.0)
						{
							right_depth=min(right_depth,cloud.at(x_2,i).z);
						}

					}
					meters=(left_depth+right_depth)/2;
					min_depth=min(left_depth,right_depth);
					min_dst_h=(min_x/meters);
					max_dst_h=(max_x/meters);
					min_dst_v=(min_y/meters);
					max_dst_v=(max_y/meters);

					door_x=(int)(cx_min+roi_x/2);
					door_y=(int)(cy_min+roi_y/2);

					room_frame_height=0;
					lintel=10000;
					sill=0;

					point=0;
					for(int m=cy_min; m<cy_max; m++)
					{				
						point3D=cloud.at(door_x,m);
						if(!std::isnan(point3D.z) && point3D.z > 0.0 && point3D.z < 5.0) 
						{
							if(point==1 && point3D.z > (prev_depth+meters)/2 + distance_to_room)
							{
								lintel=min(lintel,m);
							}
							if(point3D.z > min_depth)
							{
								sill=max(sill,m);
								//cv::line(depth, cvPoint(door_x,m), cvPoint(door_x,m), CV_RGB(0,0,0), 1, 8, 0);
							}
							prev_depth=point3D.z;
							point=1;
						}		
					}

					c3.y=min((int)c3.y,sill);
					c4.y=min((int)c4.y,sill);
					r=((double)b_c3.y-(double)cy_min)/((double)cy_max-(double)cy_min);
					c3.x=b_c2.x+(c3.x-c2.x)*r;
					c4.x=b_c1.x+(c4.x-c1.x)*r;

					c1.y=max((int)c1.y,lintel);
					c2.y=max((int)c2.y,lintel);
					r=((double)b_c1.y-(double)cy_min)/((double)cy_max-(double)cy_min);
					c2.x=c2.x+(c3.x-c2.x)*r;
					c1.x=c1.x+(c4.x-c1.x)*r;

					if(cx_min <= 10 || cx_max >= original->image.cols-10)
						min_dst_h=min_dst_h/2;
					if(cy_min <= 10 || cy_max >= original->image.rows-10)
						min_dst_v=min_dst_v/3;
					
					//filter false doors using physical constraints
					sensor_range = (meters>0.1 && !std::isnan(meters) && meters<5.0);
					perspective = (abs(dst_up-dst_down)<roi_x/2 && abs(dst_left-dst_right)<roi_y/2 && theta>0.698132);
					geometry = (c4.x<c3.x && c1.x<c2.x && c4.y>c1.y && c3.y>c2.y);
					size = (dst_h<max_dst_h && dst_v>min_dst_v && dst_v<max_dst_v && roi_x>5 && roi_y>5);

					if(!Range_filter)
						sensor_range =1; 
					if(!Persp_filter)
						perspective=1; 
					if(!Geom_filter)
						geometry=1; 
					if(!Size_filter)
						size=1; 

					if(sensor_range && perspective && geometry && size)
					{
								
						//prepare locations of the selected door frames	for the output message	
						ss_door_centroid.push_back(cvPoint(door_x,door_y));
						ss_depth.push_back(meters);
						ss_c1.push_back(c1);
						ss_c2.push_back(c2);
						ss_c3.push_back(c3);
						ss_c4.push_back(c4);
						if(SFC)
							DrawRect (depth, c1, c2, c3, c4, CV_RGB(100,100,100), 2, 0);
					}
				}
			}
		}
	}

	//Door size calibration
	min_depth=1000;
	for (int i=(int)(original->image.cols*1/3); i<(int)(original->image.cols*2/3); i++)
	{
	
		if(!std::isnan(cloud.at(i,(int)(original->image.rows/2)).z) && cloud.at(i,(int)(original->image.rows/2)).z>0.0 && cloud.at(i,(int)(original->image.rows/2)).z<5.0)
			min_depth=min(min_depth,cloud.at(i,(int)(original->image.rows/2)).z);
	}
	
	min_dst_h=(min_x/min_depth);
	max_dst_h=(max_x/min_depth);
	min_dst_v=(min_y/min_depth);
	max_dst_v=(max_y/min_depth);
	
	if(DSC)
		DoorSizeCalibration (depth, min_dst_h, max_dst_h, min_dst_v, max_dst_v);

	if (ss_door_centroid.size()>0)
	{
		b_door_centroid=cvPoint(0,0);
		b_c1=cvPoint(0,0);
		b_c2=cvPoint(0,0);
		b_c3=cvPoint(0,0);
		b_c4=cvPoint(0,0);
		b_depth=0;

		for (size_t i=0; i<ss_door_centroid.size(); i++)
		{
			b_door_centroid.x=(int)(b_door_centroid.x+ss_door_centroid.at(i).x);
			b_door_centroid.y=(int)(b_door_centroid.y+ss_door_centroid.at(i).y);
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
		b_c1.x=(int)(b_c1.x/ss_door_centroid.size());
		b_c1.y=(int)(b_c1.y/ss_door_centroid.size());
		b_c2.x=(int)(b_c2.x/ss_door_centroid.size());
		b_c2.y=(int)(b_c2.y/ss_door_centroid.size());
		b_c3.x=(int)(b_c3.x/ss_door_centroid.size());
		b_c3.y=(int)(b_c3.y/ss_door_centroid.size());
		b_c4.x=(int)(b_c4.x/ss_door_centroid.size());
		b_c4.y=(int)(b_c4.y/ss_door_centroid.size());

		//TODO--function for cx_min and cx_max!
		cx_min=min(min(b_c1.x,b_c2.x),min(b_c3.x,b_c4.x));
		cx_max=max(max(b_c1.x,b_c2.x),max(b_c3.x,b_c4.x));
		cy_min=min(min(b_c1.y,b_c2.y),min(b_c3.y,b_c4.y));
		cy_max=max(max(b_c1.y,b_c2.y),max(b_c3.y,b_c4.y));
									
		//DrawRect (depth, b_c1, b_c2, b_c3, b_c4, CV_RGB(255,255,255), 3, 0);

		if (cx_min<0)						
			cx_min=0;			if (cx_max<4)
								cx_max=4;
		if (cy_min<0)						
			cy_min=0;			if (cy_max<4)
								cy_max=4;
		if (cx_min>original->image.cols-5)						
			cx_min=original->image.cols-5;	if (cx_max>original->image.cols-1)
								cx_max=original->image.cols-1;
		if (cy_min>original->image.rows-5)						
			cy_min=original->image.rows-5;	if (cy_max>original->image.rows-1)
								cy_max=original->image.rows-1;
		
		roi_x=abs(cx_max-cx_min);
		roi_y=abs(cy_max-cy_min);
		r=(double)roi_x/(double)roi_y;	

		//Look for door frame depth
		x_1=(int)((b_c1.x+b_c4.x)/2);
		x_2=(int)((b_c2.x+b_c3.x)/2);
		min_depth=0;
		right_depth=1000;
		left_depth=1000;
		for (int i=cy_min+roi_y/2; i<cy_min+roi_y*2/3; i++)
		{
		
			if(!std::isnan(cloud.at(x_1,i).z) && cloud.at(x_1,i).z>0.0 && cloud.at(x_1,i).z<5.0)
			{
				left_depth=min(left_depth,cloud.at(x_1,i).z);
				cv::line(depth, cvPoint(x_1,i), cvPoint(x_1,i),white, 3, 8, 0);
			}
			if(!std::isnan(cloud.at(x_2,i).z) && cloud.at(x_2,i).z>0.0 && cloud.at(x_2,i).z<5.0)
			{
				right_depth=min(right_depth,cloud.at(x_2,i).z);
				cv::line(depth, cvPoint(x_2,i), cvPoint(x_2,i),white, 3, 8, 0);
			}

		}
		min_depth=(left_depth+right_depth)/2;
		min_dst_h=(min_x/min_depth);
		max_dst_h=(max_x/min_depth);
		min_dst_v=(min_y/min_depth);
		max_dst_v=(max_y/min_depth);
		size=0;
		size=(abs(x_1-x_2)<max_dst_h);


		if(s_door_centroid.x>0 && s_door_centroid.y>0)
		{
			dx=abs(b_door_centroid.x-s_door_centroid.x);
			dy=abs(b_door_centroid.y-s_door_centroid.y);
			dst=sqrt(dx*dx+dy*dy);
			if(dst<min_dst_h/4)
				support++;
		}
		
		s_door_centroid.x=b_door_centroid.x;
		s_door_centroid.y=b_door_centroid.y;
	}
	
	if(ss_door_centroid.size()==0)
		support--;
	if(support < 0)
	{
		support=0;
		s_door_centroid.x=0;
		s_door_centroid.y=0;
	}

	if(support >10)
		support=10;

	cv::Mat depth_graph;
	depth_graph = cv::Mat::zeros(depth.rows, depth.cols, CV_8UC1);

	cv::Mat panel_mask;
	panel_mask = cv::Mat::zeros(depth.rows, depth.cols, CV_8UC1);

	if(ss_door_centroid.size()>0)
	{
		/*Initilalize door state (0 = fully open door,
		-2, -1 = open left, 1, 2 = open right)*/
		side=0.0;
		
		//if the door is not fully open, find jambs
		if(size)
		{
			door_y=(int)((cy_min+cy_max)/2);
			point=0;
			left_depth=1000;
			for(int k=1; k<original->image.cols-1; k++)
			{
				if(!std::isnan(cloud.at(k,door_y).x) && !std::isnan(cloud.at(k,door_y).z) && cloud.at(k,door_y).z>0.0 && cloud.at(k,door_y).z<5.0)
				{
					if(k<(int)(-40.0-5.0/r+(b_c1.x+b_c4.x)/2)) 
					{	
						x_left=cloud.at(k,door_y).x;
						frame_left=cloud.at(k,door_y).z;
						point=1;
					}
					if(k<(int)((b_c1.x+b_c4.x)/2)-10) 
					{
						x_right=cloud.at(k,door_y).x;
						frame_right=cloud.at(k,door_y).z;
						left_door_end=k;
						point=1;

						if(point==1)
							cv::line(depth_graph, cvPoint((int)((x_left+2)*150),(int)(frame_left*100)), cvPoint((int)((2+cloud.at(k,door_y).x)*150),(int)(cloud.at(k,door_y).z*100)),white, 1, 8, 0);

					}
					if(k>(int)(-40.0-5.0/r+(b_c1.x+b_c4.x)/2) && k<(int)((b_c1.x+b_c4.x)/2))
					{
						cv::line(depth, cvPoint(k,door_y),cvPoint(k,door_y),white, 1, 8, 0);
						left_depth=min(left_depth,cloud.at(k,door_y).z);
						y_i=cloud.at(k,door_y).y;
					}
				}
			}
	
			dy=(frame_right-frame_left)*100;
			dx=(x_right-x_left)*150;
			m1=dy/(dx+0.00001);
			b1=frame_right*100-m1*(x_right+2)*150;
	
			point=0;
			right_depth=1000;
			for(int k=original->image.cols-1; k>1; k--)
			{
				if(!std::isnan(cloud.at(k,door_y).x) && !std::isnan(cloud.at(k,door_y).z) && cloud.at(k,door_y).z>0.0 && cloud.at(k,door_y).z<5.0)
				{
					if(k>(int)(40.0+5.0/r+(b_c2.x+b_c3.x)/2)) 
					{	
						x_right=cloud.at(k,door_y).x;
						frame_right=cloud.at(k,door_y).z;
						point=1;
					}
					if(k>(int)((b_c2.x+b_c3.x)/2)+10) 
					{
						x_left=cloud.at(k,door_y).x;
						frame_left=cloud.at(k,door_y).z;
						point=1;
						right_door_end=k;

						if(point==1)
							cv::line(depth_graph, cvPoint((int)((x_left+2)*150),(int)(frame_left*100)), cvPoint((int)((2+cloud.at(k,door_y).x)*150),(int)(cloud.at(k,door_y).z*100)),white, 1, 8, 0);

					}
					if(k<(int)(40.0+5.0/r+(b_c2.x+b_c3.x)/2) && k>(int)((b_c2.x+b_c3.x)/2))
					{
						cv::line(depth, cvPoint(k,door_y),cvPoint(k,door_y),white, 1, 8, 0);
						right_depth=min(right_depth,cloud.at(k,door_y).z);
						y_i=cloud.at(k,door_y).y;
					}
				}
			}

			//cv::line(depth_graph, cvPoint((int)(x_left*150),(int)(frame_left*100)), cvPoint((int)(x_right*150),(int)(frame_right*100)),white, 3, 8, 0);

			dy=(frame_right-frame_left)*100;
			dx=(x_right-x_left)*150;
			m2=dy/(dx+0.00001);
			b2=frame_left*100-m2*(x_left+2)*150;
		
			x = (b2 - b1)/(m1 - m2 + 0.0001);

			if(x>(x_left+2)*150)
			{
				door_end=right_door_end;
				side=1;
				y = (m2*depth_graph.cols-1)+b2;
				cv::line(depth_graph, cvPoint(depth_graph.cols-1,y), cvPoint((int)((x_left+2)*150),(int)(frame_left*100)), black, 5, 8, 0);

				jamb=1000;
				for(int k=depth_graph.cols-1; k>(x_left+2)*150; k--)
				{
					for(int m=1; m<depth_graph.rows-1; m++)
					{				
						if(depth_graph.data[m*depth_graph.cols+k]>0)
						{
							jamb=min(k,jamb);
						}		
					}
				}

				door_x=(int)((b_c2.x+b_c3.x)/2)+50;
				for(int k=depth_graph.cols-1; k>door_x; k--)
				{
					if(!std::isnan(cloud.at(k,door_y).x) && !std::isnan(cloud.at(k,door_y).z) && cloud.at(k,door_y).z>0.0 && cloud.at(k,door_y).z<5.0)
					{
						if(cloud.at(k,door_y).x > ((float)jamb/150)-2)
						{
							b_c2.x=k;
							b_c3.x=k;
							x_left=cloud.at(k,door_y).x;
							min_depth=left_depth;
							//cv::line(depth, cvPoint(k,door_y), cvPoint(k,door_y), black, 1, 8, 0);
						}
					}
				}
				/*if (jamb==1000)
				{
					b_c2.x=depth.cols-1;
					b_c3.x=depth.cols-1;
				}*/
				//cv::line(original->image, cvPoint((int)((b_c2.x+b_c3.x)/2),door_y),cvPoint(right_door_end,door_y),white, 3, 8, 0);
			}

			for(int k=1; k<original->image.cols-1; k++)
			{
				if(!std::isnan(cloud.at(k,door_y).x) && !std::isnan(cloud.at(k,door_y).z) && cloud.at(k,door_y).z>0.0 && cloud.at(k,door_y).z<5.0)
				{
					if(k<(int)((b_c1.x+b_c4.x)/2)-10) 
					{
						x_right=cloud.at(k,door_y).x;
						frame_right=cloud.at(k,door_y).z;
					}
				}
			}

			if(x<(x_right+2)*150)
			{	
				door_end=left_door_end;
				side=-1;
				y = m1+b1;
				cv::line(depth_graph, cvPoint(1,y), cvPoint((int)((x_right+2)*150),(int)(frame_right*100)), black, 5, 8, 0);

				jamb=0;
				for(int k=1; k<(x_right+2)*150; k++)
				{
					for(int m=1; m<depth_graph.rows-1; m++)
					{				
						if(depth_graph.data[m*depth_graph.cols+k]>0)
						{
							jamb=max(k,jamb);
						}		
					}
				}

				door_x=(int)((b_c1.x+b_c4.x)/2)-50;
				for(int k=1; k<door_x; k++)
				{
					if(!std::isnan(cloud.at(k,door_y).x) && !std::isnan(cloud.at(k,door_y).z) && cloud.at(k,door_y).z>0.0 && cloud.at(k,door_y).z<5.0)
					{
						if(cloud.at(k,door_y).x < ((float)jamb/150)-2)
						{
							b_c1.x=k;
							b_c4.x=k;
							x_right=cloud.at(k,door_y).x;
							min_depth=right_depth;
							//cv::line(depth, cvPoint(k,door_y), cvPoint(k,door_y), black, 1, 8, 0);
						}
					}
				}
				/*if (jamb==0)
				{
					b_c1.x=1;
					b_c4.x=1;
				}*/
				//cv::line(original->image, cvPoint((int)((b_c1.x+b_c4.x)/2),door_y),cvPoint(left_door_end,door_y),white, 3, 8, 0);
			}

			y = (m1*x)+b1;
			cv::line(depth_graph, cvPoint(x,y), cvPoint(x,y), white, 10, 8, 0);

			//cv::line(depth, cvPoint(x,frame_x), cvPoint(x,frame_x),white, 15, 8, 0);
		
			cx_min=min(min(b_c1.x,b_c2.x),min(b_c3.x,b_c4.x));
			cx_max=max(max(b_c1.x,b_c2.x),max(b_c3.x,b_c4.x));
			cy_min=min(min(b_c1.y,b_c2.y),min(b_c3.y,b_c4.y));
			cy_max=max(max(b_c1.y,b_c2.y),max(b_c3.y,b_c4.y));
		}

		cv::Mat mask_image;
		mask_image = cv::Mat::zeros(depth.rows, depth.cols, CV_8UC1);
						
		//Door area mask
		DrawRect (mask_image, b_c1, b_c2, b_c3, b_c4, CV_RGB(100,100,100), 1, 1);

		if (cx_min<0)						
			cx_min=0;			if (cx_max<4)
								cx_max=4;
		if (cy_min<0)						
			cy_min=0;			if (cy_max<4)
								cy_max=4;
		if (cx_min>original->image.cols-5)						
			cx_min=original->image.cols-5;	if (cx_max>original->image.cols-1)
								cx_max=original->image.cols-1;
		if (cy_min>original->image.rows-5)						
			cy_min=original->image.rows-5;	if (cy_max>original->image.rows-1)
								cy_max=original->image.rows-1;
		roi_x=abs(cx_max-cx_min);
		roi_y=abs(cy_max-cy_min);
		
		//Aspect filter
		aspect=0;	
		r=roi_x/(roi_y+0.0001);

		if(cx_min <= 10 || cx_max >= original->image.cols-10)
			aspect = (r>=0.4 && r<=0.8);	
		if(cy_min <= 10 || cy_max >= original->image.rows-10)
			aspect = (r>=0.4 && r<=1.4);
		if(cx_min >= 10 && cx_max <= original->image.cols-10 && cy_min >= 10 && cy_max <= original->image.rows-10)
			aspect = (r>=0.4 && r<=0.8);
		if((cx_min <= 10 || cx_max >= original->image.cols-10) && (cy_min <= 10 || cy_max >= original->image.rows-10))
			aspect = (r>=0.4 && r<=1.4);

		if(cx_min <= 10 || cx_max >= original->image.cols-10)
			min_dst_h=min_dst_h/2;
		if(cy_min <= 10 || cy_max >= original->image.rows-10)
			min_dst_v=min_dst_v/3;

		if(!Aspect_filter)
			aspect=1;

		//distance between corners
		dst_up=sqrt((b_c2.x-b_c1.x)*(b_c2.x-b_c1.x)+(b_c2.y-b_c1.y)*(b_c2.y-b_c1.y));
		dst_right=sqrt((b_c3.x-b_c2.x)*(b_c3.x-b_c2.x)+(b_c3.y-b_c2.y)*(b_c3.y-b_c2.y));
		dst_down=sqrt((b_c4.x-b_c3.x)*(b_c4.x-b_c3.x)+(b_c4.y-b_c3.y)*(b_c4.y-b_c3.y));
		dst_left=sqrt((b_c4.x-b_c1.x)*(b_c4.x-b_c1.x)+(b_c4.y-b_c1.y)*(b_c4.y-b_c1.y));

		dst_h=(dst_down+dst_up)/2;
		dst_v=(dst_left+dst_right)/2;

		size = 0;
		size = (dst_h>min_dst_h && dst_h<max_dst_h && dst_v>min_dst_v && dst_v<max_dst_v);

		room_frame_height = abs(sill-lintel);
		room_door_ratio = (float)room_frame_height/(float)roi_y;

		if(aspect && size)
		{
			DrawRect (original->image, b_c1, b_c2, b_c3, b_c4, CV_RGB(0,0,255), 3, 0);
			DrawRect (depth, b_c1, b_c2, b_c3, b_c4, CV_RGB(255,255,255), 3, 0);

				poses.pose.position.x = x_right;
				poses.pose.position.y = y_i;
				poses.pose.position.z = min_depth;
		
				poses.pose.orientation.x = x_left;
				poses.pose.orientation.y = y_top;
				poses.pose.orientation.z = min_depth;
				poses.pose.orientation.w = side;	

				door_centroid_publisher_.publish(poses);
			
				door_coordinates.data.clear();
				door_coordinates.data.push_back(b_c1.x);
				door_coordinates.data.push_back(b_c1.y);
				door_coordinates.data.push_back(b_c2.x);
				door_coordinates.data.push_back(b_c2.y);
				door_coordinates.data.push_back(b_c3.x);
				door_coordinates.data.push_back(b_c3.y);
				door_coordinates.data.push_back(b_c4.x);
				door_coordinates.data.push_back(b_c4.y);	
				door_coordinates.data.push_back(door_end);
				door_coordinates.data.push_back(side);

				open_door_coordinates_publisher_.publish(door_coordinates);
		}	
	}


	if(debugging_images!=0)
	{
		if(debugging_images==1)
			cv::imshow(WINDOW_1, depth);
		if(debugging_images==1)
			cv::imshow(WINDOW_2, original->image);
		//cv::imshow(WINDOW_2, depth_graph);
		//cvMoveWindow(WINDOW_1, 0, 640);
		cv::waitKey(3);  
	}
  }
  captured_depth = 0;  

  //unlock previously blocked shared variables 
  //this->alg_.unlock(); 
  this->points_mutex_.exit(); 
}

/*  [service callbacks] */

/*  [action callbacks] */

/*  [action requests] */

void OpenDoorDetectorAlgNode::node_config_update(Config &config, uint32_t level)
{
  this->alg_.lock();

	this->min_x = config.min_x;
	this->max_x = config.max_x;
	this->min_y = config.min_y;
	this->max_y = config.max_y;
	this->debugging_images = config.debugging_images;
	this->no_simulator = config.no_simulator;
	this->DSC = config.DSC;
	this->SVP = config.SVP;
	this->SVL = config.SVL;
	this->SFC = config.SFC;
        this->Range_filter = config.Range_filter;
	this->Persp_filter = config.Persp_filter;
	this->Geom_filter = config.Geom_filter ;
	this->Size_filter = config.Size_filter ;
	this->Aspect_filter = config.Aspect_filter;
	this->security_distance = config.security_distance;

  this->alg_.unlock();
}

void OpenDoorDetectorAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<OpenDoorDetectorAlgNode>(argc, argv, "open_door_detector_alg_node");
}

/* other functions */
void OpenDoorDetectorAlgNode::DoorSizeCalibration (cv::Mat inputImage, double min_dst_h, double max_dst_h, double min_dst_v, double max_dst_v)
{	

	//Smallest door frame allowed
	c1= cvPoint((inputImage.cols/2)-(min_dst_h/2), (inputImage.rows/2)-(min_dst_v/2));
	c2= cvPoint((inputImage.cols/2)+(min_dst_h/2), (inputImage.rows/2)-(min_dst_v/2));
	c3= cvPoint((inputImage.cols/2)+(min_dst_h/2), (inputImage.rows/2)+(min_dst_v/2));
	c4= cvPoint((inputImage.cols/2)-(min_dst_h/2), (inputImage.rows/2)+(min_dst_v/2));
	
	DrawRect (inputImage, c1, c2, c3, c4, white, 2, 0);

	//Biggest door frame allowed
	c1= cvPoint((inputImage.cols/2)-(max_dst_h/2), (inputImage.rows/2)-(max_dst_v/2));
	c2= cvPoint((inputImage.cols/2)+(max_dst_h/2), (inputImage.rows/2)-(max_dst_v/2));
	c3= cvPoint((inputImage.cols/2)+(max_dst_h/2), (inputImage.rows/2)+(max_dst_v/2));
	c4= cvPoint((inputImage.cols/2)-(max_dst_h/2), (inputImage.rows/2)+(max_dst_v/2));
	
	DrawRect (inputImage, c1, c2, c3, c4, white, 2, 0);
}

void OpenDoorDetectorAlgNode::DrawRect (cv::Mat inputImage, cv::Point q1, cv::Point q2, cv::Point q3, cv::Point q4, cv::Scalar color, int lineSize, int filled)
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

double OpenDoorDetectorAlgNode::AngleBetweenLines (cv::Point point1, cv::Point point2, cv::Point point3, cv::Point point4)
{	
	double m1, m2, dx, dy;

	dy=point2.y-point1.y;
	dx=point2.y-point1.y;
	m1=dy/(dx+0.0001);
	dy=point4.y-point3.y;
	dx=point4.x-point3.x;
	m2=dy/(dx+0.0001);

	double theta=atan(abs((m2-m1)/(1.0001+m1*m2)));
	
	return theta;
}

