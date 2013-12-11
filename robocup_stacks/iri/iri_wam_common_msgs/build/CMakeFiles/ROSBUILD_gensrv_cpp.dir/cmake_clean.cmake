FILE(REMOVE_RECURSE
  "../src/iri_wam_common_msgs/msg"
  "../src/iri_wam_common_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/iri_wam_common_msgs/wamaction.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/wamInverseKinematicsFromPose.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/wamInverseKinematics.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/wamGetRobotPoseFromToolPose.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/pose_move.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/bhand_cmd.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/joints_move.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/wamForwardKinematics.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/wamInverseKinematicsUsingReference.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/wamdriver.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/compute_obj_grasp_pose.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/obs_request.h"
  "../srv_gen/cpp/include/iri_wam_common_msgs/modeling.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
