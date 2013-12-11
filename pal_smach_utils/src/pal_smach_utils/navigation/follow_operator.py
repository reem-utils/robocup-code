#! /usr/bin/env python
# vim: expandtab ts=4 sw=4
### FOLOW_OPERATOR.PY ###

import rospy
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from pal_smach_utils.navigation.track_operator import TrackOperator

from pal_smach_utils.navigation.track_operator import LearnPerson

from pal_navigation_msgs.srv import DisableEmergency, DisableEmergencyRequest
from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction

from smach_ros import ServiceState, SimpleActionState

from std_srvs.srv import Empty

import os
from roslib import packages
ros_master_uri = os.environ.get('ROS_MASTER_URI')
remotelly_executing = ros_master_uri.rfind('localhost')
MOTION_FOLDER_PATH = packages.get_pkg_dir('pal_smach_utils') + '/config/interact_1.xml'
if remotelly_executing == -1:
    MOTION_FOLDER_PATH = "/mnt_flash/robocup2013/reem_at_iri/state_machines/common/config/interact_1.xml"

inside_robot = False
robot = os.environ.get('PAL_ROBOT')
if robot == 'rh2c' or robot == 'rh2m' or robot == 'reemh3c' or robot == 'reemh3m' or robot == 'reemh3':
    inside_robot = True


from pr2_controllers_msgs.msg import PointHeadGoal, PointHeadAction

from actionlib import SimpleActionClient

from smach import CBState

from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers


class FollowOperator(smach.StateMachine):
    #Its an infinite loop track_Operator

    def __init__(self, distToHuman=0.9):
        smach.StateMachine.__init__(
            self,
            outcomes=[succeeded, preempted, aborted],
            input_keys=["in_learn_person"])

        with self:

            if remotelly_executing == -1 or inside_robot:
                '''def disable_cb(userdata, request):
                    disableEmerg = DisableEmergencyRequest()
                    disableEmerg.second = 600
                    disableEmerg.useLEDs = True
                    return disableEmerg

                smach.StateMachine.add('DISABLE_EMERGENCY_STOP',
                                       ServiceState('/disable_emergency_stop',
                                                    DisableEmergency,
                                                    request_cb=disable_cb),
                                       transitions={succeeded: 'DISABLE_REEM_ALIVE'})

                smach.StateMachine.add('DISABLE_REEM_ALIVE',
                                       ServiceState('/alive_engine/stop', Empty),
                                       transitions={succeeded: 'DISABLE_FACE_TRACKING'})'''

                smach.StateMachine.add('DISABLE_FACE_TRACKING',
                                       ServiceState('/personServer/faceTracking/stop', Empty),
                                       transitions={succeeded: 'START_HEAD_CONTROLLERS'})

                smach.StateMachine.add(
                    "START_HEAD_CONTROLLERS",
                    StartRobotControllers(head=True, left=False, right=False),
                    transitions={succeeded: "CROSSING_DOOR_POS", aborted: "START_HEAD_CONTROLLERS", preempted: "START_HEAD_CONTROLLERS"})

                motion_goal = MotionManagerGoal()
                motion_goal.plan = False
                motion_goal.filename = MOTION_FOLDER_PATH
                motion_goal.checkSafety = False
                motion_goal.repeat = False

                smach.StateMachine.add('CROSSING_DOOR_POS',
                                       SimpleActionState('/motion_manager', MotionManagerAction, goal=motion_goal),
                                       transitions={succeeded: 'FIX_HEAD_POSITION',
                                                    aborted: 'FIX_HEAD_POSITION'})

            @smach.cb_interface(outcomes=[succeeded, preempted, aborted])
            def fixHeadPosition(userdata):
                head_goal = PointHeadGoal()
                head_goal.target.header.frame_id = "base_link"
                head_goal.target.point.x = 1.0
                head_goal.target.point.y = 0.0
                head_goal.target.point.z = 1.65
                head_goal.pointing_frame = "stereo_link"
                head_goal.pointing_axis.x = 1.0
                head_goal.pointing_axis.y = 0.0
                head_goal.pointing_axis.z = 0.0
                head_goal.max_velocity = 1.5
                head_goal.min_duration.secs = 1.5

                client = SimpleActionClient("/head_traj_controller/point_head_action", PointHeadAction)
                client.wait_for_server(rospy.Duration(5.0))

                client.send_goal(head_goal)

                return succeeded

            smach.StateMachine.add('FIX_HEAD_POSITION',
                                   CBState(fixHeadPosition),
                                   transitions={succeeded: "LEARN_PERSON",
                                                preempted: "LEARN_PERSON",
                                                aborted: "LEARN_PERSON"})

            smach.StateMachine.add('LEARN_PERSON',
                                   LearnPerson(),
                                   transitions={succeeded: 'TRACK_OPERATOR',
                                                aborted: aborted},
                                   remapping={'out_personTrackingData': 'out_personTrackingData',
                                              "in_learn_person": "in_learn_person"})

            smach.StateMachine.add('TRACK_OPERATOR',
                                   TrackOperator(distToHuman),
                                   remapping={'in_personTrackingData': 'out_personTrackingData'},
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted})
