#! /usr/bin/env python

import roslib
roslib.load_manifest('init_dancing_reem_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from init_dancing_reem import InitDancingReem


class PrintUserData6(smach.State):

    def __init__(self,
                 message_name1='Message1',
                 message_name2='Message2',
                 message_name3='Message3',
                 message_name4='Message4',
                 message_name5='Message5',
                 message_name6='Message6'):
            smach.State.__init__(self,
                                 outcomes=[succeeded, preempted, aborted],
                                 input_keys=['message1',
                                             'message2',
                                             'message3',
                                             'message4',
                                             'message5',
                                             'message6'])

            self._message_name1 = message_name1
            self._message_name2 = message_name2
            self._message_name3 = message_name3
            self._message_name4 = message_name4
            self._message_name5 = message_name5
            self._message_name6 = message_name6

    def execute(self, userdata):
            rospy.loginfo('This is the %s: %s' % (self._message_name1, str(userdata.message1)))
            rospy.loginfo('This is the %s: %s' % (self._message_name2, str(userdata.message2)))
            rospy.loginfo('This is the %s: %s' % (self._message_name3, str(userdata.message3)))
            rospy.loginfo('This is the %s: %s' % (self._message_name4, str(userdata.message4)))
            rospy.loginfo('This is the %s: %s' % (self._message_name5, str(userdata.message5)))
            rospy.loginfo('This is the %s: %s' % (self._message_name6, str(userdata.message6)))

            return succeeded


class InitDancingReemDummyState(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['song_bpm', 'selected_movement'])

    def execute(self, userdata):

        return succeeded


def main():
    rospy.init_node('sm_init_dancing_reem_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add('INIT_DANCING_REEM',
                               InitDancingReem(),
                               transitions={succeeded: 'PRINT_DATA_6',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'initial_future_position_out': 'future_current_position',
                                          'initial_current_position_out': 'current_position',
                                          'next_movement_name_out': 'selected_movement',
                                          'prob_vector_out': 'probability_vector',
                                          'repeat_out': 'repeat_out',
                                          'dict_movement_databse_out': 'dict_available_movements'})

        smach.StateMachine.add('PRINT_DATA_6',
                               PrintUserData6('future_current_position', 'current_position', 'selected_movement', 'probability_vector',
                                              'repeat_out', 'dict_available_movements'),
                               transitions={succeeded: succeeded,
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'message1': 'future_current_position',
                                          'message2': 'current_position',
                                          'message3': 'selected_movement',
                                          'message4': 'probability_vector',
                                          'message5': 'repeat_out',
                                          'message6': 'dict_available_movements'})

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
