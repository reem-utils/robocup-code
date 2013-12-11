FILE(REMOVE_RECURSE
  "../src/iri_moped_actionserver/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/iri_moped_actionserver/mopedAction.h"
  "../msg_gen/cpp/include/iri_moped_actionserver/mopedGoal.h"
  "../msg_gen/cpp/include/iri_moped_actionserver/mopedActionGoal.h"
  "../msg_gen/cpp/include/iri_moped_actionserver/mopedResult.h"
  "../msg_gen/cpp/include/iri_moped_actionserver/mopedActionResult.h"
  "../msg_gen/cpp/include/iri_moped_actionserver/mopedFeedback.h"
  "../msg_gen/cpp/include/iri_moped_actionserver/mopedActionFeedback.h"
  "../msg/mopedAction.msg"
  "../msg/mopedGoal.msg"
  "../msg/mopedActionGoal.msg"
  "../msg/mopedResult.msg"
  "../msg/mopedActionResult.msg"
  "../msg/mopedFeedback.msg"
  "../msg/mopedActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
