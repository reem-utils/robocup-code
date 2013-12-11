#! /usr/bin/env python

import roslib; roslib.load_manifest('bpm_analysis_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from move_head_to_the_beat import MoveHeadToTheBeat
#from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers


# 30 seconds
SONG_DURATION_MILISECONDS = 30000
BPM_TEST = 120

HARMONICS = 1.0

class HeadDummyState(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             output_keys=['message1', 'message2', 'message3'])

    def execute(self, userdata):

        userdata.message1 = SONG_DURATION_MILISECONDS

        now = rospy.get_rostime()
        rospy.loginfo("Current time seconds= %s, nanoseconds= %s", now.secs, now.nsecs)
        while now == 0:
            #We loop until ros clock starts.
            now = rospy.get_rostime()
            rospy.loginfo("Current time seconds= %s, nanoseconds= %s", now.secs, now.nsecs)
        userdata.message2 = now

        userdata.message3 = BPM_TEST

        print "DUMMY SATE ENDED"
        return succeeded


def main():
    rospy.init_node('sm_bpm_analysis_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:
        """
        smach.StateMachine.add('START_ROBOT_CONTROLERS',
                                   StartRobotControllers(),
                                   transitions={succeeded: 'DUMMY_STATE_GENERATE_SOUND_PATH',
                                                preempted: preempted,
                                                aborted: aborted})
        """
      
        smach.StateMachine.add('DUMMY_STATE_GENERATE_SOUND_PATH',
                               HeadDummyState(),
                               transitions={succeeded: 'MOVE_HEAD_TO_THE_BEAT',
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'message1': 'song_duration',
                                          'message2': 'time_song_started_playing',
                                          'message3': 'song_bpm'})

        smach.StateMachine.add('MOVE_HEAD_TO_THE_BEAT',
                               MoveHeadToTheBeat(HARMONICS),
                               transitions={'song_finished': succeeded,
                                            preempted: preempted,
                                            aborted: aborted},
                               remapping={'in_song_duration': 'song_duration',
                                          'in_start_time': 'time_song_started_playing',
                                          'in_beat': 'song_bpm'})
        """
        smach.StateMachine.add('STOP_ROBOT_CONTROLERS',
                                   StopRobotControllers(),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted})
        """

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
