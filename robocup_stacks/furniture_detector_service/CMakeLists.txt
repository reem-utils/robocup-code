cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)

rosbuild_init()

add_definitions(-DEIGEN_YES_I_KNOW_SPARSE_MODULE_IS_NOT_STABLE_YET -DEIGEN_DISABLE_UNALIGNED_ARRAY_ASSERT -DEIGEN_DONT_VECTORIZE)

find_package(Eigen REQUIRED)
include_directories(${Eigen_INCLUDE_DIRS})
find_package(VTK REQUIRED)
include(${VTK_USE_FILE})

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#uncomment if you have defined messages
#rosbuild_genmsg()
#uncomment if you have defined services
rosbuild_gensrv()

#common commands for building c++ executables and libraries
#rosbuild_add_library(${PROJECT_NAME} src/example.cpp)
#target_link_libraries(${PROJECT_NAME} another_library)
#rosbuild_add_boost_directories()
#rosbuild_link_boost(${PROJECT_NAME} thread)
#rosbuild_add_executable(example examples/example.cpp)
#target_link_libraries(example ${PROJECT_NAME})

rosbuild_add_executable(furniture_detector_server src/furniture_detector_service.cpp)
rosbuild_link_boost(furniture_detector_server system)
target_link_libraries(furniture_detector_server furniture_classification yaml-cpp pcl_common pcl_segmentation pcl_surface pcl_filters pcl_search pcl_features)

rosbuild_add_executable(furniture_scanner src/furniture_scanner.cpp)
rosbuild_link_boost(furniture_scanner system filesystem)
target_link_libraries(furniture_scanner pcl_io pcl_common pcl_filters)