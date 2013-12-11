FILE(REMOVE_RECURSE
  "../src/iri_perception_msgs/msg"
  "../src/iri_perception_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/iri_perception_msgs/srv/__init__.py"
  "../src/iri_perception_msgs/srv/_DescriptorsToVws.py"
  "../src/iri_perception_msgs/srv/_SetImage.py"
  "../src/iri_perception_msgs/srv/_StorePointCloud2.py"
  "../src/iri_perception_msgs/srv/_PclToImg.py"
  "../src/iri_perception_msgs/srv/_peopleTrackingService.py"
  "../src/iri_perception_msgs/srv/_ProcessPointCloud2.py"
  "../src/iri_perception_msgs/srv/_PclToDescriptorSet.py"
  "../src/iri_perception_msgs/srv/_PclToMarker.py"
  "../src/iri_perception_msgs/srv/_GetPointCloud2.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
