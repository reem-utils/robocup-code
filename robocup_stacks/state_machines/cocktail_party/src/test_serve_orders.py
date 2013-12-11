#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler
from move_base_msgs.msg import MoveBaseGoal
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted, transform_pose
from pal_smach_utils.navigation.serve_drinks import ServeOrdersStateMachine
from pal_smach_utils.utils.drink_order import DrinkOrder
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables
from pal_smach_utils.utils.colors import Colors


def main():
    """This is a unique test to ServeOrdersStateMachine.
    The robot will find the drink at drinks_location and assumes that the person
    is at the same position where the robot has started this test.
    """
    rospy.init_node('test_serve_orders_state_machine')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:

        sm.variables = cocktail_party_variables
        sm.c = Colors()

        def move_base_goal():
            move_base_goal = MoveBaseGoal()
            move_base_goal.target_pose.header.frame_id = "/map"
            pose = Pose()
            pose.position = Point(0, 0, 0)
            pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 3.14159))
            rospy.loginfo(sm.c.BACKGROUND_YELLOW + "Position in /base_link:\n%s %s" % (str(pose), sm.c.NATIVE_COLOR))
            pose = transform_pose(pose, "/base_link", "/map")
            rospy.loginfo(sm.c.BACKGROUND_GREEN + "Position in /map:\n%s %s" % (str(pose), sm.c.NATIVE_COLOR))
            move_base_goal.target_pose.pose = pose
            rospy.loginfo(sm.c.BACKGROUND_YELLOW + 'Sending robot to pose %s%s' % (str(move_base_goal), sm.c.NATIVE_COLOR))
            move_base_goal.target_pose.header.stamp = rospy.Time.now()
            return move_base_goal

        drink_order_1 = DrinkOrder("michael", "coke", move_base_goal())
        drink_order_2 = DrinkOrder("christopher", "juice", move_base_goal())
        drink_order_3 = DrinkOrder("matthew", "redbull", move_base_goal())
        sm.userdata.drink_orders = [drink_order_1, drink_order_2, drink_order_3]

        smach.StateMachine.add(
            "SERVE_ORDERS",
            ServeOrdersStateMachine(number_persons=1),
#            transitions={succeeded: "STOP_GRASP", aborted: "STOP_GRASP"}
            )

    sis = smach_ros.IntrospectionServer(
        'test_serve_orders_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
