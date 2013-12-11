FILE(REMOVE_RECURSE
  "../src/normal_descriptor_node/msg"
  "../src/normal_descriptor_node/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/ndesc_pc_service.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_ndesc_pc_service.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
