#! /usr/bin/env python

import rospy
import smach

from smach_ros import SimpleActionState, ServiceState


from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pr_msgs.msg import ObjectPoseList, ObjectPose

from reem_tabletop_manipulation_launch.msg import GraspTargetAction, GraspTargetGoal
from actionlib_msgs.msg import GoalStatus
from coord_translator.srv import ObjectTranslator, ObjectTranslatorRequest, ObjectTranslatorDataBase  # , ObjectTranslatorDataBaseRequest
from pr2_controllers_msgs.msg import PointHeadGoal, PointHeadAction
from pal_smach_utils.grasping.reset_collision_map import ResetCollisionMapStateMachine
from arm_navigation_msgs.msg import MoveArmAction
from pal_smach_utils.grasping.arm_and_hand_goals import get_arm_goal_for_arm_elbow_back, get_fully_open_hand, get_arm_goal_for_arm_travelling_position
from reem_final_approach.srv import FinalApproachPose, FinalApproachPoseRequest
from control_msgs.msg import FollowJointTrajectoryAction
from pal_smach_utils.utils.global_common import  set_grasp_error


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


class ScanForObjectAndGraspStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
            input_keys=['object_to_search_for'],
            output_keys=['object_found'])

        with self:

            def generic_action_result_cb(userdata, status, result):
                """ Generic action result callback that set grasp error if the status is not succeeded. """
                set_grasp_error(str(self._current_label) + " failed", status)

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
                        set_grasp_error("Object " + userdata.object_to_search_for + " not in coord_translator!")
                else:
                    set_grasp_error("We got no response from coord_translator, object " + userdata.object_to_search_for + " not in coord_translator")
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
                    transitions={succeeded: 'Scan_table_for_moving_arm_to_elbow_up', aborted: aborted})

            # Scan with head and put elbow pose
            def grasp_target_goal_cb(userdata, old_goal):
                scan_goal = PointHeadGoal()
                return scan_goal

            smach.StateMachine.add(
                'Scan_table_for_moving_arm_to_elbow_up',
                SimpleActionState(
                    '/head_traj_controller/head_scan_snapshot_action',
                    PointHeadAction,
                    goal_cb = grasp_target_goal_cb, result_cb=generic_action_result_cb),
                    transitions = {succeeded: 'Arm_to_elbow_up_pre_grasp', aborted: aborted})  

            def arm_result_cb(userdata, result_status, result):
                if result_status != GoalStatus.SUCCEEDED:  # SUCCEEDED = 3 http://www.ros.org/doc/api/move_arm_msgs/html/msg/MoveArmActionResult.html
                    set_grasp_error("MoveArmActionResult result wasn't succeeded, was: " + str(result_status) +
                    "\nmessage: \n" + str(result))
                    # if result.error_code.val == 1: # SUCCESS
                    #     rospy.loginfo("But we got SUCCESS as the result, so the planner will replan by itself.")
                    #     return succeeded
                    return aborted
                else:
                    return succeeded

            def arm_goal_cb(userdata, old_goal):
                #arm_goal = get_arm_goal(get_pose_intermediate_position(), frame_id="/base_link")
                arm_goal = get_arm_goal_for_arm_elbow_back()
                return arm_goal

            smach.StateMachine.add(
                'Arm_to_elbow_up_pre_grasp',
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal_cb=arm_goal_cb,
                    result_cb=arm_result_cb),
                transitions={succeeded: 'Grasp_target_action', aborted: aborted}) 


            # RESET collision map   NO LONGER NEEDED, NOT TOTALLY SURE, THIS STAYS HERE FOR THIS REASON 22/5/13
            # smach.StateMachine.add(
            #         'CALL_FOR_RESET_COLLISION_MAP',
            #         ResetCollisionMapStateMachine(),
            #         transitions = {succeeded: 'Grasp_target_action', aborted: aborted})


            # scan and grasp!
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

                ####obj.object_list = [None] * 10  # ugly way to allocate space in python
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
                            op = ObjectPose()
                            obj.object_list.append(op)
                            if userdata.object_id_from_name > 0:
                                obj.object_list[num_object].name = userdata.object_to_search_for
                                obj.object_list[num_object].pose = result.detectionResult.models[i].model_list[0].pose.pose
                                num_object += 1
                                break
                            else:
                                #rospy.loginfo("Going to translate ID: " + str(result.detectionResult.models[i].model_list[0].model_id))
                                rospy.wait_for_service('object_translator_dataBase')
                                obj_trans_db = rospy.ServiceProxy('object_translator_dataBase', ObjectTranslatorDataBase)
                                obj_info = obj_trans_db(result.detectionResult.models[i].model_list[0].model_id)
                                #rospy.loginfo("Got info from db: " + str(obj_info))
                                obj.object_list[num_object].name = obj_info.objname
                                obj.object_list[num_object].pose = result.detectionResult.models[i].model_list[0].pose.pose
                                num_object += 1
                except Exception as e:
                    # rospy.loginfo("Exception when looping over result.detectionResult.models[" + str(i) + "]")
                    # rospy.loginfo("result.detectionResult.models[i] looks like:\n" + str(result.detectionResult.models[i]))
                    if str(e) != "list index out of range":
                        rospy.loginfo("Got exception: " +  str(e))

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

                if status == GoalStatus.SUCCEEDED and num_object > 0:
                    return succeeded
                if status == GoalStatus.ABORTED:
                    set_grasp_error("Grasp_target_action failed")
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
                transitions = {succeeded: succeeded, aborted: 'Hand_to_normal_position'})  


            def grasp_arm_goal_cb(userdata, old_goal):
                grasp_msg = get_fully_open_hand()
                return grasp_msg

            def grasp_arm_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED:
                    #rospy.loginfo("Succeeded: result of right_hand_controller: " + str(result.error_code) )
                    return succeeded
                else:
                    rospy.loginfo("Other than succeded: result of right_hand_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code))
                    if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
                        rospy.loginfo("Continuing even with this error as it's not really aborted...")
                        return succeeded
                    else:
                        set_grasp_error("Hand_to_normal_position aborted: GOAL_TOLERANCE_VIOLATED or PATH_TOLERANCE_VIOLATED")
                        return aborted

            smach.StateMachine.add(
            'Hand_to_normal_position',
            SimpleActionState(
                '/right_hand_controller/follow_joint_trajectory',
                FollowJointTrajectoryAction,
                goal_cb=grasp_arm_goal_cb,
                result_cb=grasp_arm_result_cb),
                transitions={succeeded: 'Move_back_for_spacing_for_putting_arm_down', aborted: 'Move_back_for_spacing_for_putting_arm_down'})


            def loc_request_cb(userdata, request):
                req = FinalApproachPoseRequest()
                req.pose.position.x = -0.3
                req.pose.orientation.w = 1.0
                return req

            smach.StateMachine.add(
                'Move_back_for_spacing_for_putting_arm_down',
                ServiceState('/approachToGoal', FinalApproachPose,
                    request_cb=loc_request_cb),
                    transitions={succeeded: 'RESET_COLLISION_MAP_', aborted: aborted})

            def grasp_target_goal_cb(userdata, old_goal):
                scan_goal = PointHeadGoal()
                return scan_goal


            smach.StateMachine.add('RESET_COLLISION_MAP_',
            ResetCollisionMapStateMachine(),
            transitions = {succeeded: 'Arm_to_fallback_pose', aborted: aborted})



            def arm_goal_cb(userdata, old_goal):
                print "Setting arm pose in a non dangerous pose"
                arm_goal = get_arm_goal_for_arm_travelling_position()
                return arm_goal

            smach.StateMachine.add(
                'Arm_to_fallback_pose',
                SimpleActionState(
                    'move_right_arm_torso',
                    MoveArmAction,
                    goal_cb=arm_goal_cb, result_cb=generic_action_result_cb),
            #result_cb = arm_result_cb,
                    #input_keys = ['object_data']),
                transitions={succeeded: aborted, aborted: 'Arm_to_fallback_pose'}) # if we got here is because the grasping failed, so we abort in any case


            # @smach.cb_interface(input_keys=['pose_object'], output_keys=['object_name_from_id'])
         #    def loc_response_cb(userdata, response):
         #        if response.exists:
         #            userdata.category = response.category
         #            objname = userdata.pose_object.object_list[0].name if input_nobj != self.ONE_OBJECT else userdata.pose_object.name
         #            print "Got category " + response.category + " for object " + objname
         #            return succeeded
         #        else:
         #            userdata.category = None
         #            return aborted

         #    def loc_request_cb(userdata, request):
         #        req = ObjectTranslatorDataBaseRequest()
         #        req.databaseID = userdata.object_to_search_for
         #        print "Asking coord_translator for " + req.objname
         #        return req

         #    smach.StateMachine.add(
         #        'GET_OBJECT_CATEGORY',
         #        ServiceState('/object_translator_dataBase', ObjectTranslatorDataBase,
         #            response_cb=loc_response_cb,
         #            request_cb=loc_request_cb,
         #            input_keys=['object_to_search_for'],
         #            output_keys=['object_name_from_id']),
         #            remapping={'object_name_from_id': 'object_name_from_id'},
         #            transitions={succeeded: 'ANNOUNCE_CATEGORY'})
