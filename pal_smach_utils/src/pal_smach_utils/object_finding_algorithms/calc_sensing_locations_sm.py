#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy

from smach import CBState
from smach_ros import ServiceState
from nav_msgs.srv import GetMap
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.object_finding_algorithms.visib_prm import Visib_PRM
from pal_smach_utils.object_finding_algorithms.ofb_utils import publish_markerArray
from visualization_msgs.msg import MarkerArray, Marker


PARAM_CORNER_NAME = '/mmap/corner_data/'


class CalculateSensingLocations(smach.StateMachine):

    '''
    SMACH StateMachine to calculate sensing locations using the Visib-PRM algorithm.
    The in_room_name is the name of the room to get the corner data.
    The out_guards is a list of pairs (x,y) that represent the sensing locations.
    '''

    def __init__(self, publish_markers=True):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted, 'no_corner_info'],
                                    input_keys=['in_room_name'],
                                    output_keys=['out_guards'])

        self.userdata.out_guards = None  # To avoid error when not succeeding

        if publish_markers:
            publisher = rospy.Publisher('/sensing_locations', MarkerArray, latch=True)

        with self:
            smach.StateMachine.add('GET_MAP', ServiceState('/static_map', GetMap, response_slots=['map']),
                                   remapping={'map': 'map'},
                                   transitions={succeeded: 'CALCULATE_VISIBPRM_GUARDS',
                                                aborted: 'GET_MAP'})

            @smach.cb_interface(input_keys=['in_map', 'in_room_name'], output_keys=['out_guards'],
                                outcomes=[succeeded, 'no_corner_info'])
            def calculate_tabletop_sensing_locations_route(userdata):
                params = rospy.get_param(PARAM_CORNER_NAME+userdata.in_room_name, None)
                if params is None:
                    return 'no_corner_info'
                # Note that the ServiceState with the response slots returns in the userdata the response.map variable.
                visib = Visib_PRM(userdata.in_map, params[0], params[1], params[2], params[3], params[4])
                (guards, connection) = visib.visib_prm(in_mtrs=True)
                userdata.out_guards = guards
                # FIXME consider deleting the visib thing

                if publish_markers:
                    publish_markerArray(publisher, points=guards, rgba=(1.0, 0.0, 0.0, 1.0), shape=Marker.CYLINDER)

                return succeeded

            smach.StateMachine.add('CALCULATE_VISIBPRM_GUARDS',
                                   CBState(calculate_tabletop_sensing_locations_route,
                                           input_keys=['in_map', 'in_room_name'],
                                           output_keys=['out_guards'], outcomes=[succeeded, 'no_corner_info']),
                                   remapping={'out_guards': 'out_guards', 'in_map': 'map', 'in_room_name': 'in_room_name'},
                                   transitions={succeeded: succeeded, 'no_corner_info': 'no_corner_info'})
