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

# Include any dependencies generated for this target.
include CMakeFiles/ndesc2disk.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/ndesc2disk.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/ndesc2disk.dir/flags.make

CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: CMakeFiles/ndesc2disk.dir/flags.make
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: ../src/ndescs2disk.cpp
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: ../manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/share/roslang/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/share/roscpp/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/share/rospy/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/share/std_srvs/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/share/rosservice/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/stacks/dynamic_reconfigure/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/share/diagnostic_msgs/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/share/std_msgs/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/stacks/diagnostics/diagnostic_updater/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/iri_base_algorithm/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/share/geometry_msgs/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/share/sensor_msgs/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/share/pcl/manifest.xml
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/stacks/dynamic_reconfigure/msg_gen/generated
CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o: /opt/ros/fuerte/stacks/dynamic_reconfigure/srv_gen/generated
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o"
	/home/sampfeiffer/branches_svn/scm/bin/utils/developer_utils/g++   $(CXX_DEFINES) $(CXX_FLAGS) -ggdb  -std=c++0x -Wall -Wextra -Wno-unused-parameter -Werror=address -Werror=array-bounds  -Werror=c++0x-compat -Werror=char-subscripts -Werror=enum-compare -Werror=implicit-int -Werror=implicit-function-declaration -Werror=comment -Werror=conversion-null -Werror=div-by-zero -Werror=format -Werror=format-security -Werror=format-extra-args -Werror=init-self  -Werror=int-to-pointer-cast -Werror=missing-braces  -Werror=missing-field-initializers -Werror=return-type -Werror=nonnull  -Werror=parentheses -Werror=pointer-arith -Werror=pointer-sign -Werror=reorder -Werror=return-type -Werror=sequence-point -Werror=strict-overflow=1   -Werror=trigraphs -Werror=type-limits -Werror=unused-value -Werror=volatile-register-var -fdiagnostics-show-option -Werror=overflow -mfpmath=sse -msse3 -mssse3 -mmmx -o CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o -c /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/src/ndescs2disk.cpp

CMakeFiles/ndesc2disk.dir/src/ndescs2disk.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ndesc2disk.dir/src/ndescs2disk.i"
	/home/sampfeiffer/branches_svn/scm/bin/utils/developer_utils/g++  $(CXX_DEFINES) $(CXX_FLAGS) -ggdb  -std=c++0x -Wall -Wextra -Wno-unused-parameter -Werror=address -Werror=array-bounds  -Werror=c++0x-compat -Werror=char-subscripts -Werror=enum-compare -Werror=implicit-int -Werror=implicit-function-declaration -Werror=comment -Werror=conversion-null -Werror=div-by-zero -Werror=format -Werror=format-security -Werror=format-extra-args -Werror=init-self  -Werror=int-to-pointer-cast -Werror=missing-braces  -Werror=missing-field-initializers -Werror=return-type -Werror=nonnull  -Werror=parentheses -Werror=pointer-arith -Werror=pointer-sign -Werror=reorder -Werror=return-type -Werror=sequence-point -Werror=strict-overflow=1   -Werror=trigraphs -Werror=type-limits -Werror=unused-value -Werror=volatile-register-var -fdiagnostics-show-option -Werror=overflow -mfpmath=sse -msse3 -mssse3 -mmmx -E /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/src/ndescs2disk.cpp > CMakeFiles/ndesc2disk.dir/src/ndescs2disk.i

CMakeFiles/ndesc2disk.dir/src/ndescs2disk.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ndesc2disk.dir/src/ndescs2disk.s"
	/home/sampfeiffer/branches_svn/scm/bin/utils/developer_utils/g++  $(CXX_DEFINES) $(CXX_FLAGS) -ggdb  -std=c++0x -Wall -Wextra -Wno-unused-parameter -Werror=address -Werror=array-bounds  -Werror=c++0x-compat -Werror=char-subscripts -Werror=enum-compare -Werror=implicit-int -Werror=implicit-function-declaration -Werror=comment -Werror=conversion-null -Werror=div-by-zero -Werror=format -Werror=format-security -Werror=format-extra-args -Werror=init-self  -Werror=int-to-pointer-cast -Werror=missing-braces  -Werror=missing-field-initializers -Werror=return-type -Werror=nonnull  -Werror=parentheses -Werror=pointer-arith -Werror=pointer-sign -Werror=reorder -Werror=return-type -Werror=sequence-point -Werror=strict-overflow=1   -Werror=trigraphs -Werror=type-limits -Werror=unused-value -Werror=volatile-register-var -fdiagnostics-show-option -Werror=overflow -mfpmath=sse -msse3 -mssse3 -mmmx -S /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/src/ndescs2disk.cpp -o CMakeFiles/ndesc2disk.dir/src/ndescs2disk.s

CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o.requires:
.PHONY : CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o.requires

CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o.provides: CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o.requires
	$(MAKE) -f CMakeFiles/ndesc2disk.dir/build.make CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o.provides.build
.PHONY : CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o.provides

CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o.provides.build: CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o

# Object files for target ndesc2disk
ndesc2disk_OBJECTS = \
"CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o"

# External object files for target ndesc2disk
ndesc2disk_EXTERNAL_OBJECTS =

../bin/ndesc2disk: CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o
../bin/ndesc2disk: CMakeFiles/ndesc2disk.dir/build.make
../bin/ndesc2disk: CMakeFiles/ndesc2disk.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable ../bin/ndesc2disk"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ndesc2disk.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/ndesc2disk.dir/build: ../bin/ndesc2disk
.PHONY : CMakeFiles/ndesc2disk.dir/build

CMakeFiles/ndesc2disk.dir/requires: CMakeFiles/ndesc2disk.dir/src/ndescs2disk.o.requires
.PHONY : CMakeFiles/ndesc2disk.dir/requires

CMakeFiles/ndesc2disk.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ndesc2disk.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ndesc2disk.dir/clean

CMakeFiles/ndesc2disk.dir/depend:
	cd /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build /home/sampfeiffer/branches_svn/migration/ROBOCUP_STACKS_INTEGRATION/stacks/robocup_stacks/iri/normal_descriptor_node/build/CMakeFiles/ndesc2disk.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ndesc2disk.dir/depend
