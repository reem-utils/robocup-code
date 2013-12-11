FILE(REMOVE_RECURSE
  "../src/iri_motion_detector_mock/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/iri_motion_detector_mock/msg/__init__.py"
  "../src/iri_motion_detector_mock/msg/_MotionDetectorActionResult.py"
  "../src/iri_motion_detector_mock/msg/_MotionDetectorActionFeedback.py"
  "../src/iri_motion_detector_mock/msg/_MotionDetectorActionActionResult.py"
  "../src/iri_motion_detector_mock/msg/_MotionDetectorActionActionGoal.py"
  "../src/iri_motion_detector_mock/msg/_MotionDetectorActionActionFeedback.py"
  "../src/iri_motion_detector_mock/msg/_MotionDetectorActionGoal.py"
  "../src/iri_motion_detector_mock/msg/_MotionDetectorActionAction.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
