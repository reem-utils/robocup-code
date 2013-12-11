 #!/bin/bash

if [ "$TARGET" == "embedded" ];
then
PAL_SCRIPT_PATH="/mnt_flash/bin/launch"
else
PAL_SCRIPT_PATH="/home/icarus/branches_svn/3.5_ROBOCUP/robot/sources/bin/launch"
fi

. "$PAL_SCRIPT_PATH/palRosLaunch"


#roslaunchDaemon grasping reem_tabletop_manipulation_launch tabletop_manipulation_local_db.launch sim:=false use_snapshotter:=true load_kinematics:=true load_move_arm:=true load_move_arm_warehouse:=false
roslaunchDaemon kinect_grasping reem_tabletop_manipulation_launch perception_robot.launch