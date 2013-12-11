cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

set(PROJECT_NAME opencv_filters_alg_node)

# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)

rosbuild_init()

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#uncomment if you have defined messages
#rosbuild_genmsg()
#uncomment if you have defined services
#rosbuild_gensrv()

# added to include support for dynamic reconfiguration
rosbuild_find_ros_package(dynamic_reconfigure)
include(${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake)
gencfg()
# end dynamic reconfiguration

FIND_PACKAGE(iriutils REQUIRED)

INCLUDE_DIRECTORIES(${iriutils_INCLUDE_DIR} ./include)

#common commands for building c++ executables and libraries
#rosbuild_add_library(${PROJECT_NAME} src/example.cpp)
#target_link_libraries(${PROJECT_NAME} another_library)
#rosbuild_add_boost_directories()
#rosbuild_link_boost(${PROJECT_NAME} thread)

rosbuild_add_executable(remove_border_node src/remove_border_alg.cpp src/remove_border_alg_node.cpp)
rosbuild_add_executable(floodfill_segmentation_node src/floodfill_segmentation_alg.cpp src/floodfill_segmentation_alg_node.cpp)
rosbuild_add_executable(median_blur_node src/median_blur_alg.cpp src/median_blur_alg_node.cpp)
rosbuild_add_executable(morphological_op_node src/morphological_op_alg.cpp src/morphological_op_alg_node.cpp)
rosbuild_add_executable(remove_small_regions_node src/remove_small_regions_alg.cpp src/remove_small_regions_alg_node.cpp)
rosbuild_add_executable(fill_holes_node src/fill_holes_alg.cpp src/fill_holes_alg_node.cpp)
rosbuild_add_executable(remove_background_node src/remove_background_alg.cpp src/remove_background_alg_node.cpp)
rosbuild_add_executable(bitwise_and_node src/bitwise_and_alg.cpp src/bitwise_and_alg_node.cpp)
#rosbuild_add_executable(make_background_model_node src/make_background_model_alg.cpp src/make_background_model_alg_node.cpp)

target_link_libraries(remove_border_node ${iriutils_LIBRARY})
target_link_libraries(floodfill_segmentation_node ${iriutils_LIBRARY})
target_link_libraries(median_blur_node ${iriutils_LIBRARY})
target_link_libraries(morphological_op_node ${iriutils_LIBRARY})
target_link_libraries(remove_small_regions_node ${iriutils_LIBRARY})
target_link_libraries(fill_holes_node ${iriutils_LIBRARY})
target_link_libraries(remove_background_node ${iriutils_LIBRARY})
target_link_libraries(bitwise_and_node ${iriutils_LIBRARY})
#target_link_libraries(make_background_model_node ${iriutils_LIBRARY})
