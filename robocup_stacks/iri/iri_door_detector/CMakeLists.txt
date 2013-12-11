cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

set(PROJECT_NAME door_detector_alg_node)

# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)
find_package(Eigen REQUIRED)
include_directories(${Eigen_INCLUDE_DIRS})

rosbuild_find_ros_package(actionlib_msgs)
include(${actionlib_msgs_PACKAGE_PATH}/cmake/actionbuild.cmake)
genaction()

rosbuild_init()

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#uncomment if you have defined messages
rosbuild_genmsg()
#uncomment if you have defined services
#rosbuild_gensrv()

# added to include support for dynamic reconfiguration
rosbuild_find_ros_package(dynamic_reconfigure)
include(${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake)
gencfg()
# end dynamic reconfiguration

FIND_PACKAGE(iriutils REQUIRED)
FIND_PACKAGE(OpenCV REQUIRED)

INCLUDE_DIRECTORIES(${iriutils_INCLUDE_DIR} ./include)
INCLUDE_DIRECTORIES(${cvBlob_SOURCE_DIR} ./include)

#common commands for building c++ executables and libraries
#rosbuild_add_library(${PROJECT_NAME} src/example.cpp)
#target_link_libraries(${PROJECT_NAME} another_library)
#rosbuild_add_boost_directories()
#rosbuild_link_boost(${PROJECT_NAME} thread)

rosbuild_add_executable(closed_door_detector src/closed_door_detector_alg.cpp src/closed_door_detector_alg_node.cpp)
target_link_libraries(closed_door_detector ${iriutils_LIBRARY})
target_link_libraries(closed_door_detector cvblob)

rosbuild_add_executable(open_door_detector src/open_door_detector_alg.cpp src/open_door_detector_alg_node.cpp)
target_link_libraries(open_door_detector ${iriutils_LIBRARY})

rosbuild_add_executable(door_cloud src/door_cloud_alg.cpp src/door_cloud_alg_node.cpp)
target_link_libraries(door_cloud ${iriutils_LIBRARY})

rosbuild_add_executable(door_detector_actions src/door_detector_actions_alg.cpp src/door_detector_actions_alg_node.cpp)
target_link_libraries(door_detector_actions ${iriutils_LIBRARY})

#rosbuild_add_pyunit(smach_action_clients/See_Wait_N_Walk.py)
#rosbuild_add_pyunit(smach_action_clients/Open_The_Door.py)


