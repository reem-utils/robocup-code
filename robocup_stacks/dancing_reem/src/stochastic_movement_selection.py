#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import roslib
roslib.load_manifest('dancing_reem')
import smach
import rospy
import smach_ros
import actionlib
from smach_ros import SimpleActionState, ServiceState

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from list_movements_vector_translator import ListMovementsToVector, TurnVectorPickToMovementName, DecideIfNeedToCreateNewProbabilityVector
from pal_smach_utils.utils.probability_vector import RandomPickFromProbabilityVector
from vector_probability_management import FillRandomProbabilityVectorState, DistabliseProbabilityVectorState


class StochasticMovementSelection(smach.StateMachine):

    def __init__(self):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                                    input_keys=['in_probability_vector',
                                                'in_prev_current_position',
                                                'in_movement_database_dict',
                                                'in_current_position'],
                                    output_keys=['probability_vector_out',
                                                 'selected_random_movement_out',
                                                 'new_current_position_out',
                                                 'new_prev_current_position_out'])
        with self:

            smach.StateMachine.add('DECIDE_IF_NEED_TO_CREATE_NEW_PROBABILITY_VECTOR',
                                   DecideIfNeedToCreateNewProbabilityVector(),
                                   transitions={'changed_position': 'TURN_DATABASE_LIST_TO_PROBABLITY_VECTOR',
                                                'not_changed_position': 'DISTABLISE_PROBABILITY_VECTOR',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_prev_current_position': 'in_prev_current_position',
                                              'in_current_position': 'in_current_position'})

            smach.StateMachine.add('TURN_DATABASE_LIST_TO_PROBABLITY_VECTOR',
                                   ListMovementsToVector(),
                                   transitions={succeeded: 'FILL_RANDOM_PROBABILITIES_IN_VECTOR',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_database_dict': 'in_movement_database_dict',
                                              'in_current_position': 'in_current_position',
                                              'database_vector_out': 'probability_vector_out'})

            smach.StateMachine.add('FILL_RANDOM_PROBABILITIES_IN_VECTOR',
                                   FillRandomProbabilityVectorState(),
                                   transitions={succeeded: 'DISTABLISE_PROBABILITY_VECTOR',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_empty_vector': 'probability_vector_out',
                                              'full_vector_out': 'probability_vector_out'})

            smach.StateMachine.add('DISTABLISE_PROBABILITY_VECTOR',
                                   DistabliseProbabilityVectorState(),
                                   transitions={succeeded: 'RANDOM_PICK_MOVEMENT',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_database_dict': 'in_movement_database_dict',
                                              'in_current_position': 'in_current_position',
                                              'in_full_vector': 'probability_vector_out',
                                              'full_vector_out': 'probability_vector_out'})

            smach.StateMachine.add('RANDOM_PICK_MOVEMENT',
                                   RandomPickFromProbabilityVector(),
                                   transitions={succeeded: 'TURN_MOVEMENT_PICKED_TO_MOVEMENT_NAME',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_objective_vector': 'probability_vector_out',
                                              'pos_selected_out': 'movement_selected_in_vector'})

            smach.StateMachine.add('TURN_MOVEMENT_PICKED_TO_MOVEMENT_NAME',
                                   TurnVectorPickToMovementName(),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_movement_selected_in_vector': 'movement_selected_in_vector',
                                              'in_database_dict': 'in_movement_database_dict',
                                              'in_current_position': 'in_current_position',
                                              'movement_name_out': 'selected_random_movement_out',
                                              'new_current_position_out': 'new_current_position_out',
                                              'new_prev_current_position_out': 'new_prev_current_position_out'})
