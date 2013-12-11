FILE(REMOVE_RECURSE
  "../src/iri_wam_common_msgs/msg"
  "../src/iri_wam_common_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genaction_msgs"
  "../msg/SimpleBhandPickUpAction.msg"
  "../msg/SimpleBhandPickUpGoal.msg"
  "../msg/SimpleBhandPickUpActionGoal.msg"
  "../msg/SimpleBhandPickUpResult.msg"
  "../msg/SimpleBhandPickUpActionResult.msg"
  "../msg/SimpleBhandPickUpFeedback.msg"
  "../msg/SimpleBhandPickUpActionFeedback.msg"
  "../msg/LWPRTrajectoryReturningForceEstimationAction.msg"
  "../msg/LWPRTrajectoryReturningForceEstimationGoal.msg"
  "../msg/LWPRTrajectoryReturningForceEstimationActionGoal.msg"
  "../msg/LWPRTrajectoryReturningForceEstimationResult.msg"
  "../msg/LWPRTrajectoryReturningForceEstimationActionResult.msg"
  "../msg/LWPRTrajectoryReturningForceEstimationFeedback.msg"
  "../msg/LWPRTrajectoryReturningForceEstimationActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genaction_msgs.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
