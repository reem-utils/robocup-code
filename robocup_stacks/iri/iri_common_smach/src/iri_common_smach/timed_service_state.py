import roslib; roslib.load_manifest('iri_common_smach')
import rospy
import smach
import smach_ros
import time

from smach_ros import ServiceState

"""
Timed Service State class. Should work as ServiceState but also measures execution time.

USAGE:
User timed_service_state.TimedServiceState instead of ServiceState
"""

class TimedServiceState(ServiceState):
    """
    Timed Service State class. Should work as ServiceState but also measures execution time.
    """
    def __init__(self, service_name, service_spec, **args):
        """
        Init method also initializes timer and executions counter
        """
        ServiceState.__init__(self, service_name = service_name, service_spec = service_spec, **args)
        self.total_time = 0
        self.num_executions = 0

    def execute(self, userdata):
        """
        Calls inherited execute and measures its execution time
        """
        init_time = time.time()
        self.num_executions += 1
        result = super(TimedServiceState, self).execute(userdata)
        self.total_time += (time.time() - init_time)
        return result

    def get_execution_time(self):
        return self.total_time

    def get_number_executions(self):
        return self.num_executions
