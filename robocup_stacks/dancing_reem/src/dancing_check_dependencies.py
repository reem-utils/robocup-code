#! /usr/bin/env python
# -.- coding: utf-8 -.-
'''
DANCING_REEM_CHECK.PY
'''

import roslib
roslib.load_manifest('dancing_reem')
import smach
import smach_ros
import rospy

from pal_smach_utils.utils.check_dependences import CheckDependencesState
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted


TOPICS = []
SERVICES = []
ACTIONS = []
MAP_LOC = None


class DancingCheckDependencies(smach.StateMachine):

    '''
    Checks for all the the topics, actions and so on that restaurant depends on.
    '''

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted])

        with self:

            smach.StateMachine.add("CHECK_DEPENDENCES",
                                   CheckDependencesState(topic_names=TOPICS,
                                                         service_names=SERVICES,
                                                         action_names=ACTIONS,
                                                         map_locations=MAP_LOC),
                                   transitions={succeeded: succeeded, aborted: aborted})


def main():
    rospy.init_node('dancing_check_dependencies')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add("CHECK_DEPENDENCES_SM",
                               DancingCheckDependencies(),
                               transitions={succeeded: succeeded, aborted: aborted})

    sis = smach_ros.IntrospectionServer(
        'dancing_reem_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
