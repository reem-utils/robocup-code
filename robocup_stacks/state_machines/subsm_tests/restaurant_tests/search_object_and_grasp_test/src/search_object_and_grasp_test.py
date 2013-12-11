#! /usr/bin/env python
# -.- coding: utf-8 -.-


import roslib
roslib.load_manifest('search_object_and_grasp_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.stop_till_press_enter_and_read_key_board import StopTillPressEnterAndReadKeyBoard
from pal_smach_utils.grasping.search_object_and_grasp import SearchObjectAndGrasp

DEBUGGING = True
OBJECT_NAME_A = 'coke'

OBJECT_FETCHED_FRASE = "I've got the "
DIDNT_FIND_OBJECT_FRASE = "Couldn't find the "


class HeadDummyState(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['message1'])

    def execute(self, userdata):

        userdata.message1 = OBJECT_NAME_A

        print "DUMMY SATE ENDED"
        return succeeded


def main():
    rospy.init_node('sm_search_object_and_grasp_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "Let's search and grasp."
        smach.StateMachine.add('INTRO',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'DUMMY_STATE_GENERATE_OBJECT_NAME'})

        smach.StateMachine.add('DUMMY_STATE_GENERATE_OBJECT_NAME',
                               HeadDummyState(),
                               transitions={succeeded: 'SEARCH_FOR_OBJECT_AND_GRASP',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'message1': 'in_fetch_object_name'})

        """
        smach.StateMachine.add("START_GRASP_PROTOCOL",
                               InitGraspPipelineSM(),
                               transitions={succeeded: "SATISFY_DELIVERY_ORDER",
                                                aborted: aborted,
                                                preempted: aborted})
        """

        smach.StateMachine.add('SEARCH_FOR_OBJECT_AND_GRASP',
                               SearchObjectAndGrasp(),
                               transitions={'object_grasped_succesfully': 'OBJECT_FETCHED',
                                            'didnt_grasp_object': 'DIDNT_FIND_OBJECT',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'in_fetch_object_name': 'in_fetch_object_name',
                                          'objects_data_out': 'objects_data_out'})

        def say_text_cb(userdata):
                text_say = OBJECT_FETCHED_FRASE + userdata.in_fetch_object_name
                return text_say
        smach.StateMachine.add('OBJECT_FETCHED',
                               SpeakActionState(text_cb=say_text_cb, input_keys=['in_fetch_object_name']),
                               transitions={succeeded: 'BYE'})

        def say_text_cb(userdata):
            text_say = DIDNT_FIND_OBJECT_FRASE + userdata.in_fetch_object_name
            return text_say
        smach.StateMachine.add('DIDNT_FIND_OBJECT',
                               SpeakActionState(text_cb=say_text_cb, input_keys=['in_fetch_object_name']),
                               transitions={succeeded: 'BYE'})

        smach.StateMachine.add('BYE',
                               SpeakActionState("It was a pleasure to serve you."))

    sis = smach_ros.IntrospectionServer(
        'restaurant_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
