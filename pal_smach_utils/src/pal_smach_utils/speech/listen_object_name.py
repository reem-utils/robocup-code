#! /usr/bin/env python

import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import actionlib

from smach_ros import SimpleActionState, ServiceState

from pal_smach_utils.utils.topic_reader import *

from pal_interaction_msgs.msg import asrupdate, asrresult
from pal_interaction_msgs.srv import recognizerService
from grammar_state import GrammarState
from sound_action import SpeakActionState


FETCH_GRAMMAR_NAME = 'robocup/bring'
TAKE_SINGLE_ORDER_TIMEOUT = 25


class ListenObjectName(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted],
                                    output_keys=['object_name'])

        with self:

            smach.StateMachine.add('ENABLE_GRAMMAR_FETCH',
                                   GrammarState(FETCH_GRAMMAR_NAME, enabled=True),
                                   transitions={succeeded: 'LISTEN_BRING'})

            def bring_order_cb(userdata, message):
                actiontag = [tag for tag in message.tags if tag.key == 'action']
                drinktag = [tag for tag in message.tags if tag.key == 'object']
                if actiontag and actiontag[0].value == 'bring':
                    userdata.object_name = drinktag[0].value
                    return succeeded
                return aborted

            smach.StateMachine.add('LISTEN_BRING',
                                   TopicReaderState(topic_name='usersaid',
                                                    msg_type=asrresult,
                                                    timeout=TAKE_SINGLE_ORDER_TIMEOUT,
                                                    callback=bring_order_cb,
                                                    output_keys=['object_name']),
                                   transitions={succeeded: 'CONFIRM_OBJECT', aborted: 'LISTEN_BRING'})
                                # outputs: 'object_name'

            smach.StateMachine.add('RETAKE_OBJECT',
                                   SpeakActionState('Sorry, what did you said?'),
                                   transitions={succeeded: 'LISTEN_BRING'})

            def confirm_object(userdata):
                return "Okay! You asked me for %s." % (userdata.object_name)

            smach.StateMachine.add('CONFIRM_OBJECT',
                                   SpeakActionState(text_cb=confirm_object, input_keys=['object_name']),
                                   transitions={succeeded: 'DISABLE_GRAMMAR_FETCH',
                                                aborted: 'DISABLE_GRAMMAR_FETCH'})

            smach.StateMachine.add('DISABLE_GRAMMAR_FETCH',
                                   GrammarState(FETCH_GRAMMAR_NAME, enabled=False),
                                   transitions={succeeded: succeeded,
                                                aborted: aborted,
                                                preempted: preempted})




# vim: expandtab ts=4 sw=4
