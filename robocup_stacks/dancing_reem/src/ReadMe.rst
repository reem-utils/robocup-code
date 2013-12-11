README
======

##Info:
This is a first Version of a BPM tracking system.

##Instalation:
    For Beat Analysis it needs to have soundstretch and lame installed
    $sudo apt-get install soundstretch
    $sudo apt-get install lame

    For sound playing ans so on, maybe you need to install audio-common:
    $sudo apt-get install ros-<distro>-audio-common

##Usage:
For testing just execute the python script "dancing_bot_using_jorgen_bpm.py" in the following
way:

python dancing_bot_using_jorgen_bpm.py ""absolute path of the mp3 file you want to analyse""

##Example : $python dancing_bot_using_jorgen_bpm.py /home/rdaneelolivaw/play_ground/dancing_bot/mp3_libraExry/DaftPunkDerezzed.mp3
This should give you an output like this:
>>> BPM rate for /home/rdaneelolivaw/play_ground/dancing_bot/mp3_library/DaftPunkDerezzed.mp3 is estimated to be 120.0


"""
These are some notes for the testing of this package in ROS
"""
Simulation 
~/svn/robot/sources/bin/simulatorStart.sh  -ml

Initialise navegation
roslaunch reemh2_gazebo_2dnav navigation.launch

To test action services
rosrun actionlib axclient.py /motion_manager pal_control_msgs/MotionManager
