FILE(REMOVE_RECURSE
  "../src/iri_perception_msgs/msg"
  "../src/iri_perception_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/iri_perception_msgs/DescriptorsToVws.h"
  "../srv_gen/cpp/include/iri_perception_msgs/SetImage.h"
  "../srv_gen/cpp/include/iri_perception_msgs/StorePointCloud2.h"
  "../srv_gen/cpp/include/iri_perception_msgs/PclToImg.h"
  "../srv_gen/cpp/include/iri_perception_msgs/peopleTrackingService.h"
  "../srv_gen/cpp/include/iri_perception_msgs/ProcessPointCloud2.h"
  "../srv_gen/cpp/include/iri_perception_msgs/PclToDescriptorSet.h"
  "../srv_gen/cpp/include/iri_perception_msgs/PclToMarker.h"
  "../srv_gen/cpp/include/iri_perception_msgs/GetPointCloud2.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
