#! /usr/bin/env python

import roslib; roslib.load_manifest('learn_person_test')
import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.learn_person import LearnPerson


class PrintUserData6(smach.State):

    def __init__(self,
                message_name1='Message1',
                message_name2='Message2'):
            smach.State.__init__(self,
                    outcomes=[succeeded, preempted, aborted],
                    input_keys=['message1',
                                'message2'])

            self._message_name1 = message_name1
            self._message_name2 = message_name2

    def execute(self, userdata):
            rospy.loginfo('This is the %s: %s' % (self._message_name1, str(userdata.message1)))
            rospy.loginfo('This is the %s: %s' % (self._message_name2, str(userdata.message2)))

            return succeeded

def main():
    rospy.init_node('sm_learn_person_test_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add('SM_learn_person',
                               LearnPerson(),
                               transitions={succeeded: 'PRINT_DATA_2', aborted: aborted},
                               remapping={'PT_Id_of_person': 'PT_Id_of_person', 'LP_all_person_data': 'LP_all_person_data'})

        smach.StateMachine.add('PRINT_DATA_2',
                               PrintUserData6('PT_Id_of_person', 'LP_all_person_data'),
                               transitions={
                                        succeeded: 'SM_learn_person',
                                        preempted: preempted,
                                        aborted: aborted},
                               remapping={'message1': 'PT_Id_of_person',
                                            'message2': 'LP_all_person_data'})

    sm.execute()

    rospy.spin()

if __name__ == '__main__':
    main()
