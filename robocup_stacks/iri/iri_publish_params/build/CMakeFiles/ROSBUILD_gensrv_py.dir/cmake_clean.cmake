FILE(REMOVE_RECURSE
  "../src/iri_publish_params/msg"
  "../src/iri_publish_params/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/iri_publish_params/srv/__init__.py"
  "../src/iri_publish_params/srv/_classifier_update_service.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
