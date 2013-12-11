#! /usr/bin/env python

import roslib
roslib.load_manifest('learn_and_follow_operator_test')
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted, transform_pose

from geometry_msgs.msg import PoseStamped, Quaternion
from tf.transformations import quaternion_from_euler

#Uncomment when the callback method to move the robot is use
#from geometry_msgs.msg import Pose
#from move_base_msgs.msg import MoveBaseGoal
#from pal_smach_utils.navigation.move_action import MoveActionState

from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA

from copy import deepcopy


move_base_topic_goal = rospy.get_param("/params_learn_and_follow_operator_test/move_base_topic", "/move_base_simple/goal")

marker_id = 0
MARKERS_TAIL_LENGTH = 100
SLEEP_TIME_AFTER_SENT_GOAL = 0.5

PERSON_COLOR = ColorRGBA(0.0, 0.0, 1.0, 1.0)

PERSON_HEIGHT = 1.7

PERSON_HEAD_DIAMETER = PERSON_HEIGHT * 0.18

PERSON_TORSO_HEIGHT = (PERSON_HEIGHT - PERSON_HEAD_DIAMETER) / 2.0
PERSON_TORSO_DIAMETER = PERSON_HEAD_DIAMETER

PERSON_LEG_HEIGHT = PERSON_TORSO_HEIGHT
PERSON_LEG_DIAMETER = (PERSON_HEAD_DIAMETER / 2.0) * 0.8


class GoToLocationL(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])
        self.pub = rospy.Publisher(move_base_topic_goal, PoseStamped)
        self.marker_pub = rospy.Publisher(
            "visualization_marker",
            Marker)
        self.marker_array_pub = rospy.Publisher(
            "visualization_marker_array",
            MarkerArray)

    def execute(self, userdata):
        nav_goal = PoseStamped()
        nav_goal.header.stamp = rospy.Time.now()
        nav_goal.header.frame_id = "/map"
        #nav.goal.pose.position = Point()
        nav_goal.pose.position.x = rospy.get_param("/params_learn_and_follow_operator_test/nav_goal_x", 1.5)
        nav_goal.pose.position.y = 0.0
        nav_goal.pose.position.z = 0.0
        nav_goal.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))

        nav_goal.pose = transform_pose(nav_goal.pose, 'base_link', 'map')

        global move_base_topic_goal
        move_base_topic_goal = rospy.get_param("/params_learn_and_follow_operator_test/move_base_topic", "/move_base_simple/goal")
        self.pub = rospy.Publisher(move_base_topic_goal, PoseStamped)
        rospy.loginfo('Pose data that will be sent to the topic ' + move_base_topic_goal + ':\n%s' % str(nav_goal))

        self.pub.publish(nav_goal)

        marker = Marker()
        marker.header.frame_id = "/map"
        marker.ns = "test_markers_namespace"
        global marker_id
        marker.id = marker_id
        marker_id = marker_id + 1
        marker.type = marker.ARROW
        marker.action = marker.ADD
        marker.pose = nav_goal.pose
        marker.scale.x = 0.5
        marker.scale.y = 0.5
        marker.scale.z = 0.5
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 0.5
        marker.color.b = 0.1
        marker.lifetime = rospy.Duration.from_sec(MARKERS_TAIL_LENGTH * SLEEP_TIME_AFTER_SENT_GOAL)
        marker.header.stamp = rospy.Time.now()
        self.marker_pub.publish(marker)

        person_marker_array = MarkerArray()

        #HEAD OF THE PERSON BODY
        person_head_marker = Marker()
        person_head_marker.header.frame_id = "/map"
        person_head_marker.ns = "person_test_markers_namespace"
        person_head_marker.id = 0
        person_head_marker.type = marker.SPHERE
        person_head_marker.action = marker.ADD
        #we must copy the value to avoid a reference
        person_head_marker.pose = deepcopy(nav_goal.pose)
        person_head_marker.pose.position.z = PERSON_HEIGHT - PERSON_HEAD_DIAMETER / 2.0
        person_head_marker.scale.x = PERSON_HEAD_DIAMETER
        person_head_marker.scale.y = PERSON_HEAD_DIAMETER
        person_head_marker.scale.z = PERSON_HEAD_DIAMETER
        person_head_marker.color = PERSON_COLOR
        person_head_marker.lifetime = rospy.Duration.from_sec(SLEEP_TIME_AFTER_SENT_GOAL)
        person_head_marker.header.stamp = rospy.Time.now()
        person_marker_array.markers.append(person_head_marker)

        #TORSO OF THE PERSON BODY
        person_torso_marker = Marker()
        person_torso_marker.header.frame_id = "/map"
        person_torso_marker.ns = "person_test_markers_namespace"
        person_torso_marker.id = 1
        person_torso_marker.type = marker.CUBE
        person_torso_marker.action = marker.ADD
        person_torso_marker.pose = deepcopy(nav_goal.pose)
        person_torso_marker.pose.position.z = PERSON_HEIGHT - PERSON_HEAD_DIAMETER - PERSON_TORSO_HEIGHT / 2.0
        person_torso_marker.scale.x = PERSON_TORSO_DIAMETER
        person_torso_marker.scale.y = PERSON_TORSO_DIAMETER
        person_torso_marker.scale.z = PERSON_TORSO_HEIGHT
        person_torso_marker.color = PERSON_COLOR
        person_torso_marker.lifetime = rospy.Duration.from_sec(SLEEP_TIME_AFTER_SENT_GOAL)
        person_torso_marker.header.stamp = rospy.Time.now()
        person_marker_array.markers.append(person_torso_marker)

        #LEGS OF THE PERSON BODY
        person_leg_marker = Marker()
        person_leg_marker.header.frame_id = "/map"
        person_leg_marker.ns = "person_test_markers_namespace"
        person_leg_marker.id = 2
        person_leg_marker.type = marker.CYLINDER
        person_leg_marker.action = marker.ADD

        person_leg_marker.pose.position.x = rospy.get_param("/params_learn_and_follow_operator_test/nav_goal_x", 1.5)
        person_leg_marker.pose.position.y = PERSON_TORSO_DIAMETER / 4.0  # mid point between edge and center of the body
        person_leg_marker.pose.position.z = PERSON_HEIGHT - PERSON_HEAD_DIAMETER - PERSON_TORSO_HEIGHT - PERSON_LEG_HEIGHT / 2.0
        person_leg_marker.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
        person_leg_marker.pose = transform_pose(person_leg_marker.pose, 'base_link', 'map')

        person_leg_marker.scale.x = PERSON_LEG_DIAMETER
        person_leg_marker.scale.y = PERSON_LEG_DIAMETER
        person_leg_marker.scale.z = PERSON_LEG_HEIGHT
        person_leg_marker.color = PERSON_COLOR
        person_leg_marker.lifetime = rospy.Duration.from_sec(SLEEP_TIME_AFTER_SENT_GOAL)
        person_leg_marker.header.stamp = rospy.Time.now()
        person_marker_array.markers.append(person_leg_marker)

        person_leg_marker = deepcopy(person_leg_marker)
        person_leg_marker.id = 3
        person_leg_marker.pose.position.x = rospy.get_param("/params_learn_and_follow_operator_test/nav_goal_x", 1.5)
        person_leg_marker.pose.position.y = -PERSON_TORSO_DIAMETER / 4.0  # mid point between edge and center of the body
        person_leg_marker.pose.position.z = PERSON_HEIGHT - PERSON_HEAD_DIAMETER - PERSON_TORSO_HEIGHT - PERSON_LEG_HEIGHT / 2.0
        person_leg_marker.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
        person_leg_marker.pose = transform_pose(person_leg_marker.pose, 'base_link', 'map')
        person_marker_array.markers.append(person_leg_marker)

        self.marker_array_pub.publish(person_marker_array)

        rospy.sleep(SLEEP_TIME_AFTER_SENT_GOAL)

        return succeeded


def main():
    rospy.init_node('test_move_unsafe')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add(
            'GO_TO_LOCATION',
            GoToLocationL(),
            transitions={
                succeeded: 'GO_TO_LOCATION',
                preempted: preempted,
                aborted: aborted})

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

        smach.StateMachine.add(
            'GO_TO_LOCATION',
            MoveActionState("/base_link", "/move_by_unsafe/move_base", goal_cb=move_cb),
            transitions={succeeded: 'GO_TO_LOCATION', preempted: preempted, aborted: aborted})
        """
    sm.execute()

    rospy.spin()
if __name__ == '__main__':
    main()
