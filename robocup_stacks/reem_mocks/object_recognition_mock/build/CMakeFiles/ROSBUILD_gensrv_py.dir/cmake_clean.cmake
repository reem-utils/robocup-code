FILE(REMOVE_RECURSE
  "../src/object_recognition_mock/msg"
  "../src/object_recognition_mock/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/object_recognition_mock/srv/__init__.py"
  "../src/object_recognition_mock/srv/_enable.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
