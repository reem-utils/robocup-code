#! /usr/bin/env python
# -.- coding: utf-8 -.-
'''
RESTAURANT_CHECK_DEPENDENCIES.PY
'''

import roslib
roslib.load_manifest('restaurant')
import smach
import smach_ros
import rospy

from pal_smach_utils.utils.check_dependences import CheckDependencesState
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted


TOPICS = ['/usersaid', '/pal_navigation_sm/state', '/iri_people_tracking_rai/peopleSet', "/move_by/move_base_simple/goal"]
SERVICES = ['/asrservice', '/pal_navigation_sm', '/lookupTransform', '/object_translator', '/loc_translator', '/approachToGoal', '/personServer/faceTracking/start', '/personServer/faceTracking/stop']
ACTIONS = ['/sound', '/face_recognition', '/move_base', '/head_traj_controller/head_scan_snapshot_action', '/move_right_arm_torso',
           '/right_hand_controller/follow_joint_trajectory']
MAP_LOC = None
#TODO, we should check theat the objects and locations are in the object list and the locations list.


class RestaurantCheckDependencies(smach.StateMachine):

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
    rospy.init_node('restaurant_check_dependencies')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add("CHECK_DEPENDENCES_SM",
                               RestaurantCheckDependencies(),
                               transitions={succeeded: succeeded, aborted: aborted})

    sis = smach_ros.IntrospectionServer(
        'restaurant_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
