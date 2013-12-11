#! /usr/bin/env python

import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach
from global_common import *

CONST_SLEEP = 0.5
CONST_SLEEP_PRECISE = 0.01


class WaitState(smach.State):
    def __init__(self, time_a=0.0):
        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted])
        self._time_a = time_a

    def execute(self, userdata):
            rospy.loginfo('TimeOut of = %f' % self._time_a)
            before = rospy.get_time()
            now = rospy.get_time()
            interval = (now)-(before)
            rospy.loginfo("TIME WAITING : %f" % interval)
            while (interval < self._time_a):

            # Check for preempt
                if self.preempt_requested():
                    self.service_preempt()
                    rospy.loginfo("TIME WAITING : %f" % interval)
                    return preempted

                rospy.loginfo("TIME WAITING : %f" % interval)
                rospy.sleep(CONST_SLEEP)
                now = rospy.get_time()
                interval = (now)-(before)
                rospy.loginfo("TIME WAITING AFTER SLEEP : %f" % interval)

            return succeeded


class TimeOut(smach.StateMachine):

    def __init__(self, time_A=0.0):

        '''
        State that does nothing for the amount of seconds given
        :param In seconds.
        '''
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:

            smach.StateMachine.add('WAIT_STATE',
                                   WaitState(time_A),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted})


class TimeOutState(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['time_wait'])

    def execute(self, userdata):
            #rospy.loginfo('TimeOut of = %f' % userdata.time_wait)
            before = rospy.get_time()
            now = rospy.get_time()
            interval = (now) - (before)
            #rospy.loginfo("TIME WAITING : %f" % interval)
            while (interval < userdata.time_wait):

            # Check for preempt
                if self.preempt_requested():
                    self.service_preempt()
                    #rospy.loginfo("TIME WAITING : %f" % interval)
                    return preempted

                #rospy.loginfo("TIME WAITING : %f" % interval)
                rospy.sleep(CONST_SLEEP_PRECISE)
                now = rospy.get_time()
                interval = (now)-(before)
                #rospy.loginfo("TIME WAITING AFTER SLEEP : %f" % interval)

            return succeeded

# vim: expandtab ts=4 sw=4
