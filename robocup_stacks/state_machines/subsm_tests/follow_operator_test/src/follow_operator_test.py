#! /usr/bin/env python

import roslib; roslib.load_manifest('follow_operator_test')
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.follow_operator import FollowOperator
from iri_perception_msgs.msg import peopleTracking


class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             input_keys=['releasing_position'],
                             output_keys=['from_Dummy_person_Id', 'from_Dummy_all_Person_Data'],
                             outcomes=[succeeded])

    def execute(self, userdata):
        print "Dummy state to go to produce dummy data!"
        # in seconds
        rospy.sleep(0.5)
        userdata.from_Dummy_person_Id = 1
        userdata.from_Dummy_all_Person_Data = peopleTracking()
        return succeeded


def main():
    rospy.init_node('sm_follow_operator_test_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add('dummy_state_generate_data',
                               DummyStateMachine(),
                               transitions={succeeded: 'SM_follow'})

        ## Add some release object position key called: releasing_position
        smach.StateMachine.add('SM_follow',
                               FollowOperator(),
                               remapping={'in_targetId': 'from_Dummy_person_Id',
                                          'in_personTrackingData': 'from_Dummy_all_Person_Data'},
                               transitions={succeeded: succeeded,
                                            aborted: aborted})

    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
