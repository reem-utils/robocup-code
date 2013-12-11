#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted, previously_recognized
from pal_smach_utils.utils.learn_face import LearnFaceStateMachine
from pal_smach_utils.utils.drop_faces import DropAllFacesStateMachine


def main():
    """Unit test to LearnFaceStateMachine. Will delete all faces and restart personServer,
    ask the name of the person, and learn the face. """

    rospy.init_node('test_learn_person')
    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted, previously_recognized])
    with sm:

        smach.StateMachine.add(
            "DROP_FACES",
            DropAllFacesStateMachine(),
            transitions={succeeded: "LEARN_FACE", aborted: "LEARN_FACE"}
            )

        smach.StateMachine.add("LEARN_FACE",
            LearnFaceStateMachine()
            #transitions={succeeded: succeeded}
            )

    sis = smach_ros.IntrospectionServer(
        'test_learn_person_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
