#! /usr/bin/env python

import roslib
roslib.load_manifest('find_object_say_category_and_grasp_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.get_category_and_announce import Get_category_and_announce_object
from pal_smach_utils.grasping.complete_grasp_pipeline import CompleteGraspPipelineStateMachine
from pal_smach_utils.utils.robot_controllers_activation import StartRobotControllers, StopRobotControllers
from pal_smach_utils.object_finding_algorithms.object_finding_behaviours import ObjectFindingBehaviour


class GetObjectName(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], input_keys=['in_object_data'], output_keys=['out_object_name'])

    def execute(self, userdata):
        userdata.out_object_name = userdata.in_object_data.name
        return succeeded


def main():
    rospy.init_node('find_object_say_category_and_grasp_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])
    sm.userdata.room_name = 'kitchen'

    with sm:
        smach.StateMachine.add('START_CONTROLLERS', StartRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: 'SM_SEARCH_OBJECT', aborted: aborted})

        smach.StateMachine.add('SM_SEARCH_OBJECT',  # Search object inside a room behaviour
                               ObjectFindingBehaviour(approach='first'),
                               transitions={succeeded: 'GET_OBJECT_NAME', preempted: preempted, aborted: aborted},
                               remapping={'out_object_found': 'object_data', 'in_room_name': 'room_name',
                                          'out_location_inside_room_name': 'object_location_in_room_name'})

        smach.StateMachine.add('GET_OBJECT_NAME',
                               GetObjectName(),
                               #transitions={succeeded: 'GET_CATEGORY_AND_ANNOUNCE_OBJECT'},
                               transitions={succeeded: 'SAY_CATEGORY_AND_GRASP'},
                               remapping={'in_object_data': 'object_data', 'out_object_name': 'object_name'})

        say_category_and_grasp = smach.Concurrence(outcomes=[succeeded, aborted],
                                                   default_outcome=aborted,
                                                   input_keys=['object_name', 'object_data'],
                                                   output_keys=[],
                                                   outcome_map={succeeded: {'GET_CATEGORY_AND_ANNOUNCE_OBJECT': succeeded,
                                                                            'SM_GRASP': succeeded}})
        with say_category_and_grasp:
            category_pool = ["This %s belongs to the %s category.", "The category of the %s is %s.", "%s's category is %s."]
            smach.Concurrence.add('GET_CATEGORY_AND_ANNOUNCE_OBJECT',
                                  Get_category_and_announce_object(input_nobj=Get_category_and_announce_object.ONE_OBJECT,
                                                                   categoryphrase=category_pool),
                                  #transitions={succeeded: 'SM_GRASP'},
                                  remapping={'pose_object': 'object_data'})

            smach.Concurrence.add('SM_GRASP',
                                  CompleteGraspPipelineStateMachine(),
                                  remapping={'object_to_search_for': 'object_name'})

        smach.StateMachine.add('SAY_CATEGORY_AND_GRASP', say_category_and_grasp,
                               transitions={succeeded: 'STOP_CONTROLLERS', aborted: 'STOP_CONTROLLERS'},
                               remapping={'object_name': 'object_name', 'object_data': 'object_data'})

        smach.StateMachine.add('STOP_CONTROLLERS', StopRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})


    sis = smach_ros.IntrospectionServer(
        'find_object_say_category_and_grasp_test', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
