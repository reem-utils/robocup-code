FILE(REMOVE_RECURSE
  "../src/estirabot_msgs/msg"
  "../src/estirabot_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/belief_summary.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_belief_summary.lisp"
  "../msg_gen/lisp/TraversedEllipses.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_TraversedEllipses.lisp"
  "../msg_gen/lisp/belief.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_belief.lisp"
  "../msg_gen/lisp/DirtyArea.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_DirtyArea.lisp"
  "../msg_gen/lisp/ArrayIndexes.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_ArrayIndexes.lisp"
  "../msg_gen/lisp/GraspVerification.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_GraspVerification.lisp"
  "../msg_gen/lisp/PointsDistanceMsg.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_PointsDistanceMsg.lisp"
  "../msg_gen/lisp/Ellipse.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_Ellipse.lisp"
  "../msg_gen/lisp/GraspPointParameters.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_GraspPointParameters.lisp"
  "../msg_gen/lisp/PomdpGraspConfig.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_PomdpGraspConfig.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
