#include "normal_descriptor_alg.h"

#define PI 3.1415926535


//helper fun
inline
int get_bin(float x, float y, std::vector<float> &bin_boundsX, std::vector<float> &bin_boundsY)
{
  int row=0;
  int col=0;
  int nb=bin_boundsX.size();
  //int nby=bin_boundsX.size();
  //if(x>=bin_boundsX[nb-1] || y >=bin_boundsY[nb-1])
  //   ROS_ERROR("x: %f y: %f",x,y);
  for(int i=0;i<nb;i++)//todo nb and nby assumed equal!
  {
    if(x<bin_boundsX[i] && y<bin_boundsY[i])
      break;
    if(x>bin_boundsX[i])
      col++;
    if(y>bin_boundsY[i])
      row+=nb;
  }
  return row+col;
}

//class definition
NormalDescriptorAlgorithm::NormalDescriptorAlgorithm()
{
  //default values
  this->desc_num_side_spatial_bins_ = 1;
  this->desc_num_orient_bins_ = 24;
  this->desc_patch_radius_=15;  
  
  //patch radius
  this->set_desc_patch_radius(15);

  //Spatial bins (side)
  this->set_num_side_spatial_bins(1);

  //Orientation bins
  this->set_num_orientation_bins(24);

  //Number of total bins computed automatically

  //Sample each (num) pixels
  this->sample_each_ = 1;
}

NormalDescriptorAlgorithm::~NormalDescriptorAlgorithm()
{
}

void NormalDescriptorAlgorithm::config_update(const Config& new_cfg, uint32_t level)
{
  this->lock();

  if(this->config_.num_spatial_bins != new_cfg.num_spatial_bins)
  {
    this->set_num_side_spatial_bins(new_cfg.num_spatial_bins);
  }
  if(this->config_.num_orientation_bins != new_cfg.num_orientation_bins)
  {
    this->set_num_orientation_bins(new_cfg.num_orientation_bins);
  }
  if(this->config_.desc_patch_radius != new_cfg.desc_patch_radius)
  {
    this->set_desc_patch_radius(new_cfg.desc_patch_radius);
  }
  if(this->config_.sample_each != new_cfg.sample_each)
  {
    this->set_sample_each(new_cfg.sample_each);
  }

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// NormalDescriptorAlgorithm Public API

void NormalDescriptorAlgorithm::compute_spherical_coords(pcl::PointCloud<pcl::Normal> &pcl_normal, pcl::PointCloud<pcl::PointXY> &pcl_spherical)
{
  for (size_t i = 0; i < pcl_normal.points.size (); ++i)
  {
    pcl_spherical.points[i].x = acos(pcl_normal.points[i].normal[2]);
    pcl_spherical.points[i].y = atan2(pcl_normal.points[i].normal[1], pcl_normal.points[i].normal[0]);
    //std::cout<<"tangles: "<<pcl_spherical.points[i].x<<" "<<pcl_spherical.points[i].y<<std::endl;
  }
}

class II
{
public:
  std::vector<unsigned int*> ii_;
  unsigned int bins_;
  unsigned int width_;
  unsigned int height_;


  II(unsigned int bins, unsigned int width, unsigned int height):bins_(bins),width_(width),height_(height){
    ii_.resize(bins);
    for(unsigned int i=0;i<bins;i++)
      ii_[i]=new unsigned int[width*height];
  }
  ~II(){
    for(unsigned int i=0;i<this->bins_;i++)
      delete [] ii_[i];
  }
  void construct(std::vector<unsigned int> &im){
    //0,0
    unsigned int u=0;
    unsigned int v=0;
    for(unsigned int b=0;b<this->bins_;b++)
    {
      //printf("%d %d %d\n",u,v,b);fflush(0);
      ii_[b][this->width_*v+u] =		     \
	(im[this->width_*v+u]==b ? 1:0);
    }

    //n,0
    v=0;
    for(u=1;u<this->width_;u++)
    {
      for(unsigned int b=0;b<this->bins_;b++)
      {
	//printf("%d %d %d\n",u,v,b);fflush(0);
	ii_[b][this->width_*v+u] =		     \
	  ii_[b][this->width_*v+(u-1)] +	     \
	  (im[this->width_*v+u]==b ? 1:0);
	//printf("%d ",im[this->width_*v+u]);
      }
    }
    //printf("0,n\n");fflush(0);
    //0,n
    u=0;
    for(v=1;v<this->height_;v++)
    {
      for(unsigned int b=0;b<this->bins_;b++)
      {
	//printf("%d %d %d\n",u,v,b);fflush(0);
	ii_[b][this->width_*v+u] =		     \
	  ii_[b][this->width_*(v-1)+u] +	     \
	  (im[this->width_*v+u]==b ? 1:0);
	//printf("%d ",im[this->width_*v+u]);
      }
    }
    //n,n
    for(v=1;v<this->height_;v++)
    {
      for(u=1;u<this->width_;u++)
      {
	for(unsigned int b=0;b<this->bins_;b++)
	{
	  //printf("%d %d %d\n",u,v,b);fflush(0);
	  ii_[b][this->width_*v+u] =		     \
	    ii_[b][this->width_*(v-1)+u] +	     \
	    ii_[b][this->width_*v+(u-1)] -	     \
	    ii_[b][this->width_*(v-1)+(u-1)] +	     \
	    (im[this->width_*v+u]==b ? 1:0);
	  //printf("%d ",im[this->width_*v+u]);
	}
      }
    }
  }
  std::vector<unsigned int> get_sub_rect(unsigned int tu, unsigned int tv, unsigned int bu, unsigned int bv)
  {
    std::vector<unsigned int> ret(this->bins_);
    for(unsigned int b=0;b<this->bins_;b++)
    {
      ret[b] = ii_[b][this->width_*tv+tu] + ii_[b][this->width_*bv+bu] - ii_[b][this->width_*tv+bu] - ii_[b][this->width_*bv+tu];
    }
    return ret;
  }
};


//void NormalDescriptorAlgorithm::canonical_orientation(const )
//{
//}


void NormalDescriptorAlgorithm::compute_ndescs_integral_spatial(pcl::PointCloud<pcl::PointXYZ>& cloud, normal_descriptor_node::ndesc_pc &ndesc_pc_msg)
{

  ROS_INFO("PointCloud received");

  //TODO check if optimize with voxel-grid or subsampling http://pointclouds.org/documentation/tutorials/voxel_grid.php#voxelgrid 
  //compute normal
  pcl::NormalEstimation<pcl::PointXYZ, pcl::Normal> normal_estimator;
  pcl::PointCloud<pcl::Normal> pcl_normals;
  normal_estimator.setInputCloud(boost::make_shared<pcl::PointCloud<pcl::PointXYZ> > (cloud));
  normal_estimator.setKSearch (20);
  pcl::search::KdTree<pcl::PointXYZ>::Ptr tree (new pcl::search::KdTree<pcl::PointXYZ>);

  normal_estimator.setSearchMethod (tree);
  normal_estimator.compute (pcl_normals);

  //get spherical coordinates
  pcl::PointCloud<pcl::PointXY> pcl_spherical; //(ab)using PointXY for holding spherical angles
  pcl_spherical.width  = cloud.width;
  pcl_spherical.height = cloud.height;
  pcl_spherical.points.resize (pcl_spherical.width * pcl_spherical.height);
  this->compute_spherical_coords(pcl_normals, pcl_spherical);

  //compute descriptors
  ndesc_pc_msg.descriptors.clear();
  ndesc_pc_msg.len    = this->desc_num_total_bins_;
  ndesc_pc_msg.width  = pcl_spherical.width;
  ndesc_pc_msg.height = pcl_spherical.height;
  ndesc_pc_msg.num_orient_bins = this->desc_num_orient_bins_;
  ndesc_pc_msg.num_spa_bins = this->desc_num_side_spatial_bins_;

  std::vector<unsigned int> binned(cloud.width*cloud.height);

  for(uint v=0;v<cloud.height;v++)
  {
    for(uint u=0;u<cloud.width;u++)
    {
      if(isnan(pcl_spherical(u,v).x) || isnan(pcl_spherical(u,v).y))
	binned[u+cloud.width*v]=-1;
      else
	binned[u+cloud.width*v]=get_bin(pcl_spherical(u,v).x, pcl_spherical(u,v).y, this->orient_bin_boundsX_, this->orient_bin_boundsY_);
    }
  }

  II intim(this->desc_num_orient_bins_*this->desc_num_orient_bins_, cloud.width, cloud.height);
  intim.construct(binned);

  unsigned int spatial_bin_size    = (2*this->desc_patch_radius_+1)/this->desc_num_side_spatial_bins_;
  unsigned int spatial_bin_orients = this->desc_num_orient_bins_*this->desc_num_orient_bins_;

  for(unsigned int v=this->desc_patch_radius_;v<cloud.height-this->desc_patch_radius_-1;v+=this->sample_each_)
  {
    for(unsigned int u=this->desc_patch_radius_;u<cloud.width-this->desc_patch_radius_-1;u+=this->sample_each_)
    {      
      //ROS_INFO("v:%d u:%d, spbin size=%d",v,u,spatial_bin_size);

      //ROS_INFO("Computing base descriptor");
      normal_descriptor_node::ndesc desc;
      //insert point3D
      desc.point3d.x=cloud(u,v).x;
      desc.point3d.y=cloud(u,v).y;
      desc.point3d.z=cloud(u,v).z;
      
      //insert point2D
      desc.u=u;
      desc.v=v;
      
      desc.descriptor.resize(this->desc_num_total_bins_);

      float total_votes=0; // for normalization

      unsigned int absolute_top  = v-this->desc_patch_radius_;
      //int absolute_bottom = v+this->desc_patch_radius_;
      unsigned int absolute_left = u-this->desc_patch_radius_;
      //int absolute_right = u+this->desc_patch_radius_;
      //ROS_INFO("atop aleft %d %d",absolute_top,absolute_left);

      for(unsigned int k=0;k<this->desc_num_side_spatial_bins_; k++)
      {
	unsigned int bound_left  = absolute_left + k*spatial_bin_size;
	unsigned int bound_right = absolute_left + (k+1)*spatial_bin_size;
	for(unsigned int l=0; l<this->desc_num_side_spatial_bins_; l++)
	{
	  unsigned int bound_top    = absolute_top + l*spatial_bin_size;
	  unsigned int bound_bottom = absolute_top + (l+1)*spatial_bin_size;

	  //ROS_INFO("(l,t,r,b)(%d,%d,%d,%d)",bound_left, bound_top, bound_right, bound_bottom);
	  std::vector<unsigned int> tmp = intim.get_sub_rect(bound_left, bound_top, bound_right, bound_bottom);
	  for(unsigned int i=0;i<spatial_bin_orients;i++)
	  {
	    unsigned int offset_full_rows = l*this->desc_num_side_spatial_bins_*spatial_bin_orients;
	    unsigned int offset_this_row  = k*spatial_bin_orients;//swaped k and l, Arnau 4/4/12
	    desc.descriptor[offset_full_rows + offset_this_row + i]=tmp[i];
	    total_votes+=tmp[i];
	  }
	  //normalize per bin?
	//increment bin  (TODO soft voting)
	//norm histogram/s (L1 norm)
	//TODO: Test L2 norm 
	}
      }

      //L1 norm //aRNAU 4/4/12 DISABLED NORM
      //if(total_votes!=0){
      //   for(unsigned int i=0; i<this->desc_num_total_bins_; i++)
      //    desc.descriptor[i]/=total_votes;
      //}
      //sqrt
      /*if(0 && total_votes!=0){
	for(unsigned int i=0; i<this->desc_num_total_bins_; i++)
	  desc.descriptor[i]=sqrt(desc.descriptor[i]);
      }*/

      ndesc_pc_msg.descriptors.push_back(desc);
      ndesc_pc_msg.num++;
      //ROS_INFO("loop %d", desc.descriptor.size());
    }
  }
  ROS_INFO("Computed %d descriptors", ndesc_pc_msg.num);

  //save for debugging
  // FILE* pf=fopen("/tmp/dasdescs.txt","w");
  // for(int ii=0;ii<ndesc_pc_msg.num;ii++)
  // {
  //   fprintf(pf,"%d %d %f %f %f ",ndesc_pc_msg.descriptors[ii].u,
  // 	    ndesc_pc_msg.descriptors[ii].v,
  // 	    ndesc_pc_msg.descriptors[ii].point3d.x,
  // 	    ndesc_pc_msg.descriptors[ii].point3d.y,
  // 	    ndesc_pc_msg.descriptors[ii].point3d.z);
  //   for(int j=0;j<ndesc_pc_msg.descriptors[ii].descriptor.size();j++)
  //   fprintf(pf,"%f ",ndesc_pc_msg.descriptors[ii].descriptor[j]);
  //   fprintf(pf,"\n");
  //   //debug off
  // }
  // fclose(pf);

  //return ndesc_pc_msg; //data copying... do with shared pointer? done
}


// ARNAU 1/12/11
//Untested!

void NormalDescriptorAlgorithm::compute_descriptor_spatial_rot_inv(pcl::PointCloud<pcl::PointXYZ> &cloud, normal_descriptor_node::ndesc_pc &ndesc_pc_msg)
{

  //TODO check if optimize with voxel-grid or subsampling http://pointclouds.org/documentation/tutorials/voxel_grid.php#voxelgrid   <--- aixo s'hauria d'unificar amb la versio integral image!
  //compute normal
  pcl::NormalEstimation<pcl::PointXYZ, pcl::Normal> normal_estimator;
  pcl::PointCloud<pcl::Normal> pcl_normals;
  normal_estimator.setInputCloud(boost::make_shared<pcl::PointCloud<pcl::PointXYZ> > (cloud));
  normal_estimator.setKSearch (20);

  pcl::search::KdTree<pcl::PointXYZ>::Ptr tree (new pcl::search::KdTree<pcl::PointXYZ>);

  normal_estimator.setSearchMethod (tree);
  normal_estimator.compute (pcl_normals);

  //get spherical coordinates
  pcl::PointCloud<pcl::PointXY> pcl_spherical; //(ab)using PointXY for holding spherical angles
  pcl_spherical.width  = cloud.width;
  pcl_spherical.height = cloud.height;
  pcl_spherical.points.resize (pcl_spherical.width * pcl_spherical.height);
  this->compute_spherical_coords(pcl_normals, pcl_spherical);

  for(unsigned int v=this->desc_patch_radius_;v<cloud.height-this->desc_patch_radius_;v+=this->sample_each_)
  {
    for(unsigned int u=this->desc_patch_radius_;u<cloud.width-this->desc_patch_radius_;u+=this->sample_each_)
    {      
      ndesc_pc_msg.descriptors.push_back(this->compute_descriptor_one_spatial_rot_inv(cloud, pcl_spherical, u, v));
      ndesc_pc_msg.num++;
    }
  }  
  ROS_INFO("Computed %d descriptors", ndesc_pc_msg.num);
}


normal_descriptor_node::ndesc NormalDescriptorAlgorithm::compute_descriptor_one_spatial_rot_inv(pcl::PointCloud<pcl::PointXYZ> &cloud, pcl::PointCloud<pcl::PointXY> &pcl_spherical, uint u, uint v)
{
  //ROS_INFO("Computing spatial descriptor");
  normal_descriptor_node::ndesc desc;
  //insert point3D
  desc.point3d.x = cloud(u,v).x;
  desc.point3d.y = cloud(u,v).y;
  desc.point3d.z = cloud(u,v).z;

  //insert point2D
  desc.u = u;
  desc.v = v;

  //ROS_INFO("onpetaa1");

  //rotation invariance - determine dominant orientation in theta (spehrical.Y) angle
  //allow for 36 orientations to rotate to
  int nbins = 36;
  float orientation[36];
  //init hist
  memset(orientation, 0, sizeof(float)*36);

  int absolute_top  = v-this->desc_patch_radius_;
  int absolute_bottom = v+this->desc_patch_radius_;
  int absolute_left = u-this->desc_patch_radius_;
  int absolute_right = u+this->desc_patch_radius_;
  for(int j=absolute_top;j<absolute_bottom;j++)
  {
    for(int i=absolute_left;i<absolute_right;i++)
    {
      if(isnan(pcl_spherical(i,j).y))
	continue;
      int bin = floor(nbins*(PI+pcl_spherical(i,j).y)/(2*PI));
      //ROS_INFO("the-- %f -> bin = %i",pcl_spherical(i,j).y, bin);
      orientation[bin]+=1;
    }  
  }

  //TODO smooth histogram
  int max_ori=0;
  float max_val=0;
  for(int ii=0;ii<nbins;ii++)
  {
    //ROS_INFO("%f ", orientation[ii]);
    if(max_val<orientation[ii])
    {
      //ROS_INFO("!!!!");
      max_val=orientation[ii];
      max_ori=ii;
    }
  }
  
  
  float ori=float(max_ori)/float(nbins)*2*PI-PI;
  desc.ori=ori;
  
  // for (int uuu=0;uuu<36;uuu++)
  //   printf("%f ", orientation[uuu]);
  // printf("\n");
  //ROS_INFO("%f %i %f ori",ori,max_ori, max_val);

  desc.descriptor.resize(this->desc_num_total_bins_);
  //int absolute_top  = u+this->desc_patch_radius_;
  //int absolute_bottom = v+this->desc_patch_radius_;
  //int absolute_left = u-this->desc_patch_radius_;
  //int absolute_right = u+this->desc_patch_radius_;
  int size_bin      = (2*this->desc_patch_radius_+1)/this->desc_num_side_spatial_bins_;

  for(uint k=0; k<this->desc_num_side_spatial_bins_; k++)
  {
    uint bound_left  = absolute_left + k*size_bin;
    uint bound_right = absolute_left + (k+1)*size_bin;
    for(uint l=0; l<this->desc_num_side_spatial_bins_; l++)
    {
      uint bound_top    = absolute_top + l*size_bin;
      uint bound_bottom = absolute_top + (l+1)*size_bin;
      for(uint i=bound_left; i<=bound_right; i++)
      {
	for (uint j=bound_top; j<=bound_bottom; j++)
	{
	  //Determine new origin after rotation (rotation center is u,v)
	  int i_s = (int)round( (cos(ori)*(i-u) - sin(ori)*(j-v)) + u);
	  int j_s = (int)round( (sin(ori)*(i-u) + cos(ori)*(j-v)) + v);

	  //filter points outside
	  if((i_s<0) || (j_s<0) || (i_s>=cloud.width) || (j_s>=cloud.height))
	    continue;

	  //filter nans
	  if(isnan(pcl_spherical(i_s,j_s).x) || isnan(pcl_spherical(i_s,j_s).y))
	    continue;
	  
	  //ROS_INFO("%i %i - (%i %i / %i %i @ %i - %f) -> (%i %i)",k,l,i,j,u,v,max_ori,ori,i_s,j_s);
      
	  //determine bin
	  uint offset = (l*this->desc_num_side_spatial_bins_+k) * this->desc_num_orient_bins_;
	  float anglemod2pi=(pcl_spherical(i_s,j_s).y+PI)-(ori+PI); //in range 2PI
	  while(anglemod2pi<0){
	    //ROS_INFO("%f",anglemod2pi);
	    anglemod2pi+=2*PI;
	  }
	  anglemod2pi-=PI; //back to -PI:PI
	  uint bin    = get_bin(pcl_spherical(i_s,j_s).x, anglemod2pi, this->orient_bin_boundsX_,this->orient_bin_boundsY_);
	  //increment bin  (TODO soft voting)
	  
	  //ROS_INFO("vote (%i, %i) here %i+%i (max %i) ori=%f %f (%f)",i_s, j_s, bin,offset,ori,this->desc_num_total_bins_,pcl_spherical(i_s,j_s).y-ori,anglemod2pi);
	  //if(bin>=this->desc_num_total_bins_ || bin<0)
	  //{
	  //  ROS_INFO("kaput");
	  //  exit(10);
	  //}
	  desc.descriptor[bin+offset]++;
	}
      }
    }
  }
  //norm histogram/s (L1 norm)
  //TODO: Test L2 norm 

  //ROS_INFO("aaa1");

  //float total_votes=0;
  //for(uint i=0; i<this->desc_num_total_bins_; i++)
  //  total_votes+=desc.descriptor[i];
  //
  //for(uint i=0; i<this->desc_num_total_bins_; i++)
  //  desc.descriptor[i]/=total_votes;

  return desc;
}
