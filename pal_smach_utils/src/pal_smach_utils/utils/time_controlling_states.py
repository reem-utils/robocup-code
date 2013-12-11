# -*- encoding: utf-8 -*-

import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

#Time that we sleep to aboid PC to look every nanosecond.
SAMPLING_RATE_TIME = 1.0


class GetCurrentROSTimeState(smach.State):

    """
    Gives the current ROS time and sets the time elapsed to zero.
    """

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted], output_keys=['starting_ros_time_out'])

    def execute(self, userdata):

        now = rospy.get_rostime()
        rospy.loginfo("Current time seconds= %s, nanoseconds= %s", now.secs, now.nsecs)
        while now == 0:
            #We loop until ros clock starts.
            now = rospy.get_rostime()
            rospy.loginfo("Current time seconds= %s, nanoseconds= %s", now.secs, now.nsecs)
        userdata.starting_ros_time_out = now

        return succeeded


class TellIfSongHasFinished(smach.State):

    """
    Gives the current ROS time and sets the time elapsed to zero.
    """

    def __init__(self):

        smach.State.__init__(self, outcomes=['song_not_finished', 'song_finished', preempted, aborted], input_keys=['in_starting_ros_time', 'song_duration'])

    def execute(self, userdata):

        return SongHasFinished(userdata.in_starting_ros_time, userdata.song_duration)


def SongHasFinished(start_time, duration):

    now = rospy.get_rostime()
    #rospy.loginfo("Current time seconds= %s, nanoseconds= %s", now.secs, now.nsecs)
    time_elapsed = now - start_time
    #print "TIME ELAPSE VARIABLE ==>" + str(time_elapsed)

    #rospy.loginfo('TIME ELAPSED ==> %s', time_elapsed)

    d = rospy.Duration.from_sec(duration / 1000.0)

    #print "SONG DURATION VARIABLE ==>" + str(d)

    if time_elapsed < d:
        #rospy.sleep(SAMPLING_RATE_TIME)
        return 'song_not_finished'

    return 'song_finished'
