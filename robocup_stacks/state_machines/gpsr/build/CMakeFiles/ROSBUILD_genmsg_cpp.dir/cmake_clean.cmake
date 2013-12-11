FILE(REMOVE_RECURSE
  "../src/gpsr/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/gpsr/order.h"
  "../msg_gen/cpp/include/gpsr/action.h"
  "../msg_gen/cpp/include/gpsr/order_list.h"
  "../msg_gen/cpp/include/gpsr/action_list.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
