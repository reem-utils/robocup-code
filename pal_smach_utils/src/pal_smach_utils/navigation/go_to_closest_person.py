#! /usr/bin/env python

import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import math
#from iri_perception_msgs.msg import peopleTracking
from smach import StateMachine
from move_base_msgs.msg import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.utils.global_common import *
from smach_ros import SimpleActionState, IntrospectionServer
from text_to_speech.msg import *  # just for the test, use SpeakActionState
from pal_smach_utils.speech.sound_action import SpeakActionState
from face_recognition.msg import * #just for the test, we should use the real one
from tf.transformations import *
from geometry_msgs.msg import Quaternion
from pal_smach_utils.utils.pose_at_distance import pose_at_distance


import random
import heapq

from iri_perception_msgs.msg import peopleTrackingArray  # <-Real


class GoToClosestPerson(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=[], output_keys=[])

        with self:
            MINIMUM_CONFIDENCE = 80.0
            PERSONS_TO_VISIT = []

            def detect_persons(userdata, pepe):
                if len(pepe.peopleSet) > 0:
                    for people in pepe.peopleSet:
                        distance = math.sqrt(people.x ** 2 + people.y ** 2)
                        pose = transform_pose(people, 'base_link', 'map')
                        heapq.heappush(PERSONS_TO_VISIT, (distance, pose))

                    return 'succeeded'

                return 'aborted'

            '''
            def move_person(userdata, goal):
                moveGoal = MoveBaseGoal()
                moveGoal.target_pose.header.stamp    = rospy.Time.now()
                moveGoal.target_pose.header.frame_id = 'base_link'
                moveGoal.target_pose.pose.position.x = userdata.message.x-0.5
                moveGoal.target_pose.pose.position.y = userdata.message.y-0.5
                moveGoal.target_pose.pose.position.z = 0
                #rotationAngle = random.random()
                moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0,0,0))
                return moveGoal
            '''

            def move_person(userdata, goal):
                ROBOT_RADIUS = 0.5
                PERSON_RADIUS = 0.5
                moveGoal = MoveBaseGoal()
                moveGoal.target_pose.header.stamp = rospy.Time.now()
                moveGoal.target_pose.header.frame_id = 'base_link'
                moveGoal.target_pose.pose.position.x = userdata.message.x
                moveGoal.target_pose.pose.position.y = userdata.message.y
                moveGoal.target_pose.pose = pose_at_distance(moveGoal.target_pose.pose, PERSON_RADIUS + ROBOT_RADIUS)
                moveGoal.target_pose.pose.position.z = 0

                orientationAngle = 0.0  # userdata.robot_position.orientation.z

                #orientation vector of the robot
                rV = [0, 0]
                rV[0] = math.cos(orientationAngle)
                rV[1] = math.sin(orientationAngle)
                #orientation vector of the robot
                pV = [0, 0]
                pV[0] = moveGoal.target_pose.pose.position.x
                pV[1] = moveGoal.target_pose.pose.position.y

                #we get the cosinus of the angle with the dot product of the robot orientation vector and the vector to the person
                def dot_product(v1, v2):
                    return sum((v1 * v2) for v1, v2 in zip(v1, v2))

                def length(v):
                    return dot_product(v, v) ** 0.5  # sqrt(...)

                def angle(v1, v2):
                    return math.acos(dot_product(v1, v2) / (length(v1) * length(v2)))

                #3rd component of the cross product to know if the rotation is clockwise or not
                clockwise = rV[0] * pV[1] - rV[1] * pV[0]

                print "\n\n\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                print "robot "
                print rV
                print "person "
                print pV
                print "angle between them "

                rotationAngle = angle(rV, pV)
                print str(rotationAngle) + " radians " + str(rotationAngle * (180.0) / math.pi) + " degress"
                if (clockwise < 0):
                    rotationAngle = -rotationAngle

                moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, rotationAngle * 180.0 / math.pi))

                print "final rotation angle "
                print str(rotationAngle) + " radians " + str(rotationAngle * (180.0) / math.pi) + " degrees"
                print "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n\n\n"

                return moveGoal

            def move_around(userdata, goal):
                moveGoal = MoveBaseGoal()
                moveGoal.target_pose.header.stamp = rospy.Time.now()
                moveGoal.target_pose.header.frame_id = 'base_link'
                moveGoal.target_pose.pose.position.x = random.randint(-2, 2)
                moveGoal.target_pose.pose.position.y = random.randint(-2, 2)
                moveGoal.target_pose.pose.position.z = 0
                rotationAngle = random.random()
                moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, rotationAngle))

                print moveGoal

                return moveGoal

            def tell_found(userdata, goal):
                tellGoal = SoundGoal()
                tellGoal.text = SAY_TO_PERSON
                tellGoal.wait_before_speaking = rospy.Duration(secs=0, nsecs=0)
                return tellGoal

            def face_recognition(userdata, goal):
                face_recog_goal = FaceRecognitionGoal()
                face_recog_goal.order_id = 0
                face_recog_goal.order_argument = 'Referee'
                return face_recog_goal

            class FaceProcessData(smach.State):
                def __init__(self):
                    smach.State.__init__(self, outcomes=['succeeded', 'face_not_found', 'preempted', 'aborted'],
                         input_keys=['process_names', 'process_confidence'])

                def execute(self, userdata):
                    if len(userdata.process_names) > 0:
                        for confidence_value in userdata.process_confidence:
                            if confidence_value > MINIMUM_CONFIDENCE:
                                return 'succeeded'

                    return 'face_not_found'

            class AnalyceClosestPerson(smach.State):
                def __init__(self):
                    smach.State.__init__(self, outcomes=['succeeded', 'aborted'],
                        input_keys=['robot_position'], output_keys=['message'])

                def execute(self, userdata):
                    if len(PERSONS_TO_VISIT) > 0:
                        person = heapq.heappop(PERSONS_TO_VISIT)
                        userdata.message = person[1]
                        return 'succeeded'

                    return 'aborted'

            # Add states to the container
            StateMachine.add('DETECT_PERSONS', TopicReaderState('iri_people_tracking_rai/peopleSet', peopleTrackingArray, detect_persons, 4),
                               transitions={'aborted': 'MOVE_AROUND',
                                            'succeeded': 'ANALYCE_CLOSEST_PERSON'})

            StateMachine.add('ANALYCE_CLOSEST_PERSON', AnalyceClosestPerson(),
                                    transitions={'succeeded': 'MOVE_TO_PERSON',
                                                 'aborted': 'MOVE_AROUND'},
                                    remapping={'message': 'message'})

            StateMachine.add('MOVE_TO_PERSON', SimpleActionState('move_base', MoveBaseAction, goal_cb=move_person,
                                   input_keys=['message']),
                                   transitions={'aborted': 'ANALYCE_CLOSEST_PERSON',
                                                'succeeded': 'TELL_FOUND'})

            StateMachine.add('MOVE_AROUND', SimpleActionState('move_base', MoveBaseAction, goal_cb=move_around),
                                   transitions={'aborted': 'DETECT_PERSONS',
                                                'succeeded': 'ANALYCE_CLOSEST_PERSON'})

            SAY_TO_PERSON = "Hi, dude"
            StateMachine.add('TELL_FOUND', SpeakActionState(SAY_TO_PERSON),
                                    transitions={'aborted': 'FACE_RECOGNITION_SM',
                                                   'succeeded': 'FACE_RECOGNITION_SM'})

            sm_face_recognition = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted', 'moveAround'])

            with sm_face_recognition:

                intro_text = "Please stay still while I recognise you."
                StateMachine.add('TTS_SAY_CALIB',
                                        SpeakActionState(intro_text),
                                        transitions={succeeded: 'FACE_RECOGNITION'})

                StateMachine.add('FACE_RECOGNITION', SimpleActionState('face_recognition', FaceRecognitionAction, goal_cb=face_recognition,
                                        result_slots=['order_id', 'names', 'confidence']),
                                        transitions={'succeeded': 'PROCESS_FACEDATA'},
                                        remapping={'names': 'LP_names', 'confidence': 'LP_confidence'})

                smach.StateMachine.add('PROCESS_FACEDATA', FaceProcessData(),
                                        transitions={'succeeded': 'TTS_SAY_FOUND',
                                                        'face_not_found': 'TTS_SAY_NOT_FOUND',
                                                        'aborted': 'TTS_SAY_CALIB'},

                                        remapping={'process_names': 'LP_names',
                                                     'process_confidence': 'LP_confidence',
                                                        })

                found_text = "I found you!"
                StateMachine.add('TTS_SAY_FOUND',
                                        SpeakActionState(found_text),
                                        transitions={})

                not_found_text = "Sorry, I wasn't looking for you..."
                StateMachine.add('TTS_SAY_NOT_FOUND',
                                        SpeakActionState(not_found_text),
                                        transitions={'succeeded': 'moveAround'})

            StateMachine.add('FACE_RECOGNITION_SM', sm_face_recognition,
                      transitions={'moveAround': 'ANALYCE_CLOSEST_PERSON'})


class ApproachPerson(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=[], output_keys=[])

        with self:
            PERSONS_TO_VISIT = []

            def detect_persons(userdata, pepe):
                if len(pepe.peopleSet) > 0:
                    for people in pepe.peopleSet:
                        distance = math.sqrt(people.x ** 2 + people.y ** 2)
                        pose = transform_pose(people, 'base_link', 'map')
                        heapq.heappush(PERSONS_TO_VISIT, (distance, pose))

                    return 'succeeded'

                return 'aborted'

            class AnalyceClosestPerson(smach.State):
                def __init__(self):
                    smach.State.__init__(self, outcomes=['succeeded', 'aborted'],
                        input_keys=['robot_position'], output_keys=['message'])

                def execute(self, userdata):
                    if len(PERSONS_TO_VISIT) > 0:
                        person = heapq.heappop(PERSONS_TO_VISIT)
                        userdata.message = person[1]
                        return 'succeeded'

                    return 'aborted'

            '''
            def move_person(userdata, goal):
                moveGoal = MoveBaseGoal()
                moveGoal.target_pose.header.stamp    = rospy.Time.now()
                moveGoal.target_pose.header.frame_id = 'base_link'
                moveGoal.target_pose.pose.position.x = userdata.message.x-0.5
                moveGoal.target_pose.pose.position.y = userdata.message.y-0.5
                moveGoal.target_pose.pose.position.z = 0
                #rotationAngle = random.random()
                moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0,0,0))
                return moveGoal
            '''

            def move_person(userdata, goal):
                ROBOT_RADIUS = 0.5
                PERSON_RADIUS = 0.5

                moveGoal = MoveBaseGoal()
                moveGoal.target_pose.header.stamp = rospy.Time.now()
                moveGoal.target_pose.header.frame_id = 'base_link'
                moveGoal.target_pose.pose.position.x = userdata.message.x
                moveGoal.target_pose.pose.position.y = userdata.message.y
                moveGoal.target_pose.pose = pose_at_distance(moveGoal.target_pose.pose, PERSON_RADIUS + ROBOT_RADIUS)
                moveGoal.target_pose.pose.position.z = 0

                orientationAngle = 0.0  # userdata.robot_position.orientation.z

                #orientation vector of the robot
                rV = [0, 0]
                rV[0] = math.cos(orientationAngle)
                rV[1] = math.sin(orientationAngle)
                #orientation vector of the robot
                pV = [0, 0]
                pV[0] = moveGoal.target_pose.pose.position.x
                pV[1] = moveGoal.target_pose.pose.position.y

                #we get the cosinus of the angle with the dot product of the robot orientation vector and the vector to the person
                def dot_product(v1, v2):
                    return sum((v1 * v2) for v1, v2 in zip(v1, v2))

                def length(v):
                    return dot_product(v, v) ** 0.5  # sqrt(...)

                def angle(v1, v2):
                    return math.acos(dot_product(v1, v2) / (length(v1) * length(v2)))

                #3rd component of the cross product to know if the rotation is clockwise or not
                clockwise = rV[0] * pV[1] - rV[1] * pV[0]

                print "\n\n\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                print "robot "
                print rV
                print "person "
                print pV
                print "angle between them "

                rotationAngle = angle(rV, pV)
                print str(rotationAngle) + " radians " + str(rotationAngle * (180.0) / math.pi) + " degress"
                if (clockwise < 0):
                    rotationAngle = -rotationAngle

                moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, rotationAngle * 180.0 / math.pi))

                print "final rotation angle "
                print str(rotationAngle) + " radians " + str(rotationAngle * (180.0) / math.pi) + " degrees"
                print "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n\n\n"

                return moveGoal

            def tell_found(userdata, goal):
                tellGoal = SoundGoal()
                tellGoal.text = SAY_TO_PERSON
                tellGoal.wait_before_speaking = rospy.Duration(secs=0, nsecs=0)
                return tellGoal

            # Add states to the container
            StateMachine.add('DETECT_PERSONS', TopicReaderState('iri_people_tracking_rai/peopleSet', peopleTrackingArray, detect_persons, 4),
                               transitions={'aborted': 'aborted',
                                            'succeeded': 'ANALYCE_CLOSEST_PERSON'})

            StateMachine.add('ANALYCE_CLOSEST_PERSON', AnalyceClosestPerson(),
                                    transitions={'succeeded': 'MOVE_TO_PERSON',
                                                 'aborted': 'aborted'},
                                    remapping={'message': 'message'})

            StateMachine.add('MOVE_TO_PERSON', SimpleActionState('move_base', MoveBaseAction, goal_cb=move_person,
                                   input_keys=['message']),
                                   transitions={'aborted': 'aborted',
                                                'succeeded': 'TELL_FOUND'})

            SAY_TO_PERSON = "Hi, dude"
            StateMachine.add('TELL_FOUND', SpeakActionState(SAY_TO_PERSON),
                                    transitions={'aborted': aborted,
                                                   'succeeded': succeeded})
