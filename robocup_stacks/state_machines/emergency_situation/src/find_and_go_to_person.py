#! /usr/bin/env python

import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import math
from smach import StateMachine
from move_base_msgs.msg import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.utils.global_common import *
from smach_ros import SimpleActionState
from pal_smach_utils.speech.sound_action import SpeakActionState
from tf.transformations import *
from geometry_msgs.msg import Quaternion, Pose
from pal_smach_utils.utils.pose_at_distance import pose_at_distance
from find_person_with_visit_checker import FindPersonStateMachine
import random


COUNTNUMBER = 1


class MoveAroundCounter(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted])
        self.counter = 0

    def execute(self, userdata):
        if self.counter < COUNTNUMBER:
            self.counter = self.counter + 1
            print self.counter
            return succeeded
        else:
            self.counter = 0
            return aborted


class MoveToPerson(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, aborted, preempted], input_keys=['closest_person'], output_keys=[])

        with self:

            def move_person(userdata, goal):
                ROBOT_RADIUS = 0.3
                PERSON_RADIUS = 0.3
                rospy.loginfo("POSE TYPE: "+str(type(userdata.message)))
                print "Info in closest_person (find_and_go_to_person.py): ", userdata.message
                pose_in_stereo = Pose()
                pose_in_stereo.position = userdata.message.pos

                pose_in_base_link = transform_pose(pose_in_stereo, userdata.message.header.frame_id, "/base_link")

                moveGoal = MoveBaseGoal()
                moveGoal.target_pose.header.stamp = rospy.Time.now()
                moveGoal.target_pose.header.frame_id = "/base_link"
                moveGoal.target_pose.pose.position.x = pose_in_base_link.position.x
                moveGoal.target_pose.pose.position.y = pose_in_base_link.position.y
                moveGoal.target_pose.pose.position.z = 0
                moveGoal.target_pose.pose = pose_at_distance(moveGoal.target_pose.pose, PERSON_RADIUS + ROBOT_RADIUS)

                teta = math.atan2(pose_in_base_link.position.y, pose_in_base_link.position.x)
                moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, teta))

                ######### COMMENT BELOW IF IT DOES NOT WORK AND UNCOMMENT ABOVE #######

                # orientationAngle = 0.0  # userdata.robot_position.orientation.z

                # # orientation vector of the robot
                # rV = [0, 0]
                # rV[0] = math.cos(orientationAngle)
                # rV[1] = math.sin(orientationAngle)
                # #orientation vector of the robot
                # pV = [0, 0]
                # pV[0] = moveGoal.target_pose.pose.position.x
                # pV[1] = moveGoal.target_pose.pose.position.y

                # # we get the cosinus of the angle with the dot product of the robot orientation vector and the vector to the person
                # def dot_product(v1, v2):
                #     return sum((v1 * v2) for v1, v2 in zip(v1, v2))

                # def length(v):
                #     return dot_product(v, v) ** 0.5  # sqrt(...)

                # def angle(v1, v2):
                #     return math.acos(dot_product(v1, v2) / (length(v1) * length(v2)))

                # #3rd component of the cross product to know if the rotation is clockwise or not
                # clockwise = rV[0] * pV[1] - rV[1] * pV[0]

                # print "\n\n\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                # print "robot "
                # print rV
                # print "person "
                # print pV
                # print "angle between them "

                # rotationAngle = angle(rV, pV)
                # print str(rotationAngle) + " radians " + str(rotationAngle * (180.0) / math.pi) + " degress"
                # if (clockwise < 0):
                #     rotationAngle = -rotationAngle

                # moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, rotationAngle * 180.0 / math.pi))

                # print "final rotation angle "
                # print str(rotationAngle) + " radians " + str(rotationAngle * (180.0) / math.pi) + " degrees"
                # print "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n\n\n"

                ###### COMMENT ABOVE IF IT DOES NOT WORK ##########

                print "Goal in base link (find_and_go_to_person.py)", moveGoal

                return moveGoal

            StateMachine.add(
                'MOVE_TO_PERSON',
                SimpleActionState('move_by/move_base', MoveBaseAction, goal_cb=move_person,
                input_keys=['message']),
                transitions={aborted: aborted, succeeded: succeeded},
                remapping={'message': 'closest_person'})


class FindAndGoToPersonStateMachine(smach.StateMachine):
    '''This will just move to the closest person which is outputted from FindPersonStateMachine of find_person_with_visit_checker.py'''

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, aborted, preempted], input_keys=['location_list'])

        with self:

            # def move_around(userdata, goal):
            #     moveGoal = MoveBaseGoal()
            #     moveGoal.target_pose.header.stamp = rospy.Time.now()
            #     moveGoal.target_pose.header.frame_id = 'base_link'
            #     moveGoal.target_pose.pose.position.x = random.randint(-2, 2)
            #     moveGoal.target_pose.pose.position.y = random.randint(-2, 2)
            #     moveGoal.target_pose.pose.position.z = 0
            #     rotationAngle = random.random()
            #     moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, rotationAngle))

            #     print moveGoal

            #     return moveGoal

            # FROM find_person_with_visit_checker
            smach.StateMachine.add(
                'FINDING',
                FindPersonStateMachine(),
                transitions={aborted: 'NOBODY_FOUND', succeeded: 'THERE_IS_A_PERSON'},
                remapping={'location_list': 'location_list'})

            smach.StateMachine.add(
                'NOBODY_FOUND',
                SpeakActionState("Nobody found in this room!"),
                transitions={succeeded: aborted, aborted: aborted})

            """
            smach.StateMachine.add(
                'MOVE_AROUND_DUMMY',
                MoveAroundCounter(),
                transitions={aborted: aborted, succeeded: 'MOVE_AROUND'})

            StateMachine.add('MOVE_AROUND',
                SimpleActionState('move_base', MoveBaseAction, goal_cb=move_around),
                transitions={aborted: aborted, succeeded: 'FINDING'})
            """
            smach.StateMachine.add(
                'THERE_IS_A_PERSON',
                SpeakActionState("I found a person."),
                transitions={succeeded: 'MOVE', aborted: 'MOVE'})

            smach.StateMachine.add(
                'MOVE',
                MoveToPerson(),
                transitions={succeeded: succeeded})
