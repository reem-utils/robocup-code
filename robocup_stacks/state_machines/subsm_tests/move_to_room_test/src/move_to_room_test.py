#! /usr/bin/env python
import roslib
roslib.load_manifest('move_to_room_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

IGNORE_ORIENTATION = False

if __name__ == '__main__':
    rospy.init_node('move_to_room_test')
    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])
    sm.userdata.room_name = 'kitchen'
    with sm:
        smach.StateMachine.add('MOVE_TO_ROOM', MoveToRoomStateMachine(ignore_orientation=IGNORE_ORIENTATION))

    sis = smach_ros.IntrospectionServer('move_to_room_test', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()
