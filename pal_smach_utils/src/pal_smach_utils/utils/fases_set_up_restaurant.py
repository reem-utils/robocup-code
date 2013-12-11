#! /usr/bin/env python
# -.- coding: utf-8 -.-
# vim: expandtab ts=4 sw=4
# Author RDaneelOlivaw

import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.robot_controllers_activation import StopRobotControllers
from pal_smach_utils.utils.run_script_on_robot import RunScriptOnRobot, ROBOT_SCRIPTS_PATH
#from pal_smach_utils.utils.run_script_local import RunScriptLocal
from pal_smach_utils.grasping.initialise_and_close_grasp import InitGraspPipelineSM
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.colors import Colors
from smach import CBState
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers

colors = Colors()


class InitialRestaurantFaseSetUp(smach.StateMachine):
    """
    Stops all the the services not needed during all the test and/or the initial fase.
    """

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted])

        with self:
            ## STARTS
            @smach.cb_interface(outcomes=[succeeded])
            def print_things(userdata):
                rospy.logwarn(colors.BACKGROUND_GREEN + "STARTING ALL the things that should be started for restaurant.%s" % (colors.NATIVE_COLOR))
                return succeeded

            smach.StateMachine.add('STARTING_INITIAL_RESTAURANT_FASE_SET_UP',
                                   CBState(print_things),
                                   remapping={'in_learn_person': "in_learn_person"},
                                   transitions={succeeded: 'START_PERSON_SERVER'})

            try:
                smach.StateMachine.add("START_PERSON_SERVER",
                                       RunScriptOnRobot(script_name="personServerStart.sh"),
                                       transitions={succeeded: "PEOPLE_TRACKING_RAI_START",
                                                    aborted: "PEOPLE_TRACKING_RAI_START"})
            except:
                rospy.loginfo("PERSON SERVER NOT LAUNCHED; NOTHING TO STOP")

            try:
                """
                In case of starting, it gives aborted when the service to start is already running.
                Thats why we continue.
                """
                smach.StateMachine.add("PEOPLE_TRACKING_RAI_START",
                                       RunScriptOnRobot(script_name="iri_people_tracking_raiStart.sh"),
                                       transitions={succeeded: "START_GRASP_PROTOCOL",
                                                    aborted: "START_GRASP_PROTOCOL"})
            except:
                rospy.loginfo("People TRacking NOT LAUNCHED; NOTHING TO STOP")

            smach.StateMachine.add("START_GRASP_PROTOCOL",
                                   InitGraspPipelineSM(),
                                   transitions={succeeded: "STOPPING_INITIAL_RESTAURANT_FASE_SET_UP",
                                                aborted: aborted,
                                                preempted: aborted})

            # STOPS
            @smach.cb_interface(outcomes=[succeeded])
            def print_things(userdata):
                rospy.logwarn(colors.BACKGROUND_RED + "STOPPING ALL the things that should be stopped in restaurant init.%s" % (colors.NATIVE_COLOR))
                return succeeded

            smach.StateMachine.add('STOPPING_INITIAL_RESTAURANT_FASE_SET_UP',
                                   CBState(print_things),
                                   remapping={'in_learn_person': "in_learn_person"},
                                   transitions={succeeded: 'STOP_REEM_ALIVE'})

            try:
                smach.StateMachine.add("STOP_REEM_ALIVE",
                                       RunScriptOnRobot(robot_scripts_path=ROBOT_SCRIPTS_PATH, script_name="reemAliveStop.sh"),
                                       transitions={succeeded: "FINISHED_INIT_SERVICES_RESTAURANT_SET_UP",
                                                    aborted: "FINISHED_INIT_SERVICES_RESTAURANT_SET_UP"})
            except:
                rospy.loginfo("REEM ALIVE NOT LAUNCHED; NOTHING TO STOP")

            init_text = "I'm ready to start."
            smach.StateMachine.add('FINISHED_INIT_SERVICES_RESTAURANT_SET_UP',
                                   SpeakActionState(init_text),
                                   transitions={succeeded: succeeded})


class DeliverRestaurantFaseSetUp(smach.StateMachine):
    """
    Initialises all the protocols that CompleteGraspPipelineStateMachine need to work.
    """

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted])

        with self:

            @smach.cb_interface(outcomes=[succeeded])
            def print_things(userdata):
                rospy.logwarn(colors.BACKGROUND_RED + "STOPPING the things that shouldn't be in restaurant DELIVER." + colors.NATIVE_COLOR)
                return succeeded

            smach.StateMachine.add('STOPPING_RESTAURANT_DELIVER_FASE_SET_UP',
                                   CBState(print_things),
                                   remapping={'in_learn_person': "in_learn_person"},
                                   transitions={succeeded: 'START_ALL_CONTROLLERS'})

            smach.StateMachine.add("START_ALL_CONTROLLERS",
                                   StartRobotControllers(head=True, left=True, right=True),
                                   transitions={succeeded: "STOP_PEOPLE_TRACKING",
                                                aborted: "STOP_PEOPLE_TRACKING",
                                                preempted: preempted})

            try:
                smach.StateMachine.add("STOP_PEOPLE_TRACKING",
                                       RunScriptOnRobot(script_name="iri_people_tracking_raiStop.sh"),
                                       transitions={succeeded: "STOP_PERSON_SERVER",
                                                    aborted: "STOP_PERSON_SERVER"})
            except:
                rospy.loginfo("PEOPLE TRACKING NOT LAUNCHED; NOTHING TO STOP")

            try:
                smach.StateMachine.add("STOP_PERSON_SERVER",
                                       RunScriptOnRobot(script_name="personServerStop.sh"),
                                       transitions={succeeded: "FINISHED_DELIVER_FASE_SERVICES_RESTAURANT_SET_UP",
                                                    aborted: "FINISHED_DELIVER_FASE_SERVICES_RESTAURANT_SET_UP"})
            except:
                rospy.loginfo("PERSON SERVER NOT LAUNCHED; NOTHING TO STOP")

            init_text = "I'm ready to start."
            smach.StateMachine.add('FINISHED_DELIVER_FASE_SERVICES_RESTAURANT_SET_UP',
                                   SpeakActionState(init_text),
                                   transitions={succeeded: succeeded})
