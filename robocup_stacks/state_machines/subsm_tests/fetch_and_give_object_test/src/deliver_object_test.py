#! /usr/bin/env python
# -.- coding: utf-8 -.-
#FETCH_AND_GIVE_OBJECT_TEST.PY
# vim: expandtab ts=4 sw=4

import roslib
roslib.load_manifest('fetch_and_give_object_test')
import smach
import rospy

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.grasping.deliver_object import DeliverObject

LOCATION_NAME = 'table_7'
DIDNT_FIND_OBJECT = "I couldnt find the "


class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys=['dummy_var'])

    def execute(self, userdata):
        print "Dummy STATE"
        rospy.sleep(1)
        userdata.dummy_var = LOCATION_NAME
        print "THIS IS THE LOCATION WHERE TO LEAVE THE OBJECT I HAVE IN MY HAND===> " + LOCATION_NAME

        return succeeded


def main():
    rospy.init_node('deliver_object_test_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add('DUMMYSTATEMACHINE',
                               DummyStateMachine(),
                               transitions={succeeded: 'DELIVER_OBJECT'},
                               remapping={'dummy_var': 'delivery_location'})

        smach.StateMachine.add('DELIVER_OBJECT',
                               DeliverObject(),
                               transitions={'object_delivered_succesfully': succeeded,
                                            preempted: preempted,
                                            'didnt_deliver_object': succeeded},
                               remapping={'in_delivery_location_name': 'delivery_location'})


    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
