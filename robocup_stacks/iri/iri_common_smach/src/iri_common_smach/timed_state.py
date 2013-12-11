import roslib; roslib.load_manifest('iri_common_smach')
import rospy
import smach
import smach_ros
import time

"""
Timed State class to measure execution time and number of executions

USAGE:
Init method should call timed_state.TimedState.__init__(...) instead of smach.State.__init__(...)
Use timed_execute instead of execute to measure times
"""

class TimedState(smach.State):
    """
    State class that measures times and executions
    """
    def __init__(self, **args):
        """
        Init method also initializes timer and executions counter
        WARNING user state should call the init of this class : timed_state.TimedState.__init__(...)
        """
        smach.State.__init__(self, **args)
        self.total_time = 0
        self.num_executions = 0

    def execute(self, userdata):
        """
        Calls timed_execute and measures its execution time
        WARNING Don't redefine this method
        """
        init_time = time.time()
        self.num_executions += 1
        result = self.timed_execute(userdata)
        self.total_time += (time.time() - init_time)
        return result
    
    def timed_execute(self, userdata):
        """
        Use this method instead of execute
        Code executed here is timed
        """
        raise NotImplementedError()

    def get_execution_time(self):
        return self.total_time
        
    def get_number_executions(self):
        return self.num_executions
