#! /usr/bin/env python
# -.- coding: utf-8 -.-
"""
RESTAURANT.PY
Esto es del dia antes de restaurant YEAAAAHHH.
This is the restaurant SM.
"""

import roslib
roslib.load_manifest('restaurant')
import rospy
import smach
import smach_ros
from smach_ros import ServiceState
from std_srvs.srv import Empty
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.navigation_state import ChangeNavigationMode
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.speech.listen_general_command import RecogCommand
#from pal_smach_utils.navigation.learn_person import LearnPerson
from pal_smach_utils.navigation.follow_and_stop import FollowAndStop
from pal_smach_utils.navigation.listen_and_satisfy_delivery_order import ListenAndSatisfyDeliveryOrderSM
from pal_smach_utils.navigation.memorise_ordering_location import MemoriseOrderingLocation
from pal_smach_utils.utils.fases_set_up_restaurant import InitialRestaurantFaseSetUp

from pal_smach_utils.utils.debug import debugPrint
import dynamic_reconfigure.client
from smach import CBState

import os
inside_robot = False
robot = os.environ.get('PAL_ROBOT')
if robot == 'rh2c' or robot == 'rh2m' or robot == 'reemh3c' or robot == 'reemh3m' or robot == 'reemh3':
    inside_robot = True

FOLLOW_GRAMMAR_NAME = rospy.get_param('/restaurant/follow_grammar_name')
STOP_GRAMMAR_NAME = rospy.get_param('/restaurant/stop_grammar_name')

MAPPING_MODE = 'MAP'
LOCALIZATION_MODE = 'LOC'
DISABLED = 'STOP'

DISTANCE_TO_FOLLOW = 1.0
LEARN_PERSON_FLAG = True


def main():
    rospy.init_node('restaurant_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        if (inside_robot):

            @smach.cb_interface(outcomes=[succeeded])
            def setPlannerParameters(userdata):
                debugPrint('    Setting planner parameters values for following the operator...', 4)
                node_to_reconfigure = "/move_by/move_base/PalLocalPlanner"
                client = dynamic_reconfigure.client.Client(node_to_reconfigure)
                params = {
                    'acc_lim_x': 0.65,
                    'acc_lim_th': 1.5,
                    'max_vel_x': 0.5,
                    'max_vel_th': 0.5}
                new_config = client.update_configuration(params)

                debugPrint("New configuration returned by the dynamic reconfigure server:\n" + str(new_config), 4)

                return succeeded

            smach.StateMachine.add('SET_PLANNER_PARAMETERS',
                                   CBState(setPlannerParameters),
                                   transitions={succeeded: "INTRO"})
        else:
            not_robot_text = "Cannot set the planner parameters because we are not inside the robot."
            smach.StateMachine.add('SET_PLANNER_PARAMETERS',
                                   SpeakActionState(not_robot_text),
                                   transitions={succeeded: "INTRO"})

        intro_text = "Hello, my name is REEM! What do you want me to do today?"
        smach.StateMachine.add('INTRO',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'INITIAL_SET_UP'})

        smach.StateMachine.add('INITIAL_SET_UP',
                               InitialRestaurantFaseSetUp(),
                               transitions={succeeded: 'FOLLOW_ME_COMMAND',
                                            preempted: preempted,
                                            aborted: aborted})

        ### 2. Follow me command
        smach.StateMachine.add('FOLLOW_ME_COMMAND',
                               RecogCommand(FOLLOW_GRAMMAR_NAME, 'action', 'follow', ask_for_confirmation=True),
                               transitions={succeeded: 'START_MAPPER',
                                            aborted: 'FOLLOW_ME_COMMAND'})

        smach.StateMachine.add('START_MAPPER',
                               ChangeNavigationMode(MAPPING_MODE),
                               transitions={succeeded: 'FOLLOW_ME'})

        ### 3. Start mapper
        """
        smach.StateMachine.add('START_MAPPER',
                               ChangeNavigationMode(MAPPING_MODE),
                               transitions={succeeded: 'TTS_SAY_CALIB'})

        ### 4. Follow person while mapping
##########################################################################################

        intro_text = "Please stay still while I learn how you are."
        smach.StateMachine.add('TTS_SAY_CALIB',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'SM_LEARN_PERSON'})
        #TODO, update it to the latest followme protocols.
        smach.StateMachine.add('SM_LEARN_PERSON',
                               LearnPerson(),
                               transitions={succeeded: 'TTS_SAY_CALIB_FINISHED',
                                            aborted: 'TTS_SAY_CALIB_DIDNT_QUITE_GET_IT'},
                               remapping={'PT_Id_of_person': 'out_targetId',
                                          'LP_all_person_data': 'out_personTrackingData'})

        wait_text = "Would you be so kind to wait for a bit longer."
        smach.StateMachine.add('TTS_SAY_CALIB_DIDNT_QUITE_GET_IT',
                               SpeakActionState(wait_text),
                               transitions={succeeded: 'SM_LEARN_PERSON'})

        thankyou_text = "Thank you for you patience. Let's go!"
        smach.StateMachine.add('TTS_SAY_CALIB_FINISHED',
                               SpeakActionState(thankyou_text),
                               transitions={succeeded: 'FOLLOW_ME'})

        smach.StateMachine.add('FOLLOW_ME',
                               FollowAndStop(DISTANCE_TO_FOLLOW),
                               remapping={'in_targetId': 'out_targetId',
                                          'in_personTrackingData': 'out_personTrackingData'},
                               transitions={succeeded: 'START_LOCALIZATION'})
        """
        sm.userdata.learn_person_or_not = LEARN_PERSON_FLAG
        smach.StateMachine.add('FOLLOW_ME',
                               FollowAndStop(DISTANCE_TO_FOLLOW),
                               remapping={'in_learn_person': 'learn_person_or_not'},
                               transitions={succeeded: 'START_LOCALIZATION'})

#######################################################################################################
        ### 5. start localization
        smach.StateMachine.add('START_LOCALIZATION',
                               ChangeNavigationMode(LOCALIZATION_MODE),
                               transitions={succeeded: 'MEMORISE_CURRENT_POS_AS_ORDERING_LOCATION'})

        smach.StateMachine.add('MEMORISE_CURRENT_POS_AS_ORDERING_LOCATION',
                               MemoriseOrderingLocation(),
                               transitions={succeeded: 'LISTEN_AND_SATISFY_DELIVERY_ORDER'})

        smach.StateMachine.add('LISTEN_AND_SATISFY_DELIVERY_ORDER',
                               ListenAndSatisfyDeliveryOrderSM(),
                               transitions={succeeded: 'BYE',
                                            preempted: preempted,
                                            aborted: aborted})

        ### 12. Close with some message...

        smach.StateMachine.add('BYE',
                               SpeakActionState("It was a pleasure to serve you."))

    sis = smach_ros.IntrospectionServer(
        'restaurant_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
