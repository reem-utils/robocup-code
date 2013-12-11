import roslib; roslib.load_manifest('iri_wam_smach')
import rospy
import smach
import smach_ros
import numpy

from st_wam_move_in_cartesian_pose import MoveWamInCartesianPose
from iri_common_smach.st_get_pose_from_frames import GetPoseStampedFromFrames
from iri_common_smach.homogeneous_product import *
from pprint import pprint
from tf.transformations import *

def pose_st_from_matrix(matrix, frame_id):
    """ Returns geometry_msgs.msg.Pose() from transformation.matrix

    """
    quaternion = quaternion_from_matrix(matrix)
    position = translation_from_matrix(matrix)

    pose_st = PoseStamped() 
    pose_st.header.frame_id = frame_id 
    pose_st.header.stamp    = rospy.Time()
    pose_st.pose.position.x = position[0]
    pose_st.pose.position.y = position[1] 
    pose_st.pose.position.z = position[2] 
    pose_st.pose.orientation.x = quaternion[0] 
    pose_st.pose.orientation.y = quaternion[1] 
    pose_st.pose.orientation.z = quaternion[2] 
    pose_st.pose.orientation.w = quaternion[3]

    return pose_st


class WAMGetTcpPose(smach.State):
    """
         
    """
    def __init__(self):
        smach.State.__init__(self, outcomes = ['success'],
                                   input_keys = ['pose_st', 'tool_to_tcp_pose'],
                                   output_keys = ['tcp_pose'])

    def execute(self, userdata):
        
        T1 = translation_matrix((userdata.tool_to_tcp_pose.pose.position.x,
                                 userdata.tool_to_tcp_pose.pose.position.y,
                                 userdata.tool_to_tcp_pose.pose.position.z))
        R1 = quaternion_matrix((userdata.tool_to_tcp_pose.pose.orientation.x,
                                userdata.tool_to_tcp_pose.pose.orientation.y,
                                userdata.tool_to_tcp_pose.pose.orientation.z,
                                userdata.tool_to_tcp_pose.pose.orientation.w))
        H1 = concatenate_matrices(T1,R1)

        T2 = translation_matrix((userdata.pose_st.pose.position.x,
                                 userdata.pose_st.pose.position.y,
                                 userdata.pose_st.pose.position.z))
        R2 = quaternion_matrix((userdata.pose_st.pose.orientation.x,
                                userdata.pose_st.pose.orientation.y,
                                userdata.pose_st.pose.orientation.z,
                                userdata.pose_st.pose.orientation.w))
        H2 = concatenate_matrices(T2,R2)
        
        H3 = concatenate_matrices(H2,H1)

        pose = pose_st_from_matrix(H3, userdata.pose_st.header.frame_id) 

        pprint("HOMOGENOUS PRODUCT") 
        pprint(pose.pose)
        userdata.tcp_pose = pose.pose

        return 'success'



class SM_WAM_MoveFromCartesianPose():
    """
    State machine to move the WAM given a cartesian pose.

    It is composed by two steps:
             1. Transform cartesian pose to /wam_tcp 
             2. Call to the move action using the correct cartesian pose

    @type  move_service : str
    @param move_service : URI of move in joinst wam service
    @type  ik_service   : str
    @param ik_service   : URI of inverse kinematic service
    @type  pose_st      : PoseStamped [input_key]
    @param pose_st      : Pose to move the 
    """

    def __init__(self, move_service, tool_frame):
        self.move_service = move_service
        self.tool_frame   = tool_frame
        
    def build_sm(self,tf_listener):
        sm = smach.StateMachine(outcomes=['success','aborted','no_kinematic_solution'],
                                     input_keys=['pose_st'])

        sm.userdata.tcp_frame  = 'wam_tcp'
        sm.userdata.tool_frame = self.tool_frame
        with sm:

           smach.StateMachine.add('GET_POSE_FROM_FRAMES', GetPoseStampedFromFrames(tf_listener),
                transitions = {'success' : 'GET_TCP_POSE',
                               'fail'    : 'aborted'},
                remapping   = { 'src_frame' : 'tool_frame',
                                'dest_frame' : 'tcp_frame',
                                'pose_st'   : 'sm_pose_st'})

           smach.StateMachine.add('GET_TCP_POSE', WAMGetTcpPose(),
                transitions = {'success'   : 'MOVE_IN_CARTESIAN'},
                remapping   = { 'pose_st'          : 'pose_st',
                                'tool_to_tcp_pose' : 'sm_pose_st',
                                'tcp_pose'         : 'sm_tcp_pose'})

           smach.StateMachine.add('MOVE_IN_CARTESIAN', MoveWamInCartesianPose(self.move_service, 0.2, 0.3),
                transitions = {'success' : 'success',
                               'fail'    : 'aborted'},
                remapping   = {'pose' : 'sm_tcp_pose'})

        return sm
