FILE(REMOVE_RECURSE
  "../src/iri_motion_detector/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/iri_motion_detector/msg/__init__.py"
  "../src/iri_motion_detector/msg/_MotionDetectorActionAction.py"
  "../src/iri_motion_detector/msg/_MotionDetectorActionGoal.py"
  "../src/iri_motion_detector/msg/_MotionDetectorActionActionGoal.py"
  "../src/iri_motion_detector/msg/_MotionDetectorActionResult.py"
  "../src/iri_motion_detector/msg/_MotionDetectorActionActionResult.py"
  "../src/iri_motion_detector/msg/_MotionDetectorActionFeedback.py"
  "../src/iri_motion_detector/msg/_MotionDetectorActionActionFeedback.py"
  "../msg/MotionDetectorActionAction.msg"
  "../msg/MotionDetectorActionGoal.msg"
  "../msg/MotionDetectorActionActionGoal.msg"
  "../msg/MotionDetectorActionResult.msg"
  "../msg/MotionDetectorActionActionResult.msg"
  "../msg/MotionDetectorActionFeedback.msg"
  "../msg/MotionDetectorActionActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
