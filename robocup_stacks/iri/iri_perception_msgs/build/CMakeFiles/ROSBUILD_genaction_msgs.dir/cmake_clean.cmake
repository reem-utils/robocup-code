FILE(REMOVE_RECURSE
  "../src/iri_perception_msgs/msg"
  "../src/iri_perception_msgs/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genaction_msgs"
  "../msg/voiceRecognitionAction.msg"
  "../msg/voiceRecognitionGoal.msg"
  "../msg/voiceRecognitionActionGoal.msg"
  "../msg/voiceRecognitionResult.msg"
  "../msg/voiceRecognitionActionResult.msg"
  "../msg/voiceRecognitionFeedback.msg"
  "../msg/voiceRecognitionActionFeedback.msg"
  "../msg/object_pose_detectionAction.msg"
  "../msg/object_pose_detectionGoal.msg"
  "../msg/object_pose_detectionActionGoal.msg"
  "../msg/object_pose_detectionResult.msg"
  "../msg/object_pose_detectionActionResult.msg"
  "../msg/object_pose_detectionFeedback.msg"
  "../msg/object_pose_detectionActionFeedback.msg"
  "../msg/peopleTrackAction.msg"
  "../msg/peopleTrackGoal.msg"
  "../msg/peopleTrackActionGoal.msg"
  "../msg/peopleTrackResult.msg"
  "../msg/peopleTrackActionResult.msg"
  "../msg/peopleTrackFeedback.msg"
  "../msg/peopleTrackActionFeedback.msg"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genaction_msgs.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
