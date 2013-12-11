import roslib; roslib.load_manifest('iri_wam_smach')
import rospy
import smach
import smach_ros

from iri_wam_common_msgs.srv import wamInverseKinematics

class GetJointsFromPose(smach.State):
    """
    Obtain joints positions from a given pose

    Use inverse kinematic to get corresponding joints positions from a 
    cartesian pose.

    @type  ik_service: string
    @param ik_service: URI of inverse kinematic service
    @type  pose_st   : PoseStamped [input_key]
    @param pose_st   : Pose to move the

    @rtype           : sensor_msgs/JointState
    @return          : joints_to_position [output_key]
    """
    def __init__(self, ik_service):
        smach.State.__init__(self,
                             outcomes    = ['success','empty','no_kinematic_solution'],
                             input_keys  = ['pose_st'],
                             output_keys = ['joints_to_position'])

        self.ik_service = ik_service
    def execute(self, userdata):
        if (userdata.pose_st == None):
            rospy.logwarn("Empty pose received. No movement needed")
            return 'empty'

        try:
          handler = rospy.ServiceProxy(self.ik_service, wamInverseKinematics)
          response = handler(userdata.pose_st)
          print response
          if response:
              userdata.joints_to_position = response.joints

        except rospy.ServiceException, e:
              return 'no_kinematic_solution'

        return 'success'

