#!/usr/bin/env python
import roslib
roslib.load_manifest('iri_motion_detector_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.navigation.move_to_caller import MoveToCallerStateMachine
from pal_smach_utils.utils.global_common import aborted, succeeded, preempted


def main():

    rospy.init_node("iri_motion_detector_test")

    sm = smach.StateMachine(outcomes=[preempted, succeeded, aborted])

    with sm:
        smach.StateMachine.add("GO_TO_DETECTED_MOVIMENT", MoveToCallerStateMachine(),
            transitions={succeeded: succeeded, preempted: preempted, aborted: aborted},
            )

    sis = smach_ros.IntrospectionServer("main_test_iri_motion_detector_state", sm, "/SM_ROOT")
    sis.start()

    #Execute SMACH
    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == "__main__":
    main()
