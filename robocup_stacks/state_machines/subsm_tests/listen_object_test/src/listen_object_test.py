#! /usr/bin/env python

import roslib; roslib.load_manifest('listen_object_test')
import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.listen_object_name import ListenObjectName


def main():
    rospy.init_node('sm_listen_object_test_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add('LISTEN_OBJECT',
                               ListenObjectName(),
                               transitions={succeeded: succeeded,
                                            preempted: preempted,
                                            aborted: aborted})

    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
