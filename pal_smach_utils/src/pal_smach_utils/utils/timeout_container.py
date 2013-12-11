import rospy
import smach
from smach_ros import SimpleActionState
from tf.transformations import quaternion_from_euler

from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus

from global_common import *

class SleepState(smach.State):

    _duration = None    # in sec

    def __init__(self, duration, **kwargs):
        """
        A state that sleep for a given amount of time and then succeeds.
        Support for preemption is implemented.

        :param duration time to sleep, in seconds (float)
        """
        assert duration > 0
        smach.State.__init__(self, outcomes=[succeeded, preempted], **kwargs)
        self._duration = duration

    def execute(self, userdata):
        remaining_time = self._duration

        rospy.loginfo("Sleeping for %s seconds..." % self._duration)
        while remaining_time > 0:

            if self.preempt_requested():
                self.service_preempt()
                return preempted

            duration = rospy.Duration(min(0.05, remaining_time))
            remaining_time = remaining_time - 0.05

            rospy.sleep(duration)

        return succeeded

class ConditionalSleepState(SleepState):

    def __init__(self, duration, **kwargs):
        """
        Like `SleepState', but only waits if the input key `sleep_enabled' is
        true.
        """

        if not 'input_keys' in kwargs:
            kwargs['input_keys'] = []
        kwargs['input_keys'].append('sleep_enabled')

        SleepState.__init__(self, duration, **kwargs)

    def execute(self, userdata):
        if userdata.sleep_enabled:
            return SleepState.execute(self, userdata)
        else:
            return succeeded


class TimeoutContainer(smach.Concurrence):
    """

    """

    def __init__(self, timeout, state):
        outcomes = set(state.get_registered_outcomes())
        outcomes.add(preempted)

        def generic_outcome_cb(outcomes):
            return outcomes['MAIN_STATE']

        def generic_child_termination_cb(outcomes):
            return True

        smach.Concurrence.__init__(self,
            list(outcomes),
            default_outcome=preempted,
            input_keys=list(state.get_registered_input_keys()),
            output_keys=list(state.get_registered_output_keys()),
            outcome_cb=generic_outcome_cb,
            child_termination_cb=generic_child_termination_cb)

        with self:
            smach.Concurrence.add('MAIN_STATE', state)
            smach.Concurrence.add('TIMEOUT_WATCH', SleepState(timeout))

# vim: expandtab ts=4 sw=4
