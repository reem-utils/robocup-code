FILE(REMOVE_RECURSE
  "../src/object_recognition_mock/msg"
  "../src/object_recognition_mock/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/DetectionResult.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_DetectionResult.lisp"
  "../msg_gen/lisp/DetectedObject.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_DetectedObject.lisp"
  "../msg_gen/lisp/Pixel.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_Pixel.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
