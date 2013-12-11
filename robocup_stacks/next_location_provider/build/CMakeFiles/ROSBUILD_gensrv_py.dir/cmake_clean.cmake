FILE(REMOVE_RECURSE
  "../src/next_location_provider/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/next_location_provider/srv/__init__.py"
  "../src/next_location_provider/srv/_NextProbableLocation.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
