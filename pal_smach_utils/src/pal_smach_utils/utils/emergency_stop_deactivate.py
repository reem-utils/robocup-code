##! /usr/bin/env python
# -.- coding: utf-8 -.-
# vim: expandtab ts=4 sw=4

import smach
import os
from smach_ros import ServiceState
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_navigation_msgs.srv import DisableEmergency, DisableEmergencyRequest

class DeactEmergencyStop(smach.StateMachine):
    """
    A class that deactivates the emergency stop service for a given number of seconds
    Param @time indicates the amount of time that the service is deactivated
    Deactivation is shown in the robot with LEDs in red
    """
    def __init__(self, time=20):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:
          disableEmerg = DisableEmergencyRequest()
          disableEmerg.second = time
          disableEmerg.useLEDs = True
          smach.StateMachine.add('DISABLE_EMERGENCY_STOP',
                                 ServiceState('/disable_emergency_stop',
                                              DisableEmergency,
                                              request=disableEmerg),
                                 transitions={succeeded: succeeded})
