FILE(REMOVE_RECURSE
  "../src/estirabot_msgs/msg"
  "../src/estirabot_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/rospack_gensrv"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/rospack_gensrv.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
