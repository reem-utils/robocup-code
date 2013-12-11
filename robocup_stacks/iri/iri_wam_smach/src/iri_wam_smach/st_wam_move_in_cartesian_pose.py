import roslib; roslib.load_manifest('iri_wam_smach')
import rospy
import smach
import smach_ros

from iri_wam_common_msgs.srv import pose_move

class MoveWamInCartesianPose(smach.State):
    """
    Move WAM given a cartesian pose (no planning or obstacle avoidance)
    It will use the cartesian move by torque implemented by libbarrett since 1.1.0

    @type move_service : str
    @param move_service : URI of move in joinst wam service
    @type velocity: int
    @param velocity: velocity for movement (not implemented yet)
    @type acc: int
    @acc: acceleration for movement (not implemented yet)
    """
    def __init__(self, move_service, velocity = 0, acc = 0):
        smach.State.__init__(self, outcomes    = ['success','fail'],
                                   input_keys  = ['pose'])
        self.move_service = move_service
        self.velocity = velocity
        self.acc = acc 

    def execute(self, userdata):
        try:
            handler = rospy.ServiceProxy(self.move_service, pose_move)
            response = handler(userdata.pose, self.velocity, self.acc)

        except rospy.ServiceException, e:
            return 'fail'

        return 'success'
