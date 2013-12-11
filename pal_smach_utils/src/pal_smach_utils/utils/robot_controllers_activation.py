##! /usr/bin/env python
# -.- coding: utf-8 -.-
# vim: expandtab ts=4 sw=4

import smach
import os
from smach_ros import ServiceState
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_srvs.srv import ControllerStartupRequest, ControllerStartup

robot = os.environ.get('PAL_ROBOT')
in_robot = False
if robot == 'rh2c' or robot == 'rh2m' or robot == 'reemh3c' or robot == 'reemh3m' or robot == 'reemh3':
    in_robot = True


class StartRobotControllers(smach.StateMachine):
    """
    A class that starts the robot arm controllers.
    Required when grasping movements are going to be performed
    Never activate this when the robot is performing XML based movements
    """
    def __init__(self, head=True, left=True, right=True):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:
            if in_robot and (head or left or right):

                if right:
                    smach.StateMachine.add('STEP_1',
                                           ServiceState('/Peer_controller_configurator/orocos_controller_start',
                                                        ControllerStartup,
                                                        request=ControllerStartupRequest('rightArmTorsoController')),
                                           transitions={succeeded: 'STEP_3'} if left else {succeeded: 'STEP_5'} if head else {succeeded: succeeded})

                if left:
                    smach.StateMachine.add('STEP_3',
                                           ServiceState('/Peer_controller_configurator/orocos_controller_start',
                                                        ControllerStartup,
                                                        request=ControllerStartupRequest('leftArmController')),
                                           transitions={succeeded: 'STEP_5'} if head else {succeeded: succeeded})

                if head:
                    smach.StateMachine.add('STEP_5',
                                           ServiceState('/Peer_controller_configurator/orocos_controller_start',
                                                        ControllerStartup,
                                                        request=ControllerStartupRequest('headController')),
                                           transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})
            else:  # There's an error if a SM without states is created
                def dummy_state(userdata):
                    return succeeded
                smach.StateMachine.add('NO_CONTROLLERS_TO_START', smach.CBState(dummy_state, outcomes=[succeeded]),
                                       transitions={succeeded: succeeded})


class StopRobotControllers(smach.StateMachine):
    """
    A state that stops the robot arm controllers
    Required when the controllers are activated and an XML based movement is going to be performed
    """
    def __init__(self, head=True, left=True, right=True):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:
            if in_robot and (head or left or right):
                if right:
                    smach.StateMachine.add('STEP_1',
                                           ServiceState('/Peer_controller_configurator/orocos_controller_stop',
                                                        ControllerStartup,
                                                        request=ControllerStartupRequest('rightArmTorsoController')),
                                           transitions={succeeded: 'STEP_3'} if left else {succeeded: 'STEP_5'} if head else {succeeded: succeeded})

                if left:
                    smach.StateMachine.add('STEP_3',
                                           ServiceState('/Peer_controller_configurator/orocos_controller_stop',
                                                        ControllerStartup,
                                                        request=ControllerStartupRequest('leftArmController')),
                                           transitions={succeeded: 'STEP_5'} if head else {succeeded: succeeded})

                if head:
                    smach.StateMachine.add('STEP_5',
                                           ServiceState('/Peer_controller_configurator/orocos_controller_stop',
                                                        ControllerStartup,
                                                        request=ControllerStartupRequest('headController')),
                                           transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})

            else:  # There's an error if a SM without states is created
                def dummy_state(userdata):
                    return succeeded
                smach.StateMachine.add('NO_CONTROLLERS_TO_STOP', smach.CBState(dummy_state, outcomes=[succeeded]),
                                       transitions={succeeded: succeeded})
