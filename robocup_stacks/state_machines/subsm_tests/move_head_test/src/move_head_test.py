#! /usr/bin/env python

import roslib
roslib.load_manifest('move_head_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from smach import CBState

from pal_smach_utils.utils.colors import Colors

colors = Colors()

from pr2_controllers_msgs.msg import PointHeadGoal, PointHeadAction

import actionlib
from smach_ros import ServiceState, SimpleActionState
from std_srvs.srv import Empty

from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers


def main():
    rospy.init_node('sm_move_head_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        smach.StateMachine.add(
            "START_HEAD_CONTROLLERS",
            StartRobotControllers(head=True, left=False, right=False),
            transitions={succeeded: "BEGIN_MOVE_HEAD_TEST", aborted: "START_HEAD_CONTROLLERS", preempted: "START_HEAD_CONTROLLERS"})

        @smach.cb_interface(outcomes=[succeeded, "enableFaceTracking", "disableFaceTracking"])
        def showStartMessage(userdata):
            head_goal = PointHeadGoal()
            head_goal.target.header.frame_id = "base_link"
            rospy.loginfo("SPECIAL CODE: write e to enable the face tracking or d to disable it in the x coordinate")
            x = raw_input("X: ")
            if (x == 'e'):
                return 'enableFaceTracking'
            elif (x == 'd'):
                return 'disableFaceTracking'
            y = raw_input("Y: ")
            z = raw_input("Z: ")
            head_goal.target.point.x = float(x)
            head_goal.target.point.y = float(y)
            head_goal.target.point.z = float(z)
            head_goal.pointing_frame = "stereo_link"
            head_goal.pointing_axis.x = 1.0
            head_goal.pointing_axis.y = 0.0
            head_goal.pointing_axis.z = 0.0
            head_goal.max_velocity = 1.5
            head_goal.min_duration.secs = 1.5

            client = actionlib.SimpleActionClient("/head_traj_controller/point_head_action", PointHeadAction)
            client.wait_for_server(rospy.Duration(0.3))

            client.send_goal(head_goal)

            return succeeded

        smach.StateMachine.add('BEGIN_MOVE_HEAD_TEST',
                               CBState(showStartMessage),
                               transitions={succeeded: "BEGIN_MOVE_HEAD_TEST",
                                            'enableFaceTracking': "ENABLE_FACE_TRACKING",
                                            "disableFaceTracking": "DISABLE_FACE_TRACKING"})

        smach.StateMachine.add('DISABLE_FACE_TRACKING',
                               ServiceState('/personServer/faceTracking/stop', Empty),
                               transitions={succeeded: 'BEGIN_MOVE_HEAD_TEST'})

        smach.StateMachine.add('ENABLE_FACE_TRACKING',
                               ServiceState('/personServer/faceTracking/start', Empty),
                               transitions={succeeded: 'BEGIN_MOVE_HEAD_TEST'})

    sis = smach_ros.IntrospectionServer('move_head_test_sm', sm, '/MOVE_HEAD_TEST')
    sis.start()
    sm.execute()

    rospy.spin()
    rospy.loginfo(colors.BACKGROUND_GREEN + "MOVE HEAD TEST HAS BEEN STOPPED" + colors.NATIVE_COLOR)
    sis.stop()

if __name__ == '__main__':
    main()
