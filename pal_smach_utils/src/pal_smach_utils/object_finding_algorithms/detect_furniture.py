#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy
from smach import StateMachine, CBState
from smach_ros import ServiceState, SimpleActionState

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted, transform_pose
import pal_smach_utils.object_finding_algorithms.ofb_utils as ofb_utils
#from pr2_controllers_msgs.msg import PointHeadGoal, PointHeadAction  # To use the /head_traj_controller/point_head_action
from pr2_controllers_msgs.msg import JointTrajectoryGoal, JointTrajectoryAction  # To use with the joint_trajectory action
from trajectory_msgs.msg import JointTrajectoryPoint
from furniture_detector_service.srv import FurnitureDetection
from pal_smach_utils.object_finding_algorithms.take_snapshot import TakeXtionSnapshot

HEAD_ACTION_NAME = '/head_traj_controller/joint_trajectory_action'
HEAD_ACTION_TYPE = JointTrajectoryAction
LOOK_TIME = 1  # Time in seconds for the transition to the new looking position
WAIT_BEFORE_SNAPSHOT = 2.0  # Seconds to wait before taking a Snapshot


class DetectFurniture(smach.StateMachine):

    '''
    Performs three looks and makes snapshots of the pointcloud and then calls to the FurnitureDetection service.

    It output a list of (name, pose) with a strig and a PoseStamped with the detected data in the key furniture_info.

    It outcomes 'no_furniture' if it didn't find any furniture, aborted if something else failed and succeeded if there was no problem.

    If the outcome is 'no_furniture' or aborted, the output key furniture_info is an empty list.
    '''

    def __init__(self, distance_treshold=0.5):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted, 'no_furniture'],
                                    input_keys=[],
                                    output_keys=['furniture_info'])

        with self:
            @smach.cb_interface(input_keys=[], output_keys=['out_furniture_info', 'out_n_looks'],
                                outcomes=[succeeded])
            def init_udata(userdata):
                userdata.out_n_looks = 0  # Number of looks done
                userdata.out_furniture_info = []  # To be filled in the GATHER_TTOP_DATA state
                return succeeded

            StateMachine.add('INIT_USERDATA', CBState(init_udata, output_keys=['out_furniture_info', 'out_n_looks'],
                                                      outcomes=[succeeded]),
                             remapping={'out_furniture_info': 'furniture_info',
                                        'out_n_looks': 'n_looks'},
                             transitions={succeeded: 'CONTROL_STATE'})

            @smach.cb_interface(input_keys=['in_n_looks', 'in_furniture_info'],
                                output_keys=['look_goal', 'out_n_looks'], outcomes=[succeeded, 'next', 'no_furniture'])
            def control_cb(userdata):
                if userdata.in_n_looks == 0:  # first look
                    userdata.look_goal = look_right().trajectory
                elif userdata.in_n_looks == 1:  # Second look
                    userdata.look_goal = look_straight().trajectory
                elif userdata.in_n_looks == 2:  # Third look
                    userdata.look_goal = look_left().trajectory
                else:  # Finished all the looks
                    if not userdata.in_furniture_info:
                        return 'no_furniture'
                    return succeeded
                userdata.out_n_looks = userdata.in_n_looks + 1
                return 'next'

            StateMachine.add('CONTROL_STATE', CBState(control_cb,
                                                      input_keys=['n_looks'],
                                                      output_keys=['look_goal'],
                                                      outcomes=[succeeded, 'next', 'no_furniture']),
                             transitions={'next': 'LOOK_STATE',
                                          succeeded: succeeded,
                                          'no_furniture': 'no_furniture'},
                             remapping={'in_n_looks': 'n_looks', 'out_n_looks': 'n_looks',
                                        'look_goal': 'look_goal',
                                        'in_furniture_info': 'furniture_info'})

            # Move the head before detecting furniture
            StateMachine.add('LOOK_STATE',
                             SimpleActionState(HEAD_ACTION_NAME,
                                               HEAD_ACTION_TYPE,
                                               goal_slots=['trajectory']),
                             transitions={succeeded: 'TAKE_SNAPSHOT'},
                             remapping={'trajectory': 'look_goal'})

            StateMachine.add('TAKE_SNAPSHOT', TakeXtionSnapshot(WAIT_BEFORE_SNAPSHOT),
                             transitions={succeeded: 'WAIT_FOR_FURNITURE'})

            #Wait state because if the funiture callback is slower than the transition between states.
            wait_time = 0.35

            @smach.cb_interface(outcomes=[succeeded])
            def wait(userdata):
                rospy.sleep(wait_time)
                return succeeded

            StateMachine.add('WAIT_FOR_FURNITURE', CBState(wait, outcomes=[succeeded]),
                             transitions={succeeded: 'FURNITURE_DETECTION'})

            @smach.cb_interface(input_keys=[], output_keys=['furniture_response'])
            def furniture_response_cb(userdata, response):
                if response.status == response.SUCCESS:
                    userdata.furniture_response = (response.furn_names, response.poses)  # Join the two lists to transfer them.
                    return succeeded
                return aborted

            StateMachine.add('FURNITURE_DETECTION', ServiceState('/furniture_classification', FurnitureDetection,
                                                                 response_cb=furniture_response_cb,
                                                                 output_keys=['furniture_response']),
                             remapping={'furniture_response': 'furniture_response'},
                             transitions={succeeded: 'GATHER_FURNITURE_DATA', aborted: 'CONTROL_STATE'})

            @smach.cb_interface(input_keys=['in_furniture_info', 'in_furniture_response'], output_keys=['out_furniture_info'],
                                outcomes=[succeeded])
            def check_gather_data(userdata):
                furn_names = userdata.in_furniture_response[0]
                furn_poses = userdata.in_furniture_response[1]

                for i in xrange(len(furn_names)):
                    i_pose = (furn_poses[i].pose.position.x, furn_poses[i].pose.position.y)
                    for n, p in userdata.in_furniture_info:
                        p_pose = (p.pose.position.x, p.pose.position.y)
                        if (furn_names[i] == n) and (ofb_utils.euclidean_distance(p_pose, i_pose) <= distance_treshold):
                            break
                    else:  # The loop ended without breaking
                        furn_poses[i].pose = transform_pose(furn_poses[i].pose, furn_poses[i].header.frame_id, '/base_link', timeout=3)
                        furn_poses[i].header.frame_id = '/base_link'
                        userdata.in_furniture_info.append((furn_names[i], furn_poses[i]))
                        userdata.out_furniture_info = userdata.in_furniture_info
                return succeeded

            StateMachine.add('GATHER_FURNITURE_DATA', CBState(check_gather_data,
                                                              input_keys=['in_furniture_info', 'furniture_response'],
                                                              output_keys=['out_furniture_info'],
                                                              outcomes=[succeeded]),
                             remapping={'in_furniture_response': 'furniture_response',
                                        'in_furniture_info': 'furniture_info',
                                        'out_furniture_info': 'furniture_info'},
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
