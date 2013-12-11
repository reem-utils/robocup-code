FILE(REMOVE_RECURSE
  "../src/iri_perception_msgs/msg"
  "../src/iri_perception_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/tests"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/tests.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
