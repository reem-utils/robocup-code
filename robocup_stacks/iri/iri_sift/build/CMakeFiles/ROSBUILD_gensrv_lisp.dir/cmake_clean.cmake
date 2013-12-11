FILE(REMOVE_RECURSE
  "../src/iri_sift/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/DescriptorsFromImage.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_DescriptorsFromImage.lisp"
  "../srv_gen/lisp/GeoVwSetSrv.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_GeoVwSetSrv.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
