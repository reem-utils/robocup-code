# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/build

# Utility rule file for ROSBUILD_gensrv_cpp.

# Include the progress variables for this target.
include CMakeFiles/ROSBUILD_gensrv_cpp.dir/progress.make

CMakeFiles/ROSBUILD_gensrv_cpp: ../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h
CMakeFiles/ROSBUILD_gensrv_cpp: ../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h

../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: ../srv/GeoVwDetection.srv
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/roscpp/rosbuild/scripts/gensrv_cpp.py
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/roscpp/rosbuild/scripts/genmsg_cpp.py
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/roslib/bin/gendeps
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/sensor_msgs/msg/Image.msg
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/std_msgs/msg/Header.msg
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg/GeoVwSet.msg
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: ../msg/ObjectBox.msg
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg/GeoVw.msg
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg/ImagePoint.msg
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: ../manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/roslang/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/roscpp/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/rospy/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/rosservice/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/dynamic_reconfigure/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/diagnostic_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/std_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/diagnostics/diagnostic_updater/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_base_algorithm/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/std_srvs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/geometry_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/sensor_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/pcl/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/rostest/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/actionlib_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/actionlib/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_action_server/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_publish_params/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/visualization_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/vision_opencv/opencv2/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/vision_opencv/cv_bridge/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_sift/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_plane_segmentation_pcl_rgb/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_opencv_filters/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/rosbag/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/ros/core/rosbuild/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/roslib/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/rosconsole/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/pluginlib/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/bond_core/bond/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/bond_core/smclib/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/bond_core/bondcpp/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/nodelet_core/nodelet/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/message_filters/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/nodelet_core/nodelet_topic_tools/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/bullet/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/geometry/angles/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/share/roswtf/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/geometry/tf/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/common_rosdeps/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/perception_pcl/pcl_ros/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/dynamic_reconfigure/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/dynamic_reconfigure/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_publish_params/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_publish_params/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_sift/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/bond_core/bond/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/nodelet_core/nodelet/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/geometry/tf/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h: /opt/ros/fuerte/stacks/geometry/tf/srv_gen/generated
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h"
	/opt/ros/fuerte/share/roscpp/rosbuild/scripts/gensrv_cpp.py /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/srv/GeoVwDetection.srv

../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: ../srv/RefineGraspPoint.srv
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/roscpp/rosbuild/scripts/gensrv_cpp.py
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/roscpp/rosbuild/scripts/genmsg_cpp.py
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/roslib/bin/gendeps
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/sensor_msgs/msg/Image.msg
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg/DescriptorSet.msg
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/std_msgs/msg/Header.msg
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/geometry_msgs/msg/Vector3.msg
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: ../msg/ObjectBox.msg
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg/Descriptor.msg
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg/ImagePoint.msg
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: ../manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/roslang/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/roscpp/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/rospy/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/rosservice/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/dynamic_reconfigure/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/diagnostic_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/std_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/diagnostics/diagnostic_updater/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_base_algorithm/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/std_srvs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/geometry_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/sensor_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/pcl/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/rostest/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/actionlib_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/actionlib/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_action_server/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_publish_params/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/visualization_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/vision_opencv/opencv2/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/vision_opencv/cv_bridge/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_sift/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_plane_segmentation_pcl_rgb/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_opencv_filters/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/rosbag/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/ros/core/rosbuild/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/roslib/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/rosconsole/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/pluginlib/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/bond_core/bond/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/bond_core/smclib/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/bond_core/bondcpp/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/nodelet_core/nodelet/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/message_filters/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/nodelet_core/nodelet_topic_tools/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/bullet/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/geometry/angles/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/share/roswtf/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/geometry/tf/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/common_rosdeps/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/perception_pcl/pcl_ros/manifest.xml
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/dynamic_reconfigure/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/dynamic_reconfigure/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_publish_params/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_publish_params/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_perception_msgs/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_sift/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/bond_core/bond/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/nodelet_core/nodelet/srv_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/geometry/tf/msg_gen/generated
../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h: /opt/ros/fuerte/stacks/geometry/tf/srv_gen/generated
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h"
	/opt/ros/fuerte/share/roscpp/rosbuild/scripts/gensrv_cpp.py /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/srv/RefineGraspPoint.srv

ROSBUILD_gensrv_cpp: CMakeFiles/ROSBUILD_gensrv_cpp
ROSBUILD_gensrv_cpp: ../srv_gen/cpp/include/iri_bow_object_detector/GeoVwDetection.h
ROSBUILD_gensrv_cpp: ../srv_gen/cpp/include/iri_bow_object_detector/RefineGraspPoint.h
ROSBUILD_gensrv_cpp: CMakeFiles/ROSBUILD_gensrv_cpp.dir/build.make
.PHONY : ROSBUILD_gensrv_cpp

# Rule to build all files generated by this target.
CMakeFiles/ROSBUILD_gensrv_cpp.dir/build: ROSBUILD_gensrv_cpp
.PHONY : CMakeFiles/ROSBUILD_gensrv_cpp.dir/build

CMakeFiles/ROSBUILD_gensrv_cpp.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ROSBUILD_gensrv_cpp.dir/clean

CMakeFiles/ROSBUILD_gensrv_cpp.dir/depend:
	cd /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/build /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/build /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_bow_object_detector/build/CMakeFiles/ROSBUILD_gensrv_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ROSBUILD_gensrv_cpp.dir/depend

