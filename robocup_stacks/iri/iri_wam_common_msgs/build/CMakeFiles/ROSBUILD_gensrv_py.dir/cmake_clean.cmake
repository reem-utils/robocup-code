FILE(REMOVE_RECURSE
  "../src/iri_wam_common_msgs/msg"
  "../src/iri_wam_common_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/iri_wam_common_msgs/srv/__init__.py"
  "../src/iri_wam_common_msgs/srv/_wamaction.py"
  "../src/iri_wam_common_msgs/srv/_wamInverseKinematicsFromPose.py"
  "../src/iri_wam_common_msgs/srv/_wamInverseKinematics.py"
  "../src/iri_wam_common_msgs/srv/_wamGetRobotPoseFromToolPose.py"
  "../src/iri_wam_common_msgs/srv/_pose_move.py"
  "../src/iri_wam_common_msgs/srv/_bhand_cmd.py"
  "../src/iri_wam_common_msgs/srv/_joints_move.py"
  "../src/iri_wam_common_msgs/srv/_wamForwardKinematics.py"
  "../src/iri_wam_common_msgs/srv/_wamInverseKinematicsUsingReference.py"
  "../src/iri_wam_common_msgs/srv/_wamdriver.py"
  "../src/iri_wam_common_msgs/srv/_compute_obj_grasp_pose.py"
  "../src/iri_wam_common_msgs/srv/_obs_request.py"
  "../src/iri_wam_common_msgs/srv/_modeling.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
