#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.grasping.search_object_with_confidence import Check_object_to_search_for
from coord_translator.srv import ObjectTranslator, ObjectTranslatorRequest, ObjectTranslatorDataBase
from smach_ros import SimpleActionState, ServiceState
from reem_tabletop_manipulation_launch.msg import GraspTargetAction, GraspTargetGoal
from actionlib_msgs.msg import GoalStatus
from pr_msgs.msg import ObjectPoseList, ObjectPose
from pal_smach_utils.grasping.search_objects_behaviour import CheckIfMoveCloserState
from reem_final_approach.srv import FinalApproachPose, FinalApproachPoseRequest
from pal_smach_utils.grasping.sm_grasp import pass_pose_to_search_object_key
from pr2_controllers_msgs.msg import PointHeadGoal, PointHeadAction
from arm_navigation_msgs.msg import MoveArmAction
from pal_smach_utils.grasping.arm_and_hand_goals import get_arm_goal_for_arm_travelling_position
from pal_smach_utils.grasping.arm_and_hand_goals import get_arm_goal_for_arm_elbow_back
from pal_smach_utils.grasping.arm_and_hand_goals import get_fully_open_hand
from control_msgs.msg import FollowJointTrajectoryAction
from pal_smach_utils.speech.sound_action import SpeakActionState

OUTPUT_NONE = "output_none"
GET_OBJECT_DATABASE_ID_FAILED = "get_object_database_id_failed"
GRASP_TARGET_ACTION_FAILED = "grasp_target_action_failed"
MOVE_IDEAL_POSITION_FOR_GRASP_FAILED = "move_ideal_position_for_grasp_failed"
GET_OBJECT_DATABASE_ID_AGAIN_FAILED = "get_object_database_id_again_failed"
SCAN_TABLE_FOR_MOVING_ARM_TO_ELBOW_UP_FAILED = "scan_table_for_moving_arm_to_elbow_up_failed"
ARM_TO_ELBOW_UP_PRE_GRASP_FAILED = "arm_to_elbow_up_pre_grasp_failed"
GRASP_TARGET_ACTION_AGAIN_FAILED = "grasp_target_action_again_failed"
# <The drink is not in the hand but was found>
HAND_TO_NORMAL_POSITION_FAILED = "hand_to_normal_position_failed"
MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN_FAILED = "move_back_for_spacing_for_putting_arm_down_failed"
SCAN_TABLE_FOR_MOVING_ARM_DOWN_FAILED = "scan_table_for_moving_arm_down_failed"
ARM_TO_FALLBACK_POSE_FAILED = "arm_to_fallback_pose_failed"
# <The drink is in the hand>
ARM_TO_ELBOW_BACK_FAILED = "arm_to_elbow_back_failed"
MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN_AGAIN_FAILED = "move_back_for_spacing_for_putting_arm_down_again_failed"
SCAN_TABLE_FOR_MOVIN_ARM_TO_TRAVEL_FAILED = "scan_table_for_movin_arm_to_travel_failed"
ARM_TO_SAFE_TRAVELLING_POSITION_FAILED = "arm_to_safe_travelling_position_failed"


TTS = {
OUTPUT_NONE: "I'm sure that Ruben forgot to set the variable output_none in some point!",
GET_OBJECT_DATABASE_ID_FAILED: "The object was not found in the database!",
GRASP_TARGET_ACTION_FAILED: "Grasp target action failed. No objects found or status is aborted.",  # " or status is aborted!"
MOVE_IDEAL_POSITION_FOR_GRASP_FAILED: "I found the object but I can't get closer!",
GET_OBJECT_DATABASE_ID_AGAIN_FAILED: "The object was not found in the database! But was already found in a  previous way. Why getting from database again???",
SCAN_TABLE_FOR_MOVING_ARM_TO_ELBOW_UP_FAILED: "Failing when scanning for move arm to elbow up! Why has failed here? What can cause this? In theory this should never abort! This means that the object was found but I can't scan!",
ARM_TO_ELBOW_UP_PRE_GRASP_FAILED: "Failed in arm to elbow up pre grasp. What can we do now??? This means that the object was found!",
GRASP_TARGET_ACTION_AGAIN_FAILED: "Second grasp target failed. This means that I'm not with the drink but I found it!",
HAND_TO_NORMAL_POSITION_FAILED: "Failed when backing hand to a normal position. This means that I found the object, I'm not with the drink and I can't grasp.",
MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN_FAILED: "Failed when trying move back for putting arm down. I found the object but I'm not with it!",
SCAN_TABLE_FOR_MOVING_ARM_DOWN_FAILED: "I found the drink. I'm not with the drink and has failed when scanning the table to move arm down!",
ARM_TO_FALLBACK_POSE_FAILED: "I'm not with the drink but I found it! My hand is in fallback pose! Ruben think that my hand is in front of me!",
ARM_TO_ELBOW_BACK_FAILED: "I'm with the drink in my hand, but I cant move my arm to elbow back!",
MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN_AGAIN_FAILED: "I'm with the drink in my hand, but has failed when trying move back for putting arm down.",
SCAN_TABLE_FOR_MOVIN_ARM_TO_TRAVEL_FAILED: "I'm with the drink. I already moved back. I'm with the arm up but failed when scanning to put arm in traveling position!",
ARM_TO_SAFE_TRAVELLING_POSITION_FAILED: "I'm with the drink in my hand, I'm already in a good position, I can move the arm to front of me but failed when moving!"
}

OUTPUT = OUTPUT_NONE


class GraspMegaPowerFuck(smach.StateMachine):
    def __init__(self, input_keys=[], output_keys=[]):
        smach.StateMachine.__init__(self,
            input_keys=input_keys + ['object_to_search_for'],
            output_keys=output_keys,
            outcomes=[succeeded, aborted, preempted])

        with self:

            ################ <CompleteGraspPipelineStateMachine> ################
            if True:
                ################ <SearchObjectsStateMachine > ################
                if True:
                    ################ <SearchObjectWithConfidenceStateMachine> ################
                    if True:
                        smach.StateMachine.add(
                            "CHECK_OBJECT_TO_SEARCH_FOR",
                            Check_object_to_search_for(),
                            transitions={succeeded: 'GET_OBJECT_DATABASE_ID', aborted: "GRASP_TARGET_ACTION"}
                            )
                        #input_keys=['object_to_search_for', 'object_found'], output_keys=['object_id_from_name'])

                        def get_object_database_id_response_cb(userdata, response):
                            global OUTPUT
                            if response.exists:
                                if response.databaseID != 0:
                                    userdata.object_id_from_name = response.databaseID
                                    rospy.loginfo("Got databaseID " + str(response.databaseID) + " for object " + userdata.object_to_search_for)
                                    return succeeded
                                else:
                                    OUTPUT = GET_OBJECT_DATABASE_ID_FAILED
                                    rospy.logerr("Object " + userdata.object_to_search_for + " not in coord_translator!")
                            else:
                                OUTPUT = GET_OBJECT_DATABASE_ID_FAILED
                                rospy.logerr("We got no response from coord_translator, object " + userdata.object_to_search_for + " not in coord_translator")
                            return aborted

                        def get_object_database_id_request_cb(userdata, request):
                            req = ObjectTranslatorRequest()
                            req.objname = userdata.object_to_search_for
                            rospy.loginfo("Asking coord_translator for " + req.objname)
                            return req

                        smach.StateMachine.add(
                            'GET_OBJECT_DATABASE_ID',
                            ServiceState('/object_translator', ObjectTranslator,
                                response_cb=get_object_database_id_response_cb,
                                request_cb=get_object_database_id_request_cb,
                                input_keys=['object_to_search_for'],
                                output_keys=['object_name_from_id']),
                                remapping={'object_id_from_name': 'object_id_from_name'},
                                transitions={succeeded: 'GRASP_TARGET_ACTION', aborted: aborted}
                                )

                        def grasp_target_action_goal_cb(userdata, old_goal):
                            grasp_target_goal = GraspTargetGoal()
                            grasp_target_goal.onlyPerception = True  # this SM is only for perception!
                            grasp_target_goal.appearanceID = userdata.object_to_search_for
                            grasp_target_goal.databaseID = userdata.object_id_from_name
                            rospy.loginfo("GraspTargetGoal:\n" + str(grasp_target_goal))
                            return grasp_target_goal

                        def grasp_target_action_result_cb(userdata, status, result):
                            # here parse the result and compose a ObjectPoseList of what we found and return it in the output key object_found
                            obj = ObjectPoseList()
                            obj.header = result.detectionResult.table.pose.header  # just copying some header
                            num_object = 0
                            i = 0
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
                                            rospy.loginfo("Going to translate ID: " + str(result.detectionResult.models[i].model_list[0].model_id))
                                            rospy.wait_for_service('object_translator_dataBase')
                                            obj_trans_db = rospy.ServiceProxy('object_translator_dataBase', ObjectTranslatorDataBase)
                                            obj_info = obj_trans_db(result.detectionResult.models[i].model_list[0].model_id)
                                            #rospy.loginfo("Got info from db: " + str(obj_info))
                                            if obj_info.objname == '':
                                                obj.object_list[num_object].name = 'unknown'
                                            else:
                                                obj.object_list[num_object].name = obj_info.objname
                                            obj.object_list[num_object].pose = result.detectionResult.models[i].model_list[0].pose.pose
                                            num_object += 1
                            except Exception as e:
                                rospy.loginfo("Exception when looping over result.detectionResult.models[" + str(i) + "]")
                                rospy.loginfo("result.detectionResult.models[i] looks like:\n" + str(result.detectionResult.models[i]))
                                if str(e) != "list index out of range":
                                    rospy.loginfo("Got exception: " + str(e))
                                pass  # this exception should be that we are looping too far...

                            userdata.object_found = obj
                            rospy.loginfo("userdata.object_found generated as: " + str(obj))

                            if status == GoalStatus.SUCCEEDED and num_object > 0:
                                return succeeded
                            else:
                                global OUTPUT
                                OUTPUT = GRASP_TARGET_ACTION_FAILED
                                return aborted

                        smach.StateMachine.add(
                            'GRASP_TARGET_ACTION',
                            SimpleActionState(
                                'tabletop_grasping_node',
                                GraspTargetAction,
                                goal_cb=grasp_target_action_goal_cb,
                                result_cb=grasp_target_action_result_cb,
                                input_keys=['object_to_search_for', 'object_id_from_name'],
                                output_keys=['object_found']),
                            transitions={succeeded: "CHECK_IF_CAN_MOVE_CLOSER", aborted: aborted}
                            )
                    ################ </SearchObjectWithConfidenceStateMachine> ################
                    # input_keys=['object_to_search_for'], output_keys=['object_found'])

                    smach.StateMachine.add(
                        'CHECK_IF_CAN_MOVE_CLOSER',
                        CheckIfMoveCloserState(),
                        transitions={succeeded: 'MOVE_IDEAL_POSITION_FOR_GRASP', aborted: "INIT_USERDATA_OBJECT_FOUND_TO_POSE_OBJECT"}  # FIXME: What to do when cant move closer?
                        )  # succeeded we move, aborted we dont

                    @smach.cb_interface(input_keys=['pose_for_goal_for_final_approach'])
                    def move_ideal_position_for_grasp_request_cb(userdata, request):
                        req = FinalApproachPoseRequest()
                        req.pose = userdata.pose_for_goal_for_final_approach
                        global OUTPUT
                        OUTPUT = MOVE_IDEAL_POSITION_FOR_GRASP_FAILED
                        return req

                    smach.StateMachine.add(
                        'MOVE_IDEAL_POSITION_FOR_GRASP',
                        ServiceState('/approachToGoal', FinalApproachPose,
                            request_cb=move_ideal_position_for_grasp_request_cb,
                            input_keys=['pose_for_goal_for_final_approach']),
                            transitions={succeeded: "INIT_USERDATA_OBJECT_FOUND_TO_POSE_OBJECT", aborted: aborted})  # FIXME: Check this transitions
                ################ </SearchObjectsStateMachine > ################
                # input_keys = ['object_to_search_for'], output_keys = ['object_found'])

                # GraspStateMachine needs pose_object key fullfilled to grasp
                @smach.cb_interface(input_keys=['object_to_search_for', 'object_found'], output_keys=['pose_object'], outcomes=[succeeded])
                def fulfill_userdata(userdata):
                    userdata.pose_object = userdata.object_found.object_list[0]
                    return succeeded

                smach.StateMachine.add(
                    'INIT_USERDATA_OBJECT_FOUND_TO_POSE_OBJECT',
                    smach.CBState(fulfill_userdata,
                        input_keys=['object_to_search_for',
                        'object_found_in_base_link_ref_frame'],
                        output_keys=['pose_object'],
                        outcomes=[succeeded]),
                    transitions={succeeded: 'PASS_POSE_TO_SEARCH_OBJECT_KEY'})
                    # output_keys=['pose_object']

                ################ <GraspStateMachine> ################
                if True:
                    smach.StateMachine.add(
                        "PASS_POSE_TO_SEARCH_OBJECT_KEY",
                        pass_pose_to_search_object_key(),
                        transitions={succeeded: 'CHECK_OBJECT_TO_SEARCH_FOR_AGAIN'}
                        )
                    # input_keys= ['pose_object'], output_keys=['object_to_search_for'])

                    ################ <ScanForObjectAndGraspStateMachine> ################
                    if True:
                        smach.StateMachine.add(
                            "CHECK_OBJECT_TO_SEARCH_FOR_AGAIN",
                            Check_object_to_search_for(),
                            transitions={succeeded: 'GET_OBJECT_DATABASE_ID_AGAIN', aborted: 'GRASP_TARGET_ACTION_AGAIN'}
                        )

                        def get_object_database_id_again_request_cb(userdata, request):
                            return get_object_database_id_request_cb(userdata, request)

                        def get_object_database_id_again_response_cb(userdata, response):
                            status = get_object_database_id_response_cb(userdata, response)
                            global OUTPUT
                            OUTPUT = GET_OBJECT_DATABASE_ID_AGAIN_FAILED
                            return status

                        smach.StateMachine.add(
                            'GET_OBJECT_DATABASE_ID_AGAIN',
                            ServiceState('/object_translator', ObjectTranslator,
                                response_cb=get_object_database_id_again_response_cb,
                                request_cb=get_object_database_id_again_request_cb,
                                input_keys=['object_to_search_for'],
                                output_keys=['object_name_from_id']),
                                remapping={'object_id_from_name': 'object_id_from_name'},
                                transitions={succeeded: "SCAN_TABLE_FOR_MOVING_ARM_TO_ELBOW_UP", aborted: aborted}
                                )

                        # Scan with head and put elbow pose
                        def scan_table_for_moving_arm_to_elbow_up_goal_cb(userdata, old_goal):
                            global OUTPUT
                            OUTPUT = SCAN_TABLE_FOR_MOVING_ARM_TO_ELBOW_UP_FAILED
                            scan_goal = PointHeadGoal()
                            return scan_goal

                        smach.StateMachine.add(
                            "SCAN_TABLE_FOR_MOVING_ARM_TO_ELBOW_UP",
                            SimpleActionState(
                                '/head_traj_controller/head_scan_snapshot_action',
                                PointHeadAction,
                                goal_cb=scan_table_for_moving_arm_to_elbow_up_goal_cb),
                            transitions={succeeded: "ARM_TO_ELBOW_UP_PRE_GRASP", aborted: aborted}  # FIXME: Aborted transition
                            )

                        def arm_to_elbow_up_pre_grasp_result_cb(userdata, result_status, result):
                            if result_status != GoalStatus.SUCCEEDED:  # SUCCEEDED = 3 http://www.ros.org/doc/api/move_arm_msgs/html/msg/MoveArmActionResult.html
                                rospy.loginfo("MoveArmActionResult result wasn't succeeded, was: " + str(result_status) +
                                    "\nmessage: \n" + str(result))
                                # if result.error_code.val == 1: # SUCCESS
                                #     rospy.loginfo("But we got SUCCESS as the result, so the planner will replan by itself.")
                                #     return succeeded

                                global OUTPUT
                                OUTPUT = ARM_TO_ELBOW_UP_PRE_GRASP_FAILED
                                return aborted
                            else:
                                return succeeded

                        def arm_to_elbow_up_pre_grasp_goal_cb(userdata, old_goal):
                            #arm_goal = get_arm_goal(get_pose_intermediate_position(), frame_id="/base_link")
                            print "Preparing MoveArmGoal() to move the arm to a safe travel position"
                            arm_goal = get_arm_goal_for_arm_elbow_back()
                            return arm_goal

                        smach.StateMachine.add(
                            "ARM_TO_ELBOW_UP_PRE_GRASP",
                            SimpleActionState(
                                'move_right_arm_torso',
                                MoveArmAction,
                                goal_cb=arm_to_elbow_up_pre_grasp_goal_cb,
                                result_cb=arm_to_elbow_up_pre_grasp_result_cb),
                            transitions={succeeded: "GRASP_TARGET_ACTION_AGAIN", aborted: aborted}  # FIXME: aborted transition
                            )

                        def grasp_target_action_again_goal_cb(userdata, old_goal):
                            return grasp_target_action_goal_cb(userdata, old_goal)

                        def grasp_target_action_again_result_cb(userdata, status, result):
                            status = grasp_target_action_result_cb(userdata, status, result)
                            global OUTPUT
                            OUTPUT = GRASP_TARGET_ACTION_AGAIN_FAILED
                            return status

                        smach.StateMachine.add(
                            "GRASP_TARGET_ACTION_AGAIN",
                            SimpleActionState(
                                'tabletop_grasping_node',
                                GraspTargetAction,
                                goal_cb=grasp_target_action_again_goal_cb,
                                result_cb=grasp_target_action_again_result_cb,
                                input_keys=['object_to_search_for', 'object_id_from_name'],
                                output_keys=['object_found']),
                            transitions={succeeded: "ARM_TO_ELBOW_BACK", aborted: 'HAND_TO_NORMAL_POSITION'})  # FIXME: Transitions

                        def hand_to_normal_position_goal_cb(userdata, old_goal):
                            grasp_msg = get_fully_open_hand()
                            return grasp_msg

                        def hand_to_normal_position_result_cb(userdata, status, result):
                            if status == GoalStatus.SUCCEEDED:
                                #rospy.loginfo("Succeeded: result of right_hand_controller: " + str(result.error_code) )
                                return succeeded
                            else:
                                rospy.loginfo("Other than succeded: result of right_hand_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code))
                                if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
                                    rospy.loginfo("Continuing even with this error as it's not really aborted...")
                                    return succeeded
                                else:
                                    global OUTPUT
                                    OUTPUT = HAND_TO_NORMAL_POSITION_FAILED
                                    return aborted

                        smach.StateMachine.add(
                            "HAND_TO_NORMAL_POSITION",
                            SimpleActionState(
                                '/right_hand_controller/follow_joint_trajectory',
                                FollowJointTrajectoryAction,
                                goal_cb=hand_to_normal_position_goal_cb,
                                result_cb=hand_to_normal_position_result_cb),
                            transitions={succeeded: "MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN", aborted: "MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN"})

                        def move_back_for_spacing_for_putting_arm_down_request_cb(userdata, request):
                            global OUTPUT
                            OUTPUT = MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN_FAILED
                            req = FinalApproachPoseRequest()
                            req.pose.position.x = -0.3
                            req.pose.orientation.w = 1.0
                            return req

                        smach.StateMachine.add(
                            'MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN',
                            ServiceState('/approachToGoal', FinalApproachPose,
                                request_cb=move_back_for_spacing_for_putting_arm_down_request_cb),
                                transitions={succeeded: 'SCAN_TABLE_FOR_MOVING_ARM_DOWN', aborted: aborted})

                        def scan_table_for_moving_arm_down_goal_cb(userdata, old_goal):
                            goal = scan_table_for_moving_arm_to_elbow_up_goal_cb(userdata, old_goal)
                            global OUTPUT
                            OUTPUT = SCAN_TABLE_FOR_MOVING_ARM_DOWN_FAILED
                            return goal

                        smach.StateMachine.add(
                            'SCAN_TABLE_FOR_MOVING_ARM_DOWN',
                            SimpleActionState(
                                '/head_traj_controller/head_scan_snapshot_action',
                                PointHeadAction,
                                goal_cb=scan_table_for_moving_arm_down_goal_cb),
                            transitions={succeeded: "ARM_TO_FALLBACK_POSE", aborted: aborted}
                            )

                        def arm_to_fallback_pose_goal_cb(userdata, old_goal):
                            print "Setting arm pose in a non dangerous pose"
                            arm_goal = get_arm_goal_for_arm_travelling_position()
                            global OUTPUT
                            OUTPUT = ARM_TO_FALLBACK_POSE_FAILED
                            return arm_goal

                        smach.StateMachine.add(
                            "ARM_TO_FALLBACK_POSE",
                            SimpleActionState(
                                'move_right_arm_torso',
                                MoveArmAction,
                                goal_cb=arm_to_fallback_pose_goal_cb),
                            transitions={succeeded: aborted, aborted: 'ARM_TO_FALLBACK_POSE'})
                    ################ </ScanForObjectAndGraspStateMachine> ################

                    # GraspStateMachine::Arm_to_elbow_back
                    def arm_to_elbow_back_goal_cb(userdata, old_goal):
                        goal = arm_to_elbow_up_pre_grasp_goal_cb(userdata, old_goal)
                        global OUTPUT
                        OUTPUT = ARM_TO_ELBOW_BACK_FAILED
                        return goal

                    smach.StateMachine.add(
                        "ARM_TO_ELBOW_BACK",
                        SimpleActionState(
                            'move_right_arm_torso',
                            MoveArmAction,
                            goal_cb=arm_to_elbow_back_goal_cb),
                        transitions={succeeded: 'MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN_AGAIN', aborted: aborted})

                    def move_back_for_spacing_for_putting_arm_down_again(userdata, request):
                        req = FinalApproachPoseRequest()
                        req.pose.position.x = -0.2
                        req.pose.orientation.w = 1.0
                        global OUTPUT
                        OUTPUT = MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN_AGAIN_FAILED
                        return req

                    smach.StateMachine.add(
                        'MOVE_BACK_FOR_SPACING_FOR_PUTTING_ARM_DOWN_AGAIN',
                        ServiceState('/approachToGoal', FinalApproachPose,
                            request_cb=move_back_for_spacing_for_putting_arm_down_again),
                            transitions={succeeded: "SCAN_TABLE_FOR_MOVIN_ARM_TO_TRAVEL", aborted: aborted})  # FIXME: TRANSITIONS

                    def scan_table_for_movin_arm_to_travel_goal_cb(userdata, old_goal):
                        goal = scan_table_for_moving_arm_to_elbow_up_goal_cb(userdata, old_goal)
                        global OUTPUT
                        OUTPUT = SCAN_TABLE_FOR_MOVIN_ARM_TO_TRAVEL_FAILED
                        return goal

                    smach.StateMachine.add(
                        "SCAN_TABLE_FOR_MOVIN_ARM_TO_TRAVEL",
                        SimpleActionState(
                            '/head_traj_controller/head_scan_snapshot_action',
                            PointHeadAction,
                            goal_cb=scan_table_for_movin_arm_to_travel_goal_cb),   # Scan with head and put travelling pose
                            transitions={succeeded: "ARM_TO_SAFE_TRAVELLING_POSITION", aborted: aborted}
                            )

                    def arm_to_safe_travelling_position_goal_cb(userdata, old_goal):
                        arm_goal = arm_to_fallback_pose_goal_cb(userdata, old_goal)
                        global OUTPUT
                        OUTPUT = ARM_TO_SAFE_TRAVELLING_POSITION_FAILED
                        return arm_goal

                    smach.StateMachine.add(
                        "ARM_TO_SAFE_TRAVELLING_POSITION",
                        SimpleActionState(
                            'move_right_arm_torso',
                            MoveArmAction,
                            goal_cb=arm_to_safe_travelling_position_goal_cb),
                        transitions={succeeded: succeeded, aborted: aborted})
                ################ </GraspStateMachine> ################
                # input_keys=['pose_object']

            ################ </CompleteGraspPipelineStateMachine> ################
            # input_keys=['object_to_search_for'], output_keys=['object_found'])


def main():
    rospy.init_node('test_grap_mega_power_fuck')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:

        sm.userdata.object_to_search_for = "juice"

        sm.add(
            "TEST_GRASP_MEGA_POWER_FUCK",
            GraspMegaPowerFuck(),
            transitions={succeeded: succeeded, aborted: "SAY_ERROR"}
            )

        sm.add(
            "SAY_OK",
            SpeakActionState("The grasp was perfectly performed! Congratulations!")
            )

        sm.add(
            "SAY_ERROR",
            SpeakActionState(TTS[OUTPUT])
            )

    sis = smach_ros.IntrospectionServer(
        'test_grap_mega_power_fuck_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
