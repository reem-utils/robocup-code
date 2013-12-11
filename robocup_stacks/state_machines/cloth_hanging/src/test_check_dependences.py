#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cloth_hanging')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.utils.check_dependences import CheckDependencesState


TOPICS = ['/head_mount_xtion/depth_registered/points','/scan_filtered']
SERVICES = ['/personServer/faceTracking/stop', '/sb04/sonars/SetStatus','/motion_manager']
ACTIONS = ['/move_by/move_base','/move_right_arm_torso']
MAP_LOCATIONS = []

def main():
    rospy.init_node('test_check_dependences')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:
        smach.StateMachine.add("TEST_CHECK_DEPENDENCES",
            CheckDependencesState(
                    topic_names=TOPICS,
                    service_names=SERVICES,
                    action_names=ACTIONS,
                    map_locations=MAP_LOCATIONS),
            transitions={succeeded: succeeded, aborted: aborted}
            )

    sis = smach_ros.IntrospectionServer(
        'test_check_dependences_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
