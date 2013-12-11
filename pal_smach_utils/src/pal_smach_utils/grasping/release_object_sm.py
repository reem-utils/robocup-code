#! /usr/bin/env python
# -.- coding: utf-8 -.-
# vim: expandtab ts=4 sw=4

import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
from smach_ros import ServiceState
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from geometry_msgs.msg import Pose, Point, Quaternion
from pal_smach_utils.grasping.sm_release import ReleaseObjectStateMachine
from tf.transformations import quaternion_from_euler
from coord_translator.srv import ObjectTranslator, ObjectTranslatorRequest
try:
    from pr_msgs.msg import ObjectPose
except ImportError:
    from pr_msgs.msg import ObjectPose
#from sm_reem_deliver_sm import SMReemDeliverStateMachine

OBJECT_DELIVERED_FRASE = "I delivered this cute object. I'm so proud."

"""
class ReleaseObjectSM(smach.StateMachine):
    def __init__(self):
      #WITH GRASP
        smach.StateMachine.__init__(self,
                                    ['object_delivered_succesfully',
                                     'didnt_deliver_object',
                                     preempted,
                                     aborted],
                                    input_keys=['object_name'])

        with self:

            smach.StateMachine.add('GET_OBJECT_ARM_RELEASE_LOCATION',
                                   GetObjectReleaseLocationSM(),
                                   transitions={succeeded: 'SM_RELEASE',
                                                preempted: preempted,
                                                aborted: 'didnt_deliver_object'},
                                   remapping={'object_name': 'object_name',
                                              'object_location': 'object_location',
                                              'object_release_location': 'object_release_location'})

            #TODO, why do we need the object_location?

            smach.StateMachine.add('SM_RELEASE',
                                   ReleaseObjectStateMachine(speak=False),
                                   transitions={succeeded: 'OBJECT_DELIVERED',
                                                preempted: preempted,
                                                aborted: 'didnt_deliver_object'},
                                   remapping={'releasing_position': 'object_release_location'})

            def say_text_cb(userdata):
                text_say = OBJECT_DELIVERED_FRASE
                return text_say
            smach.StateMachine.add('OBJECT_DELIVERED',
                                   SpeakActionState(text_cb=say_text_cb, input_keys=['object_name']),
                                   transitions={succeeded: 'object_delivered_succesfully'})


"""

class ReleaseObjectSM(smach.StateMachine):
    def __init__(self):
      #WITHOUT GRASP
        smach.StateMachine.__init__(self,
                                    ['object_delivered_succesfully',
                                     'didnt_deliver_object',
                                     preempted,
                                     aborted],
                                    input_keys=['object_name'])

        with self:

            smach.StateMachine.add('GET_OBJECT_ARM_RELEASE_LOCATION',
                                   GetObjectReleaseLocationSM(),
                                   transitions={succeeded: 'OBJECT_DELIVERED',
                                                preempted: preempted,
                                                aborted: 'didnt_deliver_object'},
                                   remapping={'object_name': 'object_name',
                                              'object_location': 'object_location',
                                              'object_release_location': 'object_release_location'})

            def say_text_cb(userdata):
                text_say = OBJECT_DELIVERED_FRASE
                return text_say
            smach.StateMachine.add('OBJECT_DELIVERED',
                                   SpeakActionState(text_cb=say_text_cb, input_keys=['object_name']),
                                   transitions={succeeded: 'object_delivered_succesfully'})



class GetObjectReleaseLocationSM(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded,
                                     preempted,
                                     aborted],
                                    input_keys=['object_name'],
                                    output_keys=['object_location', 'object_release_location'])

        with self:

            @smach.cb_interface(input_keys=['object_name'], output_keys=['object_location', 'object_release_location'])
            def obj_response_cb(userdata, response):
                if response.exists:
                    pose = Pose()
                    pose.position = Point(response.base_coordinates.x, response.base_coordinates.y, 0)
                    pose.orientation = Quaternion(*quaternion_from_euler(0, 0, response.base_coordinates.z))
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
                                   transitions={succeeded: succeeded,
                                                aborted: aborted})


"""

class ArmDeliverTargetPoseStampedCreator(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys=['target_pose_stamped'])

    def execute(self, userdata):
        print "Target PoseStamped created foe the Grasping"

        test_pose_st = PoseStamped()
        test_pose_st.header.stamp = rospy.Time.now()
        test_pose_st.header.frame_id = "/base_link"
        test_pose_st.pose = Pose()
        test_pose_st.pose.position.x = 0.4
        test_pose_st.pose.position.y = -0.25
        test_pose_st.pose.position.z = 1.13
        test_pose_st.pose.orientation.x = 0.5
        test_pose_st.pose.orientation.y = -0.5
        test_pose_st.pose.orientation.z = 0.5
        test_pose_st.pose.orientation.w = -0.5
        userdata.target_pose_stamped = test_pose_st
        print "target_pose_stamped" + str(test_pose_st)
        return succeeded


class FAKEReleaseObjectSM(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self,
                                    ['object_delivered_succesfully',
                                     'didnt_deliver_object',
                                     preempted,
                                     aborted],
                                    input_keys=['object_name'])

        with self:

            # TODO This should recognize a surface coord to put the object.
            smach.StateMachine.add('RECOGNIZE_OBJECTS',
                                   SearchSurfaceToDeliverObject(),
                                   remapping={'surface_data': 'surface_data'},
                                   transitions={succeeded: '',
                                                aborted: 'DIDNT_FIND_SURFACE'})


            smach.StateMachine.add('FAKE_ARM_TARGET_POSE',
                                   ArmDeliverTargetPoseStampedCreator(),
                                   transitions={succeeded: 'SM_DELIVER'},
                                   remapping={'target_pose_stamped': 'found_object_pose_stamped'})

            smach.StateMachine.add('SM_DELIVER',
                                   SMReemDeliverStateMachine(),
                                   transitions={succeeded: 'OBJECT_FETCHED'},
                                   remapping={'target_pose_stamped': 'found_object_pose_stamped'})

            def say_text_cb(userdata):
                text_say = OBJECT_DELIVERED_FRASE
                return text_say
            smach.StateMachine.add('OBJECT_FETCHED',
                                   SpeakActionState(text_cb=say_text_cb, input_keys=['object_name']),
                                   transitions={succeeded: 'object_delivered_succesfully'})
"""
