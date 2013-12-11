FILE(REMOVE_RECURSE
  "../src/gpsrSoar/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genaction_msgs"
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
  INCLUDE(CMakeFiles/ROSBUILD_genaction_msgs.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
