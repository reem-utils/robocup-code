#! /usr/bin/env python


import roslib
roslib.load_manifest('set_up_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.fases_set_up_restaurant import InitialRestaurantFaseSetUp

from pal_smach_utils.utils.debug import debugPrint
import dynamic_reconfigure.client
from smach import CBState

import os
inside_robot = False
robot = os.environ.get('PAL_ROBOT')
if robot == 'rh2c' or robot == 'rh2m' or robot == 'reemh3c' or robot == 'reemh3m' or robot == 'reemh3':
    inside_robot = True


def main():
    rospy.init_node('sm_init_set_up_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        intro_text = "Let's set up the robot."
        smach.StateMachine.add('START',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'SET_PLANNER_PARAMETERS'})

        if (inside_robot):

            @smach.cb_interface(outcomes=[succeeded])
            def setPlannerParameters(userdata):
                debugPrint('    Setting planner parameters values for following the operator...', 4)
                node_to_reconfigure = "/move_by/move_base/PalLocalPlanner"
                client = dynamic_reconfigure.client.Client(node_to_reconfigure)
                params = {
                    'acc_lim_x': 0.65,
                    'acc_lim_th': 2.4,
                    'max_vel_x': 0.59,
                    'max_vel_th': 0.5}
                new_config = client.update_configuration(params)

                debugPrint("New configuration returned by the dynamic reconfigure server:\n" + str(new_config), 4)

                return succeeded

            smach.StateMachine.add('SET_PLANNER_PARAMETERS',
                                   CBState(setPlannerParameters),
                                   transitions={succeeded: "INITIAL_SET_UP"})
        else:
            not_robot_text = "Cannot set the planner parameters because we are not inside the robot."
            smach.StateMachine.add('SET_PLANNER_PARAMETERS',
                                   SpeakActionState(not_robot_text),
                                   transitions={succeeded: "INITIAL_SET_UP"})

        smach.StateMachine.add('INITIAL_SET_UP',
                               InitialRestaurantFaseSetUp(),
                               transitions={succeeded: 'END',
                                            preempted: preempted,
                                            aborted: aborted})

        intro_text = "INIT RESTAURANT Set Up finished, have a nice day."
        smach.StateMachine.add('END',
                               SpeakActionState(intro_text),
                               transitions={succeeded: succeeded})


    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
