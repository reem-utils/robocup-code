FILE(REMOVE_RECURSE
  "../src/iri_sift/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/iri_sift/DescriptorsFromImage.h"
  "../srv_gen/cpp/include/iri_sift/GeoVwSetSrv.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
