FILE(REMOVE_RECURSE
  "../src/estirabot_msgs/msg"
  "../src/estirabot_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/estirabot_msgs/obs2action.h"
  "../srv_gen/cpp/include/estirabot_msgs/StateRepresentationChanges.h"
  "../srv_gen/cpp/include/estirabot_msgs/ArmMovementsPosesSrv.h"
  "../srv_gen/cpp/include/estirabot_msgs/RepresentationToString.h"
  "../srv_gen/cpp/include/estirabot_msgs/AddAction.h"
  "../srv_gen/cpp/include/estirabot_msgs/TransformPose.h"
  "../srv_gen/cpp/include/estirabot_msgs/AddState.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
