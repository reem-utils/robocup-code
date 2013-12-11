# Message containing results from a sequence of verification actions on a grasAFTER_SHAKING = 1p

# Currently positions in the vector correspond to the following actions
# 0 -> Result after basic lift movement
# 1 -> Result after shaking the cloth when lifted

int32 AFTER_LIFT = 0
int32 AFTER_SHAKING = 1

object_manipulation_msgs/GraspResult[] grasp_results
sensor_msgs/PointCloud2[] grasp_images
