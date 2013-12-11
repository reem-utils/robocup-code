FILE(REMOVE_RECURSE
  "../src/upperbody_mock/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/upperbody_mock/UpperBodyAction.h"
  "../msg_gen/cpp/include/upperbody_mock/UpperBodyGoal.h"
  "../msg_gen/cpp/include/upperbody_mock/UpperBodyActionGoal.h"
  "../msg_gen/cpp/include/upperbody_mock/UpperBodyResult.h"
  "../msg_gen/cpp/include/upperbody_mock/UpperBodyActionResult.h"
  "../msg_gen/cpp/include/upperbody_mock/UpperBodyFeedback.h"
  "../msg_gen/cpp/include/upperbody_mock/UpperBodyActionFeedback.h"
  "../msg/UpperBodyAction.msg"
  "../msg/UpperBodyGoal.msg"
  "../msg/UpperBodyActionGoal.msg"
  "../msg/UpperBodyResult.msg"
  "../msg/UpperBodyActionResult.msg"
  "../msg/UpperBodyFeedback.msg"
  "../msg/UpperBodyActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
