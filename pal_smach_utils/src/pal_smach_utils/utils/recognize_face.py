import smach
from actionlib_msgs.msg import GoalStatus
from smach_ros import SimpleActionState

from face_recognition.msg import FaceRecognitionAction, FaceRecognitionGoal

from pal_interaction_msgs.msg import asrresult

from pal_smach_utils.utils.global_common import FACE_RECOGNITION_CONFIDENCE_THRESHOLD, RECOGNIZE_UNKNOWN_PERSON_TIMEOUT, succeeded, preempted, aborted, unknown_face
from pal_smach_utils.speech.sound_action import SpeakActionFromPoolStateMachine, SpeakActionState
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables
from rospy.rostime import Duration


class RecognizeFaceStateMachine(smach.StateMachine):
    """RecognizeFaceStateMachine.

    Use this State Machine to recognize a face.

    """

    def __init__(self, announce_unknown_face=True, instructions_tts=True):
        """Constructor for RecognizeFaceStateMachine.

        @type announce_unknown_face: boolean
        @param announce_unknown_face: If True, the robot will say something if can't recognize the person.

        @type instructions_tts: boolean
        @param instructions_tts: If True, the robot will ask the person to look at his face. Otherwise, will try recognize without instructions.

        Output Keys:
            @type out_person_name: string|None
            @return out_person_name: If a person is recognized, out_person_name="Person name", otherwise out_person_name=None

        """
        smach.StateMachine.__init__(self,
            output_keys=['out_person_name'],
            outcomes=[succeeded, preempted, aborted, unknown_face]
            )

        with self:
            self.variables = cocktail_party_variables

            if instructions_tts is True:
                smach.StateMachine.add(
                    'INSTRUCTIONS_TTS',
                    SpeakActionFromPoolStateMachine(["Please, look at my face!"]),
                    transitions={succeeded: 'RECOGNIZE_FACE'})

            @smach.cb_interface(outcomes=[succeeded, unknown_face], output_keys=['out_person_name'])
            def recognize_face_result_cb(userdata, status, result):
                userdata.out_person_name = None
                if status == GoalStatus.SUCCEEDED:
                    print "Face recognition result:\n", result
                    if len(result.names) > 0 and result.confidence[0] > FACE_RECOGNITION_CONFIDENCE_THRESHOLD:
                        userdata.out_person_name = result.names[0]
                        return succeeded
                    return unknown_face
                return aborted

            faceGoal = FaceRecognitionGoal()
            faceGoal.order_id = 0  # recognize_once

            smach.StateMachine.add(
                'RECOGNIZE_FACE',
                SimpleActionState(
                    self.variables.A_FACE_RECOGNITION,
                    FaceRecognitionAction,
                    exec_timeout=Duration(RECOGNIZE_UNKNOWN_PERSON_TIMEOUT),
                    result_cb=recognize_face_result_cb,
                    goal=faceGoal),
                transitions={succeeded: "ANNOUNCE_PERSON_RECOGNIZED",
                unknown_face: "ANNOUNCE_UNKNOWN_FACE" if announce_unknown_face else unknown_face,
                aborted: "ANNOUNCE_UNKNOWN_FACE" if announce_unknown_face else unknown_face})

            def announce_recognized_cb(userdata):
                # "nice" must be lowercase so it isn't pronounced like the city!
#                return 'Hello, %s. nice to see you again.' % userdata.out_person_name
                return 'Hello, %s!' % userdata.out_person_name

            smach.StateMachine.add(
                'ANNOUNCE_PERSON_RECOGNIZED',
                SpeakActionState(text_cb=announce_recognized_cb, input_keys=['out_person_name']),
                transitions={succeeded: succeeded, aborted: succeeded, preempted: succeeded}
            )

            smach.StateMachine.add(
                'ANNOUNCE_UNKNOWN_FACE',
                SpeakActionState("I'm sorry, I don't recognize you"),
                transitions={succeeded: unknown_face})


class RecognizeSeveralFacesStateMachine(smach.Iterator):
    """
    Looks for `num_persons' persons introducing themselves to the robot
    one after another (with a PERSON_CHANGE_TIME second long wait between
    them).

    The names of all persons are returned in an ordered list in `person_names'.
    """

    def __init__(self, num_persons, recognize_existing=True):
        smach.Iterator.__init__(
            self,
            outcomes=[succeeded, aborted],
            input_keys=[],
            output_keys=['person_names'],
            it=lambda: range(num_persons),
            it_label='wait_for_person',
            exhausted_outcome=succeeded)

        self.userdata.person_names = []

        def transition_cb(userdata, active_states):
            self.userdata.person_names.append(userdata.person_name)

        self.register_transition_cb(transition_cb)

        with self:
            # The input key 'wait_for_person` will evalute to True (and thus
            # result in WaitForPerson being executed) for every iteration
            # other than the first one.
            smach.Iterator.set_contained_state(
                'SM_RECOGNIZE_FACE',
                RecognizeFaceStateMachine(learn=True,
                    recognize_existing=recognize_existing, enable_waiting=True,
                    enable_name_check=True),
                loop_outcomes=[succeeded])
