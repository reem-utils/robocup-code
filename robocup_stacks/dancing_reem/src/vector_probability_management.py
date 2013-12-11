# -*- encoding: utf-8 -*-

import roslib; roslib.load_manifest('dancing_reem')
import rospy
import smach
import smach_ros
import random

from dancing_utils import NameIsAStep, NumberOfTransitions
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.probability_vector import NormalizeVector, FillRandomProbabilityVector

TRANSITION_FACTOR_MAXIMUM = 0.01
TRANSITION_FACTOR_MINIMUM = 0.0

NUMBER_REPET_BEFORE_DIESTABLE = 1


def DistabliseProbabilityVector(vector, database_dict, current_pos):

    """
    We increse (transition_factor) the probability in those vector elements that correspond to
    transitions and dicrease (step_factor) probabilities in those that are steps.
    This way, the more time we spend in tha same position, the more increases the
    the probability to make a transition to another pose.
    This dicrese in the probability in the steps will be higher if we have
    fewer transitions in that position. That is what the number_transitions is used for.
    Eventualy, the step probabilities will be zero, and the 100 percent will tend to be distributed
    in equal parts between the transition movements, but because when all the steps prob will be zero,
    a transition will be made, never will they have all the transitions the same probability.
    """

    number_transitions = NumberOfTransitions(database_dict, current_pos)
    transition_factor = random.uniform(TRANSITION_FACTOR_MINIMUM, TRANSITION_FACTOR_MAXIMUM)
    step_factor = -(transition_factor / (2 * number_transitions))

    for i in range(len(vector)):
        movement_name = database_dict.get(current_pos)[i]
        if NameIsAStep(movement_name):

            vector[i] = vector[i] + step_factor

            if vector[i] < 0.0:
                vector[i] = 0.0

        else:
            vector[i] = vector[i] + transition_factor

    # Now we normalize the resulting vector
    vector = NormalizeVector(vector)

    return vector


class DistabliseProbabilityVectorState(smach.State):

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted],
                                    input_keys=['in_database_dict',
                                                'in_current_position',
                                                'in_full_vector'],
                                    output_keys=['full_vector_out'])

    def execute(self, userdata):

        probability_vector = DistabliseProbabilityVector(userdata.in_full_vector,
                                                        userdata.in_database_dict,
                                                        userdata.in_current_position)
        userdata.full_vector_out = probability_vector

        return succeeded


class FillRandomProbabilityVectorState(smach.State):

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted],
                                    input_keys=['in_empty_vector'],
                                    output_keys=['full_vector_out'])

    def execute(self, userdata):

        probability_vector = FillRandomProbabilityVector(userdata.in_empty_vector)
        userdata.full_vector_out = probability_vector
        return succeeded
