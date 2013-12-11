import smach
import rospy
import platform
from actionlib_msgs.msg import GoalStatus
from smach_ros import SimpleActionState
import random

from pal_interaction_msgs.msg import asrresult

from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_smach_utils.utils.colors import Colors
from face_recognition.msg import FaceRecognitionAction, FaceRecognitionGoal
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted  # , unknown_face, previously_recognized, existing_name
from pal_smach_utils.speech.grammar_state import GrammarState
from pal_smach_utils.speech.sound_action import SpeakActionFromPoolStateMachine, SpeakActionState
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables
#from recognize_face import RecognizeFaceStateMachine

COUNT_NUMBER = 2
COUNT_WARNING = 1
COMPUTER_NAME = platform.node()
warning = "warning"
colors = Colors()
PERSON_NAMES = cocktail_party_variables.PERSONS_NAME
#PATH_IAM = "/mnt_flash/etc/interaction/sphinx/model/gram/en_US/robocup/iam.gram"

class CountCheck(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted, warning])
        self.count = 0

    def execute(self, userdata):
        self.count += 1
        rospy.loginfo("\n ===== Count check %d/%d =====" % (self.count, COUNT_NUMBER))
        if self.count < COUNT_NUMBER:
            if self.count == COUNT_WARNING:
                return warning
            return succeeded
        self.count = 0
        return aborted


class CheckRepeatedNames(smach.State):
    def __init__(self):
        smach.State.__init__(self, input_keys=["names_already_asigned", "current_name"], output_keys=[], outcomes=[succeeded, aborted])

    def execute(self, userdata):
        rospy.loginfo("\n===== Checking if name %s already exists in %s =====" % (userdata.current_name, userdata.names_already_asigned))
        if userdata.current_name in userdata.names_already_asigned:
            return aborted
        return succeeded


class AsignANewName(smach.State):
    def __init__(self):
        smach.State.__init__(self, input_keys=["names_already_asigned"], output_keys=["out_person_name"], outcomes=[succeeded, aborted])
        self.color = Colors()

    def execute(self, userdata):
        userdata.out_person_name = PERSON_NAMES[0]
        while True:
            name = PERSON_NAMES[random.randint(0, int(len(PERSON_NAMES) / 2))]  #XXX A random name from the first half list. Assuming the first half as male's name
            rospy.loginfo(self.color.BACKGROUND_GREEN + "Trying identify '%s' in %s %s" % (name, userdata.names_already_asigned, self.color.NATIVE_COLOR))
            if name not in userdata.names_already_asigned:
                userdata.out_person_name = name
                return succeeded


class LearnFaceStateMachine(smach.StateMachine):
    """LearnFaceStateMachine.

    Use this State Machine to learn a face.

    Steps of this State Machine:
        The robot will: ask for name; enable the grammar defined on cocktail_party.yaml file as 'people_grammar_name'; listen the name;
        ask the person to look at his face and learn the face.
    Important:
        If the robot can't understand what the person is saying or the name was already asigned to another person, then a new person name
        will be asigned. The name is a random name loaded from the iam.gram file located on the Cocktail Party package. The names should be the
        same of the grammar robocup/iam.gram located on the robot.

    Output Keys:
        @type out_person_name: out_person_name
        @return out_person_name:  If a face is learned, out_person_name="Person name", otherwise out_person_name=None

    """
    def __init__(self):
        """Constructor for LearnFaceStateMachine.

        """
        smach.StateMachine.__init__(self,
            input_keys=[],
            output_keys=["out_person_name"],
            outcomes=[succeeded, aborted, preempted])  # , previously_recognized])  # ,existing_name])

        with self:
            self.variables = cocktail_party_variables
            self.userdata.names_already_asigned = []
            self.userdata.current_name = None
            self.count_check = CountCheck()

            # smach.StateMachine.add("TRY_RECOGNIZE",
            #     RecognizeFaceStateMachine(announce_unknown_face=False),
            #     transitions={succeeded: previously_recognized, unknown_face: "ASK_FOR_NAME"}
            #     )

            ask_for_name_phrases = ["Hi! What is your name?", "What is your name?", "What's your name, sweety?", "Tell me your name, handsome!", "Please, tell me your name!"]

            smach.StateMachine.add(
                    'ASK_FOR_NAME',
                    SpeakActionFromPoolStateMachine(ask_for_name_phrases),
                    transitions={succeeded: 'ENABLE_NAME_GRAMMAR', aborted: "ENABLE_NAME_GRAMMAR",  preempted: "ASK_FOR_NAME"})

            smach.StateMachine.add(
                'ENABLE_NAME_GRAMMAR',
                GrammarState(self.variables.PEOPLE_GRAMMAR_NAME, enabled=True),
                transitions={succeeded: 'LISTEN_TO_NAME'})

            def listen_name_cb(userdata, message):
                tags = [tag for tag in message.tags if tag.key == 'name']
                if tags:
                    name = tags[0].value
                    userdata.out_person_name = name
                    self.userdata.current_name = name
                    return succeeded
                return aborted

            smach.StateMachine.add(
                'LISTEN_TO_NAME',
                TopicReaderState(
                    topic_name=self.variables.T_USERSAID,
                    msg_type=asrresult,
                    timeout=10,
                    callback=listen_name_cb,
                    output_keys=['out_person_name'],
                    outcomes=[succeeded, aborted, preempted]),  # existing_name]),
                transitions={aborted: 'LISTEN_COUNT_CHECK', succeeded: 'CHECK_REPEATED_NAME'})

            smach.StateMachine.add(
                "LISTEN_COUNT_CHECK",
                self.count_check,
                transitions={succeeded: "LISTEN_TO_NAME", warning: "ASK_SPEAK_HIGHER", aborted: "ASIGN_A_NEW_NAME_2"}
                )

            smach.StateMachine.add(
                "ASK_SPEAK_HIGHER",
                SpeakActionState("I'm sorry! Can you repeat your name higher please?"),
                transitions={succeeded: "LISTEN_TO_NAME", aborted: "LISTEN_TO_NAME", aborted: "LISTEN_TO_NAME"}
                )

            smach.StateMachine.add(
                "CHECK_REPEATED_NAME",
                CheckRepeatedNames(),
                transitions={succeeded: "DISABLE_NAME_GRAMMAR", aborted: "ASIGN_A_NEW_NAME"}
                )

            smach.StateMachine.add(
                "ASIGN_A_NEW_NAME",
                AsignANewName(),
                transitions={aborted: "ASIGN_A_NEW_NAME_WARNING", succeeded: "ASIGN_A_NEW_NAME_WARNING"}
                )

            smach.StateMachine.add(
                "ASIGN_A_NEW_NAME_2",
                AsignANewName(),
                transitions={aborted: "ASIGN_A_NEW_NAME_WARNING_2", succeeded: "ASIGN_A_NEW_NAME_WARNING_2"}
                )

            def asign_a_new_name_cb(userdata):
                return "I'm sorry. I understood %s and this name was already asigned. I'll call you %s!" % (userdata.current_name, userdata.in_person_name)

            smach.StateMachine.add(
                'ASIGN_A_NEW_NAME_WARNING',
                SpeakActionState(text_cb=asign_a_new_name_cb, input_keys=['in_person_name', "current_name"]),
                remapping={"in_person_name": "out_person_name"},
                transitions={succeeded: 'DISABLE_NAME_GRAMMAR', aborted: 'DISABLE_NAME_GRAMMAR', preempted: "DISABLE_NAME_GRAMMAR"})

            def asign_a_new_name_2_cb(userdata):
                return "I'm sorry. I can't understand you. I'll call you %s!" % (userdata.in_person_name)

            smach.StateMachine.add(
                'ASIGN_A_NEW_NAME_WARNING_2',
                SpeakActionState(text_cb=asign_a_new_name_2_cb, input_keys=['in_person_name']),
                remapping={"in_person_name": "out_person_name"},
                transitions={succeeded: 'DISABLE_NAME_GRAMMAR', aborted: 'DISABLE_NAME_GRAMMAR', preempted: "DISABLE_NAME_GRAMMAR"})

            smach.StateMachine.add(
                'DISABLE_NAME_GRAMMAR',
                GrammarState(self.variables.PEOPLE_GRAMMAR_NAME, enabled=False),
                transitions={succeeded: 'ANNOUNCE_LEARN_FACE_NAME'})

            def announce_learn_face_name_cb(userdata):
                self.userdata.names_already_asigned.insert(len(self.userdata.names_already_asigned), userdata.in_person_name)
                self.count_check.count = 0
                return "Okay %s, look at my lovely face!" % userdata.in_person_name

            smach.StateMachine.add(
                'ANNOUNCE_LEARN_FACE_NAME',
                SpeakActionState(text_cb=announce_learn_face_name_cb, input_keys=['in_person_name']),
                remapping={"in_person_name": "out_person_name"},
                transitions={succeeded: 'LEARN_FACE'})

            def learn_face_goal_cb(userdata, old_goal):
                faceGoal = FaceRecognitionGoal()
                faceGoal.order_id = 3  # (re)train
                faceGoal.order_argument = userdata.in_person_name
                return faceGoal

            @smach.cb_interface(outcomes=[succeeded, aborted], output_keys=['out_person_name'])
            def learn_face_result_cb(userdata, status, result):
                if status == GoalStatus.SUCCEEDED and len(result.names) > 0:
                    return succeeded
                userdata.out_person_name = None
                return aborted

            smach.StateMachine.add(
                'LEARN_FACE',
                SimpleActionState(
                    self.variables.A_FACE_RECOGNITION,
                    FaceRecognitionAction,
                    goal_cb=learn_face_goal_cb,
                    result_cb=learn_face_result_cb,
                    input_keys=["in_person_name"]),
                    remapping={"in_person_name": "out_person_name"},
                    transitions={succeeded: "POST_LEARN_FACE", aborted: "ANNOUNCE_CANT_LEARN", preempted: "LEARN_FACE"})

            post_learn_face_phrases = ["You're my new best friend %s!", "Ok. Nice to meet you %s.", "I'm happy because now we are friends %s!"]

            smach.StateMachine.add(
                'POST_LEARN_FACE',
                SpeakActionFromPoolStateMachine(post_learn_face_phrases, arg_key="out_person_name"),
                transitions={succeeded: succeeded, aborted: "POST_LEARN_FACE", preempted: preempted}
                )

            smach.StateMachine.add(
                "ANNOUNCE_CANT_LEARN",
                SpeakActionState("Sorry, by some unknoun reason, I could not learn your face."),
                transitions={succeeded: aborted}
            )
