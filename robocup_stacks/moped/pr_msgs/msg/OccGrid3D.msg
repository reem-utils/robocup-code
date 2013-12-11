#a 3-D grid map, modeled after the OccGrid.msg type
Header header

#resolution of cells [m/side] 
float32 resolution

# num cells in {x,y,z} direction
uint32 num_x_voxels
uint32 num_y_voxels
uint32 num_z_voxels

# exact center of map (always an odd number of voxels in each dimension)
geometry_msgs/Point32 origin

# the map data. 0-100, representing probability: ceil(100*p_occupied-0.5)
# index =  kk * num_y_voxels * num_x_voxels + jj * num_x_voxels + ii
byte[] data
