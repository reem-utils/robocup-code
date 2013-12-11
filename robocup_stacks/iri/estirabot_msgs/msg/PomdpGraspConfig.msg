# Message containing configuration for the pomdp grasping process

# Define grabbing_zones
int8 GRAB = 0
int8 DROP = 1

# Define grabbing_zones
int8 BOTH_ZONES = 0
int8 LEFT_ZONE = 1
int8 RIGHT_ZONE = 2

# Define best pose algorithms
int8 MAX_HEIGHT_ALG = 0
int8 MAX_WRINKLE_ALG = 1
int8 FUSION_ALG = 2

# Define posible approach identifiers
int8 APPROACH_TOP_DEEP = 0
int8 APPROACH_TOP_SURFACE = 1
int8 APPROACH_SIDE_DEEP = 2
int8 APPROACH_SIDE_SURFACE = 3

int8 best_pose_algorithm_id
int8 actiontype
int8 grabbing_zone
estirabot_msgs/GraspPointParameters approach_config
string[] fingers_grasp_configs
geometry_msgs/PoseStamped place_point
