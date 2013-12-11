FILE(REMOVE_RECURSE
  "../src/iri_bow_object_detector/msg"
  "../src/iri_bow_object_detector/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/iri_bow_object_detector/GetGraspingPointAction.h"
  "../msg_gen/cpp/include/iri_bow_object_detector/GetGraspingPointGoal.h"
  "../msg_gen/cpp/include/iri_bow_object_detector/GetGraspingPointActionGoal.h"
  "../msg_gen/cpp/include/iri_bow_object_detector/GetGraspingPointResult.h"
  "../msg_gen/cpp/include/iri_bow_object_detector/GetGraspingPointActionResult.h"
  "../msg_gen/cpp/include/iri_bow_object_detector/GetGraspingPointFeedback.h"
  "../msg_gen/cpp/include/iri_bow_object_detector/GetGraspingPointActionFeedback.h"
  "../msg_gen/cpp/include/iri_bow_object_detector/WrinkledMap.h"
  "../msg_gen/cpp/include/iri_bow_object_detector/ObjectBox.h"
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
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
