#! /usr/bin/env python
# vim: expandtab ts=4 sw=4
### FOLOW_OPERATOR.PY ###

import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from pal_smach_utils.navigation.listen_command_for_restaurant import ListenCommandForRestaurant
from pal_smach_utils.navigation.listen_command_for_follow_me import ListenCommandForFollowMe
from pal_smach_utils.navigation.listen_command_for_follow_me_again import ListenCommandForFollowMeAgain
from pal_smach_utils.navigation.listen_command_for_gpsr_follow import ListenCommandForGpsrFollow


class ListenCommands(smach.StateMachine):
    def __init__(self, state_machine_name="restaurant"):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])
        with self:

            if (state_machine_name == "restaurant"):
                smach.StateMachine.add('LISTEN_COMMANDS_FOR_RESTAURANT',
                                       ListenCommandForRestaurant(),
                                       transitions={succeeded: succeeded})
            elif (state_machine_name == "follow_me"):
                smach.StateMachine.add('LISTEN_COMMANDS_FOR_FOLLOW_ME',
                                       ListenCommandForFollowMe(),
                                       transitions={succeeded: succeeded})
            elif (state_machine_name == "follow_me_again"):
                smach.StateMachine.add('LISTEN_COMMANDS_FOR_FOLLOW_ME_AGAIN',
                                       ListenCommandForFollowMeAgain(),
                                       transitions={succeeded: succeeded})
            elif (state_machine_name == "gpsr_follow"):
                smach.StateMachine.add('LISTEN_COMMANDS_FOR_GPSR_FOLLOW',
                                       ListenCommandForGpsrFollow(),
                                       transitions={succeeded: succeeded})
            else:
                rospy.logerr("NO STATE MACHINE NAME WAS PROVIDED TO START LISTENING COMMANDS")
                return aborted
