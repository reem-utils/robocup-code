FILE(REMOVE_RECURSE
  "CMakeFiles/ROSBUILD_gencfg_cpp"
  "../cfg/cpp/as_hri/as_hri_alg_configConfig.h"
  "../docs/as_hri_alg_configConfig.dox"
  "../docs/as_hri_alg_configConfig-usage.dox"
  "../src/as_hri/cfg/as_hri_alg_configConfig.py"
  "../docs/as_hri_alg_configConfig.wikidoc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gencfg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
