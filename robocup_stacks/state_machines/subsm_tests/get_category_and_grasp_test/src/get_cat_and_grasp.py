#! /usr/bin/env python

import roslib
roslib.load_manifest('get_category_and_grasp_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.get_category_and_announce import Get_category_and_announce_object
from pal_smach_utils.grasping.complete_grasp_pipeline import CompleteGraspPipelineStateMachine
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers
from pr_msgs.msg import ObjectPose
from geometry_msgs.msg import Pose


def main():
    rospy.init_node('get_category_and_grasp_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])
    #From the object_recognition_mock...
    sm.userdata.object_name = 'coke'
    sm.userdata.object_data = ObjectPose()
    sm.userdata.object_data.name = sm.userdata.object_name
    sm.userdata.object_data.pose = Pose()
    sm.userdata.object_data.pose.position.x = 0.30
    sm.userdata.object_data.pose.position.y = -0.30
    sm.userdata.object_data.pose.position.z = 1.13
    sm.userdata.object_data.pose.orientation.x = 0.5
    sm.userdata.object_data.pose.orientation.y = -0.5
    sm.userdata.object_data.pose.orientation.z = 0.5
    sm.userdata.object_data.pose.orientation.w = -0.5
    sm.userdata.in_target_object = ''

    with sm:
        smach.StateMachine.add('START_CONTROLLERS', StartRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: 'GET_CATEGORY_AND_ANNOUNCE_OBJECT', aborted: aborted})

        smach.StateMachine.add('GET_CATEGORY_AND_ANNOUNCE_OBJECT',
                               Get_category_and_announce_object(input_nobj=Get_category_and_announce_object.ONE_OBJECT),
                               transitions={succeeded: 'SM_GRASP'},
                               remapping={'pose_object': 'object_data'})

        # Call SM_GRASP
        smach.StateMachine.add('SM_GRASP',
                               CompleteGraspPipelineStateMachine(),
                               remapping={'object_to_search_for': 'object_name'},
                               transitions={succeeded: 'STOP_CONTROLLERS', aborted: 'STOP_CONTROLLERS', preempted: 'STOP_CONTROLLERS'})

        smach.StateMachine.add('STOP_CONTROLLERS', StopRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})

    sis = smach_ros.IntrospectionServer(
        'get_category_and_grasp_test', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
