#! /usr/bin/env python

import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import actionlib


from pal_smach_utils.utils.topic_reader import *

from pal_interaction_msgs.msg import asrresult
from sound_action import SpeakActionState

POI_GRAMMAR_NAME = 'robocup/poi_grammar'


class ListenPoiName(smach.StateMachine):
    """
    State that reads at the topic of the speech recognizer for the last word that has been said,
    It expects that either a poi name, or the word stop has been said
    If a poi has been said, the state will return succeeded and the poi name in the userdata.poi_name
    If the word stop has been said, it will return preempted
    If none of those were said, it will return aborted
    what_you_heard_out : will have value only when you say a poi or stop and wait.
    """
    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted],
                                    output_keys=['poi_name', 'orientation_side', 'what_you_heard_out'])

        with self:

            """
            def poi_name_cb(userdata, message):
                rospy.loginfo("MESSAGE LISTENES $$$$ %s" % message)
                userdata.what_you_heard_out = ""
                goto_tags = [tag for tag in message.tags if tag.key == 'poi']
                if goto_tags:
                    userdata.poi_name = goto_tags[0].value
                    userdata.what_you_heard_out = goto_tags[0].value
                    return succeeded

                stop_tags = [tag for tag in message.tags if tag.key == 'action']
                if stop_tags and stop_tags[0].value == 'stopwait':
                    userdata.what_you_heard_out = stop_tags[0].value
                    return preempted

                return aborted
            """
            def poi_name_cb(userdata, message):
                rospy.loginfo("MESSAGE LISTENES $$$$ %s" % message)
                userdata.what_you_heard_out = ""
                goto_tags = [tag for tag in message.tags if tag.key == 'poi']
                orient_tags = [tag for tag in message.tags if tag.key == 'orientation']
                if goto_tags and orient_tags:
                    userdata.poi_name = goto_tags[0].value
                    userdata.orientation_side = orient_tags[0].value
                    userdata.what_you_heard_out = str(goto_tags[0].value) + " to the " + str(orient_tags[0].value)
                    return succeeded

                stop_tags = [tag for tag in message.tags if tag.key == 'action']
                if stop_tags and stop_tags[0].value == 'stopwait':
                    userdata.what_you_heard_out = stop_tags[0].value
                    return preempted

                return aborted

            smach.StateMachine.add('LISTEN',
                                   TopicReaderState(topic_name='usersaid',
                                                    msg_type=asrresult,
                                                    timeout=None,
                                                    callback=poi_name_cb,
                                                    output_keys=['poi_name', 'orientation_side', 'what_you_heard_out']),
                                   transitions={succeeded: 'I_HEARD'})

            def confirm_object(userdata):
                text_to_say = "Yupi, I heard " + str(userdata.what_you_heard_out)
                return text_to_say

            smach.StateMachine.add('I_HEARD',
                                   SpeakActionState(text_cb=confirm_object, input_keys=['what_you_heard_out']),
                                   transitions={succeeded: succeeded})

# vim: expandtab ts=4 sw=4
