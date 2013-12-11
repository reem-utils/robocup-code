import smach

from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.math_utils import multiply_vector, normalize_vector, substract_vector

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted, unknown_face, APPROACH_UNKNOWN_PERSON_TIMEOUT, RECOGNIZE_UNKNOWN_PERSON_TIMEOUT
from pal_smach_utils.utils.find_person import FindPersonStateMachine
from pal_smach_utils.utils.timeout_container import TimeoutContainer
from pal_smach_utils.utils.recognize_face import RecognizeFaceStateMachine


class FindAndRecognizePersonStateMachine(smach.StateMachine):

    def __init__(self):

        smach.StateMachine.__init__(
            self,
            outcomes=[succeeded, preempted, aborted],
            output_keys=['person_name', 'person_pos'])

        with self:

            smach.StateMachine.add(
                'FIND_PERSON',
                FindPersonStateMachine(),
                transitions={succeeded: 'MOVE_TO_PERSON', aborted: 'ROTATE'})
            # outputs: closest_person

            def move_to_person_goal_cb(userdata, nav_goal):
                position = Point(userdata.closest_person.x, userdata.closest_person.y, 0)
                distance_vector = multiply_vector(normalize_vector(position), 1)
                position = substract_vector(position, distance_vector)

                nav_goal.target_pose.pose.position = position
                nav_goal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
                userdata.person_pos = nav_goal.target_pose.pose

                return nav_goal

            smach.StateMachine.add(
                'MOVE_TO_PERSON',
                TimeoutContainer(APPROACH_UNKNOWN_PERSON_TIMEOUT, MoveActionState(
                    goal_cb=move_to_person_goal_cb,
                    input_keys=['closest_person'],
                    output_keys=['person_pos'])),
                transitions={
                    succeeded: 'PERSON_FOUND_TTS',
                    aborted: 'RECOGNIZE_FACE',
                    preempted: 'RECOGNIZE_FACE'})

            smach.StateMachine.add(
                'PERSON_FOUND_TTS',
                SpeakActionState("I've found you!"),
                transitions={succeeded: 'RECOGNIZE_FACE'})

            smach.StateMachine.add(
                'RECOGNIZE_FACE',
                TimeoutContainer(
                    RECOGNIZE_UNKNOWN_PERSON_TIMEOUT,
                    RecognizeFaceStateMachine()),
                remapping={"out_person_name": "person_name"},
                transitions={
                    succeeded: succeeded,
                    unknown_face: 'ROTATE',
                    aborted: 'ROTATE',
                    preempted: 'ROTATE'})
            # outputs: 'person_name'

            pose = Pose()
            pose.position = Point(0, 0, 0)
            pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 30))

            smach.StateMachine.add(
                'ROTATE',
                MoveActionState("/base_link", pose=pose),
                transitions={succeeded: 'FIND_PERSON'})
