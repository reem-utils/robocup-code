import roslib; roslib.load_manifest('iri_wam_smach')
import rospy
import smach
import smach_ros

from st_get_joints_from_pose import GetJointsFromPose
from st_wam_move_in_joints   import MoveWamInJoints

class SM_WAM_MoveFromPose():
    """
    State machine to move the WAM given a pose.

    It is composed by two steps:
             1. Use inverse kinematics to convert pose to joints
             2. Call to the move action using the joints

    @type  move_service : str
    @param move_service : URI of move in joinst wam service
    @type  ik_service   : str
    @param ik_service   : URI of inverse kinematic service
    @type  pose_st      : PoseStamped [input_key]
    @param pose_st      : Pose to move the 
    """

    def __init__(self, move_service, ik_service = None):
        self.sm = smach.StateMachine(outcomes=['success','aborted','no_kinematic_solution'],
                                     input_keys=['pose_st'])
        self.ik_service   = ik_service
        self.move_service = move_service

        if (self.ik_service == None):
            rospy.logfatal("No IK service provided to SM_WAM_MoveFromPose()")

    def build_sm(self):
        with self.sm:
           smach.StateMachine.add('POSE_TO_JOINTS', GetJointsFromPose(self.ik_service),
                transitions = {'success'               : 'MOVE_IN_JOINTS',
                               'empty'                 : 'success', # This handle empty pose requests
                               'no_kinematic_solution' : 'no_kinematic_solution'},
                remapping   = {'pose_st' : 'pose_st',
                               'joints_to_position' : 'sm_joints'})

           smach.StateMachine.add('MOVE_IN_JOINTS', MoveWamInJoints(self.move_service),
                transitions = {'success' : 'success',
                               'fail'    : 'aborted'},
                remapping   = { 'joints_to_position' : 'sm_joints'})

        return self.sm
