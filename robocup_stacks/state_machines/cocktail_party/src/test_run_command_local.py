#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.utils.run_command_local import RunCommandLocal


def main():
    """Unit test for RunCommandLocal. """

    rospy.init_node('test_run_command')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:
        smach.StateMachine.add("TEST_RUN_COMMAND",
            RunCommandLocal("/home/icarus/workspace/reem_at_iri/trunk/scripts/graspingStop.sh"),
            transitions={succeeded: succeeded, aborted: aborted}
            )


    sis = smach_ros.IntrospectionServer(
        'test_run_command_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
