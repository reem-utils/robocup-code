#!/bin/bash
###For launching the simulation

roslaunch reem_gazebo reem_pal_empty_world.launch &
roslaunch reem_arm_navigation reem_arm_navigation.launch &
export PAL_INSTALL_DIR=~/usr/default
./navigationStart.sh
./motionManagerServerStart.sh
~/usr/default/bin/launch/deployerMotorsGazeboStart.sh