#!/bin/bash
PAL_SCRIPT_PATH="/mnt_flash/bin/launch"
. "$PAL_SCRIPT_PATH/applicationNames"
. "$PAL_SCRIPT_PATH/palRosLaunch"
. "$PAL_SCRIPT_PATH/navigationLaunch"

roslaunchDaemon $EMERGENCY_SIT emergency_situation emergency_situation.launch 
