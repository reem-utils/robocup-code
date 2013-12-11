FILE(REMOVE_RECURSE
  "../src/door_detector_pal/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/door_detector_pal/msg/__init__.py"
  "../src/door_detector_pal/msg/_DoorDetectorAction.py"
  "../src/door_detector_pal/msg/_DoorDetectorGoal.py"
  "../src/door_detector_pal/msg/_DoorDetectorActionGoal.py"
  "../src/door_detector_pal/msg/_DoorDetectorResult.py"
  "../src/door_detector_pal/msg/_DoorDetectorActionResult.py"
  "../src/door_detector_pal/msg/_DoorDetectorFeedback.py"
  "../src/door_detector_pal/msg/_DoorDetectorActionFeedback.py"
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
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
