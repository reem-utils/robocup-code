# -*- encoding: utf-8 -*-

import roslib; roslib.load_manifest('dancing_reem')
import smach
import rospy

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from dancing_utils import UpdatePosition


class ListMovementsToVector(smach.State):

    """
    Using the database_dictionary and the current_position key,
    we output a vector of the same size as the list in the dictionary
    linked to the key corresponding to current_position.
    """

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted],
                                input_keys=['in_database_dict',
                                            'in_current_position'],
                                output_keys=['database_vector_out'])

    def execute(self, userdata):

        movements_list = userdata.in_database_dict.get(userdata.in_current_position)
        movement_vector = [0.0] * len(movements_list)
        userdata.database_vector_out = movement_vector

        return succeeded


class TurnVectorPickToMovementName(smach.State):

    def __init__(self):

        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             input_keys=['in_movement_selected_in_vector',
                                         'in_database_dict',
                                         'in_current_position'],
                             output_keys=['movement_name_out', 'new_current_position_out', 'new_prev_current_position_out'])

    def execute(self, userdata):

        """
        We get from the dictionary,in the current pos, the movement_name
        selected randomly from the list.
        """
        print "CURRENT POS == > " + str(userdata.in_current_position)
        print "MOVEMENT SELECTED IN VECTOR == > " + str(userdata.in_movement_selected_in_vector)
        print "DATABSE DICT CURRENT POSITION LIST ==> " + str(userdata.in_database_dict.get(userdata.in_current_position))
        name = userdata.in_database_dict.get(userdata.in_current_position)[userdata.in_movement_selected_in_vector]
        userdata.movement_name_out = name

        userdata.new_current_position_out, userdata.new_prev_current_position_out = UpdatePosition(name, userdata.in_current_position)
        return succeeded


class DecideIfNeedToCreateNewProbabilityVector(smach.State):

    """
    This state looks if we have changed of position or not.
    It will also detect the first time we enter the SM because the prev_pos will
    be 'None' and the current 'middle', so it will treat it as if had changed pos.
    Changed_pos means that we have to create a new probability vetor, due to the differences
    in number of steps that might have each position.
    Otherwise, we have already a probability vector and we have to go directly
    to distablize the probability vector.
    """

    def __init__(self):

            smach.State.__init__(self, outcomes=['changed_position', 'not_changed_position', preempted, aborted],
                                        input_keys=['in_prev_current_position', 'in_current_position'])

    def execute(self, userdata):

            if ChangedOfPosition(userdata.in_prev_current_position, userdata.in_current_position):
                return 'changed_position'

            return 'not_changed_position'


def ChangedOfPosition(prev_pos, current_pos):

    return prev_pos != current_pos
