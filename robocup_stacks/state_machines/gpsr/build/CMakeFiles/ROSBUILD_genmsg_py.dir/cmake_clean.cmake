FILE(REMOVE_RECURSE
  "../src/gpsr/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/gpsr/msg/__init__.py"
  "../src/gpsr/msg/_order.py"
  "../src/gpsr/msg/_action.py"
  "../src/gpsr/msg/_order_list.py"
  "../src/gpsr/msg/_action_list.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
