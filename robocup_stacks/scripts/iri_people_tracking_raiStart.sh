#!/bin/bash
PAL_SCRIPT_PATH="/mnt_flash/bin/launch"
. "$PAL_SCRIPT_PATH/applicationNames"
. "$PAL_SCRIPT_PATH/palRosLaunch"
. "$PAL_SCRIPT_PATH/navigationLaunch"

roslaunchDaemon $IRI_PEOPLE_TRACKING_RAI iri_people_tracking_rai reemTest.launch 
