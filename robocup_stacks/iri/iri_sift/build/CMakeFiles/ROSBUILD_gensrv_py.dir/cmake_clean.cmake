FILE(REMOVE_RECURSE
  "../src/iri_sift/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/iri_sift/srv/__init__.py"
  "../src/iri_sift/srv/_DescriptorsFromImage.py"
  "../src/iri_sift/srv/_GeoVwSetSrv.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
