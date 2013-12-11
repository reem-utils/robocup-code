import roslib
roslib.load_manifest('dancing_reem')
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.time_out import TimeOutState
from pal_smach_utils.utils.bpm_conversions import BpmToPeriod
from pal_smach_utils.utils.time_controlling_states import GetCurrentROSTimeState


ENABLE_CORRECTING_BEAT = False
WHAT_TO_LOOK_FOR_IN_MOVEMENTS = 'delta_time'
# False movements means the movements that although they have a time they wont be made because
# Reem is already there.
NUMBER_OF_FALSE_MOVEMENTS = 0
SECURITY_TIME = 0.0

class CalculateHowManySecondToWait(smach.State):
    def __init__(self, harmonic=1.0):
        smach.State.__init__(self,
                             outcomes=['wait_time', 'do_not_wait', preempted, aborted],
                             input_keys=['in_time_sent_last_movement',
                                         'in_next_movement_name_path',
                                         'in_repeat',
                                         'in_bpm'],
                             output_keys=['time_to_wait_out'])
        self._harmonic = harmonic

    def execute(self, userdata):

        file_path = userdata.in_next_movement_name_path
        #rospy.loginfo("MOVEMENT THAT WE ARE WAITING FOR, THAT IS EXECUTING RIGHT NOW ========> " + str(file_path))
        movement_string = open(file_path, 'r').read()
        number_submovements = movement_string.count(WHAT_TO_LOOK_FOR_IN_MOVEMENTS)
        #rospy.loginfo("HOW MANY SUB MOVEMENTS HAS THIS FILE ========> " + str(number_submovements))
        #rospy.loginfo("HOW MANY SUB MOVEMENTS CONSIDER FALSE ========> " + str(NUMBER_OF_FALSE_MOVEMENTS))

        time_length_movement = BpmToPeriod(userdata.in_bpm, self._harmonic)
        number_movements_end = number_submovements - NUMBER_OF_FALSE_MOVEMENTS
        if number_submovements == 0:
            number_movements_end = 0

        movement_duration_seconds = (number_movements_end) * time_length_movement + SECURITY_TIME
        #rospy.loginfo("CALCULATION ========> ( " + str(number_submovements) + " - " + str(NUMBER_OF_FALSE_MOVEMENTS) + " ) * " + str(time_length_movement))

        now = rospy.Time.now()
        #rospy.loginfo("ROS TIME NOW ========> " + str(now))
        last_time_sent_movement = userdata.in_time_sent_last_movement
        #rospy.loginfo("LAST TIME ===========> " + str(last_time_sent_movement))
        time_elapsed_seconds = (now - last_time_sent_movement)
        #rospy.loginfo("Time ELAPSED seconds ========> " + str(time_elapsed_seconds.to_sec()))
        #rospy.loginfo("Time MOVEMENT DURATION seconds ========> " + str(movement_duration_seconds))
        final_time_to_wait = movement_duration_seconds - time_elapsed_seconds.to_sec()

        if final_time_to_wait < 0.0:
            rospy.loginfo("TIME NEGATIVE; YOU ARE TOO SLOW")
            final_time_to_wait = 0.0
            rospy.loginfo("Time to WAIT before sending another movement ========> " + str(final_time_to_wait))
            userdata.time_to_wait_out = final_time_to_wait
            return 'do_not_wait'

        if userdata.in_repeat:
            rospy.loginfo("REPEATING MOVEMENT ##########")
            final_time_to_wait = final_time_to_wait * 2.0

        rospy.loginfo("Time to WAIT before sending another movement ========> " + str(final_time_to_wait))
        userdata.time_to_wait_out = final_time_to_wait

        return 'wait_time'


class WaitToSendNextMovement(smach.StateMachine):

    """
    Given the complete absolute path of the xml file that describes the movement,
    Its sends it to the robot to be executed.
    ITS SENDED WITH NO TRAJECTORY VALIDATION, which means that it won't validate
    if there is an obstacle in the way of the movement or not!
    """

    def __init__(self, harmonic=1.0):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                                    input_keys=['in_time_sent_last_movement',
                                                'in_old_file_name',
                                                'in_repeat',
                                                'in_bpm'],
                                    output_keys=['time_sent_last_movement_out'])

        self._harmonic = harmonic

        with self:

            smach.StateMachine.add('CALCULATE_HOW_MANY_SECOND_TO_WAIT',
                                   CalculateHowManySecondToWait(self._harmonic),
                                   transitions={'wait_time': 'WAIT',
                                                'do_not_wait': 'LOOK_TIME',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_time_sent_last_movement': 'in_time_sent_last_movement',
                                              'in_next_movement_name_path': 'in_old_file_name',
                                              'in_repeat': 'in_repeat',
                                              'in_bpm': 'in_bpm',
                                              'time_to_wait_out': 'time_to_wait'})

            smach.StateMachine.add('WAIT',
                                   TimeOutState(),
                                   transitions={succeeded: 'LOOK_TIME',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'time_wait': 'time_to_wait'})

            smach.StateMachine.add('LOOK_TIME',
                                   GetCurrentROSTimeState(),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'starting_ros_time_out': 'time_sent_last_movement_out'})
