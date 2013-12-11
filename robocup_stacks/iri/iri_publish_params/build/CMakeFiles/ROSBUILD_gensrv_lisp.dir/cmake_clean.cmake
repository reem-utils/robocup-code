FILE(REMOVE_RECURSE
  "../src/iri_publish_params/msg"
  "../src/iri_publish_params/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/classifier_update_service.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_classifier_update_service.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
