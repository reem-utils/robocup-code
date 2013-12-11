#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach
from smach import StateMachine, CBState
from smach_ros import ServiceState, SimpleActionState

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pr2_controllers_msgs.msg import PointHeadGoal, PointHeadAction
from tabletop_object_detector.srv import TabletopDetection, TabletopDetectionRequest


class DetectTabletop(smach.StateMachine):

    '''
    Performs a head scan action that makes snapshots of the pointcloud and the calls to the TabletopDetection service.

    If the parameter recognize_objects is True, the output key tabletop_info is a list with one message of type
        tabletop_object_detector/TabletopDetectionResult that contains the results of the detection.
    If the parameter recognize_objects is False, the output key tabletop_info is a list with one message of type
        tabletop_object_detector/Table that contains the results of the detected table.
    It outcomes 'no_table' if it didn't find a table, aborted if something else failed and succeeded if there was no problem.

    If the outcome is 'no_table' or aborted, the output key tabletop_info is a list with one message of type TabletopDetectionResult.

    Note: to have the position of the table, the values to be used are the "x_min, y_min, x_max and y_max" of the Table message.
          The PoseStamped of the message is needed to have the z component and the Header message with the frame_id.
          The other coordinates of the PoseStamped are not used (x and y are almost 0 in base_link frame).

          Example of Pose at the center of the table: Pose(Point((x_min+x_max)/2, (y_min+y_max)/2, z), Quaternion())
          Where z is the z component of the position in the PoseStamped. The frame_id is the same as the PoseStamped too.
          Example of pose at a certain distance of the table: Pose(Point(x_min-DIST_TO_TABLE, (y_min+y_max)/2, z), Quaternion())
    '''

    def __init__(self, recognize_objects=False):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted, 'no_table'],
                                    input_keys=[],
                                    output_keys=['tabletop_info'])

        with self:

            # HeadScan and Snapshot action call
            scan_table = PointHeadGoal()
            StateMachine.add('SCAN_TABLE',
                             SimpleActionState('/head_traj_controller/head_scan_snapshot_action',
                                               PointHeadAction,
                                               goal=scan_table),
                             transitions={succeeded: 'TABLE_DETECTION'})

            # TabletopDetection call
            detect_table = TabletopDetectionRequest()
            # Return the pointcloud (cluster) for each detected object
            # if this is false, you have no data to pass to tabletop_collision_map_processing node
            detect_table.return_clusters = recognize_objects
            # Return matching object models
            # Each cluster will have 1 or more models, even if the confidence rating is too low to display a marker in Rviz
            # If the household objects database is not connected, the model list will be empty
            detect_table.return_models = recognize_objects
            # Number of models to return for each object cluster
            # If there is more than 1 model with high confidence, they will all be displayed in Rviz
            detect_table.num_models = 1

            @smach.cb_interface(input_keys=[], output_keys=['tabletop_info'])
            def table_response_cb(userdata, response):
                if response.detection.result == response.detection.SUCCESS:
                    if recognize_objects:
                        userdata.tabletop_info = [response.detection]  # Return table and detected objects
                    else:
                        userdata.tabletop_info = [response.detection.table]  # Return only the table
                    return succeeded
                userdata.tabletop_info = [response.detection]
                return aborted

            StateMachine.add('TABLE_DETECTION', ServiceState('/object_detection', TabletopDetection,
                                                             request=detect_table, response_cb=table_response_cb,
                                                             output_keys=['tabletop_info']),
                             remapping={'tabletop_info': 'tabletop_info'},
                             transitions={succeeded: succeeded, aborted: 'CHECK_RESPONSE'})

            # Check why it failed
            @smach.cb_interface(input_keys=['tabletop_info'], output_keys=[], outcomes=[succeeded, 'no_table'])
            def check_tabletop_data(userdata):
                if userdata.tabletop_info[0].result == userdata.tabletop_info.NO_TABLE:
                   #or userdata.tabletop_info.result == userdata.tabletop_info.NO_CLOUD_RECEIVED:
                    return 'no_table'
                return aborted

            StateMachine.add('CHECK_RESPONSE', CBState(check_tabletop_data,
                                                       input_keys=['in_map', 'in_room_name'],
                                                       output_keys=['out_route'], outcomes=[aborted, 'no_table']),
                             remapping={'tabletop_info': 'tabletop_info'},
                             transitions={'no_table': 'no_table', aborted: aborted})
