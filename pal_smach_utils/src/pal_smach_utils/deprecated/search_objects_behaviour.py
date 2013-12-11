#! /usr/bin/env python

import roslib
import rospy
import copy
import smach
#import smach_ros
import actionlib
import math
from smach_ros import SimpleActionState, ServiceState


from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.grasping.head_goals import *
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.grasping.search_object_with_confidence import *
#from pal_smach_utils.grasping.search_object_with_confidence_moped import *
from pr_msgs.msg import ObjectPoseList, ObjectPose

from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler
from control_msgs.msg import *
from actionlib_msgs.msg import GoalStatus
from sensor_msgs.msg import JointState

import dynamic_reconfigure.client



class DownAndRightJointStateCheck(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted],
        input_keys = ['joint_states_data'])

    def execute(self, userdata):
        headid_1 = userdata.joint_states_data.name.index('head_1_joint')
        headpos_1 = userdata.joint_states_data.position[headid_1]
        headid_2 = userdata.joint_states_data.name.index('head_2_joint')
        headpos_2 = userdata.joint_states_data.position[headid_2]
        # check if the head joints are at [-0.3, 0.5] aprox (floats)
        if headpos_1 > -0.31 and headpos_1 < -0.29 and headpos_2  > 0.49 and headpos_2  < 0.51:
            return succeeded
        else:
            return aborted




class IsHeadLookingDownRightStateMachine(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, outcomes=[succeeded, aborted])

        with self:

            smach.StateMachine.add(
                'get_joint_states',
                TopicReaderState(
                                 topic_name='/joint_states',
                                 msg_type=JointState,
                                 timeout=2),
                remapping= {'message' : 'joint_states_data'},
                transitions = {succeeded: 'check_if_head_down_and_right', aborted: 'get_joint_states', preempted: aborted})

            smach.StateMachine.add(
                'check_if_head_down_and_right',
                DownAndRightJointStateCheck(),
                transitions = {succeeded: succeeded, aborted: aborted})



class create_object_goal_move_position(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded],input_keys=['object_found_in_base_link_ref_frame', 'distance_to_object'], output_keys=['object_pose'])

    def execute(self, userdata):
        pose_obj = Pose()
        pose_obj.orientation =  Quaternion(*quaternion_from_euler(0, 0, 0))
        pose_obj.position = userdata.object_found_in_base_link_ref_frame.pose.position
        pose_obj.position.z = 0.0
        pose_obj.position.x -= userdata.distance_to_object - 0.60 # try to get into graspable distance.
        userdata.object_pose = pose_obj

        return succeeded


class lower_inflation_radius(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys = ['old_inflation_radius'])

    def execute(self, userdata):
        userdata.old_inflation_radius = rospy.get_param('/move_by/move_base/local_costmap/inflation_radius')
        client = dynamic_reconfigure.client.Client('/move_by/move_base/local_costmap')
        params = { 'inflation_radius' : 0.1 }
        config = client.update_configuration(params)
        return succeeded


class restore_inflation_radius(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], input_keys = ['old_inflation_radius'])

    def execute(self, userdata):
        client = dynamic_reconfigure.client.Client('/move_by/move_base/local_costmap')
        params = { 'inflation_radius' : userdata.old_inflation_radius }
        config = client.update_configuration(params)
        return succeeded


class Try_to_move_closer(smach.StateMachine):

  def __init__(self):

    smach.StateMachine.__init__(self, [succeeded, aborted, preempted], input_keys = ['object_found_in_base_link_ref_frame','distance_to_object'])

    with self:
        # Tell move_by to move to the object pose. it should try to get near
        pose_obj = Pose()
        pose_obj.orientation =  Quaternion(*quaternion_from_euler(0, 0, 0))
        smach.StateMachine.add('GET_OBJECT_POSITION',
                                create_object_goal_move_position(),
                                remapping = {'object_pose' : 'object_pose'},
                                transitions = {succeeded: 'MOVE_CLOSER_TO_OBJECT'})


        smach.StateMachine.add( 'MOVE_CLOSER_TO_OBJECT',
                                MoveActionState("/base_link", goal_key='object_pose'),
                                transitions = {succeeded: succeeded, aborted: aborted, preempted: aborted}) 
        #FIXME: CAN'T TRUST THIS. SOMETIMES MOVES. ALWAYS ABORTS BECAUSE WE TRY TO MOVE TOO CLOSE
        # TODO: substract to the position the distance where the laser says we are too close so we can have SUCCEEDED here




class TransformObjectReferenceFrame(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded],input_keys=['object_found', 'transformed_object_data'], output_keys=['transformed_object_data'])

    def execute(self, userdata):
        rospy.loginfo("Transforming pose of object from the vision frame to the base_link frame.")
        rospy.loginfo("Asking tf to transform from " + userdata.object_found.header.frame_id + " to /base_link the pose:\n " + str(userdata.object_found.object_list[0].pose))
        object_in_base_link = transform_pose (userdata.object_found.object_list[0].pose,  userdata.object_found.header.frame_id, "/base_link" ) 
        rospy.loginfo("tf returns the pose transformed:\n" +  str(object_in_base_link))
        userdata.transformed_object_data = copy.deepcopy(userdata.object_found.object_list[0])
        userdata.transformed_object_data.pose = object_in_base_link
        return succeeded


class Check_graspable_distance(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted],input_keys=['object_found_in_base_link_ref_frame'], output_keys=['distance_to_object'])

    def execute(self, userdata):
        origin = Pose()
        origin.position = Point(0.0, 0.0, 0.0)
        origin_in_arm_frame = transform_pose (origin,  "/arm_right_2_link", "/base_link" ) 
        rospy.loginfo("origin in arm frame is: " + str(origin_in_arm_frame))
        rospy.loginfo("object_found_in_base_link_ref_frame is:" + str(userdata.object_found_in_base_link_ref_frame))
        o = origin_in_arm_frame.position
        rospy.loginfo("This is o: " + str(o))
        p = userdata.object_found_in_base_link_ref_frame.pose.position
        rospy.loginfo("This is p: " + str(p))
        dist = math.sqrt((p.x - o.x) ** 2 +
                        (p.y - o.y) ** 2 +
                        (p.z - o.z) ** 2) 
        userdata.distance_to_object = dist
        if dist < 0.60:
            rospy.loginfo("Object is at " + str(dist) + "m from the shoulder, we may be able to grasp it")
            return succeeded
        else:
            rospy.loginfo("Object is at " + str(dist) + "m from the shoulder, too far to grasp")
            return aborted




class MoveBodyForObjectSearchStateMachine(smach.StateMachine):

  def __init__(self):

    smach.StateMachine.__init__(self, [succeeded, aborted, preempted])

    with self:
        # Move pi/8 to the NW, left of robot
        pose_nw = Pose()
        pose_nw.orientation =  Quaternion(*quaternion_from_euler(0, 0, 0.3927)) # 45deg / 2
        smach.StateMachine.add( 'N2_TURN_NW',
                                MoveActionState("/base_link", pose_nw),
                                transitions = {succeeded: succeeded, aborted: aborted, preempted: aborted}) # FIXME: Maybe we get into a loop here

    #After turning we should center the vision on the object or before!


class MoveHeadForObjectSearchStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, aborted])


        with self:
            def head_goal_cb(userdata, old_goal):
                head_msg = get_head_look_arbitrary(-0.4, 0.5, 2) # look down and right, do the movement in 2 secs
                return head_msg

            def head_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED:
                    userdata.head_in_down_right_pose = True
                    return succeeded
                else:
                    rospy.loginfo("Other than succeded: result of head_controller ( GOAL_TOLERANCE_VIOLATED=-5 ): " + str(result.error_code) )
                    if result.error_code != result.GOAL_TOLERANCE_VIOLATED or result.error_code != result.PATH_TOLERANCE_VIOLATED:
                        rospy.loginfo("Continuing even with this error as it's not really aborted...")
                        return succeeded
                    else:
                        return aborted

            smach.StateMachine.add(
                'HEAD_MOVE_RIGHT_DOWN',
                SimpleActionState(
                    # '/head_controller/follow_joint_trajectory', for simulation
                    '/head_traj_controller/follow_joint_trajectory',
                    FollowJointTrajectoryAction,
                    goal_cb = head_goal_cb,
                    result_cb = head_result_cb),
                transitions = {succeeded: succeeded, aborted: 'HEAD_MOVE_RIGHT_DOWN', preempted: aborted}) 




class DecideWhatToMoveStateMachine(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, aborted])


        with self:
            # check if the head looks down and right (where we can grasp)
            smach.StateMachine.add(
                    'CHECK_IF_HEAD_LOOKING_DOWN_RIGHT',
                    IsHeadLookingDownRightStateMachine(),
                    transitions = {succeeded: 'LOWER_INFLATION_RADIUS', aborted: 'MOVE_HEAD_DOWN_RIGHT'})

            # move body
            smach.StateMachine.add(
                'LOWER_INFLATION_RADIUS',
                lower_inflation_radius(),
                transitions = {succeeded: 'MOVE_ROBOT_TURNING'})

            smach.StateMachine.add(
                    'MOVE_ROBOT_TURNING',
                    MoveBodyForObjectSearchStateMachine(),
                    transitions = {succeeded: 'RESTORE_INFLATION_RADIUS', preempted: aborted, aborted: 'RESTORE_INFLATION_RADIUS_WHEN_ABORTED'})

            smach.StateMachine.add(
                'RESTORE_INFLATION_RADIUS',
                restore_inflation_radius(),
                transitions = {succeeded: succeeded})

            smach.StateMachine.add(
                'RESTORE_INFLATION_RADIUS_WHEN_ABORTED',
                restore_inflation_radius(),
                transitions = {succeeded: aborted}) # FIXME: Sorry, this is ugly, but I'm trying to make it work


            # move head
            smach.StateMachine.add(
                    'MOVE_HEAD_DOWN_RIGHT',
                    MoveHeadForObjectSearchStateMachine(),
                    transitions = {succeeded: succeeded})



class SearchObjectsStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, aborted, preempted],
            input_keys = ['object_to_search_for'],
            output_keys = ['object_found_in_base_link_ref_frame', 'object_found'])


        with self:

            smach.StateMachine.add(
                'LOOK_FOR_OBJECTS',
                SearchObjectWithConfidenceStateMachine(),
                transitions = {succeeded: 'transform_object_reference_frame', aborted: 'MOVE_ROBOT_TO_GET_VISION'}) #TODO: aborted -> move something
            



            # smach.StateMachine.add(
            #         'look_for_objects',
            #         TopicReaderState(
            #                          topic_name='/blort_tracker/outputOPL',
            #                          msg_type=ObjectPoseList,
            #                          timeout=10),
            #         remapping= {'message' : 'object_found'},
            #         transitions = {succeeded: 'CHECK_IF_OBJECT_FOUND', aborted: 'MOVE_HEAD_TO_GET_VISION'})



            smach.StateMachine.add(
                'transform_object_reference_frame',
                TransformObjectReferenceFrame(),
                remapping= {'transformed_object_data' : 'object_found_in_base_link_ref_frame'},
                transitions = {succeeded: 'CHECK_GRASPABLE_DISTANCE'})

            smach.StateMachine.add(
                'MOVE_ROBOT_TO_GET_VISION',
                DecideWhatToMoveStateMachine(),
                transitions = {succeeded: 'LOOK_FOR_OBJECTS'})


            smach.StateMachine.add(
                'CHECK_GRASPABLE_DISTANCE',
                Check_graspable_distance(),
                transitions = {succeeded: succeeded, aborted: 'LOWER_INFLATION_RADIUS'})

            smach.StateMachine.add(
                'LOWER_INFLATION_RADIUS',
                lower_inflation_radius(),
                transitions = {succeeded: 'TRY_TO_MOVE_CLOSER'})


            smach.StateMachine.add(
                'TRY_TO_MOVE_CLOSER',
                Try_to_move_closer(),
                transitions = {succeeded: 'RESTORE_INFLATION_RADIUS', aborted: 'RESTORE_INFLATION_RADIUS_WHEN_ABORTED'})

            smach.StateMachine.add(
                'RESTORE_INFLATION_RADIUS',
                restore_inflation_radius(),
                transitions = {succeeded: 'LOOK_FOR_OBJECTS'})

            smach.StateMachine.add(
                'RESTORE_INFLATION_RADIUS_WHEN_ABORTED',
                restore_inflation_radius(),
                transitions = {succeeded: 'MOVE_ROBOT_TO_GET_VISION'})








             # if fails move head and search again

             # if fails move body and search again

             # if fails num_times_tried += 1... and try again until... 3?
