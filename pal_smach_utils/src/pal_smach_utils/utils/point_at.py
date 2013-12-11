#!/usr/bin/env python

import roslib
roslib.load_manifest('pal_smach_utils')
import os
import smach

from smach_ros import SimpleActionState
import roslib.packages


from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction
from pal_smach_utils.grasping.st_reem_hand import OpenReemHand2
from pal_smach_utils.speech.sound_action import SpeakActionState


ros_master_uri = os.environ.get('ROS_MASTER_URI')
remotelly_executing = (ros_master_uri.rfind('localhost') == -1)
MOTION_FOLDER_PATH = ''

if remotelly_executing:
    MOTION_FOLDER_PATH = "/mnt_flash/robocup2013/reem_at_iri/state_machines/common/src/utils/"
else:
    MOTION_FOLDER_PATH = roslib.packages.get_pkg_dir('pal_smach_utils') + '/src/utils/'

class SMPointInFront(smach.StateMachine):
    """
    Point in fornt

    """
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:

            # move arm to point position
            filename = MOTION_FOLDER_PATH + "point_at.xml"
            point_at_motion_goal = MotionManagerGoal()
            point_at_motion_goal.plan = False
            point_at_motion_goal.filename = filename
            point_at_motion_goal.checkSafety = False
            point_at_motion_goal.repeat = False
            point_at_motion_action = SimpleActionState('/motion_manager', MotionManagerAction,
                                           goal=point_at_motion_goal)
            smach.StateMachine.add('POINT', point_at_motion_action,
                                   transitions={succeeded: 'OPEN_HAND',
                                                preempted: preempted,
                                                aborted: aborted})

            # open
            smach.StateMachine.add(
                    'OPEN_HAND',
                    OpenReemHand2(),
                    transitions={succeeded: 'TELL_HERE', preempted: preempted, aborted: aborted})

            #Tell pointed
            smach.StateMachine.add('TELL_HERE',
                                   SpeakActionState(text="Here it is"),
                                   transitions={succeeded: 'MOVE_TO_FINISH_POSE',
                                                preempted: preempted,
                                                aborted: aborted})

            #move arm home
            filename = MOTION_FOLDER_PATH + "final_pose_point_at.xml"
            finish_motion_goal = MotionManagerGoal()
            finish_motion_goal.plan = False
            finish_motion_goal.filename = filename
            finish_motion_goal.checkSafety = False
            finish_motion_goal.repeat = False
            finish_motion_action = SimpleActionState('/motion_manager', MotionManagerAction,
                                           goal=finish_motion_goal)
            smach.StateMachine.add('MOVE_TO_FINISH_POSE', finish_motion_action,
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted})





