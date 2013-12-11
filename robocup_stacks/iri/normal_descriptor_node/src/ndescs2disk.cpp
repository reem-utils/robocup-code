#include "ndescs2disk.h"
#include <dirent.h>
//#include <sstream>

bool DirectoryExists( const char* pzPath )
{
  if ( pzPath == NULL) return false;
 
  DIR *pDir;
  bool bExists = false;
 
  pDir = opendir (pzPath);
 
  if (pDir != NULL)
  {
    bExists = true;    
    (void) closedir (pDir);
  }
 
  return bExists;
}

//Already defined in normaldescnode
//template <class T>
//inline std::string to_string (const T& t)
//{
//  std::stringstream ss;
//  ss << t;
//  return ss.str();
//}

void Ndescs2Disk::write_point(FILE *pf, const normal_descriptor_node::ndesc &point)
{
  int dim=point.descriptor.size();
  if (fwrite (&(point.u), sizeof (int), 1, pf) != 1){
    fprintf(stderr, "Error writting to file\n"); exit(-1);}
  if (fwrite (&(point.v), sizeof (int), 1, pf) != 1){
    fprintf(stderr, "Error writting to file\n"); exit(-1);}
  if (fwrite (&(point.ori), sizeof (float), 1, pf) != 1){
    fprintf(stderr, "Error writting to file\n"); exit(-1);}
  if (fwrite (&(point.point3d.x), sizeof (float), 1, pf) != 1){
    fprintf(stderr, "Error writting to file\n"); exit(-1);}
  if (fwrite (&(point.point3d.y), sizeof (float), 1, pf) != 1){
    fprintf(stderr, "Error writting to file\n"); exit(-1);}
  if (fwrite (&(point.point3d.z), sizeof (float), 1, pf) != 1){
    fprintf(stderr, "Error writting to file\n"); exit(-1);}
  if (fwrite (&dim, sizeof (int), 1, pf) != 1){
    fprintf(stderr, "Error writting to file\n"); exit(-1);}
  for(unsigned int j=0;j<dim;j++)
    if (fwrite (&(point.descriptor[j]), sizeof (float), 1, pf) != 1){
      fprintf(stderr, "Error writting to file\n"); exit(-1);}
}

Ndescs2Disk::Ndescs2Disk(char *pref_out) //, int max_frames)
{
  //init class attributes if necessary
  this->prefix_out_=std::string(pref_out);
  this->counter_=0;
  this->keep_nan_points_=false;
  //this->max_frames_=max_frames;
  //string for port names

  // [init publishers]

  // [init subscribers]
  this->points_subscriber_ = this->node_handle_.subscribe("ndesc", 1, &Ndescs2Disk::points_callback, this);

  // [init services]

  // [init clients]

  // [init action servers]

  // [init action clients]
  ROS_INFO("Init ndescs2disk node. Saving to %s",pref_out);  //, maxframes=%d\n",pref_out,max_frames);
}

void Ndescs2Disk::points_callback(const normal_descriptor_node::ndesc_pc::ConstPtr& ndesc_pc_msg)
{
  ROS_INFO("Received ndesc pointset");
  //TODO: think of a better name generation tech.
  std::string file_name=this->prefix_out_+to_string(this->counter_)+".ndesc";
  this->counter_++;
  int saved_points=0;
  FILE* pf=fopen(file_name.c_str(),"wb");
  for(int ii=0;ii<ndesc_pc_msg->num;ii++)
  {
    if( (!isnan(ndesc_pc_msg->descriptors[ii].point3d.x) &&
	 !isnan(ndesc_pc_msg->descriptors[ii].point3d.y) &&
	 !isnan(ndesc_pc_msg->descriptors[ii].point3d.z)) ||
	this->keep_nan_points_)
    {
      write_point(pf, ndesc_pc_msg->descriptors[ii]);
      saved_points++;
    }
    // fprintf(pf,"%d %d %f %f %f ",ndesc_pc_msg->descriptors[ii].u,
    //      ndesc_pc_msg->descriptors[ii].v,
    //      ndesc_pc_msg->descriptors[ii].point3d.x,
    //      ndesc_pc_msg->descriptors[ii].point3d.y,
    //      ndesc_pc_msg->descriptors[ii].point3d.z);
    // for(unsigned int j=0;j<ndesc_pc_msg->descriptors[ii].descriptor.size();j++)
    //   fprintf(pf,"%f ",ndesc_pc_msg->descriptors[ii].descriptor[j]);
    // fprintf(pf,"\n");
  }
  ROS_INFO("%d descriptors (out of %d) of size %d written to disk.\n",saved_points, ndesc_pc_msg->num, ndesc_pc_msg->descriptors[0].descriptor.size());
  fclose(pf);
  //if(this->max_frames_<=this->counter_ && this->max_frames_!=0)
  //  exit(0);
}



/* main function */
int main(int argc,char *argv[])
{
  if(argc<2){
    ROS_ERROR("Not enough arguments!\nUsage: ndesc2disk PREFIX_SAVE [-f MAX_FRAMES]");
    return -1;
  }

  //if(!DirectoryExists(argv[1]))
  //{
  //  ROS_ERROR("Error: %s does not exist",argv[1]);
  //}
  ros::init(argc, argv, "ndescs2disk");
  //int max_frames=0;
  //if (std::string(argv[2])==std::string("-f"))
  //  std::stringstream(std::string(argv[3])) >> max_frames;
  Ndescs2Disk ndescs2disk(argv[1]);//, max_frames);
  ros::spin();
}



