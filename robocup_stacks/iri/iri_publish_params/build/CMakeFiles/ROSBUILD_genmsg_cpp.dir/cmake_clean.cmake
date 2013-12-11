FILE(REMOVE_RECURSE
  "../src/iri_publish_params/msg"
  "../src/iri_publish_params/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/iri_publish_params/classifier_update.h"
  "../msg_gen/cpp/include/iri_publish_params/classifier_params.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
