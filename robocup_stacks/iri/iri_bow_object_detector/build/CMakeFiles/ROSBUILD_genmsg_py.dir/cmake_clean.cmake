FILE(REMOVE_RECURSE
  "../src/iri_bow_object_detector/msg"
  "../src/iri_bow_object_detector/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/iri_bow_object_detector/msg/__init__.py"
  "../src/iri_bow_object_detector/msg/_GetGraspingPointAction.py"
  "../src/iri_bow_object_detector/msg/_GetGraspingPointGoal.py"
  "../src/iri_bow_object_detector/msg/_GetGraspingPointActionGoal.py"
  "../src/iri_bow_object_detector/msg/_GetGraspingPointResult.py"
  "../src/iri_bow_object_detector/msg/_GetGraspingPointActionResult.py"
  "../src/iri_bow_object_detector/msg/_GetGraspingPointFeedback.py"
  "../src/iri_bow_object_detector/msg/_GetGraspingPointActionFeedback.py"
  "../src/iri_bow_object_detector/msg/_WrinkledMap.py"
  "../src/iri_bow_object_detector/msg/_ObjectBox.py"
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
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
