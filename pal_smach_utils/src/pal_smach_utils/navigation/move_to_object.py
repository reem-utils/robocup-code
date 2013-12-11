import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import actionlib
from smach_ros import ServiceState

from tf.transformations import quaternion_from_euler

from geometry_msgs.msg import Pose, Point, Quaternion
from coord_translator.srv import ObjectTranslator, ObjectTranslatorRequest
from move_action import MoveActionState
from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.pose_at_distance import pose_at_distance
try:
    from pr_msgs.msg import ObjectPose
except ImportError:
    from pr_msgs.msg import ObjectPose

#Distance we want Reem to mantain from the position the object is. And if be enable it.
MANTAIN_DISTANCE_FROM_OBJECT = False
DISTANCE_FROM_OBJECT = 0.5


class MoveToObjectBelongingLocSM(smach.StateMachine):

    """
    The name of the target object is expected to be in a input key named `object_name'.
    """
    def __init__(self):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                                    input_keys=['object_name'], output_keys=['object_location', 'object_release_location'])

        with self:

            @smach.cb_interface(input_keys=['object_name'], output_keys=['object_location', 'object_release_location'])
            def obj_response_cb(userdata, response):
                if response.exists:
                    pose = Pose()
                    #Wont there be problems mixing float32 with 64? TODO
                    pose.position = Point(response.base_coordinates.x, response.base_coordinates.y, 0)
                    #TODO, this may give problems
                    pose.orientation = Quaternion(*quaternion_from_euler(0, 0, response.base_coordinates.z))
                    if MANTAIN_DISTANCE_FROM_OBJECT:
                        pose = pose_at_distance(pose, DISTANCE_FROM_OBJECT)
                    userdata.object_location = pose

                    release_pose = ObjectPose()
                    release_pose.pose = response.arm_coordinates
                    userdata.object_release_location = release_pose

                    print "\n\n printing pose for move to object"
                    print pose
                    print "\n\n printing pose for releasing the object"
                    print release_pose
                    print "\n that was the pose of the object\n\n"
                    print userdata.object_name
                    print "is the object name"
                    return succeeded
                else:
                    userdata.object_location = None
                    return aborted

            def obj_request_cb(userdata, request):
                req = ObjectTranslatorRequest()
                req.objname = userdata.object_name
                print "Asking coord_translator for " + req.objname
                return req
            #Although is an object, we only need now the position, like a location
            smach.StateMachine.add('TRANSLATE_OBJECT_NAME',
                                   ServiceState('object_translator', ObjectTranslator,
                                   response_cb=obj_response_cb,
                                   request_cb=obj_request_cb,
                                   input_keys=['object_name'],
                                   output_keys=['object_location', 'object_release_location']),
                                   transitions={succeeded: 'MOVE_TO_OBJECT',
                                                aborted: aborted})

            smach.StateMachine.add('MOVE_TO_OBJECT',
                                   MoveActionState("/map", goal_key='object_location'),
                                   transitions={succeeded: succeeded})

# vim: expandtab ts=4 sw=4
