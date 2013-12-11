#! /usr/bin/env python

import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from smach_ros import ServiceState
from smach import CBState

from pal_smach_utils.utils.global_common import *

from sound_action import SpeakActionState, SpeakActionFromPoolStateMachine
from coord_translator.srv import ObjectTranslator, ObjectTranslatorRequest



class AnnounceCategoryFromPool(smach.StateMachine):
    '''Used when Get_category_and_announce_object receives a list with a pool of messages to say.
    input_nobj argument indicates if the userdata pose_object is a simple ObjectPose or an ObjectPoseList.
    category_pool argument in the constructor is the text to be said to announce the category of the object.
                  All the strings in the list must have two %s to be replaced for the object's name and the category, in that order.
    '''
    def __init__(self, category_pool, input_nobj):
        smach.StateMachine.__init__(self, outcomes=[succeeded, aborted, preempted],
                                          input_keys=['pose_object', 'category'])
        with self:
            @smach.cb_interface(input_keys=['pose_object', 'category'], output_keys=['out_tell_arg'], outcomes=[succeeded])
            def prepare_userdata(userdata):
                objname = userdata.pose_object.object_list[0].name if input_nobj != Get_category_and_announce_object.ONE_OBJECT else userdata.pose_object.name
                userdata.out_tell_arg = (objname, userdata.category)
                return succeeded

            smach.StateMachine.add('PREPARE_POOL_ARGS',
                             CBState(prepare_userdata,
                                     input_keys=['pose_object', 'category'],
                                     output_keys=['out_tell_arg'], outcomes=[succeeded]),
                             remapping={'pose_object': 'pose_object',
                                        'category': 'category',
                                        'out_tell_arg': 'tell_arg'},
                             transitions={succeeded: 'TELL_PHRASE_FROM_POOL'})

            smach.StateMachine.add('TELL_PHRASE_FROM_POOL',
                         SpeakActionFromPoolStateMachine(category_pool, arg_key="tell_arg"),
                         remapping={"tell_arg": "tell_arg"},
                         transitions={succeeded: succeeded, aborted: aborted, preempted: preempted})


class Get_category_and_announce_object(smach.StateMachine):

    '''
    input_nobj argument indicates if the userdata pose_object is a simple ObjectPose or an ObjectPoseList.
    categoryphrase argument in the constructor is the text to be said to announce the category of the object.
        If it's a string, a SpeakActionState is used. If it's a list of strings, a SpeakActionFromPoolStateMachine is used.
        All the strings (either the single string or all the strings inside the list) must have two %s to be replaced for the
        object's name and the category, in that order. '''

    ONE_OBJECT = 1
    LIST_OBJECT = 0

    def __init__(self, input_nobj=LIST_OBJECT, categoryphrase="Hey look, I found an object called %s of category %s I'm going to pick it up."):
        smach.StateMachine.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['pose_object'])

    #def execute(self, userdata):
        with self:
            @smach.cb_interface(input_keys=['pose_object'], output_keys=['category'])
            def loc_response_cb(userdata, response):
                if response.exists:
                    userdata.category = response.category
                    objname = userdata.pose_object.object_list[0].name if input_nobj != self.ONE_OBJECT else userdata.pose_object.name
                    print "Got category " + response.category + " for object " + objname
                    return succeeded
                else:
                    userdata.category = None
                    return aborted

            def loc_request_cb(userdata, request):
                req = ObjectTranslatorRequest()
                req.objname = userdata.pose_object.object_list[0].name if input_nobj != self.ONE_OBJECT else userdata.pose_object.name
                print "Asking coord_translator for " + req.objname
                return req

            smach.StateMachine.add(
                'GET_OBJECT_CATEGORY',
                ServiceState('object_translator', ObjectTranslator,
                    response_cb=loc_response_cb,
                    request_cb=loc_request_cb,
                    input_keys=['pose_object'],
                    output_keys=['category']),
                    remapping={'category': 'category'},
                    transitions={succeeded: 'ANNOUNCE_CATEGORY'})

            def announce_category_cb(userdata):
                objname = userdata.pose_object.object_list[0].name if input_nobj != Get_category_and_announce_object.ONE_OBJECT else userdata.pose_object.name
                category_phrase = categoryphrase % (objname, userdata.category)
                print "categoryphrase is:" + category_phrase
                return category_phrase

            if type(categoryphrase) is str:  # We have an only string, we can use a simple speakActionState.
                smach.StateMachine.add(
                        'ANNOUNCE_CATEGORY',
                        SpeakActionState(text_cb=announce_category_cb,
                                         input_keys=['pose_object', 'category']),
                        transitions={succeeded: succeeded})

            else:  # We have a list (or it should, it'll fail if not) so we use a SpeakActionFromPoolSM
                smach.StateMachine.add(
                        'ANNOUNCE_CATEGORY',
                        AnnounceCategoryFromPool(categoryphrase, input_nobj),
                        transitions={succeeded: succeeded})


# vim: expandtab ts=4 sw=4
