import roslib
import rospy
import smach
import smach_ros
import actionlib
from smach_ros import SimpleActionState, ServiceState

from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.navigation.move_action import MoveActionState

try:
    from pr_msgs.msg import ObjectPoseList, ObjectPose
    from pr_msgs.srv import *
    from iri_moped_handler.srv import *
except ImportError:
    from pr_msgs.msg import ObjectPoseList, ObjectPose
    from object_recognition_mock.srv import *

from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

# Temporary file for use until sm_search_obj.py is finished!

class SearchObjectStateMachine(smach.StateMachine):

    def __init__(self):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
        output_keys=['object_data'])

        with self:

            pose = Pose()
            pose.position = Point(0, 0, 0)
            pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 45))
            
            smach.StateMachine.add(
                'N2_go_to_dep_policy',
                MoveActionState("/base_link", pose=pose),
                transitions = {succeeded: 'look_for_objects'})

            def moped_enable_cb(userdata, response):
                if response.correct != None:
                    rospy.loginfo("ENABLE_CLOSE_OBJECT_SEARCH response: " + \
                                  str(response.correct))
                    return succeeded
                else:
                    return aborted
                      
            smach.StateMachine.add(
            'ENABLE_CLOSE_OBJECT_SEARCH',
            ServiceState('/iri_moped_handler/enable', enable,
            response_cb = moped_enable_cb,
            #request_key = 'object_name',
            request = True),
            transitions = {succeeded:'look_for_objects'})

            # FIXME: why is there a smaller ctimeout & retry on aborted?
            # If something goes wrong it'd rather have it fail than having
            # it keep hanging on forever... --Siegfried
            smach.StateMachine.add(
                'look_for_objects',
                TopicReaderState(
                    topic_name='/iri_moped_handler/outputOPL',
                    msg_type=ObjectPoseList,
                    timeout=10),
                remapping= {'message' : 'object_data'},
                transitions = {succeeded: 'DISABLE_CLOSE_OBJECT_SEARCH', aborted: 'look_for_objects'})

            def moped_disable_cb(userdata, response):
                if response.correct != None:
                    rospy.loginfo("DISABLE_CLOSE_OBJECT_SEARCH response: " + \
                                  str(response.correct))
                    return succeeded
                else:
                    return aborted

            smach.StateMachine.add(
                'DISABLE_CLOSE_OBJECT_SEARCH',
                ServiceState('/iri_moped_handler/enable', enable,
                    response_cb = moped_disable_cb,
                    #request_key = 'object_name',
                    request = False),
                transitions = {succeeded: succeeded})

# vim: expandtab ts=4 sw=4
