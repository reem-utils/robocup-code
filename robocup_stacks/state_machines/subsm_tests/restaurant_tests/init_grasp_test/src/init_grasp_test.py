#! /usr/bin/env python
# -.- coding: utf-8 -.-


import roslib
roslib.load_manifest('init_grasp_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.time_out import TimeOut
from pal_smach_utils.grasping.initialise_and_close_grasp import InitGraspPipelineSM, CloseGraspPipelineSM

MOVING_MOCK_TIME = 10.0


def main():
    rospy.init_node('sm_init_grasp_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        intro_text = "m"
        smach.StateMachine.add('INTRO',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'START_GRASP_PROTOCOL'})

        smach.StateMachine.add("START_GRASP_PROTOCOL",
                               InitGraspPipelineSM(),
                               transitions={succeeded: succeeded,
                                            aborted: aborted,
                                            preempted: aborted})

        smach.StateMachine.add('MOCK_TIME',
                               TimeOut(MOVING_MOCK_TIME),
                               transitions={succeeded: 'STOP_GRASP_PROTOCOL',
                                            preempted: preempted,
                                            aborted: aborted})

        smach.StateMachine.add("STOP_GRASP_PROTOCOL",
                               CloseGraspPipelineSM(),
                               transitions={succeeded: 'BYE',
                                            aborted: aborted,
                                            preempted: preempted})

        smach.StateMachine.add('BYE',
                               SpeakActionState("m"))

    sis = smach_ros.IntrospectionServer(
        'restaurant_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
