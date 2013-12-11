#! /usr/bin/env python
# -.- coding: utf-8 -.-
#FETCH_AND_GIVE_OBJECT_TEST.PY
# vim: expandtab ts=4 sw=4

import roslib; roslib.load_manifest('fetch_and_give_object_test')
import rospy
import smach
import actionlib

import tf

import smach_ros
from std_msgs import *
from geometry_msgs.msg import *

from pal_smach_utils.utils.global_common import *
from pal_smach_utils.grasping.fetch_object import FetchObject
from pal_smach_utils.navigation.get_current_pos import GetPosition
from pal_smach_utils.speech.listen_object_name import ListenObjectName
from pal_smach_utils.speech.listen_poi_name import ListenPoiName
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.speech.sm_hear_voice_commands_and_pois import SM_MemorisePois
from pal_smach_utils.speech.grammar_state import GrammarState

POI_GRAMMAR_NAME = 'robocup12/poi_grammar'
OBJECT_GRAMMAR_NAME = 'robocup12/object_grammar'

def main():

    """
    This SM memorises a poi with the Poi name given and after fetches the object told and
    if it has memorised a poi with that name then he goes to that position.
    Finally it returns to the starting position called Referee location
    """

    rospy.init_node('sm_memorise_and_fetch_and_give_object_test_state_machine')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:



        #Here we memorise the poi in the rosparam
        smach.StateMachine.add('START_SPEECHRECOG_POI_GRAMMAR',
                                GrammarState(POI_GRAMMAR_NAME, enabled=True),
                                transitions = {succeeded: 'LISTEN_POI'})


        smach.StateMachine.add( 'LISTEN_POI',
                                ListenPoiName(),
                                transitions = { succeeded:'SM_FO_MEMORISE_POI',
                                                aborted: 'LISTEN_POI',
                                                preempted: 'DISABLE_GRAMMAR_WITH_POI'},
                                remapping = {'poi_name':'poi_name'})

        smach.StateMachine.add( 'SM_FO_MEMORISE_POI',
                                SM_MemorisePois(),
                                transitions = {succeeded: 'DISABLE_GRAMMAR_WITH_POI'},
                                remapping = {'FO_POI_name':'poi_name'})

        smach.StateMachine.add( 'DISABLE_GRAMMAR_WITH_POI',
                                GrammarState(POI_GRAMMAR_NAME, enabled=False),
                                transitions = {succeeded:'GET_POSITION'})


        #Here starts the fetching SM

        smach.StateMachine.add( 'GET_POSITION',
                                GetPosition(),
                                transitions={succeeded: 'LISTEN_OBJECT_NAME'},
                                remapping = {'memorised_poi_data':'position'})

        smach.StateMachine.add( 'LISTEN_OBJECT_NAME',
                                ListenObjectName(),
                                transitions = { succeeded: 'GO_TO_POI_OF_GIVEN_OBJECT_NAME',
                                                aborted:'LISTEN_OBJECT_NAME'},
                                remapping = {'object_name':'object_name'})

        smach.StateMachine.add( 'GO_TO_POI_OF_GIVEN_OBJECT_NAME',
                                FetchObject(),
                                transitions = { succeeded : 'RETURN_TO_REFEREE',
                                                aborted: 'DIDNT_FIND_OBJECT_NAME_IN_ROSPARAM'},
                                remapping = {'fetch_object_name':'object_name'})

        def say_text_cb(userdata):
            text_say = "I don't remmember where I can find " + userdata.object_name
            return text_say
        smach.StateMachine.add( 'DIDNT_FIND_OBJECT_NAME_IN_ROSPARAM',
                                SpeakActionState(text_cb=say_text_cb,input_keys = ['object_name']),
                                transitions = {succeeded:'RETURN_TO_REFEREE'})

        smach.StateMachine.add( 'RETURN_TO_REFEREE',
                                MoveActionState('/map', goal_key='position'),
                                transitions = {succeeded:succeeded })


    sm.execute()
    rospy.spin()

if __name__ == '__main__':
    main()
