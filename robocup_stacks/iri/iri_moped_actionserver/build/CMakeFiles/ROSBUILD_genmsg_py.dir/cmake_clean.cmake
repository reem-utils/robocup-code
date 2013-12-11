FILE(REMOVE_RECURSE
  "../src/iri_moped_actionserver/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/iri_moped_actionserver/msg/__init__.py"
  "../src/iri_moped_actionserver/msg/_mopedAction.py"
  "../src/iri_moped_actionserver/msg/_mopedGoal.py"
  "../src/iri_moped_actionserver/msg/_mopedActionGoal.py"
  "../src/iri_moped_actionserver/msg/_mopedResult.py"
  "../src/iri_moped_actionserver/msg/_mopedActionResult.py"
  "../src/iri_moped_actionserver/msg/_mopedFeedback.py"
  "../src/iri_moped_actionserver/msg/_mopedActionFeedback.py"
  "../msg/mopedAction.msg"
  "../msg/mopedGoal.msg"
  "../msg/mopedActionGoal.msg"
  "../msg/mopedResult.msg"
  "../msg/mopedActionResult.msg"
  "../msg/mopedFeedback.msg"
  "../msg/mopedActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
