#! /usr/bin/env python
# vim: expandtab ts=4 sw=4

import roslib
roslib.load_manifest('emergency_situation_subsm_tests')
import rospy
import smach

from pal_smach_utils.utils.find_person.py import FindPersonStateMachine
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.utils.find_person import FindPersonStateMachine
# from pal_smach_utils.navigation.go_to_closest_person import GoToClosestPerson
from pal_smach_utils.navigation.move_action import MoveActionState
import random


class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded','aborted'], output_keys = ['room_name'])
        self.room_number=0

    def execute(self, userdata):
        self.room_list=['kitchen','charger','software','business']
        if self.room_number < len(self.room_list):
            userdata.room_name = self.room_list[self.room_number]
            self.room_number = self.room_number + 1
            return 'succeeded'
        else:
            return 'aborted'


class FindAPersonStateMachine(smach.StateMachine):
    rospy.init_node('pdf_and_mail_subsm_test')

    def __init__(self):
        smach.StateMachine.__init__(self, outcomes=['succeeded','preempted','aborted'])
            
        with self:
            smach.StateMachine.add(
                'FIND_A_PERSON_T1',
                FindPersonStateMachine(),
                transitions={'aborted':'MOVE_AROUND','succeeded':'succeeded'})

            def move_around(userdata, goal):
                moveGoal = MoveBaseGoal()
                moveGoal.target_pose.header.stamp = rospy.Time.now()
                moveGoal.target_pose.header.frame_id = 'base_link'
                moveGoal.target_pose.pose.position.x = random.randint(0, 2)
                moveGoal.target_pose.pose.position.y = random.randint(0, 2)
                moveGoal.target_pose.pose.position.z = 0
                rotationAngle = random.random()
                moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, rotationAngle))

                print moveGoal

                return moveGoal

            StateMachine.add('MOVE_AROUND', 
                SimpleActionState('move_base', MoveBaseAction, goal_cb=move_around),
                transitions={'succeeded': 'FIND_A_PERSON_T2'})

            smach.StateMachine.add(
                'FIND_A_PERSON_T2',
                FindPersonStateMachine(),
                transitions={'aborted':'dummy_state','succeeded':'succeeded'})
            
            smach.StateMachine.add(
                'dummy_state',
                DummyStateMachine(),
                transitions={'succeeded':'GO_TO_NEXT_ROOM', 'abotred':'aborted'})

            smach.StateMachine.add(
                'GO_TO_NEXT_ROOM',
                MoveToRoomStateMachine(),
                transitions = {'succeeded': 'FIND_A_PERSON', 'aborted': 'dummy_state'})               
