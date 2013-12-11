FILE(REMOVE_RECURSE
  "../src/door_detector_pal/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genaction_msgs"
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
  INCLUDE(CMakeFiles/ROSBUILD_genaction_msgs.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
