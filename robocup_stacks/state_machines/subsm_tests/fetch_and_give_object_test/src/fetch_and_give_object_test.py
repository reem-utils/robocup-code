#! /usr/bin/env python
# -.- coding: utf-8 -.-
#FETCH_AND_GIVE_OBJECT_TEST.PY
# vim: expandtab ts=4 sw=4

import roslib
roslib.load_manifest('fetch_and_give_object_test')
import smach
import rospy

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.grasping.fetch_object import FetchObject

OBJECT_NAME = 'pringels'
DIDNT_FIND_OBJECT = "I couldnt find the "


class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys=['dummy_var'])

    def execute(self, userdata):
        print "Dummy STATE"
        rospy.sleep(1)
        userdata.dummy_var = OBJECT_NAME
        print "THIS IS THE OBJECT TO FETCH===> " + OBJECT_NAME

        return succeeded


def main():
    rospy.init_node('sm_fetch_and_give_object_test_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add('DUMMYSTATEMACHINE',
                               DummyStateMachine(),
                               transitions={succeeded: 'FETCH_OBJECT'},
                               remapping={'dummy_var': 'object_name'})

        smach.StateMachine.add('FETCH_OBJECT',
                               FetchObject(),
                               transitions={'object_fetched_succesfully': succeeded,
                                            'didnt_fetch_object': succeeded,
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'in_fetch_object_name': 'object_name'})


    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
