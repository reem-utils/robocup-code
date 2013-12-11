#! /usr/bin/env python
# vim: expandtab ts=4 sw=4
### FOLOW_OPERATOR.PY ###

import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted, transform_pose

from move_base_msgs.msg import MoveBaseGoal

from pal_smach_utils.navigation.move_action import MoveActionState

from smach import CBState
from visualization_msgs.msg import Marker

import rosbag
from roslib import packages

import dynamic_reconfigure.client

from pal_smach_utils.utils.math_utils import euclidean_distance

from pal_smach_utils.utils.debug import debugPrint, getDebugLevel

from geometry_msgs.msg import Pose


node_to_reconfigure = "/move_by/move_base/PalLocalPlanner"


class ElevatorHandling(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])
        with self:

            @smach.cb_interface(outcomes=[succeeded])
            def printOdometryBag(userdata):
                '''
                bag = rosbag.Bag(packages.get_pkg_dir('common') + '/config/getin_odometry.bag')

                odometry_marker_pub = rospy.Publisher("/track_operator/odometry_elevator", Marker)
                i = 0
                for topic, msg, t in bag.read_messages(topics=['/base_odometry/odom']):
                    #rospy.loginfo(str(topic) + '\n\n\n')
                    #rospy.loginfo(str(msg) + '\n\n\n')
                    #rospy.loginfo(str(t) + '\n\n\n')

                    marker = Marker()
                    marker.header.frame_id = "/odom"
                    marker.ns = "odometry_elevator_namespace"
                    marker.id = i
                    marker.type = marker.SPHERE
                    marker.action = marker.ADD
                    marker.pose = msg.pose.pose
                    marker.scale.x = 0.5
                    marker.scale.y = 0.7
                    marker.scale.z = 0.9
                    marker.color.a = 1.0
                    marker.color.r = 0.0
                    marker.color.g = 1.0
                    marker.color.b = 1.0
                    marker.lifetime = rospy.Duration(600.0)
                    marker.header.stamp = rospy.Time.now()

                    rospy.loginfo("\033[00;32m" + str(marker) + "\033[m")

                    odometry_marker_pub.publish(marker)

                    i += 1
                bag.close()
                '''

                bag = rosbag.Bag(packages.get_pkg_dir('common') + '/config/getin_odometry.bag')

                odometry_marker_pub = rospy.Publisher("/track_operator/baselink_to_odometry_elevator", Marker)
                i = 0
                stack = []
                for topic, msg, t in bag.read_messages(topics=['/base_odometry/odom']):
                    #rospy.loginfo(str(topic) + '\n\n\n')
                    #rospy.loginfo(str(msg) + '\n\n\n')
                    #rospy.loginfo(str(t) + '\n\n\n')

                    pose_transformed = transform_pose(msg.pose.pose, '/odom', '/base_link')
                    if (getDebugLevel() >= 3):
                        marker = Marker()
                        marker.header.frame_id = "/base_link"
                        marker.ns = "baselink_to_odometry_elevator_namespace"
                        marker.id = i
                        marker.type = marker.SPHERE
                        marker.action = marker.ADD
                        marker.pose = pose_transformed
                        marker.scale.x = 0.05
                        marker.scale.y = 0.05
                        marker.scale.z = 0.05
                        marker.color.a = 1.0
                        marker.color.r = 0.0
                        marker.color.g = 0.0
                        marker.color.b = 1.0
                        marker.lifetime = rospy.Duration(600.0)
                        marker.header.stamp = rospy.Time.now()
                        odometry_marker_pub.publish(marker)

                        debugPrint("\033[01;33m" + str(marker) + "\033[m", 3)

                    stack.append(pose_transformed)

                    i += 1
                bag.close()

                #TODO SHOULD WORK MOST OF THE TIMES, BUT IF THE BAG IS EMPTY OR WHITH LESS THAN 2 POSES THIS CODE WILL CRASH!!!
                try:
                    initial_pose = stack.pop()
                    final_pose = stack.pop()
                    last_dist = euclidean_distance(initial_pose, final_pose)
                    while (len(stack) > 0 and last_dist < 2.0):
                        new_final_pose = stack.pop()
                        new_dist = euclidean_distance(new_final_pose, initial_pose)
                        if (new_dist > last_dist):
                            last_dist = new_dist
                            final_pose = new_final_pose
                except Exception as ex:
                    debugPrint(str(ex), 0)
                    debugPrint("The bag was empty. Setting a final pose of 2 meters backwards...", 0)
                    initial_pose = Pose()
                    initial_pose.position.x = 0.0
                    initial_pose.position.y = 0.0
                    final_pose = Pose()
                    final_pose.position.x = -2.0
                    final_pose.position.y = 0.0

                marker = Marker()
                marker.header.frame_id = "/base_link"
                marker.ns = "baselink_to_odometry_elevator_namespace"
                marker.id = i
                marker.type = marker.CYLINDER
                marker.action = marker.ADD
                marker.pose = initial_pose
                marker.scale.x = 0.1
                marker.scale.y = 0.1
                marker.scale.z = 2.0
                marker.color.a = 1.0
                marker.color.r = 0.0
                marker.color.g = 1.0
                marker.color.b = 0.0
                marker.lifetime = rospy.Duration(600.0)
                marker.header.stamp = rospy.Time.now()

                debugPrint("    Publishing \033[01;32m(GREEN)\033[mmarker of the INITIAL pose outside the elevator...", 3)
                debugPrint(rospy.loginfo("\033[01;32m" + str(marker) + "\033[m"), 3)

                odometry_marker_pub.publish(marker)

                marker = Marker()
                marker.header.frame_id = "/base_link"
                marker.ns = "baselink_to_odometry_elevator_namespace"
                marker.id = i + 1
                marker.type = marker.CYLINDER
                marker.action = marker.ADD
                marker.pose = final_pose
                marker.scale.x = 0.1
                marker.scale.y = 0.1
                marker.scale.z = 1.0
                marker.color.a = 1.0
                marker.color.r = 1.0
                marker.color.g = 0.0
                marker.color.b = 0.0
                marker.lifetime = rospy.Duration(600.0)
                marker.header.stamp = rospy.Time.now()

                debugPrint("    Publishing \033[01;33m(RED)\033[mmarker of the FINAL pose outside the elevator...", 3)
                debugPrint("    \033[01;33m" + str(marker) + "\033[m", 3)

                odometry_marker_pub.publish(marker)

                userdata.final_pose = final_pose

                return succeeded

            smach.StateMachine.add('PRINT_ODOMETRY_BAG_AND_SELECT_FINAL_POSE',
                                   CBState(printOdometryBag, output_keys=['final_pose']),
                                   transitions={succeeded: 'LEAVE_ELEVATOR_HANDLING'},
                                   remapping={'final_pose': 'final_pose'})

            def leaveElevatorCallback(userdata, nav_goal):

                new_travel_speed_sfl = 0.1
                new_point_b_sfl = -0.26
                new_enable_oa = False

                node_to_reconfigure = "/move_by/move_base/PalLocalPlanner"

                client = dynamic_reconfigure.client.Client(node_to_reconfigure)
                old_config = client.update_configuration({})

                rospy.loginfo('    Gathering planner parameters values to recover later...')
                userdata.old_travel_speed_sfl = old_config.travel_speed_sfl
                userdata.old_point_b_sfl = old_config.point_b_sfl
                userdata.old_enable_oa = old_config.enable_oa

                rospy.loginfo('    Tunning planner parameters values of the robot to leave elevator backwards...')
                new_params = {'travel_speed_sfl': new_travel_speed_sfl, 'point_b_sfl': new_point_b_sfl, 'enable_oa': new_enable_oa}
                new_config = client.update_configuration(new_params)

                rospy.loginfo('    Planner parameters values reconfigured. The new values are:')
                rospy.loginfo('        travel_speed_sfl : ' + str(new_travel_speed_sfl) + " => " + str(new_config.travel_speed_sfl))
                rospy.loginfo('        point_b_sfl      : ' + str(new_point_b_sfl) + " => " + str(new_config.point_b_sfl))
                rospy.loginfo('        enable_oa        : ' + str(new_enable_oa) + " => " + str(new_config.enable_oa))

                leave_goal = MoveBaseGoal()
                leave_goal.target_pose.header.stamp = rospy.Time.now()
                leave_goal.target_pose.header.frame_id = "/base_link"
                leave_goal.target_pose.pose = userdata.final_pose

                rospy.loginfo('    Leaving elevator...i\'m going backwards to ' + str(userdata.final_pose))

                return leave_goal

            smach.StateMachine.add('LEAVE_ELEVATOR_HANDLING',
                                   MoveActionState(
                                       move_base_action_name='/move_by/move_base',
                                       goal_cb=leaveElevatorCallback,
                                       input_keys=['final_pose'],
                                       output_keys=['old_enable_oa', 'old_travel_speed_sfl', 'old_point_b_sfl']),
                                   transitions={succeeded: 'RECOVER_OLD_PLANNER_PARAMETERS',
                                                aborted: 'RECOVER_OLD_PLANNER_PARAMETERS'},
                                   remapping={'old_enable_oa': 'old_enable_oa',
                                              'old_travel_speed_sfl': 'old_travel_speed_sfl',
                                              'old_point_b_sfl': 'old_point_b_sfl'})

            @smach.cb_interface(outcomes=[succeeded])
            def recoverOldPlannerParameters(userdata):

                rospy.loginfo('    Recovering old planner parameters values...')
                client = dynamic_reconfigure.client.Client(node_to_reconfigure)
                params = {'travel_speed_sfl': userdata.old_travel_speed_sfl, 'point_b_sfl': userdata.old_point_b_sfl, 'enable_oa': userdata.old_enable_oa}
                new_config = client.update_configuration(params)

                rospy.loginfo('    Planner parameters values reconfigured. The new values are:')
                rospy.loginfo('        travel_speed_sfl : ' + str(userdata.old_travel_speed_sfl) + " => " + str(new_config.travel_speed_sfl))
                rospy.loginfo('        point_b_sfl      : ' + str(userdata.old_point_b_sfl) + " => " + str(new_config.point_b_sfl))
                rospy.loginfo('        enable_oa        : ' + str(userdata.old_enable_oa) + " => " + str(new_config.enable_oa))
                return succeeded

            smach.StateMachine.add('RECOVER_OLD_PLANNER_PARAMETERS',
                                   CBState(recoverOldPlannerParameters, input_keys=['old_enable_oa', 'old_travel_speed_sfl', 'old_point_b_sfl']),
                                   transitions={succeeded: succeeded})
