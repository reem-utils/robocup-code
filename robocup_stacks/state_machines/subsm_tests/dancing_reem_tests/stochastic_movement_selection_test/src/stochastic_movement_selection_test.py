#! /usr/bin/env python

import roslib; roslib.load_manifest('stochastic_movement_selection_test')
import rospy
import smach

import actionlib

from std_msgs import *

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from stochastic_movement_selection import StochasticMovementSelection

INIT_CURRENT_POS = 'middle'
INIT_PREV_CURRENT_POS = 'none'
MIDDLE_MOV_LIST = ['waiting_1.xml', 'transition_from_middle_to_sides.xml']
UP_MOV_LIST = ['waiting_1.xml', 'transition_from_up_to_middle.xml']
SIDES_MOV_LIST = ['waiting_1.xml', 'transition_from_sides_to_middle.xml']
DANGEROUS_MOV_LIST = ['waiting_1.xml', 'transition_from_dangerous_to_up.xml']


class PrintUserData4(smach.State):

    def __init__(self,
                message_name1='Message1',
                message_name2='Message2',
                message_name3='Message3',
                message_name4='Message4'):
            smach.State.__init__(self,
                    outcomes=['another_loop', 'end_program', preempted, aborted],
                    input_keys=['message1',
                                'message2',
                                'message3',
                                'message4'])

            self._message_name1 = message_name1
            self._message_name2 = message_name2
            self._message_name3 = message_name3
            self._message_name4 = message_name4

    def execute(self, userdata):
            rospy.loginfo('This is the %s: %s' % (self._message_name1, str(userdata.message1)))
            rospy.loginfo('This is the %s: %s' % (self._message_name2, str(userdata.message2)))
            rospy.loginfo('This is the %s: %s' % (self._message_name3, str(userdata.message3)))
            rospy.loginfo('This is the %s: %s' % (self._message_name4, str(userdata.message4)))

            pressed_key = raw_input('##### Press ENTER key to make another execution, any other key to end: #####')
            if pressed_key == '':
                return 'another_loop'

            return 'end_program'


class StochasticDummyState(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                            outcomes=[succeeded, preempted, aborted],
                            output_keys=['current_position_out',
                                    'prev_current_position_out',
                                    'dict_available_movements_out',
                                    'probability_vector_out'])

    def execute(self, userdata):

        curr_pos = INIT_CURRENT_POS
        userdata.current_position_out = INIT_CURRENT_POS
        prev_pos = INIT_PREV_CURRENT_POS
        userdata.prev_current_position_out = INIT_PREV_CURRENT_POS
        dict_av = CreateFillAvailMovDict()
        userdata.dict_available_movements_out = CreateFillAvailMovDict()
        pro_vec = [0.0]
        userdata.probability_vector_out = [0.0]
        rospy.loginfo("DUMMY STATE DATA GENERATED:\nINIT_CURRENT_POS: %s \nPREV_CURRENT_POS: %s \nDICT_MOV: %s \nPROB_VECTOR: %s" % (str(curr_pos), str(prev_pos), str(dict_av), str(pro_vec)))
        return succeeded


def CreateFillAvailMovDict():

    mov_dict = {}
    mov_dict['middle'] = MIDDLE_MOV_LIST
    mov_dict['up'] = UP_MOV_LIST
    mov_dict['sides'] = SIDES_MOV_LIST
    mov_dict['dangerous'] = DANGEROUS_MOV_LIST

    return mov_dict


def main():
    rospy.init_node('sm_stochastic_movement_selection_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add('STOCHASTIC_DUMMY_STATE',
                                StochasticDummyState(),
                                transitions={succeeded: 'STOCHASTIC_MOVEMENT_SELECTION',
                                                preempted: preempted,
                                                aborted: aborted},
                                remapping={
                                    'current_position_out': 'current_position',
                                    'prev_current_position_out': 'prev_current_position',
                                    'dict_available_movements_out': 'in_dict_available_movements',
                                    'probability_vector_out': 'probability_vector'})

        smach.StateMachine.add('STOCHASTIC_MOVEMENT_SELECTION',
                                StochasticMovementSelection(),
                                transitions={
                                    succeeded: 'PRINT_DATA',
                                    preempted: preempted,
                                    aborted: aborted},
                                remapping={'in_probability_vector': 'probability_vector',
                                            'in_prev_current_position': 'prev_current_position',
                                            'in_movement_database_dict': 'in_dict_available_movements',
                                            'in_current_position': 'current_position',
                                            'probability_vector_out': 'probability_vector',
                                            'selected_random_movement_out': 'selected_movement',
                                            'new_current_position_out': 'current_position',
                                            'new_prev_current_position_out': 'prev_current_position'})

        smach.StateMachine.add('PRINT_DATA',
                                PrintUserData4(
                                    'probability_vector',
                                    'selected_movement',
                                    'current_position',
                                    'prev_current_position'),
                                transitions={'another_loop': 'STOCHASTIC_MOVEMENT_SELECTION',
                                    'end_program': succeeded,
                                    preempted: preempted,
                                    aborted: aborted},
                                remapping={
                                    'message1': 'probability_vector',
                                    'message2': 'selected_movement',
                                    'message3': 'current_position',
                                    'message4': 'prev_current_position'})

    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
