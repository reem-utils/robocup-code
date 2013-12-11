FILE(REMOVE_RECURSE
  "../src/estirabot_msgs/msg"
  "../src/estirabot_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/estirabot_msgs/belief_summary.h"
  "../msg_gen/cpp/include/estirabot_msgs/TraversedEllipses.h"
  "../msg_gen/cpp/include/estirabot_msgs/belief.h"
  "../msg_gen/cpp/include/estirabot_msgs/DirtyArea.h"
  "../msg_gen/cpp/include/estirabot_msgs/ArrayIndexes.h"
  "../msg_gen/cpp/include/estirabot_msgs/GraspVerification.h"
  "../msg_gen/cpp/include/estirabot_msgs/PointsDistanceMsg.h"
  "../msg_gen/cpp/include/estirabot_msgs/Ellipse.h"
  "../msg_gen/cpp/include/estirabot_msgs/GraspPointParameters.h"
  "../msg_gen/cpp/include/estirabot_msgs/PomdpGraspConfig.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
