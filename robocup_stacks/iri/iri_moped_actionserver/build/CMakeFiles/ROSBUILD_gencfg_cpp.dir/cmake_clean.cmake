FILE(REMOVE_RECURSE
  "../src/iri_moped_actionserver/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_gencfg_cpp"
  "../cfg/cpp/iri_moped_actionserver/moped_actionserver_alg_configConfig.h"
  "../docs/moped_actionserver_alg_configConfig.dox"
  "../docs/moped_actionserver_alg_configConfig-usage.dox"
  "../src/iri_moped_actionserver/cfg/moped_actionserver_alg_configConfig.py"
  "../docs/moped_actionserver_alg_configConfig.wikidoc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gencfg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
