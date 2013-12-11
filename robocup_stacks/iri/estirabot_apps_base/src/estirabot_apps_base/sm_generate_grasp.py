#!/usr/bin/env python

import roslib; roslib.load_manifest('estirabot_apps_base')
import rospy
import smach
import smach_ros

from pprint import pprint
from std_msgs.msg import Int8
from geometry_msgs.msg                    import Transform, PoseStamped, Pose
from estirabot_msgs.msg                   import PomdpGraspConfig
from iri_common_smach.transform_manager   import TransformManager
from iri_common_smach.homogeneous_product import homogeneous_product_pose_transform
from estirabot_apps_base.pickup           import build_simple_pickup_goal

# DEPRECATED: do not use this code outside this app
# Should be migrated to iri_wam_smach st_get_joints_from_pose
from iri_wam_common_msgs.srv import wamInverseKinematics
def get_inverse_kinematics_from_pose(pose):
    handler = rospy.ServiceProxy('/estirabot/iri_wam_tcp_ik/get_wam_ik', wamInverseKinematics)
    response = handler(pose)

    if (response):
        return response.joints

    # Solution could not be found
    return NoKinematicSolutionException()

class CalculateGrasp(smach.State):
    """
    TODO: This state should be converted to use different smaller states
    """
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['success','fail','no_ik_solution','all_ik_fail'],
                           input_keys=['grasp_pose','pomdp_grasp_config'],
                          output_keys=['pomdp_grasp_config','grasp_goal'])
        self.tf_manager = TransformManager()

    def execute(self, userdata):
        # shorcuts
        pomdp_config  = userdata.pomdp_grasp_config
        grasp_pose_st = userdata.grasp_pose

        rospy.set_param('/estirabot/skills/grasp/fingers_configuration', pomdp_config.fingers_grasp_configs)

        # grasp_pose_st comes referecence to camera frame_id
        # we need to transform the message to wam base frame /wam_link0
        grasp_pose_st_wam = self.tf_manager.transform_pose('/wam_link0', grasp_pose_st)

        # Orientation is fixed so ignoring previous
        grasp_pose_st_wam.pose.orientation.x = 0
        grasp_pose_st_wam.pose.orientation.y = 0
        grasp_pose_st_wam.pose.orientation.z = 0
        grasp_pose_st_wam.pose.orientation.w = 1.0

        pprint("Grasp original")
        pub = rospy.Publisher('/debug/grasp/original', PoseStamped, None, False, True)
        pub.publish(grasp_pose_st_wam)

        # real grasp is build applying grasp modifier to grasp_pose
        current_modifier     = pomdp_config.approach_config.grasp_modifier_used
        pprint("Using grasp modifier number: " + str(current_modifier))
        real_grasp_st        = PoseStamped()
        real_grasp_st.header = grasp_pose_st_wam.header
        real_grasp_st.pose   = homogeneous_product_pose_transform(grasp_pose_st_wam.pose,
                                                          pomdp_config.approach_config.grasp_modifiers[current_modifier])
        if (real_grasp_st.pose.position.z < -0.282):
            real_grasp_st.pose.position.z = -0.282

        pprint("Grasp modifier applied")
        pub = rospy.Publisher('/debug/grasp/real', PoseStamped, None, False, True)
        pub.publish(real_grasp_st)

        # pre-grasp posture is relative to real_grasp pose
        pre_grasp_pose_st        = PoseStamped()
        pre_grasp_pose_st.header = grasp_pose_st_wam.header

        pre_grasp_pose_st.pose = homogeneous_product_pose_transform(real_grasp_st.pose,
                                                          pomdp_config.approach_config.pre_grasp_modifier)
        pprint("PRE-Grasp modifier applied")
        pub = rospy.Publisher('/debug/grasp/pre_grasp', PoseStamped, None, False, True)
        pub.publish(pre_grasp_pose_st)

        # GRASP is Kinematic compliant so save and log the final configuration
        pub_config = rospy.Publisher('/log/pomdp_config', PomdpGraspConfig, None, False, True)
        pub_config.publish(pomdp_config)

        # For both grasp and pre-grasp we need the inverse kinematics and get joinst positions
        try:
            joints_grasp     = get_inverse_kinematics_from_pose(real_grasp_st)
            joints_pre_grasp = get_inverse_kinematics_from_pose(pre_grasp_pose_st)

        #except NoKinematicSolutionException, e:
        except rospy.ServiceException, e:
            # Let's go to next grasp_modifier (if any)
            if (current_modifier < len(pomdp_config.approach_config.grasp_modifiers)-1):
                # Mark next configuration to use 
                pomdp_config.approach_config.grasp_modifier_used = pomdp_config.approach_config.grasp_modifier_used + 1
                pomdp_config.approach_config.pre_grasp_modifier
                return 'no_ik_solution'
            else:
                # all modifiers were tested and are not valid. Return error
                pub = rospy.Publisher('/log/number_of_clothes', Int8, None, False, True)
                pub.publish(0)
                rospy.logerr("Inverse Kinematics has no solution")
                return 'all_ik_fail'

        #     rospy.logerr("WamIK service failed")
        #           return 'fail'

        userdata.grasp_goal =  build_simple_pickup_goal(joints_grasp,
                                                        joints_pre_grasp,
                                                        pomdp_config.fingers_grasp_configs)
        return 'success'

class SM_ESTIRABOT_GenerateGraspMsg:
    def __init__(self):
        self.sm = smach.StateMachine(
                  outcomes=['success','fail','no_ik_solution','all_ik_fail'],
                input_keys=['grasp_pose','pomdp_grasp_config'],
               output_keys=['pomdp_grasp_config','grasp_goal'])

    def build_sm(self):
        with self.sm:
            smach.StateMachine.add('CALCULATE_GRASP', CalculateGrasp(),
                transitions = {'success'        : 'success',
                               'no_ik_solution' : 'no_ik_solution',
                               'fail'           : 'fail',
                               'all_ik_fail'    : 'all_ik_fail'},
                remapping   = {'grasp_pose'     : 'grasp_pose',
                               'grasp_goal'     : 'grasp_goal'})

        return self.sm;
