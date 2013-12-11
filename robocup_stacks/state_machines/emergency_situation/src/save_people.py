#! /usr/bin/env python
# vim: expandtab ts=4 sw=4

import roslib
roslib.load_manifest('emergency_situation')
import smach
import rospy

# from find_a_person import DummyStateMachine
from locate_a_person import FindAPersonStateMachine
from pal_smach_utils.speech.sm_listen_orders import ListenOrders
from pal_smach_utils.navigation.get_current_pos import GetPosition
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from go_to_exit_and_follow_checker import GoExitAndFollowChecker
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine

YES_NO_GRAMMAR = 'confirming'
TIMEOUT_YES_NO = 10


class DummyStateMachineExit(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted, preempted], output_keys=['room_name'])

    def execute(self, userdata):
        userdata.room_name = 'pre_exit'
        return 'succeeded'


class RecordPosition(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted, preempted], input_keys=['location_of_person'], output_keys=['location_list'])
        self.people_need_assistance = []

    def execute(self, userdata):
        print rospy.loginfo("Saving Location ................")
        self.people_need_assistance.append([userdata.location_of_person.position.x, userdata.location_of_person.position.y])
        print rospy.loginfo("Location is saved successfully !!!!")
        print str(userdata.location_of_person)
        print "People need assistance: ", str(self.people_need_assistance)
        userdata.location_list = self.people_need_assistance
        return succeeded


class DummyIHeard(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['i_heard_yes', 'i_heard_no', 'i_heard_nothing'], input_keys=['i_heard'])

    def execute(self, userdata):
        #userdata.location_list = []
        if userdata.i_heard.tags[0].value == 'no':
            return 'i_heard_no'
        if userdata.i_heard.tags[0].value == 'yes':
            return 'i_heard_yes'
        else:
            return 'i_heard_nothing'


class SavePeopleStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], output_keys=['location_list'])

        with self:
            self.userdata.location_list = []
            # When there is no person around, location_list is not created. To avoid error this initialization
            # is added
            smach.StateMachine.add(
                'SAY_SAVE_PEOPLE_STARTED',
                SpeakActionState("Superman mode activated. I will save people."),
                transitions={aborted: 'SAY_SAVE_PEOPLE_STARTED', succeeded: 'FIND_A_PERSON_TO_SAVE'})

            # FROM "locate_a_person.py"
            smach.StateMachine.add(
                'FIND_A_PERSON_TO_SAVE',
                FindAPersonStateMachine(),
                transitions={aborted: succeeded, succeeded: 'INFORM_THE_PERSON'},
                remapping={'location_list': 'location_list'})

            smach.StateMachine.add(
                'INFORM_THE_PERSON',
                SpeakActionState("There is a fire in the kitchen. Are you Ok? Can you walk?"),
                transitions={succeeded: 'ARE_YOU_OK_ANSWER', aborted: 'INFORM_THE_PERSON'})

            smach.StateMachine.add(
                'ARE_YOU_OK_ANSWER',
                ListenOrders(YES_NO_GRAMMAR, timeout=TIMEOUT_YES_NO),
                transitions={succeeded: 'WHAT_I_HEARD1', aborted: 'ARE_YOU_OK_ANSWER', preempted: "GET_POSITION"},
                remapping={'o_userSaidData': 'i_heard'})

            smach.StateMachine.add(
                'WHAT_I_HEARD1',
                DummyIHeard(),
                transitions={'i_heard_yes': 'ASK_THE_PERSON_THE_EXIT', 'i_heard_no': 'GET_POSITION', 'i_heard_nothing': 'GET_POSITION'})

            smach.StateMachine.add(
                'GET_POSITION',
                GetPosition(),
                transitions={succeeded: 'RECORD_POSITION'},
                remapping={'memorised_poi_data': 'location_of_person'})
            #output_keyes=["memorised_poi_data"]

            smach.StateMachine.add(
                'RECORD_POSITION',
                RecordPosition(),
                transitions={succeeded: 'COMFORT_THE_PERSON'},
                remapping={'location_list': 'location_list'})

            smach.StateMachine.add(
                'COMFORT_THE_PERSON',
                SpeakActionState("Do not worry. Your position is recorded"),
                transitions={succeeded: 'FIND_A_PERSON_TO_SAVE'})

            smach.StateMachine.add(
                'ASK_THE_PERSON_THE_EXIT',
                SpeakActionState("Do you know the exit?"),
                transitions={succeeded: 'EXIT_ANSWER', aborted: 'ASK_THE_PERSON_THE_EXIT'})

            smach.StateMachine.add(
                'EXIT_ANSWER',
                ListenOrders(YES_NO_GRAMMAR),
                transitions={succeeded: 'WHAT_I_HEARD2', aborted: 'EXIT_ANSWER'},
                remapping={'o_userSaidData': 'i_heard'})

            smach.StateMachine.add(
                'WHAT_I_HEARD2',
                DummyIHeard(),
                transitions={'i_heard_yes': 'TELL_TO_GO_OUT', 'i_heard_no': 'FOLLOW', 'i_heard_nothing': 'EXIT_ANSWER'})

            smach.StateMachine.add(
                'FOLLOW',
                SpeakActionState("Please follow me to the exit"),
                transitions={succeeded: 'GO_TO_EXIT_DUMMY', aborted: 'FOLLOW'})

            smach.StateMachine.add(
                'TELL_TO_GO_OUT',
                SpeakActionState("Please go to exit."),
                transitions={succeeded: 'FIND_A_PERSON_TO_SAVE', aborted: 'INFORM_THE_PERSON'})

            smach.StateMachine.add(
                'GO_TO_EXIT_DUMMY',
                DummyStateMachineExit(),
                transitions={succeeded: 'GO_TO_EXIT_DOOR'})

            smach.StateMachine.add(
                'GO_TO_EXIT_DOOR',
                #GoExitAndFollowChecker(),  #Ricardo said that in GermanOpen we don't should check if the person is following
                MoveToRoomStateMachine(),
                transitions={succeeded: 'THIS_IS_EXIT', aborted: 'GO_TO_EXIT_DOOR'})

            smach.StateMachine.add(
                'THIS_IS_EXIT',
                SpeakActionState("Exit is here. Please leave the appartment."),
                transitions={succeeded: 'FIND_A_PERSON_TO_SAVE', aborted: 'FIND_A_PERSON_TO_SAVE'})
