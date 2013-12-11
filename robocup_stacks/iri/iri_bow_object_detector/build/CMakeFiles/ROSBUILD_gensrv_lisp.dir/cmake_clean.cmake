FILE(REMOVE_RECURSE
  "../src/iri_bow_object_detector/msg"
  "../src/iri_bow_object_detector/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/GeoVwDetection.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_GeoVwDetection.lisp"
  "../srv_gen/lisp/RefineGraspPoint.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_RefineGraspPoint.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
