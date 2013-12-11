#! /usr/bin/env python

import roslib; roslib.load_manifest('move_arm_to_object_grasp_and_back_test')
import rospy
import smach
import smach_ros
import actionlib

#from smach_ros import SimpleActionState, ServiceState
from std_msgs import *


from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.grasping.sm_reem_grasp_cloth import SMReemClothGraspStateMachine
from pal_smach_utils.grasping.arm_and_hand_goals import *
from pal_smach_utils.grasping.arm_movement_to_object import *
from pal_smach_utils.grasping.arm_movement_to_travel import *
from pal_smach_utils.grasping.arm_movement_grasp_sequence import *

from pr_msgs.msg import ObjectPoseList


class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys=['target_pose_stamped'])

    def execute(self, userdata):
        print "Dummy state to go to  ArmMovementGraspSequenceStateMachine initializing transformed_object_data and object_data"
        #rospy.sleep(1)  # in seconds
        
        test_pose_st = PoseStamped()
        test_pose_st.header.stamp = rospy.Time.now()
        test_pose_st.header.frame_id = "/base_link"
        test_pose_st.pose = Pose()
        test_pose_st.pose.position.x = 0.4
        test_pose_st.pose.position.y = -0.25
        test_pose_st.pose.position.z = 1.13
        test_pose_st.pose.orientation.x = 0.5
        test_pose_st.pose.orientation.y = -0.5
        test_pose_st.pose.orientation.z = 0.5
        test_pose_st.pose.orientation.w = -0.5
        userdata.target_pose_stamped = test_pose_st
        
        pub = rospy.Publisher('/debug/grasp_point', PoseStamped, None, False, True)
        rospy.sleep(1) # wait for subscribers
        pub.publish(test_pose_st)

        return succeeded


def main():
    rospy.init_node('sm_ArmMovementGraspSequenceStateMachine_test_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        # Using this state to wait and to initialize object_to_search_for input_key (needed by SearchAndGraspStateMachine() )
        smach.StateMachine.add(
            'dummy_state',
            DummyStateMachine(),
            transitions={succeeded: 'ArmMovementGraspSequenceStateMachine'})

        smach.StateMachine.add(
                    'ArmMovementGraspSequenceStateMachine',
                    SMReemClothGraspStateMachine(),
                    transitions={succeeded: succeeded, aborted: aborted})
         # NOT USING ANYTHING  MORE

    sis = smach_ros.IntrospectionServer(
        'sm_ArmMovementGraspSequenceStateMachine_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
