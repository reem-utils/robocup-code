#! /usr/bin/env python
# -.- coding: utf-8 -.-
'''
MOVE_TO_TABLE.PY
'''

import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
from smach_ros import ServiceState
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from std_srvs.srv import Empty

SEEN_A_TABLE_FRASE = "Oh, there's a table right ahead. Let's see what there  is there"
DIDNT_FIND_TABLE_FRASE = "Ahoy, there are no tables in sight."
FOUND_TABLE_FRASE = "I found a table."
MOVED_TO_TABLE_FRASE = "Yeah!"
DIDNT_MOVE_TO_TABLE_FRASE = "Couldn't reach the table."


class MoveToTable(smach.StateMachine):

    '''
    Moves to a table in sight.
    '''

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    ['got_to_table', 'didnt_get_to_table', preempted, aborted])

        with self:

            smach.StateMachine.add('START_MOVE_TABLE',
                                   SpeakActionState(SEEN_A_TABLE_FRASE),
                                   transitions={succeeded: 'FIND_TO_TABLE_LUCA_SERVICE',
                                                preempted: preempted,
                                                aborted: aborted})

            def find_table_response_cb(userdata, response):
                if response:
                    return succeeded
                else:
                    rospy.loginfo("")
                    return aborted

            smach.StateMachine.add('FIND_TO_TABLE_LUCA_SERVICE',
                                   ServiceState("find", Empty, response_cb=find_table_response_cb),
                                   transitions={succeeded: 'FOUND_TABLE',
                                                aborted: 'DIDNT_FIND_TABLE'})

            smach.StateMachine.add('FOUND_TABLE',
                                   SpeakActionState(FOUND_TABLE_FRASE),
                                   transitions={succeeded: 'MOVE_TO_TABLE_LUCA_SERVICE',
                                                preempted: preempted,
                                                aborted: aborted})

            smach.StateMachine.add('DIDNT_FIND_TABLE',
                                   SpeakActionState(DIDNT_FIND_TABLE_FRASE),
                                   transitions={succeeded: 'didnt_get_to_table',
                                                preempted: preempted,
                                                aborted: aborted})

            def move_to_table_response_cb(userdata, response):
                if response:
                    rospy.loginfo("TABLE FOUND")
                    return succeeded
                else:
                    rospy.loginfo("TABLE NOT FOUND")
                    return aborted

            smach.StateMachine.add('MOVE_TO_TABLE_LUCA_SERVICE',
                                   ServiceState("find", Empty, response_cb=move_to_table_response_cb),
                                   transitions={succeeded: 'MOVED_TO_TABLE',
                                                aborted: 'DIDNT_MOVE_TO_TABLE'})

            smach.StateMachine.add('MOVED_TO_TABLE',
                                   SpeakActionState(MOVED_TO_TABLE_FRASE),
                                   transitions={succeeded: 'got_to_table',
                                                preempted: preempted,
                                                aborted: aborted})

            smach.StateMachine.add('DIDNT_MOVE_TO_TABLE',
                                   SpeakActionState(DIDNT_MOVE_TO_TABLE_FRASE),
                                   transitions={succeeded: 'didnt_get_to_table',
                                                preempted: preempted,
                                                aborted: aborted})


# vim: expandtab ts=4 sw=4
