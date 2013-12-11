#!/usr/bin/env python

import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.grasping.st_reem_hand import CloseReemHand


if __name__ == "__main__":
    rospy.init_node("close_reem_hand", anonymous=True)

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add('INTRO', CloseReemHand())

    sm.execute()

    rospy.spin()
