import roslib
roslib.load_manifest('dancing_reem')
import smach

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
#This pal_control will burst if mock update isnt made.
from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction
from smach_ros import SimpleActionState
from send_mov import SendMov
from wait_to_send_next_movement import WaitToSendNextMovement
from write_old_movement import WriteOldMovement


class ExecuteMovement(smach.StateMachine):

    """
    Given the complete absolute path of the xml file that describes the movement,
    Its sends it to the robot to be executed.
    ITS SENDED WITH NO TRAJECTORY VALIDATION, which means that it won't validate
    if there is an obstacle in the way of the movement or not!
    """

    def __init__(self, harmonic=1.0):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                                    input_keys=['in_old_movement_name_path',
                                                'in_time_sent_last_movement',
                                                'in_next_movement_name_path',
                                                'in_repeat',
                                                'in_execute_bpm'],
                                    output_keys=['time_sent_last_movement_out',
                                                 'old_movement_name_path_out'])

        self._harmonic = harmonic

        with self:
            
            smach.StateMachine.add('WAIT_TO_SEND_NEXT_MOVEMENT',
                                   WaitToSendNextMovement(self._harmonic),
                                   transitions={succeeded: 'EXECUTE_MOVEMENT',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_time_sent_last_movement': 'in_time_sent_last_movement',
                                              'in_old_file_name': 'in_old_movement_name_path',
                                              'in_repeat': 'in_repeat',
                                              'in_bpm': 'in_execute_bpm',
                                              'time_sent_last_movement_out': 'time_sent_last_movement_out'})
 
            smach.StateMachine.add('EXECUTE_MOVEMENT',
                                   SendMov(),
                                   transitions={succeeded: 'WRITE_OLD_MOVEMENT',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'file_name': 'in_next_movement_name_path',
                                              'repeat': 'in_repeat'})
            """
            #Deprecated Because it stops between movements around 3 seconds.
            def bow_motion_goal_cb(userdata, goal):
                movement_goal = MotionManagerGoal()
                movement_goal.plan = False
                movement_goal.filename = userdata.file_name
                movement_goal.checkSafety = False
                movement_goal.repeat = False
                movement_goal.priority = 0
                return movement_goal
            smach.StateMachine.add('EXECUTE_MOVEMENT',
                                   SimpleActionState('/motion_manager',
                                                     MotionManagerAction,
                                                     goal_cb=bow_motion_goal_cb,
                                                     input_keys=['file_name']),
                                   transitions={succeeded: 'WRITE_OLD_MOVEMENT',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'file_name': 'in_next_movement_name_path'})

            """
            smach.StateMachine.add('WRITE_OLD_MOVEMENT',
                                   WriteOldMovement(),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_file_name': 'in_next_movement_name_path',
                                              'old_file_name_out': 'old_movement_name_path_out'})
