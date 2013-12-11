FILE(REMOVE_RECURSE
  "../src/iri_motion_detector/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/iri_motion_detector/MotionDetectorActionAction.h"
  "../msg_gen/cpp/include/iri_motion_detector/MotionDetectorActionGoal.h"
  "../msg_gen/cpp/include/iri_motion_detector/MotionDetectorActionActionGoal.h"
  "../msg_gen/cpp/include/iri_motion_detector/MotionDetectorActionResult.h"
  "../msg_gen/cpp/include/iri_motion_detector/MotionDetectorActionActionResult.h"
  "../msg_gen/cpp/include/iri_motion_detector/MotionDetectorActionFeedback.h"
  "../msg_gen/cpp/include/iri_motion_detector/MotionDetectorActionActionFeedback.h"
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
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
