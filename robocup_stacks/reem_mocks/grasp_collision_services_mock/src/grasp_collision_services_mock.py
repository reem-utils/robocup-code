#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('grasp_collision_services_mock')
import rospy
from std_srvs.srv import Empty, EmptyResponse
from tabletop_collision_map_processing.srv import TabletopCollisionMapProcessing, TabletopCollisionMapProcessingResponse
from arm_navigation_msgs.srv import GetPlanningScene, GetPlanningSceneResponse

def octomat_reset_cb(req):
    rospy.loginfo('Octomap Reset \'/octomap_server/reset was called')
    return EmptyResponse()
s_octomat_reset = {'name': '/octomap_server/reset', 'service_class': Empty, 'handler': octomat_reset_cb}


def snapshot_reset_cb(req):
    rospy.loginfo('Snapshot Reset \'/xtion_snapshotter/snapshot was called')
    return EmptyResponse()
s_snapshot_reset = {'name': '/xtion_snapshotter/snapshot', 'service_class': Empty, 'handler': snapshot_reset_cb}


def collision_map_reset_cb(req):
    rospy.loginfo('Collision Map Reset \'/tabletop_collision_map_processing/tabletop_collision_map_processing was called')
    return TabletopCollisionMapProcessingResponse()
s_collision_map_reset = {'name': '/tabletop_collision_map_processing/tabletop_collision_map_processing', 'service_class': TabletopCollisionMapProcessing, 'handler': collision_map_reset_cb}


def environment_server_cb(req):
    rospy.loginfo('Environment Server \'/environment_server/set_planning_scene_diff was called')
    return GetPlanningSceneResponse()
s_environment_server = {'name': '/environment_server/set_planning_scene_diff', 'service_class': GetPlanningScene, 'handler': environment_server_cb}


if __name__ == '__main__':
    rospy.init_node('grasp_collision_services_mock')

    rospy.Service(**s_octomat_reset)
    rospy.Service(**s_snapshot_reset)
    rospy.Service(**s_collision_map_reset)
    rospy.Service(**s_environment_server)

    rospy.spin()
