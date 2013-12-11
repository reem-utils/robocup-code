#! /usr/bin/env python

import roslib; roslib.load_manifest('release_test')
import rospy
import smach
import smach_ros
import actionlib

from std_msgs import *

from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.grasping.sm_release import *
from pal_smach_utils.grasping.arm_and_hand_goals import *
from geometry_msgs.msg import Pose


class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, input_keys=['releasing_position'], output_keys=['releasing_position'], outcomes=[succeeded])

    def execute(self, userdata):
        print "Dummy state to go to SM_release (generating releasing_position key)!"
        rospy.sleep(0.5)  # in seconds
        newpose = Pose()
        newpose.position.x = 0.3
        newpose.position.y = -0.4
        newpose.position.z = 1.3
        newpose.orientation.w = 1.0
        userdata.releasing_position = newpose #None #get_pose_for_arm_in_front()
        return succeeded


def main():
    rospy.init_node('sm_release_test_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add(
                    'dummy_state_generate_position',
                    DummyStateMachine(),
                    transitions={succeeded: 'SM_release'})

          ## Add some release object position key called: releasing_position
        smach.StateMachine.add(
                    'SM_release',
                    ReleaseObjectStateMachine(),
                    transitions={succeeded: succeeded, aborted: aborted})

         # NOT USING ANYTHING  MORE

    sis = smach_ros.IntrospectionServer(
        'sm_release_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
