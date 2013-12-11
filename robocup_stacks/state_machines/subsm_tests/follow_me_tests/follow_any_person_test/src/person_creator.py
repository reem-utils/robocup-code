#! /usr/bin/env python

import roslib
roslib.load_manifest('follow_any_person_test')
import rospy
import smach
import random
import math
from geometry_msgs.msg import Pose
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.math_utils import xy_with_angle
from pal_smach_utils.utils.publish_marker import PublishPoseMarkers

DISTANCE_TO_FOLLOW = 0.8
DISPLACEMENT = 0.5
ALFA = math.pi / 4
DEBUGGING = True
robot_lost_person = True

LIST_PERSONS = ["far_front", "far_right", "far_left", "near_front", "near_right", "near_left", "line_front", "line_right", "line_left"]
PERSON_CREATOR_MARKER_NAME = "/person_creator/person_pose"
PERSON_CREATOR_MARKER_TYPE = "CYLINDER"
PERSON_CREATOR_MARKER_COLOUR = "GREEN"


class Persons():

    """
         ^ X IN Base Link, AXIS of REEM
         |
    Y    |
    <----+

    """

    def __init__(self):
        self.person_far_infornt()
        self.person_far_right()
        self.person_far_left()
        self.person_near_infront()
        self.person_near_right()
        self.person_near_left()
        self.person_line_infront()
        self.person_line_right()
        self.person_line_left()

    # FAR
    def person_far_infornt(self):
        self.personFarInfornt = Pose()
        self.personFarInfornt.position.x = 2.0 * DISTANCE_TO_FOLLOW
        self.personFarInfornt.position.y = 0.0

    def person_far_right(self):
        self.personFarRight = Pose()
        self.personFarRight.position.x = 2.0 * DISTANCE_TO_FOLLOW
        self.personFarRight.position.y = -DISPLACEMENT

    def person_far_left(self):
        self.personFarLeft = Pose()
        self.personFarLeft.position.x = 2.0 * DISTANCE_TO_FOLLOW
        self.personFarLeft.position.y = DISPLACEMENT

    # NEAR
    def person_near_infront(self):
        self.personNearInfront = Pose()
        self.personNearInfront.position.x = DISTANCE_TO_FOLLOW / 2.0
        self.personNearInfront.position.y = 0.0

    def person_near_right(self):
        self.personNearRight = Pose()
        self.personNearRight.position.x = DISTANCE_TO_FOLLOW / 2.0
        self.personNearRight.position.y = -DISPLACEMENT

    def person_near_left(self):
        self.personNearLeft = Pose()
        self.personNearLeft.position.x = DISTANCE_TO_FOLLOW / 2.0
        self.personNearLeft.position.y = DISPLACEMENT

    # LINE
    def person_line_infront(self):
        self.personLineInfront = Pose()
        self.personLineInfront.position.x = DISTANCE_TO_FOLLOW
        self.personLineInfront.position.y = 0.0

    def person_line_right(self):

        self.personLineRight = Pose()
        self.personLineRight.position.x, self.personLineRight.position.y = xy_with_angle(-ALFA, DISTANCE_TO_FOLLOW)

    def person_line_left(self):

        self.personLineLeft = Pose()
        self.personLineLeft.position.x, self.personLineLeft.position.y = xy_with_angle(ALFA, DISTANCE_TO_FOLLOW)


class DummyPersonCreator(smach.State):

    """
    Creates a person pose based on the input person_info.
    If person_info wasnt created, it tells you and creates a person Far Infront.
    If the person info is not one of the supported, then it will create one random person.
    Otherwaise it will create the person designated.
    """

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             input_keys=['person_info'],
                             output_keys=['person_location_out'])
        self.persons = Persons()

    def execute(self, userdata):

        rospy.loginfo("DUMMY PERSON CREATOR INPUT PERSON_INFO ==>" + str(userdata.person_info))

        try:
            userdata.person_info
        except NameError:
            rospy.loginfo("THE PERSON INFO DIDNT EXIST")
            person_out_pose = self.persons.personFarInfornt
            return succeeded
        else:

            if any(userdata.person_info in s for s in LIST_PERSONS):
                if userdata.person_info == "":
                    print "PRESSED ONLY ENTER"
                    key_board_input = LIST_PERSONS[random.randint(0, len(LIST_PERSONS)-1)]
                else:
                    key_board_input = userdata.person_info
            else:

                key_board_input = LIST_PERSONS[random.randint(0, len(LIST_PERSONS)-1)]

            rospy.loginfo("THIS IS THE PERSON THAT WE WILL CREATE ==>" + key_board_input)

            if key_board_input == "far_front":
                person_out_pose = self.persons.personFarInfornt
            elif key_board_input == "far_right":
                person_out_pose = self.persons.personFarRight
            elif key_board_input == "far_left":
                person_out_pose = self.persons.personFarLeft
            elif key_board_input == "near_front":
                person_out_pose = self.persons.personNearInfront
            elif key_board_input == "near_right":
                person_out_pose = self.persons.personNearRight
            elif key_board_input == "near_left":
                person_out_pose = self.persons.personNearLeft
            elif key_board_input == "line_front":
                person_out_pose = self.persons.personLineInfront
            elif key_board_input == "line_right":
                person_out_pose = self.persons.personLineRight
            elif key_board_input == "line_left":
                person_out_pose = self.persons.personLineLeft
            else:
                assert(), "SOMETHING STRANGE HAPPENED"

        PublishPoseMarkers(person_out_pose, marker_name=PERSON_CREATOR_MARKER_NAME, marker_type=PERSON_CREATOR_MARKER_TYPE, colour=PERSON_CREATOR_MARKER_COLOUR)
        userdata.person_location_out = person_out_pose

        return succeeded
