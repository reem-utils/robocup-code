FILE(REMOVE_RECURSE
  "../src/iri_bow_object_detector/msg"
  "../src/iri_bow_object_detector/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/rosbuild_precompile"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/rosbuild_precompile.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
