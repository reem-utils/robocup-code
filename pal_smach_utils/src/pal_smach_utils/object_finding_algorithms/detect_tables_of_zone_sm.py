#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
import math
import pal_smach_utils.object_finding_algorithms.ofb_utils as ofb_utils

from smach import CBState
from geometry_msgs.msg import Pose, Quaternion, Point
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted, transform_pose
from pal_smach_utils.object_finding_algorithms.detect_tabletop import DetectTabletop
from tf.transformations import quaternion_from_euler
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.object_finding_algorithms.ofb_utils import publish_markerArray
from visualization_msgs.msg import MarkerArray, Marker


DEST_FRAME = '/map'


class DetectTablesOfZoneSM(smach.StateMachine):
    '''
    Detects the tables of a zone, rotating on the actual robot pose.
    It outputs in out_table_pose_list a list of tuples (x, y) with the poses of the tables,
    Also outputs out_table_orientation_list that is a list with the quaternion representing the orientation
    in DEST_FRAME frame_id for every element of the list of poses.
    You can create a single list of tuples ((x, y), q) by zipping the two lists (like this zip(table_pose_list, orientation_list))
    Creator arguments:
        rads_per_turn: Radiants to turn every time.
        times_to_turn: It will end when it has turned that number of times
        distance_treshold: Distance treshold to decide if two tables are the same.
        dist_to_table: Distance to approach to the table. The resulting poses will be at this distance from the table.
    '''
    def __init__(self, distance_treshold=0.5, dist_to_table=0.3, rads_per_turn=math.pi/2, times_to_turn=3, publish_markers=True):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted, 'no_tables'],
                                    input_keys=[],
                                    output_keys=['out_table_pose_list', 'out_table_orientation_list'])

        if publish_markers:
            publisher = rospy.Publisher('/detected_tables_zone', MarkerArray, latch=True)

        with self:
            @smach.cb_interface(output_keys=['out_times_turned', 'out_table_pose_list', 'out_table_orientation_list'],
                                outcomes=[succeeded])
            def init_udata(userdata):
                userdata.out_times_turned = 0  # Counter of turns
                userdata.out_table_pose_list = []
                userdata.out_table_orientation_list = []
                return succeeded

            smach.StateMachine.add('INIT_USERDATA', CBState(init_udata,
                                                            output_keys=['out_times_turned', 'out_table_pose_list',
                                                                         'out_table_orientation_list'],
                                                            outcomes=[succeeded]),
                                   remapping={'out_times_turned': 'times_turned',
                                              'out_table_pose_list': 'out_table_pose_list',
                                              'out_table_orientation_list': 'out_table_orientation_list'},
                                   transitions={succeeded: 'DETECT_TABLETOP'})

            smach.StateMachine.add('DETECT_TABLETOP', DetectTabletop(distance_treshold=distance_treshold, recognize_objects=False),
                                   remapping={'tabletop_info': 'tabletop_data'},
                                   transitions={succeeded: 'CHECK_TABLETOP_DATA', 'no_table': 'CHECK_IF_TURN'})

            @smach.cb_interface(input_keys=['in_tabletop_data', 'in_pose_list', 'in_orientation_list'],
                                output_keys=['out_pose_list', 'out_orientation_list'],
                                outcomes=[succeeded])
            def check_ttop_data(userdata):
                table_data = userdata.in_tabletop_data
                for t in table_data:
                    z = t.pose.pose.position.z
                    q = Quaternion(*quaternion_from_euler(0, 0, 0))
                    table_pose = Pose(Point(t.x_min-dist_to_table, (t.y_min+t.y_max)/2, z), q)

                    src_frame = t.pose.header.frame_id
                    # src_frame should be either base_link or base_footprint
                    table_pose = transform_pose(table_pose, src_frame, DEST_FRAME, timeout=3)
                    tuple_pose = (table_pose.position.x, table_pose.position.y)

                    for tp in userdata.in_pose_list:
                        if ofb_utils.euclidean_distance(tp, tuple_pose) <= distance_treshold:
                            break
                    else:  # The loop ended without breaking
                        userdata.in_pose_list.append(tuple_pose)
                        userdata.out_pose_list = userdata.in_pose_list
                        userdata.in_orientation_list.append(table_pose.orientation)  # FIXME table_pose? Should be more_less equal...
                        userdata.out_orientation_list = userdata.in_orientation_list
                return succeeded

            smach.StateMachine.add('CHECK_TABLETOP_DATA',
                                   CBState(check_ttop_data, input_keys=['in_tabletop_data', 'in_pose_list'],
                                           output_keys=['out_pose_list'],
                                           outcomes=[succeeded]),
                                   remapping={'in_tabletop_data': 'tabletop_data',
                                              'in_pose_list': 'out_table_pose_list',
                                              'out_pose_list': 'out_table_pose_list',
                                              'in_orientation_list': 'out_table_orientation_list',
                                              'out_orientation_list': 'out_table_orientation_list'},
                                   transitions={succeeded: 'CHECK_IF_TURN'})

            @smach.cb_interface(input_keys=['in_times_turned', 'in_table_poses'], output_keys=['out_times_turned'],
                                outcomes=[succeeded, 'turn_again', 'no_tables'])
            def check_if_turn(userdata):
                if userdata.in_times_turned >= times_to_turn:
                    if not userdata.in_table_poses:  # No table has been detected
                        return 'no_tables'
                    if publish_markers:  # We publish the markers
                        publish_markerArray(publisher, points=userdata.in_table_poses, rgba=(0, 1, 0, 1), shape=Marker.CUBE)
                    return succeeded
                userdata.out_times_turned = userdata.in_times_turned + 1
                return 'turn_again'

            smach.StateMachine.add('CHECK_IF_TURN',
                                   CBState(check_if_turn, input_keys=['in_times_turned', 'in_table_poses'],
                                           output_keys=['out_times_turned'],
                                           outcomes=[succeeded, 'turn_again', 'no_tables']),
                                   remapping={'in_times_turned': 'times_turned',
                                              'in_table_poses': 'out_table_pose_list',
                                              'out_times_turned': 'times_turned'},
                                   transitions={succeeded: succeeded,
                                                'no_tables': 'no_tables',
                                                'turn_again': 'TURN_AROUND'})

            turn = Pose()
            turn.position = Point(0, 0, 0)
            turn.orientation = Quaternion(*quaternion_from_euler(0, 0, rads_per_turn))
            smach.StateMachine.add('TURN_AROUND',
                                   MoveActionState('/base_link', pose=turn),
                                   transitions={succeeded: 'DETECT_TABLETOP',
                                                aborted: aborted})
