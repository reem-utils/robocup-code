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
from pal_smach_utils.object_finding_algorithms.detect_furniture import DetectFurniture
from tf.transformations import quaternion_from_euler
from pal_smach_utils.navigation.move_action import MoveActionState
from pal_smach_utils.object_finding_algorithms.ofb_utils import publish_markerArray
from visualization_msgs.msg import MarkerArray, Marker


DEST_FRAME = '/map'


class DetectFurnitureOfZoneSM(smach.StateMachine):
    '''
    Detects the furniture of a zone, rotating on the actual robot pose.
    It outputs in out_furniture_pose_list a list of tuples (x, y) with the poses of the detected furniture.
    Also outputs out_furniture_orientation_list that is a list with the quaternion representing the orientation
    in DEST_FRAME frame_id for every element of the list of poses.
    You can create a single list of tuples ((x, y), q) by zipping the two lists (like this zip(furniture_pose_list, orientation_list))
    The key out_name_list contains a list of the names of the furniture, each position in the list corresponding to the pose and orientation
    in the same position in the list.
    Creator arguments:
        rads_per_turn: Radiants to turn every time.
        times_to_turn: It will end when it has turned that number of times
        distance_treshold: Distance treshold to decide if two furniture are the same.
        dist_to_furniture: Distance to approach to the furniture. The resulting poses will be at this distance from the furniture.
    '''
    def __init__(self, distance_treshold=0.5, dist_to_furniture=1.0, rads_per_turn=math.pi/2, times_to_turn=3, publish_markers=True):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted, 'no_furniture'],
                                    input_keys=[],
                                    output_keys=['out_furniture_pose_list', 'out_furniture_orientation_list', 'out_furniture_name_list'])

        if publish_markers:
            publisher = rospy.Publisher('/detected_furniture_zone', MarkerArray, latch=True)

        with self:
            @smach.cb_interface(output_keys=['out_times_turned', 'out_furniture_pose_list', 'out_furniture_orientation_list',
                                             'out_furniture_name_list'],
                                outcomes=[succeeded])
            def init_udata(userdata):
                userdata.out_times_turned = 0  # Counter of turns
                userdata.out_furniture_pose_list = []
                userdata.out_furniture_orientation_list = []
                userdata.out_furniture_name_list = []
                return succeeded

            smach.StateMachine.add('INIT_USERDATA', CBState(init_udata,
                                                            output_keys=['out_times_turned', 'out_furniture_pose_list',
                                                                         'out_furniture_orientation_list'],
                                                            outcomes=[succeeded]),
                                   remapping={'out_times_turned': 'times_turned',
                                              'out_furniture_pose_list': 'out_furniture_pose_list',
                                              'out_furniture_orientation_list': 'out_furniture_orientation_list',
                                              'out_furniture_name_list': 'out_furniture_name_list'},
                                   transitions={succeeded: 'DETECT_FURNITURE'})

            smach.StateMachine.add('DETECT_FURNITURE', DetectFurniture(distance_treshold=distance_treshold),
                                   remapping={'furniture_info': 'furniture_data'},
                                   transitions={succeeded: 'CHECK_FURNITURE_DATA', 'no_furniture': 'CHECK_IF_TURN'})

            @smach.cb_interface(input_keys=['in_furniture_data', 'in_pose_list', 'in_orientation_list', 'in_name_list'],
                                output_keys=['out_pose_list', 'out_orientation_list', 'out_name_list'],
                                outcomes=[succeeded])
            def check_furn_data(userdata):
                furniture_data = userdata.in_furniture_data
                for f_name, f_pose in furniture_data:
                    q = Quaternion(*quaternion_from_euler(0, 0, 0))
                    f_pose.pose.position.x -= dist_to_furniture
                    furniture_pose = Pose(f_pose.pose.position, q)

                    src_frame = f_pose.header.frame_id
                    # src_frame should be either base_link or base_footprint
                    furniture_pose = transform_pose(furniture_pose, src_frame, DEST_FRAME, timeout=3)
                    tuple_pose = (furniture_pose.position.x, furniture_pose.position.y)

                    for n, tp in zip(userdata.in_name_list, userdata.in_pose_list):
                        if (f_name == n) and (ofb_utils.euclidean_distance(tp, tuple_pose) <= distance_treshold):
                            break
                    else:  # The loop ended without breaking
                        userdata.in_pose_list.append(tuple_pose)
                        userdata.out_pose_list = userdata.in_pose_list
                        userdata.in_orientation_list.append(furniture_pose.orientation)
                        userdata.out_orientation_list = userdata.in_orientation_list
                        userdata.in_name_list.append(f_name)
                        userdata.out_name_list = userdata.in_name_list
                return succeeded

            smach.StateMachine.add('CHECK_FURNITURE_DATA',
                                   CBState(check_furn_data, input_keys=['in_furniture_data', 'in_pose_list'],
                                           output_keys=['out_pose_list'],
                                           outcomes=[succeeded]),
                                   remapping={'in_furniture_data': 'furniture_data',
                                              'in_pose_list': 'out_furniture_pose_list',
                                              'out_pose_list': 'out_furniture_pose_list',
                                              'in_orientation_list': 'out_furniture_orientation_list',
                                              'out_orientation_list': 'out_furniture_orientation_list',
                                              'in_name_list': 'out_furniture_name_list',
                                              'out_name_list': 'out_furniture_name_list'},
                                   transitions={succeeded: 'CHECK_IF_TURN'})

            @smach.cb_interface(input_keys=['in_times_turned', 'in_furniture_poses'], output_keys=['out_times_turned'],
                                outcomes=[succeeded, 'turn_again', 'no_furniture'])
            def check_if_turn(userdata):
                if userdata.in_times_turned >= times_to_turn:
                    if not userdata.in_furniture_poses:  # No furniture has been detected
                        return 'no_furniture'
                    if publish_markers:  # We publish the markers
                        publish_markerArray(publisher, points=userdata.in_furniture_poses, rgba=(0, 1, 0, 1), shape=Marker.CUBE)
                    return succeeded
                userdata.out_times_turned = userdata.in_times_turned + 1
                return 'turn_again'

            smach.StateMachine.add('CHECK_IF_TURN',
                                   CBState(check_if_turn, input_keys=['in_times_turned', 'in_furniture_poses'],
                                           output_keys=['out_times_turned'],
                                           outcomes=[succeeded, 'turn_again', 'no_furniture']),
                                   remapping={'in_times_turned': 'times_turned',
                                              'in_furniture_poses': 'out_furniture_pose_list',
                                              'out_times_turned': 'times_turned'},
                                   transitions={succeeded: succeeded,
                                                'no_furniture': 'no_furniture',
                                                'turn_again': 'TURN_AROUND'})

            turn = Pose()
            turn.position = Point(0, 0, 0)
            turn.orientation = Quaternion(*quaternion_from_euler(0, 0, rads_per_turn))
            smach.StateMachine.add('TURN_AROUND',
                                   MoveActionState('/base_link', pose=turn),
                                   transitions={succeeded: 'DETECT_FURNITURE',
                                                aborted: aborted})
