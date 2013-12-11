FILE(REMOVE_RECURSE
  "../src/coord_translator/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/ObjectTranslatorDataBase.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_ObjectTranslatorDataBase.lisp"
  "../srv_gen/lisp/LocationTranslator.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_LocationTranslator.lisp"
  "../srv_gen/lisp/ObjectTranslator.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_ObjectTranslator.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
