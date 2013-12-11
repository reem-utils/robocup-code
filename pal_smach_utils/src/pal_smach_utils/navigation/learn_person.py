#! /usr/bin/env python

import rospy
import smach
from smach_ros import SimpleActionState
from face_recognition.msg import FaceRecognitionAction, FaceRecognitionGoal

from iri_perception_msgs.msg import peopleTrackingArray, peopleTracking

from pal_smach_utils.utils.math_utils import vector_magnitude

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from geometry_msgs.msg import Pose

from pal_smach_utils.utils.topic_reader import TopicReaderState

face_not_found = 'face_not_found'
faulty_peopletrack = 'faulty_peopletrack'
no_plausible_candidate = 'no_plausible_candidate'

# the max distance from the robot at which a person can be enrolled
DEFAULT_MAX_DISTANCE = 2.0
MAX_DISTANCE = rospy.get_param('/params_follow_me/max_distance', DEFAULT_MAX_DISTANCE)
# the max distance in the 'x' axis at which a person can be enrolled
MAX_DISPLACE = rospy.get_param('/params_follow_me/max_displace', 1.0)

# This is the time the SM will wait until retry. Used to avoid too quick retries (too much use of CPU), in seconds
SLEEP_TIME_WHEN_FAILS = rospy.get_param('/params_follow_me/sleep_time_when_fails', 1.5)

# This is the minumum confidence that we alow for a face recognition to be True
MINIMUM_CONFIDENCE = rospy.get_param('/params_follow_me/minimum_confidence', 80.0)


def face_recog_goal_cb(userdata, goal):
    face_recog_goal = FaceRecognitionGoal()
    #In Retrain we are just learning one face,order_id = 3  (re)train
    face_recog_goal.order_id = 3
    #For the moment we won't use this, but it's needed for face recognition.
    face_recog_goal.order_argument = 'Referee'
    print 'This is the name we are learning : ' + face_recog_goal.order_argument
    return face_recog_goal


'''class PrintUserData(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                outcomes = [succeeded],
                input_keys=['print_persondId','FR_name_of_person'])

    def execute(self, userdata):
        rospy.loginfo('$$$$$$$$$$This is the TARGETID: %i'%userdata.print_persondId)
        rospy.loginfo('$$$$$$$$$$This is the NAME: %s'%userdata.FR_name_of_person)
        return succeeded'''


class FaceProcessData(smach.State):

    '''
    You input a vector of names 'process_names' and confidence 'process_confidence'
    if (confidence > MINIMUM_CONFIDENCE) -->    it returns succeeded and
                                                the name of the highest confidence
    else -->    returns face_not_found and
                the name = 'no_name'
                At the end it will wait t = SLEEP_TIME_WHEN_FAILS,
                after which the state will terminate.
    '''
    def __init__(self):
        smach.State.__init__(
            self,
            outcomes=[succeeded, face_not_found, preempted, aborted],
            input_keys=['process_names', 'process_confidence'],
            output_keys=['person_name'])

    def execute(self, userdata):

        #UserdData Init
        rospy.loginfo('Executing ::FaceProcessData::')
        userdata.person_name = 'no_name'
        #We check we are seeing someones face
        if len(userdata.process_names) > 0:

            #Now we check if confidence of each face seen is greater than MINIMUM_CONFIDENCE.
            #And from those we see who has the greater value.
            rospy.loginfo('CONFIDENCE:%s' % str(userdata.process_confidence))
            rospy.loginfo('NAMES:%s' % str(userdata.process_names))

            max_confidence_value = MINIMUM_CONFIDENCE
            i = 0
            found_face = False

            for confidence_value in userdata.process_confidence:
                if confidence_value > max_confidence_value:
                    max_confidence_value = confidence_value
                    max_confidence_candidate_name = userdata.process_names[i]
                    found_face = True
                i += 1

            if found_face:
                userdata.person_name = max_confidence_candidate_name

                return succeeded

        rospy.loginfo('FACE NOT FOUND FACE NOT FOUND FACE NOT FOUND')
        rospy.sleep(SLEEP_TIME_WHEN_FAILS)
        return face_not_found


#TODO
class PeopleTrackingProcessData(smach.State):

    '''
    You input a vector of an array 'process_peopleSet' type peopleTRacking.msg
    if (    distance between Reem and candidate < MAX_DISTANCE and
            the canditade is properly centered abs(pos.y) < MAX_DISPLACEMENT  )
                --> it returns succeeded and
                    the Id of the candidate nearest to Reem and the whole peopleTracking message
    else -->    returns faulty_peopletrack and
                the name = 'no_name'
                At the end it will wait t = SLEEP_TIME_WHEN_FAILS,
                after which the state will terminate.
    '''

    def __init__(self):
        smach.State.__init__(
            self,
            outcomes=[succeeded, faulty_peopletrack, preempted, aborted],
            input_keys=['process_peopleSet'],
            output_keys=['personId', 'all_person_data'])

    def execute(self, userdata):

        #UserdData Init
        rospy.loginfo('Executing ::PeopleTrackingProcessData::')
        userdata.personId = 101
        userdata.all_person_data = peopleTracking()
        rospy.loginfo('###############Numero Personas detectadas %i' % len(userdata.process_peopleSet.peopleSet))
        #We check there's someone
        if len(userdata.process_peopleSet.peopleSet) > 0:
            numero_personas_detectadas = len(userdata.process_peopleSet.peopleSet)
            rospy.loginfo('Numero Personas detectadas %i' % numero_personas_detectadas)
            i = 0
            found_person = False
            min_distance = MAX_DISTANCE

            for data_peopleSet in userdata.process_peopleSet.peopleSet:
                #Now we make the calculations for knowing the Displecement in Y-Axis
                #And the distance magnitude.
                p = Pose()
                p.position.x = data_peopleSet.x
                p.position.y = data_peopleSet.y
                distance = vector_magnitude(p.position)
                displace = abs(p.position.y)
                rospy.loginfo('::ID = %i::\nDistance VS MAX_DISTANCE ::%f = %f::,\ndisplace VS MAX_DISPLACE ::%f = %f::'
                              % (data_peopleSet.targetId, distance, MAX_DISTANCE, displace, MAX_DISPLACE))

                #We only select who has the minimum distance. The displacement is just a filter.
                if displace < MAX_DISPLACE:
                    if distance < min_distance:
                        min_distance = distance
                        data_personId = data_peopleSet.targetId
                        rospy.loginfo('PLAUSIBLE CANDIDATE FOUND,With ID ::%i::,\nAt distance ::%f::,\nDisplacement ::%f::  '
                                      % (data_personId, min_distance, displace))
                        all_per_data = data_peopleSet
                        rospy.loginfo('ALL PLAUSIBLE PERSON DATA \n%s'
                                      % str(all_per_data))
                        found_person = True
                    else:
                        rospy.loginfo('NOT PLAUSIBLE CANDIDATE with ID = %i\nNo person close enough to the robot or \nWe found a person closer'
                                      % (data_peopleSet.targetId))
                else:
                    rospy.loginfo('NOT PLAUSIBLE CANDIDATE with ID = %i\nBecause no person infront of the robot or \nPerson not centered'
                                  % (data_peopleSet.targetId))

                i += 1

            if found_person:
                userdata.personId = data_personId
                userdata.all_person_data = all_per_data
                return succeeded

        rospy.loginfo('NO PEOPLE  NO PEOPLE  NO PEOPLE  NO PEOPLE')
        rospy.sleep(SLEEP_TIME_WHEN_FAILS)
        return faulty_peopletrack


#Defining the state Machine of Learn Person

class LearnPerson(smach.StateMachine):

    """
    Returns the perosnId and positions and speed data of the closest person in the people_tracking_learning area.
    This Area is defined by the params in the file params_follow_me in teh follow_me pkg.
    """

    def __init__(self, learn_face=False):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted],
                                    output_keys=['PT_Id_of_person', 'LP_all_person_data'])

        with self:

            smach.StateMachine.add('AC_ASK_PEOPLETRACK_TO_LEARN_PERSON',
                                   TopicReaderState(topic_name='/iri_people_tracking_rai/peopleSet', msg_type=peopleTrackingArray, timeout=None),
                                   transitions={succeeded: 'PROCESS_PEOPLETRACK_DATA',
                                                preempted: preempted,
                                                aborted: 'AC_ASK_PEOPLETRACK_TO_LEARN_PERSON'},
                                   remapping={'message': 'LP_peopleSet'})

            people_track_next_state = succeeded
            if learn_face:
                people_track_next_state = 'AC_ASK_PEOPLETRACK_TO_LEARN_PERSON'

            smach.StateMachine.add('PROCESS_PEOPLETRACK_DATA',
                                   PeopleTrackingProcessData(),
                                   transitions={succeeded: people_track_next_state,
                                                faulty_peopletrack: 'AC_ASK_PEOPLETRACK_TO_LEARN_PERSON',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'process_peopleSet': 'LP_peopleSet',
                                              'personId': 'PT_Id_of_person',
                                              'all_person_data': 'LP_all_person_data'})

            smach.StateMachine.add('AC_ASK_PERSON_RECOG_TO_ENROLL_PERSON',
                                   SimpleActionState('face_recognition', FaceRecognitionAction, goal_cb=face_recog_goal_cb, result_slots=['order_id', 'names', 'confidence']),
                                   transitions={succeeded: 'PROCESS_FACEDATA',
                                                aborted: 'AC_ASK_PERSON_RECOG_TO_ENROLL_PERSON'},
                                   remapping={'names': 'LP_names',
                                              'confidence': 'LP_confidence'})

            smach.StateMachine.add('PROCESS_FACEDATA',
                                   FaceProcessData(),
                                   transitions={succeeded: succeeded,
                                                face_not_found: 'AC_ASK_PEOPLETRACK_TO_LEARN_PERSON',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'process_names': 'LP_names',
                                              'process_confidence': 'LP_confidence',
                                              'person_name': 'FR_name_of_person'})

# vim: expandtab ts=4 sw=4
