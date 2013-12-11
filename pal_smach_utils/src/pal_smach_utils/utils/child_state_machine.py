#! /usr/bin/env python
# -.- coding: utf-8 -.-
import roslib
roslib.load_manifest('smach')
import smach

import inspect
import traceback

from global_common import aborted
from pal_smach_utils.utils.colors import Colors

c = Colors()
states_dictionary = {}

class ChildStateMachine(smach.StateMachine):
    """ChildStateMachine.

    This StateMachine is a child of smach.StateMachine
    The differences between this StateMachine and smach.StateMachine are:
        If a state aborts, will be printed a message with the filename and line where the state was added to the StateMachine.
    """
    def __init__(self, outcomes, input_keys=[], output_keys=[]):
        super(ChildStateMachine, self).__init__(outcomes, input_keys, output_keys)

    ### Construction methods
    @staticmethod
    def add(label, state, transitions = None, remapping = None):

        frame = inspect.currentframe()
        stack = traceback.extract_stack(f=frame, limit=2)
        last_line = stack[0][:-1]
        last_line = ["'%s' line %d." % (last_line[0], last_line[1])]

        if not states_dictionary.has_key(label):
            states_dictionary[label] = last_line
        else:
            states_dictionary[label] += last_line

        smach.StateMachine.add(label, state, transitions, remapping)

    def _update_once(self):
        """Method that updates the state machine once.
        This checks if the current state is ready to transition, if so, it
        requests the outcome of the current state, and then extracts the next state
        label from the current state's transition dictionary, and then transitions
        to the next state.

        Is the transition is aborted, a message with the filname and the linenumber where the state was defined will be printed on the screen.
        """
        label = self._current_label
        outcome = super(ChildStateMachine, self)._update_once()

        if str(outcome) == aborted:
            for line in states_dictionary[label]:
                print c.YELLOW_UNDERSCORE +'State \'' + label +'\' aborted. Defined on file ' + str(line) + c.NATIVE_COLOR

        return outcome
