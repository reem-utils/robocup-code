 #!/bin/bash

if [ "$TARGET" == "embedded" ];
then
PAL_SCRIPT_PATH="/mnt_flash/bin/launch"
else
PAL_SCRIPT_PATH="/home/icarus/branches_svn/3.5_ROBOCUP/robot/sources/bin/launch"
fi

. "$PAL_SCRIPT_PATH/palRosLaunch"

export LD_LIBRARY_PATH=/mnt_flash/stacks/overlay/arm_kinematics_constraint_aware/lib/:/mnt_flash/stacks/overlay/collision_space/lib/:$LD_LIBRARY_PATH;  roslaunchDaemon constraint_aware_kinematics reem_arm_navigation constraint_aware_kinematics.launch


LD_LIBRARY_PATH=/mnt_flash/stacks/reem_object_manipulation/reem_final_approach/lib:$LD_LIBRARY_PATH roslaunchDaemon final_approach reem_final_approach reem_final_approach.launch

export LD_LIBRARY_PATH=/mnt_flash/stacks/pal_image_processing/pal_appearance_models/lib:/mnt_flash/stacks/pal_vision/pal_pcl/lib:/mnt_flash/stacks/pal_image_processing/pal_vision_segmentation/lib:/mnt_flash/stacks/overlay/arm_kinematics_constraint_aware/lib:/mnt_flash/stacks/reem_object_manipulation/object_manipulator/lib:/mnt_flash/stacks/overlay/household_objects_database/lib:/mnt_flash/stacks/overlay/tabletop_object_detector/lib:/mnt_flash/stacks/overlay/tabletop_collision_map_processing/lib:/mnt_flash/stacks/overlay/collision_space/lib:$LD_LIBRARY_PATH; roslaunchDaemon grasping reem_tabletop_manipulation_launch manipulation_robot_with_db_all_flags_set.launch

#sleep 40
