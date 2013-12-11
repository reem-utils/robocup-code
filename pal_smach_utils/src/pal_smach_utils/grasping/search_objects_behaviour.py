#! /usr/bin/env python

import rospy
#import copy
import smach
from smach_ros import ServiceState


from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
#from pal_smach_utils.utils.topic_reader import TopicReaderState
#from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.grasping.search_object_with_confidence import SearchObjectWithConfidenceStateMachine

from geometry_msgs.msg import Pose, Point, Quaternion
#from tf.transformations import quaternion_from_euler
#from sensor_msgs.msg import JointState

#import dynamic_reconfigure.client

from reem_final_approach.srv import FinalApproachPose, FinalApproachPoseRequest



# class DownAndRightJointStateCheck(smach.State):
#     def __init__(self):
#         smach.State.__init__(self, outcomes=[succeeded, aborted],
#         input_keys = ['joint_states_data'])

#     def execute(self, userdata):
#         headid_1 = userdata.joint_states_data.name.index('head_1_joint')
#         headpos_1 = userdata.joint_states_data.position[headid_1]
#         headid_2 = userdata.joint_states_data.name.index('head_2_joint')
#         headpos_2 = userdata.joint_states_data.position[headid_2]
#         # check if the head joints are at [-0.3, 0.5] aprox (floats)
#         if headpos_1 > -0.31 and headpos_1 < -0.29 and headpos_2  > 0.49 and headpos_2  < 0.51:
#             return succeeded
#         else:
#             return aborted




# class IsHeadLookingDownRightStateMachine(smach.StateMachine):
#     def __init__(self):
#         smach.StateMachine.__init__(self, outcomes=[succeeded, aborted])

#         with self:

#             smach.StateMachine.add(
#                 'get_joint_states',
#                 TopicReaderState(
#                                  topic_name='/joint_states',
#                                  msg_type=JointState,
#                                  timeout=2),
#                 remapping= {'message' : 'joint_states_data'},
#                 transitions = {succeeded: 'check_if_head_down_and_right', aborted: 'get_joint_states', preempted: aborted})

#             smach.StateMachine.add(
#                 'check_if_head_down_and_right',
#                 DownAndRightJointStateCheck(),
#                 transitions = {succeeded: succeeded, aborted: aborted})



# class create_object_goal_move_position(smach.State):
#     def __init__(self):
#         smach.State.__init__(self, outcomes=[succeeded],input_keys=['object_found_in_base_link_ref_frame', 'distance_to_object'], output_keys=['object_pose'])

#     def execute(self, userdata):
#         pose_obj = Pose()
#         pose_obj.orientation =  Quaternion(*quaternion_from_euler(0, 0, 0))
#         pose_obj.position = userdata.object_found_in_base_link_ref_frame.pose.position
#         pose_obj.position.z = 0.0
#         pose_obj.position.x -= userdata.distance_to_object - 0.60 # try to get into graspable distance.
#         userdata.object_pose = pose_obj
#         rospy.loginfo("CREATED GOAL TO APPROACH TO OBJECT:\n" + str(pose_obj))

#         return succeeded


# class lower_inflation_radius(smach.State):
#     def __init__(self):
#         smach.State.__init__(self, outcomes=[succeeded], output_keys = ['old_inflation_radius'])

#     def execute(self, userdata):
#         userdata.old_inflation_radius = rospy.get_param('/move_by/move_base/local_costmap/inflation_radius')
#         # client = dynamic_reconfigure.client.Client('/move_by/move_base/local_costmap')
#         # params = { 'inflation_radius' : 0.1 }
#         # config = client.update_configuration(params)
#         return succeeded


# class restore_inflation_radius(smach.State):
#     def __init__(self):
#         smach.State.__init__(self, outcomes=[succeeded], input_keys = ['old_inflation_radius'])

#     def execute(self, userdata):
#         # client = dynamic_reconfigure.client.Client('/move_by/move_base/local_costmap')
#         # params = { 'inflation_radius' : userdata.old_inflation_radius }
#         # config = client.update_configuration(params)
#         return succeeded


# class Try_to_move_closer(smach.StateMachine):

#   def __init__(self):

#     smach.StateMachine.__init__(self, [succeeded, aborted, preempted], input_keys = ['object_found_in_base_link_ref_frame','distance_to_object'])

#     with self:
#         # Tell move_by to move to the object pose. it should try to get near
#         pose_obj = Pose()
#         pose_obj.orientation =  Quaternion(*quaternion_from_euler(0, 0, 0))
#         smach.StateMachine.add('GET_OBJECT_POSITION',
#                                 create_object_goal_move_position(),
#                                 remapping = {'object_pose' : 'object_pose'},
#                                 transitions = {succeeded: 'MOVE_CLOSER_TO_OBJECT'})


#         smach.StateMachine.add( 'MOVE_CLOSER_TO_OBJECT',
#                                 MoveActionState(move_base_action_name="/move_by/move_base", frame_id="/base_link", goal_key='object_pose'),
#                                 transitions = {succeeded: succeeded, aborted: aborted, preempted: aborted}) 
#         #FIXME: CAN'T TRUST THIS. SOMETIMES MOVES. ALWAYS ABORTS BECAUSE WE TRY TO MOVE TOO CLOSE
#         # TODO: substract to the position the distance where the laser says we are too close so we can have SUCCEEDED here




# class TransformObjectReferenceFrame(smach.State):

#     def __init__(self):
#         smach.State.__init__(self, outcomes=[succeeded],input_keys=['object_found', 'transformed_object_data'], output_keys=['transformed_object_data'])

#     def execute(self, userdata):
#         rospy.loginfo("Transforming pose of object from the vision frame to the base_link frame.")
#         rospy.loginfo("Asking tf to transform from " + userdata.object_found.header.frame_id + " to /base_link the pose:\n " + str(userdata.object_found.object_list[0].pose))
#         object_in_base_link = transform_pose (userdata.object_found.object_list[0].pose,  userdata.object_found.header.frame_id, "/base_link" ) 
#         rospy.loginfo("tf returns the pose transformed:\n" +  str(object_in_base_link))
#         userdata.transformed_object_data = copy.deepcopy(userdata.object_found.object_list[0])
#         userdata.transformed_object_data.pose = object_in_base_link
#         return succeeded


class CheckIfMoveCloserState(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted],input_keys=['object_found', 'object_to_search_for'], output_keys=['pose_for_goal_for_final_approach'])

    def execute(self, userdata):
        ideal_x_distance = 0.45  # table > 1m 0.45 was ok, FOR RH31 CALIBNRATION IS WRONG
        ideal_y_distance = -0.1  # This is the distance from base_link to the shoulder, aprox
        threshold_x_distance = 0.1
        threshold_y_distance = 0.1

        index_of_object_to_search_for = 0
        object_found = False
        while not object_found:
            if userdata.object_found.object_list[0].name == userdata.object_to_search_for:
                object_found = True
            else:
                index_of_object_to_search_for += 1


        move_to_ideal_position = Pose()
        move_to_ideal_position.position = Point()
        move_to_ideal_position.orientation = Quaternion()
        move_to_ideal_position.orientation.w = 1.0  # orientation ignored, but we must have it correctly formatted
        move_to_ideal_position.position.x = (userdata.object_found.object_list[index_of_object_to_search_for].pose.position.x - ideal_x_distance)
        move_to_ideal_position.position.y = (userdata.object_found.object_list[index_of_object_to_search_for].pose.position.y - ideal_y_distance)
        #if userdata.object_found.object_list[0].pose.position.z < 1.0:
            #move_to_ideal_position.position.y += (1 - userdata.object_found.object_list[0].pose.position.z) / 4.0 # if the table is lower we need to move more to the right
            #move_to_ideal_position.position.x -= (1 - userdata.object_found.object_list[0].pose.position.z) / 2.0

        if abs(move_to_ideal_position.position.x) < threshold_x_distance and abs(move_to_ideal_position.position.y) < threshold_y_distance:
            # dont move, we are good
            rospy.loginfo("OK! Object is at " + str(move_to_ideal_position.position) +
             " inside of our ideal distances of, (x,y): " + str(ideal_x_distance) + " " + str(ideal_y_distance) + 
             " with our thresholds of, (x,y): " +  str(threshold_x_distance) + " " + str(threshold_y_distance) )
            return aborted
        else:
            # move there
            rospy.loginfo("Not OK! Object is at " + str(move_to_ideal_position.position) +
             " too far of our ideal distances of, (x,y): " + str(ideal_x_distance) + " " + str(ideal_y_distance) + 
             " which exceeds our thresholds of, (x,y): " +  str(threshold_x_distance) + " " + str(threshold_y_distance) )
            userdata.pose_for_goal_for_final_approach = move_to_ideal_position
            return succeeded




class SearchObjectsStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, aborted, preempted],
            input_keys = ['object_to_search_for'],
            output_keys = ['object_found'])


        with self:

            smach.StateMachine.add(
                'LOOK_FOR_OBJECTS',
                SearchObjectWithConfidenceStateMachine(),
                transitions = {succeeded: 'Check_if_move_closer', aborted: aborted})

            smach.StateMachine.add(
                'Check_if_move_closer',
                CheckIfMoveCloserState(),
                transitions={succeeded: 'Move_ideal_position_for_grasp', aborted: succeeded})  # succeeded we move, aborted we dont

            @smach.cb_interface(input_keys=['pose_for_goal_for_final_approach'])
            def loc_request_cb(userdata, request):
                req = FinalApproachPoseRequest()
                req.pose = userdata.pose_for_goal_for_final_approach
                return req

            smach.StateMachine.add(
                'Move_ideal_position_for_grasp',
                ServiceState('/approachToGoal', FinalApproachPose,
                    request_cb=loc_request_cb,
                    input_keys=['pose_for_goal_for_final_approach']),
                    transitions={succeeded: succeeded, aborted: aborted})
