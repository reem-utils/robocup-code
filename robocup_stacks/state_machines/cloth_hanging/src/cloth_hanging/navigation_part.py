#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib; roslib.load_manifest('cloth_hanging')
import rospy
import smach
import smach_ros

from smach_ros import SimpleActionState
from geometry_msgs.msg import Pose, Quaternion

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

# generic libraries
import roslib.packages

from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.navigation.move_action import MoveActionState
from tf.transformations import quaternion_from_euler
from pal_smach_utils.speech.sound_action import SpeakActionState

from cloth_hanging.approach_hanger import SMClothHangingApproachHangerPartStateMachine


# TODO add to map
HANGER_NAME = "hanger_d"


class SMClothHangingNavigationPartStateMachine(smach.StateMachine):
    """
    The robot navigates to the hanger.

    Required parameters:
    No parameters

    Optional parameters:
    No optional parameters.

    No imput keys.
    No output keys.
    No io_keys.

    """
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])
        
        with self:
            intro_text = "Good!, I will take it to the hanger."
            smach.StateMachine.add('INTRO',
                                   SpeakActionState(intro_text),
                                   transitions={succeeded: 'MOVE_TO_HANGER'})
            
            # move to hanger
            self.userdata.hanger = HANGER_NAME
            smach.StateMachine.add('MOVE_TO_HANGER',
                                  MoveToRoomStateMachine(announcement=None),
                                  transitions={succeeded: 'APPROACH_TO_HANGER',
                                               preempted: preempted,
                                               aborted: 'MOVE_TO_HANGER'},
                                  remapping={'room_name': 'hanger'})

            # Rotate 180º
            pose_turn = Pose()
            pose_turn.orientation = Quaternion(*quaternion_from_euler(0,0,3.6))
            #smach.StateMachine.add('MOVE_TO_HANGER',
                                   #MoveActionState(move_base_action_name='/move_by/move_base',pose=pose_turn),
                                   #transitions={succeeded: 'APPROACH_TO_HANGER',
                                                #preempted: preempted,
                                                #aborted: 'MOVE_TO_HANGER'},
                                   #remapping={'room_name': 'hanger'})
                                   
            smach.StateMachine.add('APPROACH_TO_HANGER',
                                   SMClothHangingApproachHangerPartStateMachine(),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted})





