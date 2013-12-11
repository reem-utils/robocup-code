#! /usr/bin/env python
# -.- coding: utf-8 -.-
# vim: expandtab ts=4 sw=4
# Author RDaneelOlivaw

import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy

from geometry_msgs.msg import Pose, Quaternion, PoseStamped
from tf.transformations import quaternion_from_euler
from smach_ros import ServiceState
from coord_translator.srv import ObjectTranslator, ObjectTranslatorRequest

from pr_msgs.msg import ObjectPoseList, ObjectPose
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine

from search_object_and_grasp import SearchObjectAndGrasp
#from sm_put_on_tray import PutOnTrayStateMachine

OBJECT_FETCHED_FRASE = "I've got the "
DIDNT_FIND_OBJECT_FRASE = "Couldn't find the "
DIDNT_FIND_LOCATION_OF_OBJECT_FRASE = "I didnt find where the location of "


class FetchObject(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self,
                                    ['object_fetched_succesfully',
                                     'didnt_fetch_object',
                                     preempted,
                                     aborted],
                                    input_keys=['in_fetch_object_name'])

        with self:

            @smach.cb_interface(input_keys=['object_name'], output_keys=['category'])
            def loc_response_cb(userdata, response):
                if response.exists:
                    userdata.category = response.category
                    return succeeded
                else:
                    userdata.category = None
                    return aborted

            def loc_request_cb(userdata, request):
                req = ObjectTranslatorRequest()
                req.objname = userdata.object_name
                rospy.loginfo("Asking coord_translator for " + req.objname)
                return req

            smach.StateMachine.add('GET_OBJECT_CATEGORY',
                                   ServiceState('object_translator',
                                                ObjectTranslator,
                                                response_cb=loc_response_cb,
                                                request_cb=loc_request_cb,
                                                input_keys=['object_name'],
                                                output_keys=['category']),
                                   remapping={'object_name': 'in_fetch_object_name',
                                              'category': 'category'},
                                   transitions={succeeded: 'MOVE_TO_OBJECT',
                                                aborted: 'DIDNT_FIND_LOCATION_OF_OBJECT'})

            #Goes to the location (in_fetch_object_name, its category ).
            smach.StateMachine.add('MOVE_TO_OBJECT',
                                   MoveToRoomStateMachine(),
                                   transitions={succeeded: 'SEARCH_FOR_OBJECT_AND_GRASP',
                                                preempted: preempted,
                                                aborted: 'DIDNT_FIND_LOCATION_OF_OBJECT'},
                                   remapping={'room_name': 'category'})

            smach.StateMachine.add('SEARCH_FOR_OBJECT_AND_GRASP',
                                   SearchObjectAndGrasp(),
                                   transitions={'object_grasped_succesfully': 'object_fetched_succesfully',
                                                'didnt_grasp_object': 'didnt_fetch_object',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_fetch_object_name': 'in_fetch_object_name'})

            def say_text_cb(userdata):
                text_say = DIDNT_FIND_LOCATION_OF_OBJECT_FRASE + userdata.in_fetch_object_name + " is"
                return text_say
            smach.StateMachine.add('DIDNT_FIND_LOCATION_OF_OBJECT',
                                   SpeakActionState(text_cb=say_text_cb, input_keys=['in_fetch_object_name']),
                                   transitions={succeeded: 'didnt_fetch_object'})
