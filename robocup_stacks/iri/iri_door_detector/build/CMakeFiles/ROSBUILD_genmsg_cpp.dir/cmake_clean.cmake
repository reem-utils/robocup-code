FILE(REMOVE_RECURSE
  "../src/iri_door_detector/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/iri_door_detector/FindADoorAction.h"
  "../msg_gen/cpp/include/iri_door_detector/FindADoorGoal.h"
  "../msg_gen/cpp/include/iri_door_detector/FindADoorActionGoal.h"
  "../msg_gen/cpp/include/iri_door_detector/FindADoorResult.h"
  "../msg_gen/cpp/include/iri_door_detector/FindADoorActionResult.h"
  "../msg_gen/cpp/include/iri_door_detector/FindADoorFeedback.h"
  "../msg_gen/cpp/include/iri_door_detector/FindADoorActionFeedback.h"
  "../msg/FindADoorAction.msg"
  "../msg/FindADoorGoal.msg"
  "../msg/FindADoorActionGoal.msg"
  "../msg/FindADoorResult.msg"
  "../msg/FindADoorActionResult.msg"
  "../msg/FindADoorFeedback.msg"
  "../msg/FindADoorActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
