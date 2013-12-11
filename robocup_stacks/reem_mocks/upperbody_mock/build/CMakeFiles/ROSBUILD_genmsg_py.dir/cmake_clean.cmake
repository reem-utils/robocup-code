FILE(REMOVE_RECURSE
  "../src/upperbody_mock/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/upperbody_mock/msg/__init__.py"
  "../src/upperbody_mock/msg/_UpperBodyAction.py"
  "../src/upperbody_mock/msg/_UpperBodyGoal.py"
  "../src/upperbody_mock/msg/_UpperBodyActionGoal.py"
  "../src/upperbody_mock/msg/_UpperBodyResult.py"
  "../src/upperbody_mock/msg/_UpperBodyActionResult.py"
  "../src/upperbody_mock/msg/_UpperBodyFeedback.py"
  "../src/upperbody_mock/msg/_UpperBodyActionFeedback.py"
  "../msg/UpperBodyAction.msg"
  "../msg/UpperBodyGoal.msg"
  "../msg/UpperBodyActionGoal.msg"
  "../msg/UpperBodyResult.msg"
  "../msg/UpperBodyActionResult.msg"
  "../msg/UpperBodyFeedback.msg"
  "../msg/UpperBodyActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
