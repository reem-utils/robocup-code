#! /usr/bin/env python

import roslib
roslib.load_manifest('dancing_reem_sm_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from nod_head_with_bpm_sm import NodHeadWithBeatSM


def main():
    rospy.init_node('nod_head_sm_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add('NOD_HEAD_SM',
                               NodHeadWithBeatSM(),
                               transitions={succeeded: succeeded,
                                            preempted: preempted,
                                            aborted: aborted})

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
