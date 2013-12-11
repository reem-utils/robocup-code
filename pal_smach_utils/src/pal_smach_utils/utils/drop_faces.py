#! /usr/bin/env python

import smach
from global_common import succeeded, aborted
from pal_smach_utils.utils.run_script_on_robot import RunScriptOnRobot, ROBOT_SCRIPTS_PATH
from pal_smach_utils.utils.run_command_on_robot import RunCommandOnRobot

# WARNING: All folders in $FACES_DATABASE_PATH will be removed recursively. Don't set this variable to '/' NEVER.
FACES_DATABASE_PATH = "/mnt_flash/etc/database/people/"


class DropAllFacesStateMachine(smach.StateMachine):
    """DropAllFacesStateMachine.

    Use this State Machine to drop all faces on the robot.
    This state machine drop all faces on the robot's 'database' and restart the PersonServer.
    """
    def __init__(self, input_keys=[], output_keys=[]):
        """Constructor for DropAllFacesStateMachine.

        """
        smach.StateMachine.__init__(self, input_keys=input_keys, output_keys=output_keys, outcomes=[succeeded, aborted])
        self.YELLOW_BOLD = "\033[01;33m"
        self.NATIVE_COLOR = "\033[m"

        with self:
            command = "rm " + FACES_DATABASE_PATH + "* -rfv"

            smach.StateMachine.add(
                "DROP_FACES",
                RunCommandOnRobot(command),
                transitions={succeeded: "STOP_PERSON_SERVER", aborted: "STOP_PERSON_SERVER"}
                )

            smach.StateMachine.add(
                "STOP_PERSON_SERVER",
                RunScriptOnRobot(robot_scripts_path=ROBOT_SCRIPTS_PATH, script_name="personServerStop.sh"),
                transitions={succeeded: "START_PERSON_SERVER", aborted: "START_PERSON_SERVER"}
                )

            smach.StateMachine.add(
                "START_PERSON_SERVER",
                RunScriptOnRobot(robot_scripts_path=ROBOT_SCRIPTS_PATH, script_name="personServerStart.sh"),
                transitions={succeeded: succeeded, aborted: succeeded}
                )
