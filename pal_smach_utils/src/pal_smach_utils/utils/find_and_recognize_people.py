import smach

from text_to_speech.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.speech.sound_action import SpeakActionState
from math_utils import *

from global_common import *
from find_person import FindPersonStateMachine
from recognize_face import RecognizeFaceStateMachine
from timeout_container import TimeoutContainer


class FindAndRecognizePersonStateMachine(smach.StateMachine):

    def __init__(self):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
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
                transitions={succeeded: 'PERSON_FOUND_TTS',
                    aborted: 'RECOGNIZE_FACE', preempted: 'RECOGNIZE_FACE'})

            smach.StateMachine.add(
                'PERSON_FOUND_TTS',
                SpeakActionState("I've found you!"),
                transitions={succeeded: 'RECOGNIZE_FACE'})

            smach.StateMachine.add(
                'RECOGNIZE_FACE',
                TimeoutContainer(RECOGNIZE_UNKNOWN_PERSON_TIMEOUT,
                    RecognizeFaceStateMachine()),
                transitions={succeeded: succeeded, unknown_face: 'ROTATE',
                    aborted: 'ROTATE', preempted: 'ROTATE'}, 
                remapping={"out_person_name":"person_name"})
            # outputs: 'person_name'

            pose = Pose()
            pose.position = Point(0, 0, 0)
            pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 30))

            smach.StateMachine.add(
                'ROTATE',
                MoveActionState("/base_link", pose=pose),
                transitions={succeeded: 'FIND_PERSON'})


class FindAndRecognizeParticularPersonStateMachine(smach.StateMachine):

    def __init__(self, name_key=None, name_cb=None, input_keys=[]):

        if name_key and name_cb:
            raise ValueError("You've set more than one of `name_key' and `name_cb'")
        elif not name_key and not name_cb:
            raise ValueError("Neither `name_key' nor `name_cb' were set!")

        if name_key:
            assert input_keys == []
            input_keys = [name_key]

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                input_keys=input_keys, output_keys=['person_pos'])

        class CheckResult(smach.State):

            def __init__(self):
                smach.State.__init__(self, outcomes=[succeeded, aborted],
                    input_keys=input_keys + ['person_name'])

            def execute(self, userdata):
                if name_cb:
                    target_person_name = name_cb(userdata)
                else:
                    target_person_name = name_key

                if userdata.person_name.lower() == target_person_name.lower():
                    return succeeded

                return aborted

        with self:

            smach.StateMachine.add(
                'SM_FRP',
                FindAndRecognizePersonStateMachine(),
                transitions={succeeded: 'CHECK_PERSON'})
            # outputs: 'person_name', 'person_pos'

            smach.StateMachine.add(
                'CHECK_PERSON',
                CheckResult(),
                transitions={succeeded: succeeded, aborted: 'ROTATE'})

            pose = Pose()
            pose.position = Point(0, 0, 0)
            pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 30))

            smach.StateMachine.add(
                'ROTATE',
                MoveActionState("/base_link", pose=pose),
                transitions={succeeded: 'SM_FRP'})


class FindAndRecognizePeopleStateMachine(smach.Iterator):

    def __init__(self):
        smach.Iterator.__init__(
            self,
            outcomes=[succeeded, aborted],
            input_keys=[],
            output_keys=[],
            it=lambda: range(3),
            it_label='index',
            exhausted_outcome=succeeded)

        with self:
            smach.Iterator.set_contained_state(
                'SM_FIND_AND_RECOGNIZE_PERSON',
                FindAndRecognizePersonStateMachine(),
                loop_outcomes=['succeeded'])

# vim: expandtab ts=4 sw=4
