#!/bin/bash
PAL_SCRIPT_PATH="/mnt_flash/bin/launch"
. "$PAL_SCRIPT_PATH/applicationNames"
. "$PAL_SCRIPT_PATH/palRosLaunch"
. "$PAL_SCRIPT_PATH/navigationLaunch"

# <avoid_errors_in_execution_time>
REEM_AT_IRI_SCRIPTS_PATH=$(rospack find scripts)  					# "/mnt_flash/stacks/robocup_stacks/scripts"

"$PAL_SCRIPT_PATH/gestureRecognitionStop.sh"						# To avoid conflicts with grasping
"$REEM_AT_IRI_SCRIPTS_PATH/iri_people_tracking_raiStop.sh"    		# Save processing.
"$REEM_AT_IRI_SCRIPTS_PATH/graspingStartNoKinect.sh"				# Because we need disable kinect to enable again, but to gesture_recognition.
"$REEM_AT_IRI_SCRIPTS_PATH/startRobotControllers.sh"				# This is to put the hands of the robot in 'home position'
rosrun reem_move_arm_action move --arm=left --pose=home_to_init	 	# Left hand  to initial pose
rosrun reem_move_arm_action move --arm=right --pose=home_to_init 	# Right hand to initial pose
"$PAL_SCRIPT_PATH/reemAliveStart.sh"								# Should be running because EnterRoom will disable it.
"$REEM_AT_IRI_SCRIPTS_PATH/kinectToGraspStart.sh"               	# To the grasp start completly
"$REEM_AT_IRI_SCRIPTS_PATH/stopRobotControllers.sh"					# Because to put the arms in front (EnterRoom), is using xml movements.
# </avoid_errors_in_execution_time>

roslaunchDaemon $COCKTAIL_PARTY cocktail_party cocktail_party.launch 
