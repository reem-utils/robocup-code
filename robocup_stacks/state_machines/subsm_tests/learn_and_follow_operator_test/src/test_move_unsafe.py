#! /usr/bin/env python

import roslib
roslib.load_manifest('learn_and_follow_operator_test')
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from geometry_msgs.msg import Pose, Point, Quaternion, Vector3, PoseStamped
from tf.transformations import quaternion_from_euler

from pal_smach_utils.navigation.move_action import MoveActionState
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


MOVE_BASE_TOPIC_GOAL = '/move_by/move_base_simple/goal'


class GoToLocationL(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])
        self.pub = rospy.Publisher(MOVE_BASE_TOPIC_GOAL, PoseStamped)

    def execute(self, userdata):

      nav_goal = PoseStamped()
      nav_goal.header.stamp = rospy.Time.now()
      nav_goal.header.frame_id = "/base_link"
      #nav.goal.pose.position = Point()
      nav_goal.pose.position.x = 1.5
      nav_goal.pose.position.y = 0.0
      nav_goal.pose.position.z = 0.0
      nav_goal.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
      rospy.loginfo('Data that will be sent to the topic ' + MOVE_BASE_TOPIC_GOAL + ' the pose:\n%s' % str(nav_goal))
      nav_goal.header.stamp = rospy.Time.now()
      self.pub.publish(nav_goal)
      rospy.sleep(1.5)
      return succeeded


def main():
    rospy.init_node('test_move_unsafe')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])
    

    with sm:

            smach.StateMachine.add('GO_TO_LOCATION',
                                   GoToLocationL(),
                                   transitions={succeeded: 'GO_TO_LOCATION', preempted: preempted, aborted: aborted})

            """
            def move_cb(userdata, nav_goal):
                nav_goal = MoveBaseGoal()
                nav_goal.target_pose.header.stamp = rospy.Time.now()
                nav_goal.target_pose.header.frame_id = "/base_link"
                nav_goal.target_pose.pose.position.x = 3.0
                nav_goal.target_pose.pose.position.y = 0.0
                nav_goal.target_pose.pose.position.z = 0.0
                nav_goal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
                return nav_goal

            smach.StateMachine.add('GO_TO_LOCATION',
                                   MoveActionState("/base_link", "/move_by_unsafe/move_base", goal_cb=move_cb),
                                   transitions={succeeded: 'GO_TO_LOCATION', preempted: preempted, aborted: aborted})
            """
    sm.execute()

    rospy.spin()
if __name__ == '__main__':
    main()
