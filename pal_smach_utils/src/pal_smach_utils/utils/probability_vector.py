# -*- encoding: utf-8 -*-
import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import smach_ros
import random

from global_common import succeeded, preempted, aborted


def CreateAcumulatedProbabilityVector(vector):
    """
    This creates a vector that the lements with higher probability
    have a bigger segment of the interval [0,1]. This will invitably
    lead to elements with bigger segments will be more often pos_selected
    than the others when generated a random number range[0,1]

    Example: v = [0'2,0'3,0'5] --> v_acu = [0'2,0'5,1]
         A   B    C
        |--|---|-----|

    Bare in mind that if the input vector isn't normalized,
    it will be normalized to produce a correct acumulated probability vector.
    """

    if AddList(vector) != 1:
        vector = NormalizeVector(vector)

    acumulated_vector = list(vector)
    slice_value = 0.0
    for i in range(len(vector)):
        acumulated_vector[i] = vector[i] + slice_value
        slice_value = acumulated_vector[i]
    return acumulated_vector


def AddList(vector):
    sum = 0
    for i in range(0, len(vector)):
        sum = sum + vector[i]

    return sum


def NormalizeVector(vector):
    """
    Normalize Vector, al the vector numbers sum up a total of 1.
    Thre is an exception: if the vector is a Null vector ( all elemnts are Zero)
    then normalize has no meaning and therefore the vector is returned unmodified.
    """
    vector_sum = AddList(vector)

    if vector_sum != 0.0:
        for i in range(len(vector)):
            vector[i] = vector[i] / vector_sum

    return vector


def GenerateVector(L):
    """
    Creates a vector full of zeros of length 'L'

    """
    return [0.0] * L


def FillRandomProbabilityVector(vector):

    """
    Given a vector, it fills it with random numbers that add up to 1
    """
    #Fill vector with random floats [0,1]
    for i in range(len(vector)):
        vector[i] = random.random()

    vector = NormalizeVector(vector)

    return vector


class RandomPickFromProbabilityVector(smach.State):

    """
    Given a probability vector , it will return in pos_selected_out the element
    picked randomly, but based on who has more probabilities of winning.
    """

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted],
                                    input_keys=['in_objective_vector'],
                                    output_keys=['pos_selected_out'])

    def execute(self, userdata):

        acumulated_prob_vector = CreateAcumulatedProbabilityVector(userdata.in_objective_vector)
        i = 0
        random_number = random.random()
        random_number_not_in_interval = True
        while random_number_not_in_interval:
            random_number_not_in_interval = (random_number >= acumulated_prob_vector[i])
            i += 1

        userdata.pos_selected_out = i - 1
        return succeeded
