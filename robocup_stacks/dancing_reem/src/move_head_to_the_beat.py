#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import roslib
roslib.load_manifest('dancing_reem')
import smach
import rospy
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
import actionlib
from geometry_msgs.msg import PointStamped
from pal_smach_utils.utils.time_controlling_states import SongHasFinished
from pal_smach_utils.utils.bpm_conversions import BpmToFreq
from pr2_controllers_msgs.msg import PointHeadAction, PointHeadGoal

# Look at a point 45 degrees up
X_HEAD_VALUE = 1.0
Y_HEAD_VALUE = 0.0
Z_HEAD_VALUE = 1.5
Z_HEAD_CHANGE = 0.07
#CORRECT_FACT = 0
MAX_HEAD_VEL = 2

POINTING_FRAME_RH2 = "stereo_link"
POINTING_FRAME_RH3 = "/head_mount_xtion_link"


class MoveHeadToTheBeat(smach.State):

    """
    Move the head to the given beat during the song duration given,
    and taking in acount the time when the song started.
    """

    def __init__(self, harmonic=1.0):

        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             input_keys=['in_song_duration', 'in_start_time', 'in_beat'])
        self._harmonic = harmonic

    def execute(self, userdata):

        period = 1 / (BpmToFreq(userdata.in_beat) / self._harmonic)
        rospy.loginfo("PERIOD TO BE SENT" + str(period))
        cg = control_head(period)
        cg.main(userdata.in_song_duration, userdata.in_start_time, userdata.in_beat, self._harmonic)
        return succeeded


def check_correct_goal(goal):
    if goal.pointing_frame != '':
        return True
    else:
        return False

    """
    if goal.target.header.frame_id != '' and goal.pointing_frame != '':
        return True
    else:
        return False
    """


class control_head():

    def __init__(self, period):
        self.client = actionlib.SimpleActionClient('/head_traj_controller/point_head_action', PointHeadAction)
        self.client.wait_for_server()
        self.period = period
        self.head_goal = PointStamped()
        self.setMoves()


    def new_goal(self, message):
        #rospy.loginfo("We got a message on new_goal: \n" + str(message))
        self.head_goal = message

    def move_head(self):
        if self.head_goal.point.x == 0.0:
            return None

        goal = PointHeadGoal()
        goal.pointing_frame = POINTING_FRAME_RH2
        goal.pointing_axis.x = 1.0
        goal.pointing_axis.y = 0.0
        goal.pointing_axis.z = 0.0
        print "MOVEMENT TIME" + str(self.period)
        goal.min_duration = rospy.Duration(self.period)
        #goal.min_duration = rospy.Duration(2.0)
        goal.max_velocity = MAX_HEAD_VEL
        goal.target = self.head_goal
        rospy.loginfo('Goal frame id [%s]', goal.target.header.frame_id)
        goal.target.header.stamp = rospy.Time().now()
        if check_correct_goal(goal):
            #rospy.loginfo('GOOOOOAAAAL SEEENT [%s]', str(goal))
            self.client.send_goal(goal)
        else:
            rospy.loginfo("Not sending goal because it's malformed: \n" + str(goal))
        return None

    def setMoves(self):
        self.upMovement = PointStamped()
        self.upMovement.point.x = X_HEAD_VALUE
        self.upMovement.point.y = Y_HEAD_VALUE
        self.upMovement.point.z = Z_HEAD_VALUE + Z_HEAD_CHANGE
        self.upMovement.header.frame_id = "base_link"

        self.downMovement = PointStamped()
        self.downMovement.point.x = X_HEAD_VALUE
        self.downMovement.point.y = Y_HEAD_VALUE
        self.downMovement.point.z = Z_HEAD_VALUE - Z_HEAD_CHANGE
        self.downMovement.header.frame_id = "base_link"

    def main(self, song_duration, start_time, beat, harmonic):

        rospy.loginfo("STARING TO MOVE THE HEAD \n")
        frequency = BpmToFreq(beat) / harmonic
        rospy.loginfo("FREQUENCY \n" + str(frequency))
        rospy.loginfo("PERIOD \n" + str(1 / frequency))
        r = rospy.Rate(frequency)
        move = 'down'

        while not SongHasFinished(start_time, song_duration) == 'song_finished' and not rospy.is_shutdown():

            if move == 'up':
                self.new_goal(self.upMovement)
                rospy.loginfo("LOOK UP \n")
                move = 'down'
            else:
                self.new_goal(self.downMovement)
                rospy.loginfo("LOOK DOWN \n")

                move = 'up'

            self.move_head()
            r.sleep()
