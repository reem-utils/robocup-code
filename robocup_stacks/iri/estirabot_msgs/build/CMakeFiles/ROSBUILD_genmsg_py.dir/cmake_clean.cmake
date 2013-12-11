FILE(REMOVE_RECURSE
  "../src/estirabot_msgs/msg"
  "../src/estirabot_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/estirabot_msgs/msg/__init__.py"
  "../src/estirabot_msgs/msg/_belief_summary.py"
  "../src/estirabot_msgs/msg/_TraversedEllipses.py"
  "../src/estirabot_msgs/msg/_belief.py"
  "../src/estirabot_msgs/msg/_DirtyArea.py"
  "../src/estirabot_msgs/msg/_ArrayIndexes.py"
  "../src/estirabot_msgs/msg/_GraspVerification.py"
  "../src/estirabot_msgs/msg/_PointsDistanceMsg.py"
  "../src/estirabot_msgs/msg/_Ellipse.py"
  "../src/estirabot_msgs/msg/_GraspPointParameters.py"
  "../src/estirabot_msgs/msg/_PomdpGraspConfig.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
