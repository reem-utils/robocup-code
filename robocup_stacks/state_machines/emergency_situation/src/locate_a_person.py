#! /usr/bin/env python
# vim: expandtab ts=4 sw=4

import roslib
roslib.load_manifest('emergency_situation')
import rospy
import smach

from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from find_and_go_to_person import FindAndGoToPersonStateMachine
# from pal_smach_utils.navigation.go_to_closest_person import GoToClosestPerson
# from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
# Creating the room list

GERMAN_OPEN_LOCATION_LIST = ["software", "exit", "kitchen"]
ROBOCUP_LOCATION_LIST = ["bedroom", "hallway", "living_room"]


class IncreaseRoomNumber(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted], output_keys=['room_number'], input_keys=['room_number'])

    def execute(self, userdata):
        userdata.room_number = userdata.room_number + 1
        return succeeded


class RoomNameList(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted], output_keys=['room_name', 'room_number'], input_keys=['room_number'])
        self.room_number = 0
        self.room_list = []

    def execute(self, userdata):
        if not self.room_list:
            self.pois = rospy.get_param("/mmap/poi/submap_0")

            for key, value in self.pois.iteritems():
                # self.room_list.append(value[1])
                if value[1] in ROBOCUP_LOCATION_LIST:
                    self.room_list.append(value[1])

            rospy.loginfo("\n=============== We have %d locations ===========\n" % len(self.room_list))
            rospy.loginfo("\n=============== %s ===========\n" % self.room_list)

            # self.room_list.pop(self.room_list.index('kitchen'))
            # self.room_list.pop(self.room_list.index('exit'))
            # self.room_list.append('kitchen')
            self.room_list.reverse()

        if userdata.room_number < len(self.room_list):
            print ":::::::::::  ROOM INDEX NO :" + str(userdata.room_number)
            userdata.room_name = str(self.room_list[userdata.room_number])
            return succeeded
        else:
            return aborted


class FindAPersonStateMachine(smach.StateMachine):
    '''It will move from room to room and look for any person. Finding person is from find_and_go_to_person.py (It will move to person)'''

    def __init__(self):
        smach.StateMachine.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['location_list'])

        with self:
            self.userdata.room_number = 0
            smach.StateMachine.add(
                'ROOM_NAME_LIST',
                RoomNameList(),
                transitions={succeeded: 'GO_TO_NEXT_ROOM', aborted: aborted})

            smach.StateMachine.add(
                'GO_TO_NEXT_ROOM',
                MoveToRoomStateMachine(),
                transitions={succeeded: 'FIND_A_PERSON', aborted: 'ROOM_NAME_LIST'})

            # FROM find_and_go_to_person.py
            smach.StateMachine.add(
                'FIND_A_PERSON',
                FindAndGoToPersonStateMachine(),
                transitions={aborted: 'INCREASE_ROOM_NUMBER', succeeded: succeeded},
                remapping={'location_list': 'location_list'})

            smach.StateMachine.add(
                'INCREASE_ROOM_NUMBER',
                IncreaseRoomNumber(),
                transitions={succeeded: 'ROOM_NAME_LIST'})
