FILE(REMOVE_RECURSE
  "../src/gpsrSoar/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/gpsrSoar/gpsrActionAction.h"
  "../msg_gen/cpp/include/gpsrSoar/gpsrActionGoal.h"
  "../msg_gen/cpp/include/gpsrSoar/gpsrActionActionGoal.h"
  "../msg_gen/cpp/include/gpsrSoar/gpsrActionResult.h"
  "../msg_gen/cpp/include/gpsrSoar/gpsrActionActionResult.h"
  "../msg_gen/cpp/include/gpsrSoar/gpsrActionFeedback.h"
  "../msg_gen/cpp/include/gpsrSoar/gpsrActionActionFeedback.h"
  "../msg_gen/cpp/include/gpsrSoar/order.h"
  "../msg/gpsrActionAction.msg"
  "../msg/gpsrActionGoal.msg"
  "../msg/gpsrActionActionGoal.msg"
  "../msg/gpsrActionResult.msg"
  "../msg/gpsrActionActionResult.msg"
  "../msg/gpsrActionFeedback.msg"
  "../msg/gpsrActionActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
