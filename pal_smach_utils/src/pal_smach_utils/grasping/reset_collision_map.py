#! /usr/bin/env python

import smach

from smach_ros import ServiceState

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from std_srvs.srv import Empty, EmptyRequest
from arm_navigation_msgs.srv import GetPlanningScene, GetPlanningSceneRequest
from arm_navigation_msgs.msg import CollisionObject, CollisionObjectOperation
from tabletop_collision_map_processing.srv import TabletopCollisionMapProcessing, TabletopCollisionMapProcessingRequest


class ResetCollisionMapStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:
            # reset collision map
            def reset1_request_cb(userdata, request):
            	print "Creating empty request for octomap_server"
                empty_request = EmptyRequest()
                return empty_request

            smach.StateMachine.add(
                'RESET_COLLISION_MAP_STEP_1_OCTOMAP',
                ServiceState('/octomap_server/reset',
                	Empty,
                    request_cb=reset1_request_cb),
                    transitions={succeeded: 'RESET_COLLISION_MAP_STEP_2_SNAPSHOT', aborted: aborted} )

            def request2_request_cb(userdata, request):
                print "Creating empty request for xtion_snapshotter"
                empty_request = EmptyRequest()
                return empty_request

            smach.StateMachine.add(
                'RESET_COLLISION_MAP_STEP_2_SNAPSHOT',
                ServiceState('/xtion_snapshotter/snapshot',
                    Empty,
                    request_cb=request2_request_cb),
                    transitions={succeeded: 'RESET_COLLISION_MAP_STEP_3_COLLISION_PROCESSING', aborted: aborted} )
            

            def reset3_request_cb(userdata, request):
                print "Creating resetting request for tabletop_collision_map_processing"
                deleting_request = TabletopCollisionMapProcessingRequest()
                deleting_request.reset_collision_models = True
                deleting_request.reset_attached_models = True

                return deleting_request

            smach.StateMachine.add(
                'RESET_COLLISION_MAP_STEP_3_COLLISION_PROCESSING',
                ServiceState('/tabletop_collision_map_processing/tabletop_collision_map_processing', TabletopCollisionMapProcessing,
                    request_cb=reset3_request_cb),
                    transitions={succeeded: 'RESET_COLLISION_MAP_STEP_4_ENV_SERVER', aborted: aborted})

            def reset4_request_cb(userdata, request):
            	print "Creating empty request for environment_server"
                empty_request = GetPlanningSceneRequest()
                # I dont think this is needed anymore but as its working i dont want to touch it
                col_obj = CollisionObject()
                col_obj.operation.operation = CollisionObjectOperation.REMOVE
                col_obj.id = "table"  # die you bastard

                empty_request.planning_scene_diff.collision_objects.append(col_obj)
                return empty_request

            smach.StateMachine.add(
                'RESET_COLLISION_MAP_STEP_4_ENV_SERVER',
                ServiceState('/environment_server/set_planning_scene_diff', GetPlanningScene,
                    request_cb=reset4_request_cb),
                    transitions={succeeded: succeeded, aborted: aborted})
