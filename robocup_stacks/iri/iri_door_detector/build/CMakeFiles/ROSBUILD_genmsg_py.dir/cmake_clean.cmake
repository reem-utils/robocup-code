FILE(REMOVE_RECURSE
  "../src/iri_door_detector/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/iri_door_detector/msg/__init__.py"
  "../src/iri_door_detector/msg/_FindADoorAction.py"
  "../src/iri_door_detector/msg/_FindADoorGoal.py"
  "../src/iri_door_detector/msg/_FindADoorActionGoal.py"
  "../src/iri_door_detector/msg/_FindADoorResult.py"
  "../src/iri_door_detector/msg/_FindADoorActionResult.py"
  "../src/iri_door_detector/msg/_FindADoorFeedback.py"
  "../src/iri_door_detector/msg/_FindADoorActionFeedback.py"
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
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
