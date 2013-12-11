#!/bin/bash

import os

os.system('rostopic echo /joint_states -n 1 | grep position  | cut -c11- > tmp.txt')
f = open('tmp.txt','r')
positions_raw = f.readline()
positions_raw = positions_raw[1:-2]
positions_str = positions_raw.split(',')
position = map(lambda x: float(x), positions_str)

name= ['world_joint', 'base_footprint_joint', 'base_cargo_link', 'base_center_joint', 'base_ir_01_joint', 'base_ir_02_joint', 'base_ir_03_joint', 'base_laser_joint', 'base_sonar_01_joint', 'base_sonar_02_joint', 'base_sonar_03_joint', 'base_sonar_04_joint', 'base_sonar_05_joint', 'base_sonar_06_joint', 'base_sonar_07_joint', 'base_sonar_08_joint', 'base_sonar_09_joint', 'base_sonar_10_joint', 'base_sonar_11_joint', 'base_sonar_12_joint', 'base_torso_laser_joint', 'caster_left_1_joint', 'caster_left_2_joint', 'caster_right_1_joint', 'caster_right_2_joint', 'torso_1_joint', 'torso_2_joint', 'arm_left_1_joint', 'arm_left_2_joint', 'arm_left_3_joint', 'arm_left_4_joint', 'arm_left_5_joint', 'arm_left_6_joint', 'arm_left_7_joint', 'arm_left_tool_joint', 'hand_left_palm_joint', 'hand_left_grasping_frame_joint', 'hand_left_index_1_joint', 'hand_left_index_2_joint', 'hand_left_index_3_joint', 'hand_left_middle_1_joint', 'hand_left_middle_2_joint', 'hand_left_middle_3_joint', 'hand_left_thumb_joint', 'arm_right_1_joint', 'arm_right_2_joint', 'arm_right_3_joint', 'arm_right_4_joint', 'arm_right_5_joint', 'arm_right_6_joint', 'arm_right_7_joint', 'arm_right_tool_joint', 'hand_right_palm_joint', 'hand_right_grasping_frame_joint', 'hand_right_index_1_joint', 'hand_right_index_2_joint', 'hand_right_index_3_joint', 'hand_right_middle_1_joint', 'hand_right_middle_2_joint', 'hand_right_middle_3_joint', 'hand_right_thumb_joint', 'back_camera_frame_joint', 'back_camera_gazebo_back_camera_frame_joint', 'back_camera_optical_frame_joint', 'head_1_joint', 'head_2_joint', 'base_sonar_16_joint', 'head_mount_xtion_joint', 'stereo_frame_joint', 'stereo_gazebo_l_stereo_camera_frame_joint', 'stereo_gazebo_l_stereo_camera_optical_frame_joint', 'stereo_gazebo_r_stereo_camera_frame_joint', 'stereo_gazebo_r_stereo_camera_optical_frame_joint', 'stereo_optical_frame_joint', 'torso_sonar_13_joint', 'torso_sonar_14_joint', 'torso_sonar_15_joint', 'wheel_left_joint', 'wheel_right_joint']

#position= [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7037660468233651, -0.009227562117161359, -0.6914278168965473, 0.5718789863389979, 0.0, 0.015599897166070215, 0.959815389443976, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(len(name)):
	if position[i] != 0.0:
		print str(name[i]) + " : " + str(position[i])

