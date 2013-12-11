 #!/bin/bash
PAL_SCRIPT_PATH="/mnt_flash/bin/launch"
. "$PAL_SCRIPT_PATH/applicationNames"
. "$PAL_SCRIPT_PATH/palRosLaunch"
ROBOCUP_SCRIPT_PATH="/mnt_flash/robocup2013/reem_at_iri/scripts"
. "$ROBOCUP_SCRIPT_PATH/robocupLaunch"

roslaunchDaemon $HANGING_CLOTHES cloth_hanging pick_up_cloth_skills_reem.launch
