#! /usr/bin/env python

import roslib
roslib.load_manifest('enter_door_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.navigation.enter_room import EnterRoomStateMachine
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted


def main():
    rospy.init_node('enter_room_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add('SM_ENTER_ROOM',
                               EnterRoomStateMachine(distance=1.5, openDoor=False),
                               transitions={succeeded: succeeded, aborted: aborted})

    sis = smach_ros.IntrospectionServer('enter_room_test_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
