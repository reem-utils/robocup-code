#! /usr/bin/env python

import roslib
roslib.load_manifest('clean_up')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.navigation.enter_room import EnterRoomStateMachine
from pal_smach_utils.navigation.move_to_object import MoveToObjectBelongingLocSM
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.object_finding_algorithms.object_finding_behaviours import ObjectFindingBehaviour
from pal_smach_utils.grasping.complete_grasp_pipeline import CompleteGraspPipelineStateMachine
#from pal_smach_utils.grasping.sm_give import GiveStateMachine
from pal_smach_utils.grasping.sm_release import ReleaseObjectStateMachine
from pal_smach_utils.speech.sm_listen_go_to_room import ListenGoToRoomStateMachine
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers
from pal_smach_utils.speech.get_category_and_announce import Get_category_and_announce_object
from pal_smach_utils.speech.sound_action import SpeakActionState, SpeakActionFromPoolStateMachine


class CleanUp(smach.StateMachine):

    NUMBER_OF_OBJECTS = 15  # A total of 25 objects in the test (15 known and 10 unknown)

    class CheckIfFinished(smach.State):

        def __init__(self):
            smach.State.__init__(self, outcomes=['finish', 'continue'], input_keys=[], output_keys=[])
            self.num_objects = 0

        def execute(self, userdata):
            self.num_objects = self.num_objects + 1
            if self.num_objects == CleanUp.NUMBER_OF_OBJECTS:
                return 'finish'
            return 'continue'

    class GetObjectName(smach.State):

        def __init__(self):
            smach.State.__init__(self, outcomes=[succeeded], input_keys=['in_object_data'], output_keys=['out_object_name'])

        def execute(self, userdata):
            userdata.out_object_name = userdata.in_object_data.name
            return succeeded

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=[], output_keys=[])

        with self:

            smach.StateMachine.add('ANNOUNCE_READY_TO_ENTER_HOUSE',
                                   SpeakActionState(text="I'm ready to enter the house."),
                                   #transitions={succeeded: 'ANNOUNCE_WHAT_ROOM_SHOULD_I_CLEAN'})  # jump over entering the door
                                   transitions={succeeded: 'SM_ENTER_HOUSE'})

            smach.StateMachine.add('SM_ENTER_HOUSE',
                                   EnterRoomStateMachine(distance=1.5, orient_after_passing=0.0),
                                   transitions={succeeded: 'START_CONTROLLERS'})

            smach.StateMachine.add('START_CONTROLLERS', StartRobotControllers(head=True, left=True, right=True),
                                   transitions={succeeded: 'SM_ASK_LISTEN_GO_TO_ROOM', aborted: 'START_CONTROLLERS'})

            smach.StateMachine.add('SM_ASK_LISTEN_GO_TO_ROOM',
                                   ListenGoToRoomStateMachine(question='What room should I clean up?', grammar_name='robocup/cleanup'),
                                   #transitions={succeeded: 'ANNOUNCE_LOOKING_FOR_OBJECTS'},
                                   transitions={succeeded: 'SM_SEARCH_OBJECT'},
                                   remapping={'room_name': 'room_name', 'room_location': 'room_location'})

            # smach.StateMachine.add('ANNOUNCE_LOOKING_FOR_OBJECTS', # We lose time here!
            #                        SpeakActionState(text="I'm looking for objects."),
            #                        transitions={succeeded: 'SM_SEARCH_OBJECT'})

            '''#FIXME delete!!! only while using blort. Delete parameters of the OFBFirstApproach too and the remapping!!
            self.userdata.pringles = 'coke-close'
            ######################################

            #TEST FOR THE GERMAN OPEN
            self.userdata.pringles = 'juice'
            smach.StateMachine.add('SM_SEARCH_OBJECT',  # Search object inside a room behaviour
                            OFBFirstApproach(target_object_key='target_obj'),  # FIXME!!! aborted should repeat looking for objects or end?
                            transitions={succeeded: 'GET_CATEGORY_AND_ANNOUNCE_OBJECT', preempted: preempted, aborted: 'ANNOUNCE_LOOKING_FOR_OBJECTS'},
                            remapping={'out_object_found': 'object_data', 'in_room_name': 'room_name',
                                       'out_location_inside_room_name': 'object_location_in_room_name',
                                       'target_obj': 'pringles'})'''

            smach.StateMachine.add('SM_SEARCH_OBJECT',  # Search object inside a room behaviour
                                   ObjectFindingBehaviour(approach='first'),  # FIXME!!! aborted should repeat looking for objects or end?
                                   transitions={succeeded: 'GET_OBJECT_NAME', preempted: preempted, aborted: 'ANNOUNCE_LOOKING_FOR_OBJECTS'},
                                   remapping={'out_object_found': 'object_data', 'in_room_name': 'room_name',
                                              'out_location_inside_room_name': 'object_location_in_room_name'})

            smach.StateMachine.add('GET_OBJECT_NAME',
                                   self.GetObjectName(),
                                   #transitions={succeeded: 'GET_CATEGORY_AND_ANNOUNCE_OBJECT'},
                                   transitions={succeeded: 'SAY_CATEGORY_AND_GRASP'},
                                   remapping={'in_object_data': 'object_data', 'out_object_name': 'object_name'})

            say_category_and_grasp = smach.Concurrence(outcomes=[succeeded, aborted],
                                                       default_outcome=aborted,
                                                       input_keys=['object_name', 'object_data'],
                                                       output_keys=[],
                                                       outcome_map={succeeded: {'GET_CATEGORY_AND_ANNOUNCE_OBJECT': succeeded,
                                                                                'SM_GRASP': succeeded}})  # FIXME aborted?
            with say_category_and_grasp:
                category_pool = ["This %s belongs to the %s category.", "The category of the %s is %s.", "%s's category is %s."]
                smach.Concurrence.add('GET_CATEGORY_AND_ANNOUNCE_OBJECT',
                                      Get_category_and_announce_object(input_nobj=Get_category_and_announce_object.ONE_OBJECT,
                                                                       categoryphrase=category_pool),
                                      #transitions={succeeded: 'SM_GRASP'},
                                      remapping={'pose_object': 'object_data'})

                smach.Concurrence.add('SM_GRASP',
                                      CompleteGraspPipelineStateMachine(),
                                      #transitions={succeeded: 'BRING_TO_DESTINATION'},
                                      remapping={'object_to_search_for': 'object_name'})

            smach.StateMachine.add('SAY_CATEGORY_AND_GRASP', say_category_and_grasp,
                                   transitions={succeeded: 'BRING_TO_DESTINATION',
                                                aborted: 'ANNOUNCE_LOOKING_FOR_OBJECTS'},
                                   remapping={'object_name': 'object_name', 'object_data': 'object_data'})

            tell_and_bring = smach.Concurrence(outcomes=[succeeded, aborted],
                                               default_outcome=aborted,
                                               input_keys=['object_name'],
                                               output_keys=['object_location', 'object_release_location'],
                                               outcome_map={succeeded: {'ANNOUNCE_BRINGING_TO_DESTINATION': succeeded,
                                                                        'MOVE_TO_BELONGING_OBJ_LOCATION': succeeded}})

            with tell_and_bring:
                bringing_pool = ["The %s doesn't belong here. I'll bring it where it belongs.",
                                 "I'm bringing the %s to its correct location.",
                                 "This %s should be in another place!", "Why is the %s here?",
                                 "The %s shouldn't be here!"]
                smach.Concurrence.add('ANNOUNCE_BRINGING_TO_DESTINATION',
                                      SpeakActionFromPoolStateMachine(bringing_pool, arg_key="tell_arg"),
                                      remapping={"tell_arg": "object_name"})

                smach.Concurrence.add('MOVE_TO_BELONGING_OBJ_LOCATION',
                                      MoveToObjectBelongingLocSM(),
                                      remapping={'object_name': 'object_name', 'object_location': 'object_location',
                                                 'object_release_location': 'object_release_location'})
                                      # input: 'object_name', output: 'object_location' 'object_release_location'

            smach.StateMachine.add('BRING_TO_DESTINATION', tell_and_bring,
                                   transitions={succeeded: 'RELEASE_OBJECT'},  # remove if working'ANNOUNCE_LEAVING_OBJECT'},
                                   remapping={'object_name': 'object_name', 'object_location': 'object_location'})

            '''leaving_object_pool = ["The %s should be here. I'm going to leave it.",
                                   "This is the %s's correct location.",
                                   "I'm leaving the %s here."]
            smach.StateMachine.add('ANNOUNCE_LEAVING_OBJECT',
                                   SpeakActionFromPoolStateMachine(leaving_object_pool, arg_key="tell_arg"),
                                   remapping={"tell_arg": "object_name"},
                                   transitions={succeeded: 'SM_GIVE'})

            # Call SM give, give pose of operator as input
            smach.StateMachine.add('SM_GIVE',
                                   GiveStateMachine(),
                                   transitions={succeeded: 'CHECK_IF_FINISHED'},
                                   remapping={'object_location': 'object_location',
                                              'object_name': 'object_name', 'pose_object': 'object_data'})  # pose_object is not used inside GiveStateMachine!'''

            tell_and_release = smach.Concurrence(outcomes=[succeeded, aborted],
                                                 default_outcome=aborted,
                                                 input_keys=['object_name', 'object_release_location'],
                                                 outcome_map={succeeded: {'ANNOUNCE_LEAVING_OBJECT': succeeded,
                                                                          'SM_RELEASE': succeeded}})
            with tell_and_release:
                leaving_object_pool = ["The %s should be here. I'm going to leave it.",
                                       "This is the %s's correct location.",
                                       "I'm leaving the %s here."]
                smach.Concurrence.add('ANNOUNCE_LEAVING_OBJECT',
                                      SpeakActionFromPoolStateMachine(leaving_object_pool, arg_key="tell_arg"),
                                      remapping={"tell_arg": "object_name"})

                smach.Concurrence.add('SM_RELEASE',
                                      ReleaseObjectStateMachine(speak=False),
                                      remapping={'releasing_position': 'object_release_location'})

            smach.StateMachine.add('RELEASE_OBJECT', tell_and_release,
                                   transitions={succeeded: 'CHECK_IF_FINISHED'},
                                   remapping={'object_release_location': 'object_release_location', 'object_name': 'object_name'})

            smach.StateMachine.add('CHECK_IF_FINISHED',
                                   self.CheckIfFinished(),
                                   transitions={'continue': 'ANNOUNCE_AND_GO_BACK_TO_ROOM',
                                                'finish': 'ANNOUNCE_FINISHED'})

            def tell_finished_cb(userdata):
                return "I'm finished! The %s is clean now!" % userdata.room_name

            smach.StateMachine.add('ANNOUNCE_FINISHED', SpeakActionState(text_cb=tell_finished_cb, input_keys=['room_name']),
                                   remapping={'room_name': 'room_name'},
                                   transitions={succeeded: succeeded})

            going_back_pool = ["I'm going back to the %s, there is more stuff to clean up.",
                               "I think there are more things in the %s to clean up.",
                               "The %s isn't clean up yet!", "I'll go back to the %s, I still haven't finished!"]
            smach.StateMachine.add('ANNOUNCE_AND_GO_BACK_TO_ROOM',
                                   MoveToRoomStateMachine(announcement=going_back_pool),
                                   transitions={succeeded: 'SM_SEARCH_OBJECT', aborted: aborted},
                                   remapping={'room_name': 'room_name', 'room_location': 'room_location'})
                                   # input: 'room_name', output: 'room_location'
