FILE(REMOVE_RECURSE
  "../src/coord_translator/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/coord_translator/ObjectTranslatorDataBase.h"
  "../srv_gen/cpp/include/coord_translator/LocationTranslator.h"
  "../srv_gen/cpp/include/coord_translator/ObjectTranslator.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
