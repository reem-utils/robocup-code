FILE(REMOVE_RECURSE
  "../src/iri_perception_msgs/msg"
  "../src/iri_perception_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/rospack_genmsg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/rospack_genmsg.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)