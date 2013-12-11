FILE(REMOVE_RECURSE
  "../src/normal_descriptor_node/msg"
  "../src/normal_descriptor_node/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/rospack_gencfg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/rospack_gencfg.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
