#!/bin/bash

if  [ "$TARGET" == "embedded" ];
then
PAL_SCRIPT_PATH="/mnt_flash/bin/launch"
else
PAL_SCRIPT_PATH="/home/icarus/branches_svn/3.5_ROBOCUP/robot/sources/bin/launch"
fi

. "$PAL_SCRIPT_PATH/palRosLaunch"

rosStopDaemon kinect_grasping
