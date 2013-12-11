#! /usr/bin/env python

import smach
import os
from pal_smach_utils.utils.global_common import succeeded, aborted
from pal_smach_utils.utils.run_command_local import RunCommandLocal


class AlertState(smach.State):
    """AlertState.

    Use this state to display an alert.
    The alert displayed will be a javax.swing.JOptionPane

    Important: This State will run the Alert.java file and is high probably that the current compiled version is not compatible with your
    computer. Then if nothing is being displayed, you should compile the java file with the command: javac Alert.java

    """
    def __init__(self, text=None, input_keys=[], output_keys=[]):
        """Construct for AlertState

        @type text: string
        @param text: The string to be displayed.

        """
        if not text:
            raise ValueError("You should set the variable 'text'")
        smach.State.__init__(self, input_keys=input_keys, output_keys=output_keys, outcomes=[succeeded, aborted])
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.text = text

    def execute(self, userdata):
        command = "java -classpath %s Alert \"%s\"" % (self.path, self.text)
        return RunCommandLocal(command=command).execute(userdata)
