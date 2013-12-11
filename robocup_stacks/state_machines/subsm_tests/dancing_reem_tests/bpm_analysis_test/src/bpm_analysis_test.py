#! /usr/bin/env python

import roslib; roslib.load_manifest('bpm_analysis_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from bpm_analysis import BpmAnalysisSM


class PrintUserData2(smach.State):

    def __init__(self,
                message_name1='Message1',
                message_name2='Message2'):
            smach.State.__init__(self,
                    outcomes=[succeeded, preempted, aborted],
                    input_keys=['message1', 'message2'])

            self._message_name1 = message_name1
            self._message_name2 = message_name2

    def execute(self, userdata):
            rospy.loginfo('This is the %s: %s' % (self._message_name1, str(userdata.message1)))
            rospy.loginfo('This is the %s: %s' % (self._message_name2, str(userdata.message2)))
            return succeeded


def main():
    rospy.init_node('sm_bpm_analysis_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add('BPM_ANALYSIS',
                                    BpmAnalysisSM(),
                                    transitions={succeeded: 'PRINT_DATA',
                                                preempted: preempted,
                                                aborted: aborted},
                                    remapping={'bpm_out': 'song_bpm',
                                                'song_path_out': 'song_path'})

        smach.StateMachine.add('PRINT_DATA',
                                PrintUserData2('song_bpm', 'song_path'),
                                transitions={
                                    succeeded: succeeded,
                                    preempted: preempted,
                                    aborted: aborted},
                                remapping={
                                    'message1': 'song_bpm',
                                    'message2': 'song_path'})

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
