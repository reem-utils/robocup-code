FILE(REMOVE_RECURSE
  "../src/iri_bow_object_detector/msg"
  "../src/iri_bow_object_detector/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genaction_msgs"
  "../msg/GetGraspingPointAction.msg"
  "../msg/GetGraspingPointGoal.msg"
  "../msg/GetGraspingPointActionGoal.msg"
  "../msg/GetGraspingPointResult.msg"
  "../msg/GetGraspingPointActionResult.msg"
  "../msg/GetGraspingPointFeedback.msg"
  "../msg/GetGraspingPointActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genaction_msgs.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
