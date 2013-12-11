 #!/bin/bash
PAL_SCRIPT_PATH="/mnt_flash/bin/launch"
. "$PAL_SCRIPT_PATH/applicationNames"
. "$PAL_SCRIPT_PATH/palRosLaunch"
ROBOCUP_SCRIPT_PATH="/mnt_flash/robocup2013/reem_at_iri/scripts"
. "$ROBOCUP_SCRIPT_PATH/robocupLaunch"

ROS_NAMESPACE=stereo rosrun stereo_image_proc stereo_image_proc /stereo/left/image_raw:=/stereo/left/image /stereo/right/image_raw:=/stereo/right/image _approximate_sync:=False &

roslaunchDaemon face_detector face_detector face_detector.reem.launch
