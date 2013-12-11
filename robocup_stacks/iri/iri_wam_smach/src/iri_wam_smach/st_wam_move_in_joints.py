import roslib; roslib.load_manifest('iri_wam_smach')
import rospy
import smach
import smach_ros

from iri_wam_common_msgs.srv import joints_move

class MoveWamInJoints(smach.State):
    """
    Move WAM given specific joints (no planning or obstacle avoidance)

    @type move_service : str
    @param move_service : URI of move in joinst wam service
    """
    def __init__(self, move_service):
        smach.State.__init__(self,
                             outcomes    = ['success','fail'],
                             input_keys  = ['joints_to_position'],
                             output_keys = [])

        self.move_service = move_service

    def execute(self, userdata):
        
        try:
            handler = rospy.ServiceProxy(self.move_service, joints_move)
            response = handler(userdata.joints_to_position.position, [], [])

        except rospy.ServiceException, e:
            return 'fail'

        return 'success'
