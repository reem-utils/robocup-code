FILE(REMOVE_RECURSE
  "../src/iri_publish_params/msg"
  "../src/iri_publish_params/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/classifier_update.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_classifier_update.lisp"
  "../msg_gen/lisp/classifier_params.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_classifier_params.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
