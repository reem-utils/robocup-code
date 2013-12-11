FILE(REMOVE_RECURSE
  "../src/estirabot_msgs/msg"
  "../src/estirabot_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/obs2action.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_obs2action.lisp"
  "../srv_gen/lisp/StateRepresentationChanges.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_StateRepresentationChanges.lisp"
  "../srv_gen/lisp/ArmMovementsPosesSrv.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_ArmMovementsPosesSrv.lisp"
  "../srv_gen/lisp/RepresentationToString.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_RepresentationToString.lisp"
  "../srv_gen/lisp/AddAction.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_AddAction.lisp"
  "../srv_gen/lisp/TransformPose.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_TransformPose.lisp"
  "../srv_gen/lisp/AddState.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_AddState.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
