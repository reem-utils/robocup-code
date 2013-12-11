FILE(REMOVE_RECURSE
  "../src/estirabot_msgs/msg"
  "../src/estirabot_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/estirabot_msgs/srv/__init__.py"
  "../src/estirabot_msgs/srv/_obs2action.py"
  "../src/estirabot_msgs/srv/_StateRepresentationChanges.py"
  "../src/estirabot_msgs/srv/_ArmMovementsPosesSrv.py"
  "../src/estirabot_msgs/srv/_RepresentationToString.py"
  "../src/estirabot_msgs/srv/_AddAction.py"
  "../src/estirabot_msgs/srv/_TransformPose.py"
  "../src/estirabot_msgs/srv/_AddState.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
