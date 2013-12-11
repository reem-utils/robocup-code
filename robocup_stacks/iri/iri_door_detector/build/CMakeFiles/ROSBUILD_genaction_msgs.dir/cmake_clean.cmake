FILE(REMOVE_RECURSE
  "../src/iri_door_detector/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genaction_msgs"
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
  INCLUDE(CMakeFiles/ROSBUILD_genaction_msgs.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
