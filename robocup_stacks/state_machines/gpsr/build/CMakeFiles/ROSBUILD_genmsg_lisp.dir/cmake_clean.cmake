FILE(REMOVE_RECURSE
  "../src/gpsr/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/order.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_order.lisp"
  "../msg_gen/lisp/action.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_action.lisp"
  "../msg_gen/lisp/order_list.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_order_list.lisp"
  "../msg_gen/lisp/action_list.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_action_list.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
