#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted, transform_pose
from pal_smach_utils.grasping.search_object_with_confidence import SearchObjectWithConfidenceStateMachine
from geometry_msgs.msg import Pose, Point
from pal_smach_utils.navigation.take_serve_drinks import TakeServeDrinkOrdersSM
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables as cp_vars
from pal_smach_utils.navigation.take_several_drink_orders import TakeSeveralDrinkOrdersStateMachine
from pal_smach_utils.utils.learn_face import LearnFaceStateMachine
from pal_smach_utils.speech.take_drink_order import TakeDrinkOrderStateMachine
from pal_smach_utils.grasping.complete_grasp_pipeline import CompleteGraspPipelineStateMachine

def main():
    """Just to make the tests of a special SM faster."""
    rospy.init_node('test_drop_faces')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:

        sm.userdata.object_to_search_for = ''

        smach.StateMachine.add(
            "LearnFaceStateMachine",
            CompleteGraspPipelineStateMachine()
        )

#        THE PART OF CODE BELOW IS TO TEST TRANSFORM_POSE
#        pose = Pose()
#        pose.position = Point(1.43800000548, 0 , 0)
#        pose.orientation.x = 0.0
#        pose.orientation.y = 0.0
#        pose.orientation.z = 0.0
#        pose.orientation.w = 1.0
#
#        def test_transform_pose(userdata):
#            p = transform_pose(pose, "base_link", "map")
#            print p
#            return succeeded
#
#        smach.StateMachine.add(
#            "TRANSFORM_POSE",
#            smach.CBState(test_transform_pose, outcomes=[succeeded])
#        )

    sis = smach_ros.IntrospectionServer(
        'test_drop_faces_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
