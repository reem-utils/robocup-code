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
CMAKE_SOURCE_DIR = /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build

# Utility rule file for ROSBUILD_gensrv_cpp.

# Include the progress variables for this target.
include CMakeFiles/ROSBUILD_gensrv_cpp.dir/progress.make

CMakeFiles/ROSBUILD_gensrv_cpp: ../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h

../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: ../srv/ndesc_pc_service.srv
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/roscpp/rosbuild/scripts/gensrv_cpp.py
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/roscpp/rosbuild/scripts/genmsg_cpp.py
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/roslib/bin/gendeps
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/sensor_msgs/msg/PointCloud2.msg
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: ../msg/ndesc_pc.msg
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/std_msgs/msg/Header.msg
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/geometry_msgs/msg/Vector3.msg
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/sensor_msgs/msg/PointField.msg
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: ../msg/ndesc.msg
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: ../manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/roslang/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/roscpp/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/rospy/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/std_srvs/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/rosservice/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/stacks/dynamic_reconfigure/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/diagnostic_msgs/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/std_msgs/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/stacks/diagnostics/diagnostic_updater/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_base_algorithm/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/geometry_msgs/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/sensor_msgs/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/share/pcl/manifest.xml
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/stacks/dynamic_reconfigure/msg_gen/generated
../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h: /opt/ros/fuerte/stacks/dynamic_reconfigure/srv_gen/generated
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h"
	/opt/ros/fuerte/share/roscpp/rosbuild/scripts/gensrv_cpp.py /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/srv/ndesc_pc_service.srv

ROSBUILD_gensrv_cpp: CMakeFiles/ROSBUILD_gensrv_cpp
ROSBUILD_gensrv_cpp: ../srv_gen/cpp/include/normal_descriptor_node/ndesc_pc_service.h
ROSBUILD_gensrv_cpp: CMakeFiles/ROSBUILD_gensrv_cpp.dir/build.make
.PHONY : ROSBUILD_gensrv_cpp

# Rule to build all files generated by this target.
CMakeFiles/ROSBUILD_gensrv_cpp.dir/build: ROSBUILD_gensrv_cpp
.PHONY : CMakeFiles/ROSBUILD_gensrv_cpp.dir/build

CMakeFiles/ROSBUILD_gensrv_cpp.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ROSBUILD_gensrv_cpp.dir/clean

CMakeFiles/ROSBUILD_gensrv_cpp.dir/depend:
	cd /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build/CMakeFiles/ROSBUILD_gensrv_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ROSBUILD_gensrv_cpp.dir/depend

