FILE(REMOVE_RECURSE
  "../src/person_detector_mock/msg"
  "../src/person_detector_mock/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/peopleTrackingArray.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_peopleTrackingArray.lisp"
  "../msg_gen/lisp/peopleTracking.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_peopleTracking.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
