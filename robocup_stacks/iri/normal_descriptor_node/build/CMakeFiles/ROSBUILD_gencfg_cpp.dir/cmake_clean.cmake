FILE(REMOVE_RECURSE
  "../src/normal_descriptor_node/msg"
  "../src/normal_descriptor_node/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gencfg_cpp"
  "../cfg/cpp/normal_descriptor_node/normal_descriptor_alg_configConfig.h"
  "../docs/normal_descriptor_alg_configConfig.dox"
  "../docs/normal_descriptor_alg_configConfig-usage.dox"
  "../src/normal_descriptor_node/cfg/normal_descriptor_alg_configConfig.py"
  "../docs/normal_descriptor_alg_configConfig.wikidoc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gencfg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
