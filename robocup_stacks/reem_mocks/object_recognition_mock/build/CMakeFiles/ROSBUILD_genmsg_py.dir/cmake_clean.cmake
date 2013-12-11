FILE(REMOVE_RECURSE
  "../src/object_recognition_mock/msg"
  "../src/object_recognition_mock/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/object_recognition_mock/msg/__init__.py"
  "../src/object_recognition_mock/msg/_DetectionResult.py"
  "../src/object_recognition_mock/msg/_DetectedObject.py"
  "../src/object_recognition_mock/msg/_Pixel.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
