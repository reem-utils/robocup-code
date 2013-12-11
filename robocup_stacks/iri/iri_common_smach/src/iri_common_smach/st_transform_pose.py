import roslib; roslib.load_manifest('iri_common_smach')
import rospy
import smach
import smach_ros
from transform_manager import TransformManager

"""
TODO: implement TransformPose which can be based on code reem_at_iri -> global_common
      which recieve a pose, src_frame, target_frame.
      Create a base class for both to share same code.
"""

class TransformPoseStamped(smach.State):
    """
    Use the tf to convert from input_key 'pose_st' (PoseStamped) to 'target_frame'
    """
    def __init__(self):
        smach.State.__init__(self, outcomes    = ['success','fail'],
                                   input_keys  = ['pose_st','target_frame'],
                                   output_keys = ['transformed_pose_st'])
        self.tf_manager = TransformManager()

    def execute(self, userdata):
        tf_pose_st = self.tf_manager.transform_pose(userdata.target_frame, userdata.pose_st)
        userdata.transformed_pose_st = tf_pose_st
        return 'success'
