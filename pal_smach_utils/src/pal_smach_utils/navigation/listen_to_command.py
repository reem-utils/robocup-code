#! /usr/bin/env python
# -.- coding: utf-8 -.-

import rospy
import smach

from pal_smach_utils.speech.listen_general_command import PrintUserData

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted, o1, o2, o3, o4

from pal_smach_utils.utils.topic_reader import TopicReaderStateMultiOutcomes

from pal_interaction_msgs.msg import asrresult

memorise_poi = 'memorise_poi'
stop_hearing = 'stop_hearing'
stop_mapping = 'stop_mapping'
STOPWAIT_VOCAB = 'stopwait'


#HEAR_VOCAB_IN_GRAMMAR_OUTCOMES = POI_GRAMMAR_VOCAB.append(preempted,aborted)

class HearVocabInGrammar(smach.StateMachine):
    def __init__(self, grammar_vocab='no_grammar'):
        smach.StateMachine.__init__(self, [memorise_poi, stop_hearing, preempted, aborted], output_keys=['POI_name'])

        with self:

            def parse_command_cb(userdata, message):
                actions = [tag.value for tag in message.tags if tag.key == 'action']
                rospy.loginfo("This is what I've Heard ::: %s", str(actions))
                if len(actions) > 0:
                    userdata.general_data = actions[0]
                    rospy.loginfo("$$$ GENERAL_DATA  $$$$$  %s", str(userdata.general_data))
                    #Looks up all the array of vocabs of POI_GRAMMAR and
                    #sees if the word Reem got is one of them
                    #If so, it returns as outcome the vocab word.
                    #TODO but for no it just return stopwait or memorise he finds a word in VOCAB.
                    for vocabs in grammar_vocab:
                        rospy.loginfo("Vocab I'm reading NOW ::: %s, %s = %s", str(vocabs == actions[0]), str(actions[0]), str(vocabs))
                        if vocabs == actions[0]:
                            if vocabs == STOPWAIT_VOCAB:
                                return o2
                            return o1
                return aborted

            smach.StateMachine.add('AWAIT_COMMAND',
                                   TopicReaderStateMultiOutcomes(topic_name='usersaid', msg_type=asrresult, callback=parse_command_cb),
                                   transitions={o1: 'PRINT_POI_NAME',
                                                o2: stop_mapping,
                                                o3: 'AWAIT_COMMAND',
                                                o4: 'AWAIT_COMMAND',
                                                aborted: aborted},
                                   remapping={'general_data': 'POI_name'})

            smach.StateMachine.add('PRINT_POI_NAME',
                                   PrintUserData(),
                                   transitions={succeeded: memorise_poi,
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'userSaidData': 'POI_name'})
