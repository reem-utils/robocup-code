#! /usr/bin/env python

import roslib
roslib.load_manifest('learn_and_follow_operator_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from pal_smach_utils.utils.check_dependences import CheckDependencesState


def main():
    rospy.init_node('check_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add("CHECK_DEPENDENCES",
                               CheckDependencesState(
                                   topic_names=None,
                                   service_names=None,
                                   action_names=None,
                                   map_locations=None),
                               transitions={succeeded: succeeded,
                                            aborted: aborted})

    sis = smach_ros.IntrospectionServer('check_sm', sm, '/check_TEST')
    sis.start()
    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
