import roslib; roslib.load_manifest('iri_wam_smach')
import rospy
import smach
import smach_ros

from iri_wam_common_msgs.srv import wamdriver
from pprint                  import pprint

class WamHold(smach.State):
    """
    HOLDON or HOLDOFF WAM ARM 
   
    @type  hold_service: string
    @param hold_service: URI of wam_wrapper hold service
    @type  call   : integer [input_key]
    @param call   : 0 -> hold ON, 1 -> hold OFF

    """
    def __init__(self, hold_service):
        smach.State.__init__(self,
                             outcomes    = ['success', 'fail'],
                             input_keys  = ['call'],
                             output_keys = [])

        self.hold_service = hold_service
        
    def execute(self, userdata):
        if (userdata.call == None):
            rospy.logwarn("Empty call received. 0 -> hold ON, 1 -> hold OFF")
            return 'fail'
        
        try:
            handler = rospy.ServiceProxy(self.hold_service, wamdriver)
            response = handler(userdata.call)

            if (response):
                pprint(response.success)

        except rospy.ServiceException, e:
            return 'fail'

        return 'success'
