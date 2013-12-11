FILE(REMOVE_RECURSE
  "../src/iri_motion_detector/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genaction_msgs"
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
  INCLUDE(CMakeFiles/ROSBUILD_genaction_msgs.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
