#! /usr/bin/env python

import roslib; roslib.load_manifest('transform_pose_test')
import rospy

from pal_smach_utils.utils.global_common import *

import smach
import smach_ros

class AskForTransform(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys = ['object_to_search_for'])

    def execute(self, userdata):
        print "Dummy state to go to SM_grasp (waiting 10s to initiate, as my pc is too slow to handle all the launch file in time)!"
            print "[                                             =D                                               ]"
        rospy.sleep(5) # in seconds
        userdata.object_to_search_for = ""
        return succeeded 



def main():
    rospy.init_node('transform_pose_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add(
            'AskForTransform',
            AskForTransform(),
            transitions={succeeded: succeeded, aborted: aborted})

         # NOT USING ANYTHING  MORE

    sis = smach_ros.IntrospectionServer(
        'sm_enter_door_test_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
