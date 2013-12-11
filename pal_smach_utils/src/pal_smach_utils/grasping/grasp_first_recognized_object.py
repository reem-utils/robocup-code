#! /usr/bin/env python

import roslib
import rospy
import copy
import smach
#import smach_ros
import actionlib
import math

from smach_ros import SimpleActionState, ServiceState
#from roslib import packages


from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pr_msgs.msg import ObjectPoseList, ObjectPose

from geometry_msgs.msg import Pose, Point, Quaternion
# from control_msgs.msg import *

from smach_ros import SimpleActionState, ServiceState
#from std_msgs import *
from pal_smach_utils.utils.global_common import *
from reem_tabletop_manipulation_launch.msg import GraspTargetAction, GraspTargetGoal
from actionlib_msgs.msg import GoalStatus

from coord_translator.srv import ObjectTranslator, ObjectTranslatorRequest, ObjectTranslatorDataBase, ObjectTranslatorDataBaseRequest


class Check_object_to_search_for(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys=['object_to_search_for', 'object_found'], output_keys=['object_id_from_name'])

    def execute(self, userdata):
        if len(userdata.object_to_search_for) > 1:  # objects should have a name bigger than 1 char
            return succeeded
        else:
            rospy.loginfo("Going to search anything")
            userdata.object_id_from_name = -1  # setting -1 means search anything
            return aborted


class GraspFirstRecognizedObjectStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
            input_keys=['object_to_search_for'],
            output_keys=['object_found'])


        with self:

            smach.StateMachine.add(
                    'Check_object_to_search_for',
                    Check_object_to_search_for(),
                    transitions = {succeeded: 'Get_object_databaseID', aborted: 'Grasp_target_action'})


            @smach.cb_interface(input_keys=['object_to_search_for'], output_keys=['object_id_from_name'])
            def loc_response_cb(userdata, response):
                if response.exists:
                    if response.databaseID != 0:
                        userdata.object_id_from_name = response.databaseID
                        rospy.loginfo("Got databaseID " + str(response.databaseID) + " for object " + userdata.object_to_search_for)
                        return succeeded
                    else:
                        rospy.logerr( "Object " + userdata.object_to_search_for + " not in coord_translator!")
                else:
                    rospy.logerr("We got no response from coord_translator, object " + userdata.object_to_search_for + " not in coord_translator")
                return aborted

            def loc_request_cb(userdata, request):
                req = ObjectTranslatorRequest()
                req.objname = userdata.object_to_search_for
                rospy.loginfo( "Asking coord_translator for " + req.objname )
                return req

            smach.StateMachine.add(
                'Get_object_databaseID',
                ServiceState('/object_translator', ObjectTranslator,
                    response_cb=loc_response_cb,
                    request_cb=loc_request_cb,
                    input_keys=['object_to_search_for'],
                    output_keys=['object_name_from_id']),
                    remapping={'object_id_from_name': 'object_id_from_name'},
                    transitions={succeeded: 'Grasp_target_action', aborted: aborted})

            def grasp_target_goal_cb(userdata, old_goal):
                grasp_target_goal = GraspTargetGoal()
                grasp_target_goal.onlyPerception = False  # this SM is only for perception!
                grasp_target_goal.appearanceID = userdata.object_to_search_for 
                grasp_target_goal.databaseID = userdata.object_id_from_name
                rospy.loginfo("GraspTargetGoal:\n" + str(grasp_target_goal))
                return grasp_target_goal

                
            def grasp_target_result_cb(userdata, status, result):
                #rospy.loginfo("Result of the cb: result: " + str(result) )
                # result is:
                # int32 status
                # copy of the tabletop detection result
                # tabletop_object_detector/TabletopDetectionResult detectionResult
                # int32 NO_CLOUD_RECEIVED=1
                # int32 NO_TABLE=2
                # int32 OTHER_ERROR=3
                # int32 SUCCESS=4
                # tabletop_object_detector/Table table
                #   geometry_msgs/PoseStamped pose
                #     std_msgs/Header header
                #       uint32 seq
                #       time stamp
                #       string frame_id
                #     geometry_msgs/Pose pose
                #       geometry_msgs/Point position
                #         float64 x
                #         float64 y
                #         float64 z
                #       geometry_msgs/Quaternion orientation
                #         float64 x
                #         float64 y
                #         float64 z
                #         float64 w
                #   float32 x_min
                #   float32 x_max
                #   float32 y_min
                #   float32 y_max
                #   arm_navigation_msgs/Shape convex_hull
                #     byte SPHERE=0
                #     byte BOX=1
                #     byte CYLINDER=2
                #     byte MESH=3
                #     byte type
                #     float64[] dimensions
                #     int32[] triangles
                #     geometry_msgs/Point[] vertices
                #       float64 x
                #       float64 y
                #       float64 z
                # sensor_msgs/PointCloud[] clusters
                #   std_msgs/Header header
                #     uint32 seq
                #     time stamp
                #     string frame_id
                #   geometry_msgs/Point32[] points
                #     float32 x
                #     float32 y
                #     float32 z
                #   sensor_msgs/ChannelFloat32[] channels
                #     string name
                #     float32[] values
                # household_objects_database_msgs/DatabaseModelPoseList[] models
                #   household_objects_database_msgs/DatabaseModelPose[] model_list
                #     int32 model_id
                #     geometry_msgs/PoseStamped pose
                #       std_msgs/Header header
                #         uint32 seq
                #         time stamp
                #         string frame_id
                #       geometry_msgs/Pose pose
                #         geometry_msgs/Point position
                #           float64 x
                #           float64 y
                #           float64 z
                #         geometry_msgs/Quaternion orientation
                #           float64 x
                #           float64 y
                #           float64 z
                #           float64 w
                #     float32 confidence
                #     string detector_name
                # int32[] cluster_model_indices
                # int32 result


                # here parse the result and compose a ObjectPoseList of what we found and return it in the output key object_found
                obj = ObjectPoseList()
                # Header header
                # ObjectPose[] object_list
                # time originalTimeStamp
                # time requestTimeStamp
                obj.header = result.detectionResult.table.pose.header  # just copying some header

                obj.object_list = [None] * 10  # ugly way to allocate space in python
                # obj.object_list[0] = ObjectPose() # only putting the "interesting result" for now
                # string name
                # geometry_msgs/Pose pose
                # geometry_msgs/Point32 pose2D
                # int16[] convex_hull_x
                # int16[] convex_hull_y
                # float32 mean_quality
                # int16 used_points
                # NameTypeValue[] properties
                # geometry_msgs/Pose[] pose_uncertainty_list

                #obj.object_list[0].name = userdata.object_to_search_for
                #rospy.loginfo("result.detectionResult.models:\n" + str(result.detectionResult.models))
                num_object = 0
                i=0
                try:
                    for i in range(0, 10):  # there wont be more objects, come on!
                        if result.detectionResult.models[i].model_list[0].model_id == userdata.object_id_from_name or userdata.object_id_from_name <= 0:  # I think we only get one returned anyways
                            obj.object_list[num_object] = ObjectPose()
                            if userdata.object_id_from_name > 0:
                                obj.object_list[num_object].name = userdata.object_to_search_for
                                obj.object_list[num_object].pose = result.detectionResult.models[i].model_list[0].pose.pose
                                break
                            else:
                                rospy.wait_for_service('object_translator_dataBase')
                                obj_trans_db = rospy.ServiceProxy('object_translator_dataBase', ObjectTranslatorDatabase)
                                obj_info = obj_trans_db(result.detectionResult.models[i].model_list[0].model_id)
                                obj.object_list[num_object].name = obj_info.objname
                                obj.object_list[num_object].pose = result.detectionResult.models[i].model_list[0].pose.pose
                                num_object += 1
                except Exception: 
                    # rospy.loginfo("Exception when looping over result.detectionResult.models[" + str(i) + "]")
                    # rospy.loginfo("result.detectionResult.models[i] looks like:\n" + str(result.detectionResult.models[i]))
                    pass  # this exception should be that we are looping too far...

                # for item, value in result.detectionResult.models.items():  # AttributeError: 'list' object has no attribute 'items' ITS A FUCKING LIST??? WTF
                #     rospy.loginfo("item: " + item + "\n value: " + value) 

                # for i in range(len(result.detectionResult.models)):  # TypeError: object of type 'DatabaseModelPoseList' has no len()
                #     for j in range(len(result.detectionResult.models[i])):
                #         if result.detectionResult.models[i].model_list[j].model_id == userdata.object_id_from_name:
                #             obj.object_list[0].pose = result.detectionResult.models[i].model_list[j].pose.pose

                # CANT DO THIS BECAUSE PYTHON KEEPS SAYING THIS IS NOT ITERABLE /CRY       
                # for model_list in result.detectionResult.models:  # TypeError: 'DatabaseModelPoseList' object is not iterable # maybe this is a UserDict? 
                #     for model in model_list:
                #         if model.model_id == userdata.object_id_from_name:
                #             obj.object_list[0].pose = model.pose.pose

                userdata.object_found = obj
                rospy.loginfo("userdata.object_found generated as: " + str(obj) )

                if status == GoalStatus.SUCCEEDED:
                    return succeeded
                if status == GoalStatus.ABORTED:
                    return aborted
                #return 'my_outcome'

            smach.StateMachine.add(
                'Grasp_target_action',
                SimpleActionState(
                    'tabletop_grasping_node',
                    GraspTargetAction,
                    goal_cb = grasp_target_goal_cb,
                    result_cb = grasp_target_result_cb,
                    input_keys = ['object_to_search_for', 'object_id_from_name'],
                    output_keys = ['object_found']),
                transitions = {succeeded: succeeded, aborted: aborted})  


            # Lift up arm

            # put in travel position

