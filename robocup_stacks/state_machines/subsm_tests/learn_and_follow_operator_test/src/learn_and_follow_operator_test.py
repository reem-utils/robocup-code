#! /usr/bin/env python

import roslib
roslib.load_manifest('learn_and_follow_operator_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.follow_and_stop import FollowAndStop

from pal_smach_utils.speech.sound_action import SpeakActionState

from smach import CBState

from pal_smach_utils.navigation.elevator_handling import ElevatorHandling

from pal_smach_utils.utils.debug import setDebugLevel, debugPrint

from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_interaction_msgs.msg import asrresult
from pal_smach_utils.speech.grammar_state import GrammarState

START_FOLLOW_ME_GRAMMAR_NAME = rospy.get_param('/restaurant/follow_grammar_name')

from pal_smach_utils.utils.timeout_container import SleepState

from geometry_msgs.msg import Pose, PoseStamped, Quaternion
from tf.transformations import quaternion_from_euler

import dynamic_reconfigure.client

MOVE_BASE_TOPIC_GOAL = "/move_by/move_base_simple/goal"

import os
inside_robot = False
robot = os.environ.get('PAL_ROBOT')
if robot == 'rh2c' or robot == 'rh2m' or robot == 'reemh3c' or robot == 'reemh3m' or robot == 'reemh3':
    inside_robot = True

DISTANCE_TO_FOLLOW = 0.9


def main():
    rospy.init_node('sm_learn_and_follow_operator_test')

    setDebugLevel(0)

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        if (inside_robot):

            @smach.cb_interface(outcomes=[succeeded])
            def setPlannerParameters(userdata):
                debugPrint('    Setting planner parameters values for following the operator...', 4)
                node_to_reconfigure = "/move_by/move_base/PalLocalPlanner"
                client = dynamic_reconfigure.client.Client(node_to_reconfigure)
                params = {
                    'acc_lim_x': 0.4,
                    'acc_lim_th': 1.7593,
                    'max_vel_x': 0.4,
                    'max_vel_th': 0.6}
                new_config = client.update_configuration(params)

                rospy.loginfo("New configuration returned by the dynamic reconfigure server:\n" + str(new_config))

                return succeeded

            smach.StateMachine.add('SET_PLANNER_PARAMETERS',
                                   CBState(setPlannerParameters),
                                   transitions={succeeded: "ENABLE_FOLLOW_ME_START_GRAMMAR"})
        else:
            not_robot_text = "Cannot set the planner parameters because we are not inside the robot."
            smach.StateMachine.add('SET_PLANNER_PARAMETERS',
                                   SpeakActionState(not_robot_text),
                                   transitions={succeeded: "ENABLE_FOLLOW_ME_START_GRAMMAR"})

        smach.StateMachine.add('ENABLE_FOLLOW_ME_START_GRAMMAR',
                               GrammarState(START_FOLLOW_ME_GRAMMAR_NAME, enabled=True),
                               transitions={succeeded: 'FOLLOW_ME_INTRO'})

        intro_text = "Hello, my name is REEM! Please, say follow me when you are ready to begin the test."
        smach.StateMachine.add('FOLLOW_ME_INTRO',
                               SpeakActionState(intro_text),
                               transitions={succeeded: 'LISTEN_FOLLOW_ME_START_COMMAND',
                                            preempted: "LISTEN_FOLLOW_ME_START_COMMAND",
                                            aborted: "LISTEN_FOLLOW_ME_START_COMMAND"})

        smach.StateMachine.add('SLEEP_STATE_BEFORE_LISTEN_AGAIN',
                               SleepState(0.5),
                               transitions={succeeded: 'LISTEN_FOLLOW_ME_START_COMMAND',
                                            preempted: 'LISTEN_FOLLOW_ME_START_COMMAND'})

        def listenFollowMeStartCommandCallback(userdata, message):
            debugPrint("The message listened is " + str(message), 3)
            grammar_tags = [tag for tag in message.tags if tag.key == 'action']
            if grammar_tags and grammar_tags[0].value == "follow":
                return succeeded
            return aborted

        smach.StateMachine.add('LISTEN_FOLLOW_ME_START_COMMAND',
                               TopicReaderState(topic_name='/usersaid', msg_type=asrresult, timeout=20.0,
                               outcomes=[succeeded, preempted, aborted], callback=listenFollowMeStartCommandCallback),
                               transitions={succeeded: "DISABLE_FOLLOW_ME_START_GRAMMAR",
                                            preempted: "SLEEP_STATE_BEFORE_LISTEN_AGAIN",
                                            aborted: "SLEEP_STATE_BEFORE_LISTEN_AGAIN"})

        smach.StateMachine.add('DISABLE_FOLLOW_ME_START_GRAMMAR',
                               GrammarState(START_FOLLOW_ME_GRAMMAR_NAME, enabled=False),
                               transitions={succeeded: 'INIT_FOLLOW_ME_PARAMETERS'})

        @smach.cb_interface(outcomes=[succeeded])
        def initFollowMeParameters(userdata):
            userdata.out_learn_person = True
            return succeeded

        smach.StateMachine.add('INIT_FOLLOW_ME_PARAMETERS',
                               CBState(initFollowMeParameters, output_keys=["out_learn_person"]),
                               transitions={succeeded: 'FOLLOW_ME'})

        smach.StateMachine.add('FOLLOW_ME',
                               FollowAndStop(DISTANCE_TO_FOLLOW, "follow_me"),
                               transitions={succeeded: 'ELEVATOR_HANDLING'},
                               remapping={"in_learn_person": "out_learn_person"})

        if (inside_robot):
            smach.StateMachine.add('ELEVATOR_HANDLING',
                                   ElevatorHandling(),
                                   transitions={succeeded: 'RESTORE_DISTANCE_TO_HUMAN'})
        else:
            not_robot_text = "Cannot execute the elevator handler because we are not inside the robot."
            smach.StateMachine.add('ELEVATOR_HANDLING',
                                   SpeakActionState(not_robot_text),
                                   transitions={succeeded: "RESTORE_DISTANCE_TO_HUMAN"})

        @smach.cb_interface(outcomes=[succeeded])
        def restoreDistance(userdata):
            while True:
                try:
                    rospy.set_param("/params_learn_and_follow_operator_test/distance_to_human", DISTANCE_TO_FOLLOW)
                    break
                except Exception as ex:
                    rospy.loginfo(str(ex))
                    rospy.logerr("There was an error while trying to set the parameter. Trying again...")

            userdata.out_learn_person = False
            return succeeded

        smach.StateMachine.add('RESTORE_DISTANCE_TO_HUMAN',
                               CBState(restoreDistance, output_keys=["out_learn_person"]),
                               transitions={succeeded: 'FOLLOW_ME_AGAIN'})

        smach.StateMachine.add('FOLLOW_ME_AGAIN',
                               FollowAndStop(DISTANCE_TO_FOLLOW, "follow_me_again"),
                               transitions={succeeded: 'STOP_ROBOT'},
                               remapping={"in_learn_person": "out_learn_person"})

        @smach.cb_interface(outcomes=[succeeded])
        def stopRobot(userdata):
            stop_goal = PoseStamped()
            stop_goal.header.stamp = rospy.Time.now()
            stop_goal.header.frame_id = "/base_link"
            stop_goal.pose.position.x = 0.1
            stop_goal.pose.position.y = 0.0
            stop_goal.pose.position.z = 0.0
            stop_goal.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
            pub = rospy.Publisher(MOVE_BASE_TOPIC_GOAL, PoseStamped)
            pub.publish(stop_goal)
            return succeeded

        smach.StateMachine.add('STOP_ROBOT',
                               CBState(stopRobot),
                               transitions={succeeded: 'SAY_FINISHED'})

        finished_text = "The follow me test has finished."
        smach.StateMachine.add('SAY_FINISHED',
                               SpeakActionState(finished_text),
                               transitions={succeeded: succeeded})

    sis = smach_ros.IntrospectionServer('learn_and_follow_operator_test_sm', sm, '/LEARN_AND_FOLLOW_OPERATOR_TEST')
    sis.start()
    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
