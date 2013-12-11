#! /usr/bin/env python
# -.- coding: utf-8 -.-
import roslib
roslib.load_manifest("emergency_situation")
import smach
import rospy
import smach_ros

from save_people import SavePeopleStateMachine
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted


def main():
    rospy.init_node('test_save_people')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:

        # sm.userdata.location_list = rospy.get_param("/mmap/poi/submap_0")

        smach.StateMachine.add("TEST_SAVE_PEOPLE",
            SavePeopleStateMachine()
            )
        #input_keys=["location_list"]

    sis = smach_ros.IntrospectionServer(
        'test_save_people_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
