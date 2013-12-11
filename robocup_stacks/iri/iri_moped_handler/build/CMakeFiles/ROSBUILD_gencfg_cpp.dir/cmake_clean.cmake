FILE(REMOVE_RECURSE
  "../src/iri_moped_handler/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gencfg_cpp"
  "../cfg/cpp/iri_moped_handler/moped_handler_alg_configConfig.h"
  "../docs/moped_handler_alg_configConfig.dox"
  "../docs/moped_handler_alg_configConfig-usage.dox"
  "../src/iri_moped_handler/cfg/moped_handler_alg_configConfig.py"
  "../docs/moped_handler_alg_configConfig.wikidoc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gencfg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
