#! /usr/bin/env python
# -.- coding: utf-8 -.-
'''
LISTEN_DELIVERY_ORDER.PY
'''

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


DELIVER_GRAMMAR_NAME = 'robocup/deliver'
#DELIVER_GRAMMAR_NAME = 'robocup/elevator'
TAKE_SINGLE_ORDER_TIMEOUT = 25
RETAKE_FRASE = "Sorry, I didn't quite get that. May you repeat again?"
#RETAKE_FRASE = ""


class ListenDeliveryOrder(smach.StateMachine):

    """
    The delivery order will have to be in the current format from usersaid topic.
    Eg:  ['action': 'deliver',
          'objectA': 'object_name', 'objectB': 'object_name', 'objectC': 'object_name',
          'location1': 'location_name', 'location2': 'location_name']

    Frase to analise : Carry the apple and the coke to table_1 and move the pringles to table_2
    To find them afterwards they must be memorised all these names in the coord_translator/config/mmap.yaml
    """

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted],
                                    output_keys=['delivery_order_list_out'])

        with self:

            smach.StateMachine.add('ENABLE_GRAMMAR_DELIVER',
                                   GrammarState(DELIVER_GRAMMAR_NAME,
                                                enabled=True),
                                   transitions={succeeded: 'LISTEN_DELIVERY_ORDER'})

            def deliver_order_cb(userdata, message):
                order_list = []
                actiontag = [tag for tag in message.tags if tag.key == 'action']
                objectAtag = [tag for tag in message.tags if tag.key == 'objectA']
                objectBtag = [tag for tag in message.tags if tag.key == 'objectB']
                objectCtag = [tag for tag in message.tags if tag.key == 'objectC']
                location1tag = [tag for tag in message.tags if tag.key == 'location1']
                location2tag = [tag for tag in message.tags if tag.key == 'location2']
                print str(message)
                print "ACTION TAG" + str(actiontag)
                print "LEN ACTION TAG" + str(len(actiontag))
                print type(actiontag)
                for i in range(len(actiontag)):
                    print "This is value of i:::" + str(i)
                    if actiontag and actiontag[i].value == 'goto' and objectAtag and objectBtag and objectCtag and location1tag and location2tag:
                        object_nameA = objectAtag[i].value
                        object_nameB = objectBtag[i].value
                        object_nameC = objectCtag[i].value
                        location_name1 = location1tag[i].value
                        location_name2 = location2tag[i].value
                        order_list.append([object_nameA, location_name1])
                        order_list.append([object_nameB, location_name1])
                        order_list.append([object_nameC, location_name2])
                        userdata.delivery_order_list_out = order_list
                        return succeeded
                return aborted

            smach.StateMachine.add('LISTEN_DELIVERY_ORDER',
                                   TopicReaderState(topic_name='usersaid',
                                                    msg_type=asrresult,
                                                    timeout=TAKE_SINGLE_ORDER_TIMEOUT,
                                                    callback=deliver_order_cb,
                                                    output_keys=['delivery_order_list_out']),
                                   transitions={succeeded: 'CONFIRM_DELIVERY_ORDER', aborted: 'RETAKE_OBJECT'},
                                   remapping={'delivery_order_list_out': 'delivery_order_list_out'})

            smach.StateMachine.add('RETAKE_OBJECT',
                                   SpeakActionState(RETAKE_FRASE),
                                   transitions={succeeded: 'LISTEN_DELIVERY_ORDER'})

            def confirm_object(userdata):
                objectA = userdata.delivery_order_list_out[0][0]
                objectB = userdata.delivery_order_list_out[1][0]
                objectC = userdata.delivery_order_list_out[2][0]
                location1 = userdata.delivery_order_list_out[0][1]
                location2 = userdata.delivery_order_list_out[2][1]

                text_to_say = "You asked me to, firstly, fetch the " + objectA + ", and the " + objectB + ", and deliver it to the " + location1 + ". Afterwards, I will fetch the " + objectC + ", and take it to the " + location2
                return "Got it! " + text_to_say

            smach.StateMachine.add('CONFIRM_DELIVERY_ORDER',
                                   SpeakActionState(text_cb=confirm_object, input_keys=['delivery_order_list_out']),
                                   transitions={succeeded: 'DISABLE_GRAMMAR_DELIVER'})

            smach.StateMachine.add('DISABLE_GRAMMAR_DELIVER',
                                   GrammarState(DELIVER_GRAMMAR_NAME, enabled=False),
                                   transitions={succeeded: succeeded,
                                                aborted: aborted,
                                                preempted: preempted})
