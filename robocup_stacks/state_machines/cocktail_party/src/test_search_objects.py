#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.utils.colors import Colors
# from pal_smach_utils.grasping.search_objects_behaviour import SearchObjectsStateMachine
from pal_smach_utils.grasping.search_object_with_confidence import SearchObjectWithConfidenceStateMachine


class Debug(smach.State):
    def __init__(self, text=None, text_cb=None, input_keys=[], output_keys=[]):
        smach.State.__init__(self, input_keys=input_keys, output_keys=output_keys, outcomes=[succeeded, aborted])
        if (text is not None) and (text_cb is not None):
            raise ValueError("You've set more than one of `text' and `text_cb'!")
        if (text is None) and (text_cb is None):
            raise ValueError("Neither `text' nor `text_cb' were set!")
        self.text = text
        self.text_cb = text_cb

    def execute(self, userdata):
        debug_text = self.text if self.text is not None else self.text_cb(userdata)
        rospy.loginfo("\n" + Colors().GREEN_BOLD + str(debug_text) + Colors().NATIVE_COLOR + "\n")


def main():

    """Unit test for SearchObjectWithConfidenceStateMachine. Looking for coke. """

    rospy.init_node('test_search_objects')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with sm:

        sm.userdata.object_to_search_for = "coke"

        smach.StateMachine.add(
            "SEARCH_OBJECT",
            # SearchObjectsStateMachine(),
            SearchObjectWithConfidenceStateMachine(),
            transitions={succeeded: "DEBUG_OBJECT_FOUND", aborted: "DEBUG_OBJECT_FOUND"}
            )
        #input_keys=['object_to_search_for'] output_keys=['object_found']

        def text_debug_cb(userdata):
            return "object_found\n" + str(userdata.object_found)

        smach.StateMachine.add(
            "DEBUG_OBJECT_FOUND",
            Debug(text_cb=text_debug_cb, input_keys=["object_found"])
            )

    sis = smach_ros.IntrospectionServer(
        'test_search_objects_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
