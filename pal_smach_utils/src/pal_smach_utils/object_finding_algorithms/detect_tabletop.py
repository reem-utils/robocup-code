#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
from smach import StateMachine, CBState
from smach_ros import ServiceState, SimpleActionState

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
import pal_smach_utils.object_finding_algorithms.ofb_utils as ofb_utils
#from pr2_controllers_msgs.msg import PointHeadGoal, PointHeadAction  # To use the /head_traj_controller/point_head_action
from pr2_controllers_msgs.msg import JointTrajectoryGoal, JointTrajectoryAction  # To use with the joint_trajectory action
from trajectory_msgs.msg import JointTrajectoryPoint
from tabletop_object_detector.srv import TabletopDetection, TabletopDetectionRequest
from pal_smach_utils.object_finding_algorithms.take_snapshot import TakeXtionSnapshot

HEAD_ACTION_NAME = '/head_traj_controller/joint_trajectory_action'
HEAD_ACTION_TYPE = JointTrajectoryAction
LOOK_TIME = 1  # Time in seconds for the transition to the new looking position
WAIT_BEFORE_SNAPSHOT = 2.0  # Seconds to wait before taking a Snapshot


class DetectTabletop(smach.StateMachine):

    '''
    Performs three looks and makes snapshots of the pointcloud and then calls to the TabletopDetection service.

    If the parameter recognize_objects is True, the output key tabletop_info is a list of messages of type
        tabletop_object_detector/TabletopDetectionResult that contains the results of the detection.
    If the parameter recognize_objects is False, the output key tabletop_info is a list of messages of type
        tabletop_object_detector/Table that contains the results of the detected table.
    It outcomes 'no_table' if it didn't find a table, aborted if something else failed and succeeded if there was no problem.

    If the outcome is 'no_table' or aborted, the output key tabletop_info is an empty list.

    Note: to have the position of the table, the values to be used are the "x_min, y_min, x_max and y_max" of the Table message.
          The PoseStamped of the message is needed to have the z component and the Header message with the frame_id.
          The other coordinates of the PoseStamped are not used (x and y are almost 0 in base_link frame).

          Example of Pose at the center of the table: Pose(Point((x_min+x_max)/2, (y_min+y_max)/2, z), Quaternion())
          Where z is the z component of the position in the PoseStamped. The frame_id is the same as the PoseStamped too.
          Example of pose at a certain distance of the table: Pose(Point(x_min-DIST_TO_TABLE, (y_min+y_max)/2, z), Quaternion())
    '''

    def __init__(self, distance_treshold=0.5, recognize_objects=False):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted, 'no_table'],
                                    input_keys=[],
                                    output_keys=['tabletop_info'])

        with self:
            @smach.cb_interface(input_keys=[], output_keys=['out_tabletop_info', 'out_n_looks'],
                                outcomes=[succeeded])
            def init_udata(userdata):
                userdata.out_n_looks = 0  # Number of looks done
                userdata.out_tabletop_info = []  # To be filled in the GATHER_TTOP_DATA state
                return succeeded

            StateMachine.add('INIT_USERDATA', CBState(init_udata, output_keys=['out_tabletop_info', 'out_n_looks'],
                                                      outcomes=[succeeded]),
                             remapping={'out_tabletop_info': 'tabletop_info',
                                        'out_n_looks': 'n_looks'},
                             transitions={succeeded: 'CONTROL_STATE'})

            @smach.cb_interface(input_keys=['in_n_looks', 'in_tabletop_info'],
                                output_keys=['look_goal', 'out_n_looks'], outcomes=[succeeded, 'next', 'no_table'])
            def control_cb(userdata):
                if userdata.in_n_looks == 0:  # first look
                    userdata.look_goal = look_right().trajectory
                elif userdata.in_n_looks == 1:  # Second look
                    userdata.look_goal = look_straight().trajectory
                elif userdata.in_n_looks == 2:  # Third look
                    userdata.look_goal = look_left().trajectory
                else:  # Finished all the looks
                    if not userdata.in_tabletop_info:
                        return 'no_table'
                    return succeeded
                userdata.out_n_looks = userdata.in_n_looks + 1
                return 'next'

            StateMachine.add('CONTROL_STATE', CBState(control_cb,
                                                      input_keys=['n_looks'],
                                                      output_keys=['look_goal'],
                                                      outcomes=[succeeded, 'next', 'no_table']),
                             transitions={'next': 'LOOK_STATE',
                                          succeeded: succeeded,
                                          'no_table': 'no_table'},
                             remapping={'in_n_looks': 'n_looks', 'out_n_looks': 'n_looks',
                                        'look_goal': 'look_goal',
                                        'in_tabletop_info': 'tabletop_info'})

            # Move the head before detecting table
            StateMachine.add('LOOK_STATE',
                             SimpleActionState(HEAD_ACTION_NAME,
                                               HEAD_ACTION_TYPE,
                                               goal_slots=['trajectory']),
                             transitions={succeeded: 'TAKE_SNAPSHOT'},
                             remapping={'trajectory': 'look_goal'})

            StateMachine.add('TAKE_SNAPSHOT', TakeXtionSnapshot(WAIT_BEFORE_SNAPSHOT),
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

            @smach.cb_interface(input_keys=[], output_keys=['tabletop_response'])
            def table_response_cb(userdata, response):
                if response.detection.result == response.detection.SUCCESS:
                    if recognize_objects:
                        userdata.tabletop_response = response.detection  # Return table and detected objects
                    else:
                        userdata.tabletop_response = response.detection.table  # Return only the table
                    return succeeded
                userdata.tabletop_response = response.detection
                return aborted

            StateMachine.add('TABLE_DETECTION', ServiceState('/object_detection', TabletopDetection,
                                                             request=detect_table, response_cb=table_response_cb,
                                                             output_keys=['tabletop_response']),
                             remapping={'tabletop_response': 'tabletop_response'},
                             transitions={succeeded: 'GATHER_TTOP_DATA', aborted: 'CHECK_FAILURE'})

            # Check why it failed
            @smach.cb_interface(input_keys=['tabletop_response'], output_keys=[], outcomes=[succeeded, 'no_table'])
            def check_if_no_table(userdata):
                if userdata.tabletop_response.result == userdata.tabletop_response.NO_TABLE:
                   #or userdata.tabletop_response.result == userdata.tabletop_response.NO_CLOUD_RECEIVED:
                    return 'no_table'
                print 'Tabletop detection aborted with status: %s' % userdata.tabletop_response.result
                return aborted

            StateMachine.add('CHECK_FAILURE', CBState(check_if_no_table,
                                                      input_keys=[],
                                                      output_keys=['out_route'], outcomes=[aborted, 'no_table']),
                             remapping={'tabletop_response': 'tabletop_response'},
                             transitions={'no_table': 'CONTROL_STATE', aborted: aborted})

            @smach.cb_interface(input_keys=['in_tabletop_info', 'in_tabletop_response'], output_keys=['out_tabletop_info'],
                                outcomes=[succeeded])
            def check_gather_data(userdata):
                table_data = userdata.in_tabletop_response

                table_orient = table_data.pose.pose.orientation
                if table_orient.w < 0.95 or table_orient.x > 0.05 or table_orient.y > 0.05 or table_orient.z > 0.05:
                    # The surface is not horizontal, so we don't care about it.
                    print 'It was not a table...'
                    return succeeded

                table_pose = ((table_data.x_min+table_data.x_max)/2, (table_data.y_min+table_data.y_max)/2)

                for ti in userdata.in_tabletop_info:
                    tp = ((ti.x_min+ti.x_max)/2, (ti.y_min+ti.y_max)/2)
                    if ofb_utils.euclidean_distance(tp, table_pose) <= distance_treshold:
                        break
                else:  # The loop ended without breaking
                    userdata.in_tabletop_info.append(userdata.in_tabletop_response)
                    userdata.out_tabletop_info = userdata.in_tabletop_info
                return succeeded
            StateMachine.add('GATHER_TTOP_DATA', CBState(check_gather_data,
                                                         input_keys=['in_tabletop_info', 'tabletop_response'],
                                                         output_keys=['out_tabletop_info'],
                                                         outcomes=[succeeded]),
                             remapping={'in_tabletop_response': 'tabletop_response',
                                        'in_tabletop_info': 'tabletop_info',
                                        'out_tabletop_info': 'tabletop_info'},
                             transitions={succeeded: 'CONTROL_STATE'})


# Default head actions
#positions[0]: 1.0 == all left, 0.0 = middle, -1.0 = all right
#positions[1]: 1.0 == all down, 0.0 = middle, -1.0 = all up
def look_straight():
    res = JointTrajectoryGoal()
    res.trajectory.joint_names = ['head_1_joint', 'head_2_joint']
    res.trajectory.points = [JointTrajectoryPoint()]
    res.trajectory.points[0].positions = [0.0, 0.0]
    res.trajectory.points[0].velocities = [0.0, 0.0]
    res.trajectory.points[0].time_from_start = rospy.Duration(LOOK_TIME, 0)
    return res


def look_right():
    res = JointTrajectoryGoal()
    res.trajectory.joint_names = ['head_1_joint', 'head_2_joint']
    res.trajectory.points = [JointTrajectoryPoint()]
    res.trajectory.points[0].positions = [-0.55, 0.0]
    res.trajectory.points[0].velocities = [0.0, 0.0]
    res.trajectory.points[0].time_from_start = rospy.Duration(LOOK_TIME, 0)
    return res


def look_left():
    res = JointTrajectoryGoal()
    res.trajectory.joint_names = ['head_1_joint', 'head_2_joint']
    res.trajectory.points = [JointTrajectoryPoint()]
    res.trajectory.points[0].positions = [0.55, 0.0]
    res.trajectory.points[0].velocities = [0.0, 0.0]
    res.trajectory.points[0].time_from_start = rospy.Duration(LOOK_TIME, 0)
    return res
