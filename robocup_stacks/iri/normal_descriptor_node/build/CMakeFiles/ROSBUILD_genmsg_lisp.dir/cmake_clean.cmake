FILE(REMOVE_RECURSE
  "../src/normal_descriptor_node/msg"
  "../src/normal_descriptor_node/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/ndesc_pc.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_ndesc_pc.lisp"
  "../msg_gen/lisp/ndesc.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_ndesc.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
