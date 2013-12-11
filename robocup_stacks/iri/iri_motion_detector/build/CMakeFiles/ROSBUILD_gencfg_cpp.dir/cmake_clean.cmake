FILE(REMOVE_RECURSE
  "../src/iri_motion_detector/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_gencfg_cpp"
  "../cfg/cpp/iri_motion_detector/motion_detector_alg_configConfig.h"
  "../docs/motion_detector_alg_configConfig.dox"
  "../docs/motion_detector_alg_configConfig-usage.dox"
  "../src/iri_motion_detector/cfg/motion_detector_alg_configConfig.py"
  "../docs/motion_detector_alg_configConfig.wikidoc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gencfg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
