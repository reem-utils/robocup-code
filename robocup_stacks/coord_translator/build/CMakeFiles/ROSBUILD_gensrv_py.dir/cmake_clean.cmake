FILE(REMOVE_RECURSE
  "../src/coord_translator/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/coord_translator/srv/__init__.py"
  "../src/coord_translator/srv/_ObjectTranslatorDataBase.py"
  "../src/coord_translator/srv/_LocationTranslator.py"
  "../src/coord_translator/srv/_ObjectTranslator.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
