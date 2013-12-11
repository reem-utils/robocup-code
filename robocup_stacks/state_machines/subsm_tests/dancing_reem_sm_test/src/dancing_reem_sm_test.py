#! /usr/bin/env python

import roslib
roslib.load_manifest('dancing_reem_sm_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from dancing_reem_sm import GetMovementForDancingReemSM


def main():
    rospy.init_node('dancing_reem_mock_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add('DANCING_REEM_SM',
                               GetMovementForDancingReemSM(),
                               transitions={succeeded: succeeded,
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'in_dict_available_movements': 'in_dict_available_movements'})

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
