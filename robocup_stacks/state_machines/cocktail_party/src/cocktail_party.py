#! /usr/bin/env python
# -.- coding: utf-8 -.-
""" Here is located the CocktailPartyStateMachine """
import roslib
roslib.load_manifest('cocktail_party')
import smach

from pal_smach_utils.navigation.enter_room import EnterRoomStateMachine
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.navigation.take_serve_drinks import TakeServeDrinkOrdersSM
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables as cp_vars
from pal_smach_utils.utils.drop_faces import DropAllFacesStateMachine
from pal_smach_utils.utils.run_script_on_robot import RunScriptOnRobot  # , ROBOT_SCRIPTS_PATH
from pal_smach_utils.speech.sound_action import SpeakActionState
#from pal_smach_utils.utils.robot_controllers_activation import StopRobotControllers
#from pal_smach_utils.utils.run_command_on_robot import RunCommandOnRobot


class CocktailPartyStateMachine(smach.StateMachine):
    """CocktailPartyStateMachine.

    Requirements:
    Before execute this State Machine, you should launch: roslaunch cocktail_party test_check_dependences.launch
    This step is to be sure that all required actions/services are running and is some node publishing on specific topics.
    Tke kinect should be connected on the robot too.


    Using this class, the robot will learn person, recognize person and and deliver drinks.
    The robot will start entering in a room. After this, it will move to the party_room, learn the face of some persons, ask the drinks names
    that they want to drink, move to drinks_location, grasp the drink and go back to party_room to delivery it (one a time).
    After serve all drinks, the robot will move to exit.

    The variables of this State Machine are defined on the file cocktail_party.yaml
    """

    def __init__(self):
        """Constructor for CocktailPartyStateMachine.

        """
        smach.StateMachine.__init__(self, input_keys=[], output_keys=[], outcomes=[succeeded, aborted, preempted])

        with self:

            def start_cb(userdata, initial_st_name):
                """ Set some variables on userdata """
                userdata.party_room = cp_vars.M_PARTY_ROOM
                userdata.exit = cp_vars.M_EXIT

            self.register_start_cb(start_cb)

            smach.StateMachine.add(
                "DROP_FACES",
                DropAllFacesStateMachine(),
                transitions={succeeded: "SAY_READY", aborted: "SAY_READY"}
                )  #In theory will never return aborted

            smach.StateMachine.add(
                "SAY_READY",
                SpeakActionState("I'm ready to start the Cocktail Party challenge!"),
                transitions={succeeded: "ENTER_ROOM", aborted: "ENTER_ROOM", preempted:  "ENTER_ROOM"}
                )

            smach.StateMachine.add(
                'ENTER_ROOM',
                EnterRoomStateMachine(cp_vars.DOOR_DISTANCE, orient_after_passing=0),
                transitions={succeeded: "STOP_KINECT_GRASP", aborted: 'ENTER_ROOM', preempted: "ENTER_ROOM"}
                )
            # outputs: "door_position"

#            smach.StateMachine.add( #This part was 'removed' because EnterRoomStateMachine will disable reemAlive
#                "STOP_REEM_ALIVE",  # Sam said: Stop reemAlive to avoid problems with a lot of sockets open
#                RunScriptOnRobot(robot_scripts_path=ROBOT_SCRIPTS_PATH, script_name="reemAliveStop.sh"),
#                transitions={succeeded: "STOP_KINECT_GRASP", aborted: "STOP_KINECT_GRASP"}
#                )

            smach.StateMachine.add(
                "STOP_KINECT_GRASP",
                RunScriptOnRobot(script_name="kinectToGraspStop.sh"),
                transitions={succeeded: "MOVE_TO_PARTY_ROOM", aborted: "MOVE_TO_PARTY_ROOM"}
                )  # Stopping kinect grasp because MoveToCaller... will enable nite_recognizer.

            smach.StateMachine.add(
                "MOVE_TO_PARTY_ROOM",
                MoveToRoomStateMachine(announcement=["I'm going to %s to take the drink orders!"]),
                remapping={"room_name": "party_room"},
                transitions={succeeded: "TAKE_AND_SERVE_DRINK_ORDERS", aborted: "WARNING_UNREACHABLE", preempted: "WARNING_UNREACHABLE"}
                )
            # inputs: "room_name". outputs: "room_location"

            smach.StateMachine.add(
                "WARNING_UNREACHABLE",
                SpeakActionState(text="I can't go to %s. I'll take the orders here!" % cp_vars.M_PARTY_ROOM),
                transitions={succeeded: "TAKE_AND_SERVE_DRINK_ORDERS", aborted: "TAKE_AND_SERVE_DRINK_ORDERS", preempted: "TAKE_AND_SERVE_DRINK_ORDERS"}
            )

            smach.StateMachine.add(
                "TAKE_AND_SERVE_DRINK_ORDERS",
                TakeServeDrinkOrdersSM(num_persons=cp_vars.NUMBER_PERSONS, all_at_a_time=cp_vars.ALL_AT_A_TIME,\
                room_name=cp_vars.M_PARTY_ROOM, sleep=cp_vars.SLEEP_MOVE_CALLER, ask_to_come=cp_vars.ASK_TO_COME),
                transitions={succeeded: "MOVE_TO_EXIT", aborted: "MOVE_TO_EXIT", preempted: "MOVE_TO_EXIT"}
            )

            smach.StateMachine.add(
                'MOVE_TO_EXIT',
                MoveToRoomStateMachine(announcement="I'm going to the %s to finish the Cocktail Party challenge!"),
                remapping={"room_name": "exit"},
                transitions={succeeded: "STOP_GRASP", aborted: "SAY_STAY_STOPPED", preempted: "SAY_STAY_STOPPED"}
                )
            # inputs: "room_name". outputs: "room_location"

            smach.StateMachine.add(
                "SAY_STAY_STOPPED",
                SpeakActionState("I can't go to the %s. I'll keep stopped here!" % cp_vars.M_EXIT),
                transitions={succeeded: "STOP_GRASP", aborted: "STOP_GRASP"}
            )

            smach.StateMachine.add(
                "STOP_GRASP",
                RunScriptOnRobot(script_name="graspingStop.sh"),
                transitions={succeeded: "SAY_FINISHED", aborted: "SAY_FINISHED"}
                )

            smach.StateMachine.add(
                "SAY_FINISHED",
                SpeakActionState("Cocktail Party finished!"),
                transitions={succeeded: succeeded, aborted: succeeded, preempted: succeeded}
                )
