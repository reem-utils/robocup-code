FILE(REMOVE_RECURSE
  "../src/upperbody_mock/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genaction_msgs"
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
  INCLUDE(CMakeFiles/ROSBUILD_genaction_msgs.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
