#! /usr/bin/env python

import roslib
roslib.load_manifest('ordering_location_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.navigation.memorise_ordering_location import MemoriseOrderingLocation
from pal_smach_utils.navigation.return_to_ordering_location import ReturnToOrderingLocation
from move_base_msgs.msg import MoveBaseGoal
from pal_smach_utils.navigation.move_action import MoveActionState
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler

DISTANCE_MOVE_BACK = -2.0


def main():
    rospy.init_node('sm_ordering_location_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        intro_text = "I am ready to memorise the ordering location."
        smach.StateMachine.add('START',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'MEMORISE_CURRENT_POS_AS_ORDERING_LOCATION'})

        smach.StateMachine.add('MEMORISE_CURRENT_POS_AS_ORDERING_LOCATION',
                               MemoriseOrderingLocation(),
                               transitions={succeeded: 'MOVE_BACK_A_DISTANCE'})

        intro_text = "Now I will move back a bit, so be careful."
        smach.StateMachine.add('SAY_MOVING',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'MEMORISE_CURRENT_POS_AS_ORDERING_LOCATION'})

        def move_cb(userdata, nav_goal):
            nav_goal = MoveBaseGoal()
            nav_goal.target_pose.header.stamp = rospy.Time.now()
            nav_goal.target_pose.header.frame_id = "/base_link"
            nav_goal.target_pose.pose.position.x = DISTANCE_MOVE_BACK
            nav_goal.target_pose.pose.position.y = 0.0
            nav_goal.target_pose.pose.position.z = 0.0
            nav_goal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
            return nav_goal

        smach.StateMachine.add('MOVE_BACK_A_DISTANCE',
                               MoveActionState("/base_link", "/move_base", goal_cb=move_cb),
                               transitions={succeeded: 'RETURN_TO_ORDERING_LOCATION',
                                            preempted: preempted,
                                            aborted: aborted})

        smach.StateMachine.add('RETURN_TO_ORDERING_LOCATION',
                               ReturnToOrderingLocation(),
                               transitions={succeeded: 'END',
                                            preempted: preempted,
                                            aborted: aborted})

        intro_text = "Memorised Ordering Location test finished, have a nice day."
        smach.StateMachine.add('END',
                               SpeakActionState(intro_text),
                               transitions={succeeded: succeeded})


    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
