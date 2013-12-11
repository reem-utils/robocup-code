FILE(REMOVE_RECURSE
  "../src/iri_wam_common_msgs/msg"
  "../src/iri_wam_common_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/test"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/test.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
