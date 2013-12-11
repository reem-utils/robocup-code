FILE(REMOVE_RECURSE
  "../src/iri_moped_handler/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/iri_moped_handler/srv/__init__.py"
  "../src/iri_moped_handler/srv/_enable.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
