FILE(REMOVE_RECURSE
  "../src/door_detector_pal/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/door_detector_pal/DoorDetectorAction.h"
  "../msg_gen/cpp/include/door_detector_pal/DoorDetectorGoal.h"
  "../msg_gen/cpp/include/door_detector_pal/DoorDetectorActionGoal.h"
  "../msg_gen/cpp/include/door_detector_pal/DoorDetectorResult.h"
  "../msg_gen/cpp/include/door_detector_pal/DoorDetectorActionResult.h"
  "../msg_gen/cpp/include/door_detector_pal/DoorDetectorFeedback.h"
  "../msg_gen/cpp/include/door_detector_pal/DoorDetectorActionFeedback.h"
  "../msg/DoorDetectorAction.msg"
  "../msg/DoorDetectorGoal.msg"
  "../msg/DoorDetectorActionGoal.msg"
  "../msg/DoorDetectorResult.msg"
  "../msg/DoorDetectorActionResult.msg"
  "../msg/DoorDetectorFeedback.msg"
  "../msg/DoorDetectorActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
