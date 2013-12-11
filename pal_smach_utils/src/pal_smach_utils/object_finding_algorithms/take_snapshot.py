#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
from smach import StateMachine, CBState
from smach_ros import ServiceState

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from std_srvs.srv import Empty


class TakeXtionSnapshot(smach.StateMachine):
    def __init__(self, wait_time=3.0):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                                    input_keys=[],
                                    output_keys=[])

        with self:
            @smach.cb_interface(outcomes=[succeeded])
            def wait(userdata):
                rospy.sleep(wait_time)
                return succeeded

            StateMachine.add('WAIT_STATE', CBState(wait, outcomes=[succeeded]), transitions={succeeded: 'TAKE_SNAPSHOT'})

            StateMachine.add('TAKE_SNAPSHOT', ServiceState('/xtion_snapshotter/snapshot', Empty),
                             transitions={succeeded: succeeded})
