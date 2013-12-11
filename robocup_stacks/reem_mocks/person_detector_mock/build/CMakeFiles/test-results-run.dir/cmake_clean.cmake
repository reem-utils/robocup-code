FILE(REMOVE_RECURSE
  "../src/person_detector_mock/msg"
  "../src/person_detector_mock/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/test-results-run"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/test-results-run.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
