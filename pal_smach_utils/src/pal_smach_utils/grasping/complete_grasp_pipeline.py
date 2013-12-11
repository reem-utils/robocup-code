#! /usr/bin/env python

import smach

from pal_smach_utils.grasping.sm_grasp import GraspStateMachine
from pal_smach_utils.grasping.search_objects_behaviour import SearchObjectsStateMachine
from pal_smach_utils.grasping.give_me_object import GiveMeObjectStateMachine
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted, reset_grasp_errors



class DecideIfNeedHelpState(smach.State):

    def __init__(self):
        smach.State.__init__(self, input_keys=['ask_for_help_key'],outcomes=['ASK_FOR_HELP', 'NORMAL_GRASP'])

    def execute(self, userdata):
        if userdata.ask_for_help_key:
            return 'ASK_FOR_HELP'
        else:
            return 'NORMAL_GRASP'



class CompleteGraspPipelineStateMachine(smach.StateMachine):
    """
    This pipeline does:
      given a a object to search in the userdata key: object_to_search_for
      Scan for the object, if it's seen and you are not close enough to grasp
      it will get closer to it and then it will grasp it

      The starting supposed position is in front of the object we want to grasp
      And the ending supposed position is just in front of the object
      with it grasped in the right hand with the "travelling position" of the arm
      If it doesn't find the object, or can't grasp it, it will abort, otherwise succeeded
    """
    def __init__(self, ask_for_help=False):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted],
                                    input_keys=['object_to_search_for', 'ask_for_help_key', 'object_found'],
                                    output_keys=['object_found'])


        with self:
            self.userdata.ask_for_help_key = ask_for_help

            smach.StateMachine.add(
                "RESET_GRASP_ERRORS",
                smach.CBState(reset_grasp_errors, outcomes=[succeeded, aborted]),
                transitions={succeeded: "DecideIfNeedHelpState", aborted: "DecideIfNeedHelpState"}
            )

            smach.StateMachine.add('DecideIfNeedHelpState',
                                   DecideIfNeedHelpState(),
                                   transitions={'ASK_FOR_HELP': 'GiveMeObjectStateMachine',
                                                'NORMAL_GRASP': 'SearchObjectAndGetCloserIfNeeded'})


            smach.StateMachine.add('GiveMeObjectStateMachine',
                                   GiveMeObjectStateMachine(),
                                   transitions={succeeded: succeeded,
                                                aborted: aborted})

            smach.StateMachine.add('SearchObjectAndGetCloserIfNeeded',
                                   SearchObjectsStateMachine(),
                                   transitions={succeeded: 'INIT_USERDATA_object_found_to_pose_object',
                                                aborted: aborted})

            # GraspStateMachine needs pose_object key fullfilled to grasp
            @smach.cb_interface(input_keys=['object_to_search_for', 'object_found'], output_keys=['pose_object'],
                                outcomes=[succeeded])
            def fulfill_userdata(userdata):
                userdata.pose_object = userdata.object_found.object_list[0]
                return succeeded

            smach.StateMachine.add('INIT_USERDATA_object_found_to_pose_object',
                                   smach.CBState(fulfill_userdata,
                                                 input_keys=['object_to_search_for',
                                                             'object_found_in_base_link_ref_frame'],
                                                 output_keys=['pose_object'],
                                                 outcomes=[succeeded]),
                                   transitions={succeeded: 'GraspFoundObject'})

            smach.StateMachine.add('GraspFoundObject',
                                   GraspStateMachine(),
                                   transitions={succeeded: succeeded,
                                                aborted: 'GiveMeObjectStateMachine'})




