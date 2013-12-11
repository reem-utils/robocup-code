FILE(REMOVE_RECURSE
  "../src/iri_bow_object_detector/msg"
  "../src/iri_bow_object_detector/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gencfg_cpp"
  "../cfg/cpp/iri_bow_object_detector/bow_object_detector_alg_configConfig.h"
  "../docs/bow_object_detector_alg_configConfig.dox"
  "../docs/bow_object_detector_alg_configConfig-usage.dox"
  "../src/iri_bow_object_detector/cfg/bow_object_detector_alg_configConfig.py"
  "../docs/bow_object_detector_alg_configConfig.wikidoc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gencfg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
