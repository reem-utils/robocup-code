#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
from smach_ros import ServiceState

#try:
    # FIXME
 #   from pal_interaction_msgs.srv import pal_navigation_sm
#except ImportError:
#    from pal_interaction_msgs.msg import asrupdate
#    from pal_interaction_msgs.srv import recognizerService

from pal_smach_utils.utils.global_common import *

from pal_navigation_msgs.srv import *
from pal_navigation_msgs.msg import NavigationStatus
from pal_smach_utils.speech.listen_general_command import PrintUserData
from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_smach_utils.speech.sound_action import SpeakActionState


# Constants
NAVIGATION_ACTION_NAME = 'pal_navigation_sm'


class ChangeNavigationMode(smach.StateMachine):

    def __init__(self, nav_mode):
        """
        Changes the navigation mode of the robot. See NavigationState.

        This may take a while.
        """

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted])

        with self:

            smach.StateMachine.add('ANNOUNCING_STATUS_CHANGE',
                                SpeakActionState('Changing navigation mode to ' + nav_mode),
                                transitions = {succeeded: 'CHANGE_STATE'})

            def navigationmode_cb(userdata,request):
                update = AcknowledgmentRequest()
                rospy.loginfo("$$$ UPDATE = %s"%str(update))
                rospy.loginfo("$$$ NAVE_MODE = %s"%nav_mode)
                update.input = nav_mode
                return update

            smach.StateMachine.add( 'CHANGE_STATE', 
                                    ServiceState('pal_navigation_sm',Acknowledgment,request_cb = navigationmode_cb ),
                                    transitions =  {succeeded: 'READ_NAV_STATE', aborted:aborted})
            

            smach.StateMachine.add('READ_NAV_STATE',TopicReaderState(
                                topic_name='/pal_navigation_sm/state',
                                msg_type= NavigationStatus,
                                timeout=3),
                                transitions={succeeded:'PRINT_NAV_MESSAGE',aborted:aborted},
                                remapping = {'message':'nave_state_read' })

            smach.StateMachine.add( 'PRINT_NAV_MESSAGE',
                                    PrintUserData(),
                                    transitions = { succeeded:succeeded,
                                                    preempted:preempted},
                                    remapping = {'userSaidData':'nave_state_read'} )            

# vim: expandtab ts=4 sw=4
