FILE(REMOVE_RECURSE
  "../src/iri_sift/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gencfg_cpp"
  "../cfg/cpp/iri_sift/sift_alg_configConfig.h"
  "../docs/sift_alg_configConfig.dox"
  "../docs/sift_alg_configConfig-usage.dox"
  "../src/iri_sift/cfg/sift_alg_configConfig.py"
  "../docs/sift_alg_configConfig.wikidoc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gencfg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
