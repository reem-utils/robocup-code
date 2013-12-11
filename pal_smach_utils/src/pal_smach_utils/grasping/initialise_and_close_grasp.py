#! /usr/bin/env python
# -.- coding: utf-8 -.-
# vim: expandtab ts=4 sw=4
# Author RDaneelOlivaw

import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers
from pal_smach_utils.utils.run_script_on_robot import RunScriptOnRobot
from pal_smach_utils.utils.run_script_local import RunScriptLocal


class InitGraspPipelineSM(smach.StateMachine):
    """
    Initialises all the protocols that CompleteGraspPipelineStateMachine need to work.
    We close befor starting just in case someone didnt finish closing correctly.
    """

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted])

        with self:

            try:
                smach.StateMachine.add("STOP_GRASP",
                                       RunScriptOnRobot(script_name="graspingStop.sh"),
                                       #RunScriptLocal(script_name="graspingStop.sh"),
                                       transitions={succeeded: "START_ALL_CONTROLLERS",
                                                    aborted: "START_ALL_CONTROLLERS"})
            except:
                rospy.loginfo("GRASP NOT LAUNCHED; NOTHING TO STOP")

            smach.StateMachine.add("START_ALL_CONTROLLERS",
                                   StartRobotControllers(head=True, left=True, right=True),
                                   transitions={succeeded: "START_GRASP",
                                                aborted: "START_ALL_CONTROLLERS",
                                                preempted: "START_ALL_CONTROLLERS"})
            """
            smach.StateMachine.add("START_KINECT_GRASP",
                                   #RunScriptOnRobot(script_name="graspingStart.sh"),
                                   RunScriptLocal(script_name="kinectToGraspStart.sh"),
                                   transitions={succeeded: succeeded,
                                                aborted: "START_GRASP"})
            """
            smach.StateMachine.add("START_GRASP",
                                   RunScriptOnRobot(script_name="graspingStart.sh"),
                                   #RunScriptLocal(script_name="graspingStart.sh"),
                                   transitions={succeeded: succeeded,
                                                aborted: "START_GRASP"})


class CloseGraspPipelineSM(smach.StateMachine):
    """
    Initialises all the protocols that CompleteGraspPipelineStateMachine need to work.
    """

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted])

        with self:
            """
            smach.StateMachine.add("STOP_KINECT_GRASP",
                                   #RunScriptOnRobot(script_name="graspingStart.sh"),
                                   RunScriptLocal(script_name="kinectToGraspStop.sh"),
                                   transitions={succeeded: "STOP_ALL_CONTROLLERS",
                                                aborted: "STOP_KINECT_GRASP"})
            """
            smach.StateMachine.add("STOP_GRASP",
                                   RunScriptOnRobot(script_name="graspingStop.sh"),
                                   #RunScriptLocal(script_name="graspingStop.sh"),
                                   transitions={succeeded: "STOP_ALL_CONTROLLERS",
                                                aborted: "STOP_GRASP"})

            smach.StateMachine.add("STOP_ALL_CONTROLLERS",
                                   StopRobotControllers(head=True, left=True, right=True),
                                   transitions={succeeded: succeeded,
                                                aborted: "STOP_ALL_CONTROLLERS",
                                                preempted: "STOP_ALL_CONTROLLERS"})
