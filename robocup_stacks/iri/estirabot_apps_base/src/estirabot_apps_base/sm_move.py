#!/usr/bin/env python

import roslib; roslib.load_manifest('estirabot_apps')
import rospy
import smach
import smach_ros

from smach import CBState
from iri_common_smach.utils_msg          import build_pose_stamped_msg
from iri_wam_smach.sm_wam_move_from_pose import SM_WAM_MoveFromPose

class SM_ESTIRABOT_GoHome():
    """
    """
    def __init__(self):
        self.sm = smach.StateMachine(outcomes=['success','aborted'])

    @smach.cb_interface(input_keys = [],
                        output_keys= ['pose_st'],
                        outcomes   = ['finish'])
    def home_pose_cb(ud):
#ud.pose_st = build_pose_stamped_msg('/wam_link0',0.5, 0, 0.13, 0.0, 1.0, 0.0, 0.0)
        ud.pose_st = build_pose_stamped_msg('/wam_link0',0.5, 0, 0, 0.0, 1.0, 0.0, 0.0)

        return 'finish'

    def build_sm(self):
        f_move = SM_WAM_MoveFromPose('/estirabot/wam_wrapper/joints_move',
                                      '/estirabot/iri_wam_tcp_ik/get_wam_ik')
        sm_move = f_move.build_sm()

        with self.sm:
            smach.StateMachine.add('DEFINE_HOME_POSE', CBState(self.home_pose_cb),
                              transitions  = {'finish'  : 'MOVE_TO_HOME'},
                              remapping    = {'pose_st' : 'sm_pose_st'})

            smach.StateMachine.add('MOVE_TO_HOME', sm_move,
                              transitions  = {'success'  : 'success',
                                              'aborted'  : 'aborted',
                                              'no_kinematic_solution' : 'aborted'},
                              remapping    = {'pose_st' : 'sm_pose_st'})
        return self.sm
