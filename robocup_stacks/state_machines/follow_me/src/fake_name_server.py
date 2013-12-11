#! /usr/bin/env python

import roslib
roslib.load_manifest('follow_me')
import rospy
import smach
from smach_ros import SimpleActionState

from face_recognition.msg import FaceRecognitionAction, FaceRecognitionGoal

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

face_not_found = 'face_not_found'


class PrintUserData2(smach.State):
    def __init__(self):
        smach.State.__init__(
            self,
            outcomes=[succeeded],
            input_keys=['FSNS_name_of_person'])

    def execute(self, userdata):
        rospy.loginfo('$$$$$$$$$$This is the NAME: %s' % userdata.FSNS_name_of_person)
        return succeeded


class ProcessData2(smach.State):
    def __init__(self):
        smach.State.__init__(
            self,
            outcomes=[succeeded, face_not_found],
            input_keys=['process_names2'],
            output_keys=['person_name2'])

    def execute(self, userdata):
        rospy.loginfo('Executing ProcessData2')

        if (len(userdata.process_names2) > 0):
            userdata.person_name2 = userdata.process_names2[0]
            return succeeded
        else:
            rospy.loginfo('FACE NOT FOUND FACE NOT FOUND FACE NOT FOUND FACE NOT FOUND')

        return face_not_found


#Defining the state Machine of Learn Person

class Fake_NameServer(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(
            self,
            ourcomes=[succeeded, preempted, aborted],
            output_keys=['FSNS_name_of_person'])

        with self:
            face_recog_goal = FaceRecognitionGoal()
            face_recog_goal.order_id = 3

            smach.StateMachine.add(
                'AC_ASK_PERSON_RECOG_TO_ENROLL_PERSON',
                SimpleActionState('face_recognition', FaceRecognitionAction, goal=face_recog_goal, result_slots=['order_id', 'names', 'confidence']),
                transitions={succeeded: 'Process_Fake_NameServer_Data'},
                remapping={'names': 'LP_names'})

            smach.StateMachine.add(
                'Process_Fake_NameServer_Data',
                ProcessData2(),
                transitions={succeeded: 'PRINT_USERDATA', face_not_found: 'AC_ASK_PERSON_RECOG_TO_ENROLL_PERSON'},
                remapping={'process_names2': 'LP_names', 'person_name2': 'FSNS_name_of_person'})

            smach.StateMachine.add(
                'PRINT_USERDATA',
                PrintUserData2(),
                transitions={succeeded: succeeded},
                remapping={})
