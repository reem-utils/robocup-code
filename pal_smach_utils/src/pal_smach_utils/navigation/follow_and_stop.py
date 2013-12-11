#! /usr/bin/env python
# vim: expandtab ts=4 sw=4
### FOLOW_AND_STOP.PY ###
import rospy
import roslib
roslib.load_manifest('pal_smach_utils')
import smach
from smach import Concurrence

from pal_smach_utils.navigation.follow_operator import FollowOperator
from pal_smach_utils.navigation.listen_commands import ListenCommands
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from pal_smach_utils.utils.debug import setDebugLevel


# gets called when ANY child state terminates
def child_term_cb(outcome_map):
    #sterminate both state machines if condition is satisfied
    #if (outcome_map['LISTEN_COMMANDS'] == succeeded):
       #return True
    #return False
    return True


# gets called when ALL child states are terminated
def out_cb(outcome_map):
    #if outcome_map['LISTEN_COMMAND_FOR_FOLLOW_ME'] == 'succeeded':
    return succeeded


class FollowAndStop(smach.Concurrence):
    def __init__(self, distToHuman=0.9, state_machine_name="restaurant"):
        smach.Concurrence.__init__(
            self,
            outcomes=[succeeded, preempted, aborted],
            default_outcome=succeeded,
            child_termination_cb=child_term_cb,
            outcome_cb=out_cb,
            input_keys=["in_learn_person"])
        rospy.set_param("/params_learn_and_follow_operator_test/distance_to_human", distToHuman)

        with self:

            setDebugLevel(0)

            Concurrence.add('FOLLOW_OPERATOR',
                            FollowOperator(distToHuman),
                            remapping={"in_learn_person": "in_learn_person"})

            Concurrence.add('LISTEN_COMMANDS',
                            ListenCommands(state_machine_name))
