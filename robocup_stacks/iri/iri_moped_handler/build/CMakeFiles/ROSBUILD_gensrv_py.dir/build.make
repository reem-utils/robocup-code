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
CMAKE_SOURCE_DIR = /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler/build

# Utility rule file for ROSBUILD_gensrv_py.

# Include the progress variables for this target.
include CMakeFiles/ROSBUILD_gensrv_py.dir/progress.make

CMakeFiles/ROSBUILD_gensrv_py: ../src/iri_moped_handler/srv/__init__.py

../src/iri_moped_handler/srv/__init__.py: ../src/iri_moped_handler/srv/_enable.py
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../src/iri_moped_handler/srv/__init__.py"
	/opt/ros/fuerte/share/rospy/rosbuild/scripts/gensrv_py.py --initpy /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler/srv/enable.srv

../src/iri_moped_handler/srv/_enable.py: ../srv/enable.srv
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/rospy/rosbuild/scripts/gensrv_py.py
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/roslib/bin/gendeps
../src/iri_moped_handler/srv/_enable.py: ../manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/roslang/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/roscpp/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/rospy/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/rosservice/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/stacks/dynamic_reconfigure/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/diagnostic_msgs/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/std_msgs/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/stacks/diagnostics/diagnostic_updater/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_base_algorithm/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/geometry_msgs/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/sensor_msgs/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/actionlib_msgs/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/rostest/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/actionlib/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_action_server/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/stacks/vision_opencv/opencv2/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/stacks/vision_opencv/cv_bridge/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/ros/core/rosbuild/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/roslib/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/rosconsole/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/stacks/pluginlib/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/message_filters/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/stacks/image_common/image_transport/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/moped2/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_actionserver/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/share/pcl/manifest.xml
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/stacks/dynamic_reconfigure/msg_gen/generated
../src/iri_moped_handler/srv/_enable.py: /opt/ros/fuerte/stacks/dynamic_reconfigure/srv_gen/generated
../src/iri_moped_handler/srv/_enable.py: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/msg_gen/generated
../src/iri_moped_handler/srv/_enable.py: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/moped/pr_msgs/srv_gen/generated
../src/iri_moped_handler/srv/_enable.py: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_actionserver/msg_gen/generated
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../src/iri_moped_handler/srv/_enable.py"
	/opt/ros/fuerte/share/rospy/rosbuild/scripts/gensrv_py.py --noinitpy /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler/srv/enable.srv

ROSBUILD_gensrv_py: CMakeFiles/ROSBUILD_gensrv_py
ROSBUILD_gensrv_py: ../src/iri_moped_handler/srv/__init__.py
ROSBUILD_gensrv_py: ../src/iri_moped_handler/srv/_enable.py
ROSBUILD_gensrv_py: CMakeFiles/ROSBUILD_gensrv_py.dir/build.make
.PHONY : ROSBUILD_gensrv_py

# Rule to build all files generated by this target.
CMakeFiles/ROSBUILD_gensrv_py.dir/build: ROSBUILD_gensrv_py
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/build

CMakeFiles/ROSBUILD_gensrv_py.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/clean

CMakeFiles/ROSBUILD_gensrv_py.dir/depend:
	cd /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler/build /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler/build /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_moped_handler/build/CMakeFiles/ROSBUILD_gensrv_py.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/depend
