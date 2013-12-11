FILE(REMOVE_RECURSE
  "../src/gpsrSoar/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/gpsrSoar/msg/__init__.py"
  "../src/gpsrSoar/msg/_gpsrActionAction.py"
  "../src/gpsrSoar/msg/_gpsrActionGoal.py"
  "../src/gpsrSoar/msg/_gpsrActionActionGoal.py"
  "../src/gpsrSoar/msg/_gpsrActionResult.py"
  "../src/gpsrSoar/msg/_gpsrActionActionResult.py"
  "../src/gpsrSoar/msg/_gpsrActionFeedback.py"
  "../src/gpsrSoar/msg/_gpsrActionActionFeedback.py"
  "../src/gpsrSoar/msg/_order.py"
  "../msg/gpsrActionAction.msg"
  "../msg/gpsrActionGoal.msg"
  "../msg/gpsrActionActionGoal.msg"
  "../msg/gpsrActionResult.msg"
  "../msg/gpsrActionActionResult.msg"
  "../msg/gpsrActionFeedback.msg"
  "../msg/gpsrActionActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
