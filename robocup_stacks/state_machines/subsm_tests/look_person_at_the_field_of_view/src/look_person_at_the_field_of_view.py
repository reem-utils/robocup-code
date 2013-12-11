#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib
roslib.load_manifest("look_person_at_the_field_of_view")
import rospy
import smach
import smach_ros
from smach_ros import SimpleActionState
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler
import random  # For decide the direction of rotation.
import math
from pal_smach_utils.utils.global_common import preempted, succeeded, aborted
from iri_perception_msgs.msg import peopleTracking
from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_smach_utils.speech.sound_action import SpeakActionState
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal		# For rotate the robot

TOPIC_NAME = "/closestPerson"
MAXIMUM_DISTANCE = 1.5
TIMEOUT = 5  # seconds
degreesToRotate = 0.0


class GoodDistance(smach.State):
    """
    This state return succeeded if the distance is less than MAXIMUM_DISTANCE, aborted otherwise
    """
    def __init__(self):
        smach.State.__init__(self, input_keys=["in_distance"], output_keys=[], outcomes=[succeeded, aborted])

    def execute(self, userdata):
        rospy.loginfo("The distance to the closest person is %s meters ", userdata.in_distance)
        global MAXIMUM_DISTANCE
        return succeeded if userdata.in_distance <= MAXIMUM_DISTANCE else aborted


class AnalizeRotatedDegrees(smach.State):
    def __init__(self):
        smach.State.__init__(self, input_keys=["in_degrees_to_rotate"], output_keys=["out_position"], outcomes=[succeeded, aborted])
        self.rotated_degrees = 0
        if random.choice(["LEFT", "RIGHT"]) == "LEFT":
            self.degrees_to_rotate = 1.5708    # 90 degrees. 90 * 3.14 / 180
        else:
            self.degrees_to_rotate = -1.5708

    def execute(self, userdata):
        pose = Pose()
        pose.orientation = Quaternion(*quaternion_from_euler(0, 0, self.degrees_to_rotate))
        moveBaseGoal = MoveBaseGoal()
        moveBaseGoal.target_pose.header.stamp = rospy.Time.now()
        moveBaseGoal.target_pose.header.frame_id = '/base_link'
        moveBaseGoal.target_pose.pose = pose
        userdata.out_position = moveBaseGoal

        if abs(self.rotated_degrees) < 6.2832:
            self.rotated_degrees += self.degrees_to_rotate
            return succeeded
        return aborted


class LookPersonAtTheFieldOfView(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, input_keys=[], output_keys=[], outcomes=[succeeded, aborted, preempted])

        with self:
            rotated_degrees = 0
            if random.choice(["LEFT", "RIGHT"]) == "LEFT":
                degrees_to_rotate = 1.5708    # 90 degrees. 90 * 3.14 / 180
            else:
                degrees_to_rotate = -1.5708

            def analize_closest_person(userdata, person):
                userdata.out_distance = math.sqrt(person.x ** 2 + person.y ** 2)
                userdata.out_person = person

            smach.StateMachine.add("DETECT_CLOSEST_PERSON",
                TopicReaderState(TOPIC_NAME, peopleTracking, timeout=TIMEOUT, callback=analize_closest_person,
                output_keys=["out_person", "out_distance"]),
                transitions={succeeded: "ANALIZE_DISTANCE", aborted: "ANALIZE_DISTANCE"}
                )

            smach.StateMachine.add("ANALIZE_DISTANCE",
                GoodDistance(),
                transitions={succeeded: "SAY_FOUND", aborted: "SAY_NOT_FOUND"},
                remapping={"in_distance": "out_distance"}
                )

            def say_found(userdata):
                return "I found you  with %s meters!" % userdata.in_distance

            smach.StateMachine.add("SAY_FOUND",
                SpeakActionState(text_cb=say_found, input_keys=["in_distance"]),
                transitions={aborted: succeeded, succeeded: succeeded},
                remapping={"in_distance": "out_distance"}
                )

            def say_not_found(userdata):
                return "I did not found someone less than 1.5 meters!"

            smach.StateMachine.add("SAY_NOT_FOUND",
                SpeakActionState(text_cb=say_not_found),
                transitions={succeeded: "ANALIZE_ROTATED_DEGREES", aborted: "ANALIZE_ROTATED_DEGREES"}
                )

            smach.StateMachine.add("ANALIZE_ROTATED_DEGREES",
                AnalizeRotatedDegrees(),
                transitions={succeeded: "ROTATE", aborted: aborted}
                )

            def calcule_rotation(userdata, goal_cb):
                pose = Pose()
                pose.orientation = Quaternion(*quaternion_from_euler(0, 0, degrees_to_rotate))
                moveBaseGoal = MoveBaseGoal()
                moveBaseGoal.target_pose.header.stamp = rospy.Time.now()
                moveBaseGoal.target_pose.header.frame_id = '/base_link'
                moveBaseGoal.target_pose.pose = pose
                return moveBaseGoal

            smach.StateMachine.add("ROTATE", SimpleActionState("/move_base", MoveBaseAction, goal_cb=calcule_rotation),
            transitions={succeeded: "DETECT_CLOSEST_PERSON", aborted: aborted})


def main():

    rospy.init_node("look_person_at_the_field_of_view")

    #Create the state machine
    sm = smach.StateMachine(outcomes=["aborted", "succeeded", "preempted"], input_keys=[], output_keys=[])

    with sm:
        smach.StateMachine.add("LOOK_PERSON_AT_THE_FIELD_OF_VIEW",
            LookPersonAtTheFieldOfView(),
            transitions={succeeded: succeeded, aborted: aborted, preempted: preempted}
            )

    #Create and start the introspection server
    sis = smach_ros.IntrospectionServer("look_person_at_the_field_of_view", sm, "/LOOK_PERSON")
    sis.start()

    sm.execute()

    #Wait for Ctrl+c to stop the application
    rospy.spin()
    sis.stop()


if __name__ == "__main__":
    main()
