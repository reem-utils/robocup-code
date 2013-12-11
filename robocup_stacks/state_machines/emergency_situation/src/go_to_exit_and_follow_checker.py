#! /usr/bin/env python
# vim: expandtab ts=4 sw=4
import roslib
roslib.load_manifest('emergency_situation')
import smach
import rospy
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_vision_msgs.msg import FollowMeResponse
from pal_vision_msgs.srv import FollowMeStart, FollowMeStop
from pal_smach_utils.navigation.move_action import MoveActionState
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler


class StartRearService(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted, preempted])

    def execute(self, userdata):
        rospy.wait_for_service('/followMeServer/start')
        try:
            is_someone_following = rospy.ServiceProxy('/followMeServer/start', FollowMeStart)
            following = is_someone_following(5)
            rospy.loginfo("Rear Service Started.")
            return succeeded
        except rospy.ServiceException, e:
            print "Follow checker service did not start: %s" % e
            return aborted


class StopRearService(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted])

    def execute(self, userdata):
        try:
            reached_to_exit = rospy.ServiceProxy('/followMeServer/stop', FollowMeStop)
            result = reached_to_exit()
            rospy.loginfo("Rear Service Stopped")
            return succeeded
        except rospy.ServiceException, e:
            print "Follow checker did not stopped: %s" % e
            return aborted


class FollowChecker(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, aborted, preempted])

        with self:
            smach.StateMachine.add(
                'START_REAR_SERVICE',
                StartRearService(),
                transitions={succeeded: 'CHECK_FOR_PERSON'})

            # Follow checker is done with TopicReaderState is it correct??
            def follow_me_cb(userdata, message):
                if message.targetDetected:
                    print "Callback is called"
                    print message.targetDetected
                    return succeeded
                else:
                    print message.targetDetected
                    rospy.loginfo("No one is following")
                    return aborted

            smach.StateMachine.add(
                'CHECK_FOR_PERSON',
                TopicReaderState(
                topic_name='/followMe/result',
                msg_type=FollowMeResponse,
                callback=follow_me_cb),
                transitions={succeeded: 'STOP_REAR_SERVICE_WITH_PERSON', aborted: 'SAY_STAY'})

            smach.StateMachine.add(
                'STOP_REAR_SERVICE_WITH_PERSON',
                StopRearService(),
                transitions={'succeeded': 'START_REAR_SERVICE', 'aborted': 'STOP_REAR_SERVICE_WITH_PERSON'})

            smach.StateMachine.add(
                'SAY_STAY',
                SpeakActionState("Where are you? Please stay behind me."),
                transitions={succeeded: 'STOP_REAR_SERVICE_NO_PERSON', aborted: 'STOP_REAR_SERVICE_NO_PERSON'})

            smach.StateMachine.add(
                'STOP_REAR_SERVICE_NO_PERSON',
                StopRearService(),
                transitions={'succeeded': aborted, aborted: 'STOP_REAR_SERVICE_NO_PERSON'})

            # pose = Pose()
            # pose.position = Point(0.1, 0, 0)
            # pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))

            # smach.StateMachine.add(
            #     'STOP_THE_ROBOT',
            #     MoveActionState("/base_link", pose=pose),
            #     transitions={'succeeded': aborted, aborted: aborted})


def child_term_cb(outcome_map):
    # terminate both state machines
    if (outcome_map['FOLLLOW_CHECKER'] == aborted and outcome_map['MOVE_TO_EXIT'] != succeeded):
        print "Person Lost"
        # class UserdataHacked():
        #     def __init__(self):
        #         self.room_name = "Something"
        # print "Userdata hacked"
        StopGoal = Pose()
        StopGoal.position.x = 0.1
        StopGoal.position.y = 0
        StopGoal.position.z = 0
        StopGoal.orientation.x = 0
        StopGoal.orientation.y = 0
        StopGoal.orientation.z = 0
        StopGoal.orientation.w = 0
        print "goal prepared"
        goal = MoveActionState("/base_link", pose=StopGoal)
        print "After move action state"
        print str(goal)
        print outcome_map
        # return False
        return True

    if (outcome_map['MOVE_TO_EXIT'] == succeeded and outcome_map['FOLLLOW_CHECKER'] != aborted):
        print "Exit Reached without losing"
        return True

    return False


def out_cb(outcome_map):
    if outcome_map['FOLLLOW_CHECKER'] == aborted:
        print "Person lost"
        reached_to_exit = rospy.ServiceProxy('/followMeServer/stop', FollowMeStop)
        result = reached_to_exit()
        return aborted
    if outcome_map['MOVE_TO_EXIT'] == succeeded:
        print "Arrived to exit"
        reached_to_exit = rospy.ServiceProxy('/followMeServer/stop', FollowMeStop)
        result = reached_to_exit()
        return succeeded


class GoExitAndFollowChecker(smach.Concurrence):
    def __init__(self):
        smach.Concurrence.__init__(
            self,
            outcomes=[succeeded, preempted, aborted],
            default_outcome=aborted,
            input_keys=['room_name'],
            child_termination_cb=child_term_cb,
            outcome_cb=out_cb)
            # outcome_map={succeeded: {'MOVE_TO_EXIT': succeeded, 'FOLLLOW_CHECKER':aborted},
            # aborted: {'FOLLLOW_CHECKER': aborted, 'MOVE_TO_EXIT': None}})

        with self:

            smach.Concurrence.add(
                'FOLLLOW_CHECKER',
                FollowChecker())

            smach.Concurrence.add(
                'MOVE_TO_EXIT',
                MoveToRoomStateMachine(),
                remapping={'room_name': 'room_name'})
