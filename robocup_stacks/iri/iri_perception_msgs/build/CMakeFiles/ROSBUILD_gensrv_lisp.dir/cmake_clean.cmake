FILE(REMOVE_RECURSE
  "../src/iri_perception_msgs/msg"
  "../src/iri_perception_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/DescriptorsToVws.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_DescriptorsToVws.lisp"
  "../srv_gen/lisp/SetImage.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_SetImage.lisp"
  "../srv_gen/lisp/StorePointCloud2.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_StorePointCloud2.lisp"
  "../srv_gen/lisp/PclToImg.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_PclToImg.lisp"
  "../srv_gen/lisp/peopleTrackingService.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_peopleTrackingService.lisp"
  "../srv_gen/lisp/ProcessPointCloud2.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_ProcessPointCloud2.lisp"
  "../srv_gen/lisp/PclToDescriptorSet.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_PclToDescriptorSet.lisp"
  "../srv_gen/lisp/PclToMarker.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_PclToMarker.lisp"
  "../srv_gen/lisp/GetPointCloud2.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_GetPointCloud2.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
