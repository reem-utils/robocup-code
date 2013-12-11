#!/usr/bin/env python

import roslib; roslib.load_manifest('estirabot_apps_base')
import rospy
import smach
import smach_ros

from pprint import pprint
from iri_common_smach.utils_msg import build_pose_stamped_msg, build_transform_msg
from estirabot_msgs.msg         import PomdpGraspConfig

class PomdpConfigFactory():
    def __init__(self):
        self.config               = PomdpGraspConfig()
        self.config.place_point   = build_pose_stamped_msg('/wam_link0',0.5, 0, 0.33, 0.0, 1.0, 0.0, 0.0)

        self.config.grabbing_zone = self.config.BOTH_ZONES
        # pre-grasp is relative to real_grasp and do not change
        self.config.approach_config.pre_grasp_modifier = build_transform_msg(0, 0, -0.1, 0, 0, 0, 1)
        self.config.approach_config.grasp_modifier_used = 0
        # always use GSO at the begging of grasp
        self.config.fingers_grasp_configs.append("GSTO")

    def get_instance(self, magic_number):

        if (magic_number > 999) or (magic_number < 0):
            rospy.logfatal("Pomdp magic number is out of ranges")

        alg_id      = magic_number / 100
        approach_id = (magic_number - (100 * alg_id)) / 10
        grasp_id    = (magic_number - (100 * alg_id) - (10 * approach_id))

        if (alg_id == 0):
            self.config.best_pose_algorithm_id = self.config.MAX_HEIGHT_ALG
        elif (alg_id == 1):
            self.config.best_pose_algorithm_id = self.config.MAX_WRINKLE_ALG
        elif (alg_id == 2):
            self.config.best_pose_algorithm_id = self.config.FUSION_ALG
        else:
            rospy.logfatal("Magic number alg_is it out of range")

        if (approach_id == self.config.APPROACH_TOP_DEEP):
            self.config.approach_config.grasp_modifiers.append(build_transform_msg(0, 0, -0.03, 1, 0, 0, 0))
        elif (approach_id == self.config.APPROACH_TOP_SURFACE):
            self.config.approach_config.grasp_modifiers.append(build_transform_msg(0, 0, 0.05, 1, 0, 0, 0))
        elif (approach_id == self.config.APPROACH_SIDE_DEEP):
            self.config.approach_config.grasp_modifiers.append(build_transform_msg(0.03, 0, 0, 0, 0.7071, 0, 0.7071))
            self.config.approach_config.grasp_modifiers.append(build_transform_msg(0, 0.03, 0, -0.5, 0.5, 0.5, 0.5))
            self.config.approach_config.grasp_modifiers.append(build_transform_msg(-0.03, 0, 0, -0.7071, 0, 0.7071,0))
            self.config.approach_config.grasp_modifiers.append(build_transform_msg(0, -0.03, 0, 0.5, 0.5, -0.5, 0.5))
        elif (approach_id == self.config.APPROACH_SIDE_SURFACE):
            self.config.approach_config.grasp_modifiers.append(build_transform_msg(-0.05, 0, 0, 0, 0.7071, 0, 0.7071))
            self.config.approach_config.grasp_modifiers.append(build_transform_msg(0, -0.05, 0, -0.5, 0.5, 0.5, 0.5))
            self.config.approach_config.grasp_modifiers.append(build_transform_msg(0.05, 0, 0, 0, -0.7071, 0, 0.7071))
            self.config.approach_config.grasp_modifiers.append(build_transform_msg(0, 0.05, 0, 0.5, 0.5, -0.5, 0.5))
        else:
            rospy.logfatal("Magic number approach is out of range")

        if (grasp_id == 0):
            pass
        elif (grasp_id == 1):
            self.config.fingers_grasp_configs.append("GM 7000")
            self.config.fingers_grasp_configs.append("GTC")
        elif (grasp_id == 2):
            self.config.fingers_grasp_configs.append("GM 10000")
            self.config.fingers_grasp_configs.append("GTC")
        elif (grasp_id == 3):
            self.config.fingers_grasp_configs.append("SM 500")
            self.config.fingers_grasp_configs.append("GTC")
        elif (grasp_id == 4):
            self.config.fingers_grasp_configs.append("SM 500")
            self.config.fingers_grasp_configs.append("GM 7000")
            self.config.fingers_grasp_configs.append("GTC")
        elif (grasp_id == 5):
            self.config.fingers_grasp_configs.append("STC")
            self.config.fingers_grasp_configs.append("GTC")
        elif (grasp_id == 6):
            self.config.fingers_grasp_configs.append("SM 1500")
            self.config.fingers_grasp_configs.append("3TC")
            self.config.fingers_grasp_configs.append("GTC")

        else:
            rospy.logfatal("Magic number grasp is out of range")

        #closing grasp config
        #self.config.fingers_grasp_configs.append("GTC")
        return self.config

def get_config_from_pomdp_action(pomdp_action):
    """
    Translate a pomdp_action number into a PomdpConfig object
    """

    if (pomdp_action > 21):
        rospy.logfatal("Pomdp action id out of range: " + str(pomdp_action))

    server = PomdpConfigFactory()

    if  (pomdp_action == 20):
        magic_number = 114
    elif (pomdp_action == 21):
        magic_number = 114
    elif (pomdp_action % 10 == 0):
        magic_number = 1
    elif (pomdp_action % 10 == 1):
        magic_number = 3
    elif (pomdp_action % 10 == 2):
        magic_number = 5
    elif (pomdp_action % 10 == 3):
        magic_number = 11
    elif (pomdp_action % 10 == 4):
        magic_number = 14
    elif (pomdp_action % 10 == 5):
        magic_number = 101
    elif (pomdp_action % 10 == 6):
        magic_number = 103
    elif (pomdp_action % 10 == 7):
        magic_number = 105
    elif (pomdp_action % 10 == 8):
        magic_number = 111
    elif (pomdp_action % 10 == 9):
        magic_number = 114

    # From magic number get configuration
    config = server.get_instance(magic_number)

    config.actiontype = config.GRAB
    # Also set the grabbing zone
    if (pomdp_action == 20):
        config.grabbing_zone = config.RIGHT_ZONE
        config.actiontype = config.DROP
    elif (pomdp_action == 21):
        config.grabbing_zone = config.LEFT_ZONE
        config.actiontype = config.DROP
    elif (pomdp_action > 9):
        config.grabbing_zone = config.LEFT_ZONE
    else:
        config.grabbing_zone = config.RIGHT_ZONE

    # 20 and 21 should get an special value for place.
    # Hack for this is set place_point to None and check for it
    # in PlaceHandler. Dirty as hell.
    if (pomdp_action == 20) or (pomdp_action == 21):
        config.place_point = None

    return config

# Class moved to each smach app, since it is application-dependant 
class TranslatePomdp(smach.State):
    def __init__(self):
        pass
