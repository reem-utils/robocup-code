FILE(REMOVE_RECURSE
  "../src/poi_current_position_sm_mock/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/lookupTransform.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_lookupTransform.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
