#! /usr/bin/env python

import smach
import roslib.packages
from global_common import succeeded, aborted
from pal_smach_utils.utils.run_command_local import RunCommandLocal


class RunScriptLocal(smach.State):
    """RunScriptLocal State.

    Use this State to execute a script locally.
    The scripts that this State can run are located on 'robocup_stacks/scripts' folder.

    """
    def __init__(self, script_name=None, sudo_enabled=False, input_keys=[], output_keys=[]):
        """Constructor for RunScriptLocal.

        @type script_name: string
        @param script_name: The script name that you want execute.

        @type sudo_enabled: boolean
        @param sudo_enabled: If True, the command will be executed as sudo. It will open a dialog and you should type your password.

        """
        smach.State.__init__(self, input_keys=input_keys, output_keys=output_keys, outcomes=[succeeded, aborted])

        if script_name is None:
            raise ValueError("You should set the variable 'script_name'")

        self.scripts_path = roslib.packages.get_pkg_dir('scripts')
        self.full_script_path = self.scripts_path + "/" +script_name
        self.script = RunCommandLocal(command=self.full_script_path, sudo_enabled=sudo_enabled)

    def execute(self, userdata):
        return self.script.execute(userdata)
