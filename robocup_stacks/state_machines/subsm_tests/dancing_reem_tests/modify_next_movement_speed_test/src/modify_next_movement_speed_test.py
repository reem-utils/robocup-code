#! /usr/bin/env python

import roslib; roslib.load_manifest('modify_next_movement_speed_test')
import rospy
import smach
import smach_ros
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from handle_dancing_movement_files import HandleDancingMovementFiles

SONG_BPM_DUMB = 120.0
SONG_MOVEMENT_INIT_DUMB = "testing_empty_movement1.xml"
SONG_MOVEMENT_DUMB = "testing_empty_movement2.xml"
PREV_CURRENT_POS = "initial"
TESTING = True
BEAT_HARMONIC = 1.0


class PrintUserData1(smach.State):

    def __init__(self,
                message_name1='Message1'):
            smach.State.__init__(self,
                    outcomes=[succeeded, preempted, aborted],
                    input_keys=['message1'])

            self._message_name1 = message_name1

    def execute(self, userdata):
            rospy.loginfo('This is the %s: %s' % (self._message_name1, str(userdata.message1)))
            return succeeded


class ModifMovSpeedInitDummyState(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                            outcomes=[succeeded, preempted, aborted],
                            output_keys=['song_bpm', 'selected_movement', 'prev_current_position'])

    def execute(self, userdata):

        userdata.song_bpm = SONG_BPM_DUMB
        userdata.selected_movement = SONG_MOVEMENT_INIT_DUMB
        userdata.prev_current_position = PREV_CURRENT_POS
        return succeeded


class ModifMovSpeedDummyState(smach.State):

    def __init__(self):
        smach.State.__init__(self,
                            outcomes=[succeeded, preempted, aborted],
                            output_keys=['song_bpm', 'selected_movement', 'prev_current_position'])

    def execute(self, userdata):

        userdata.song_bpm = SONG_BPM_DUMB
        userdata.selected_movement = SONG_MOVEMENT_DUMB
        userdata.prev_current_position = PREV_CURRENT_POS
        return succeeded


def main():
    rospy.init_node('sm_modify_next_movement_speed_test')

    sm = smach.StateMachine(outcomes=[succeeded, aborted, preempted])

    with sm:

        smach.StateMachine.add('INITIALISE_DUMMY_STATE',
                                ModifMovSpeedInitDummyState(),
                                transitions={succeeded: 'MODIFY_NEXT_MOVEMENT_SPEED_1',
                                                preempted: preempted,
                                                aborted: aborted},
                                remapping={'song_bpm': 'song_bpm',
                                            'selected_movement': 'selected_movement',
                                            'prev_current_position': 'prev_current_position'})

        smach.StateMachine.add('MODIFY_NEXT_MOVEMENT_SPEED_1',
                                HandleDancingMovementFiles(TESTING, BEAT_HARMONIC),
                                transitions={succeeded: 'PRINT_DATA_1',
                                            'ended': 'PRINT_DATA_2',
                                            preempted: preempted,
                                            aborted: aborted},
                                remapping={'in_bpm_to_use': 'song_bpm',
                                            'in_movement_to_modifie': 'selected_movement',
                                            'in_actual_pos': 'prev_current_position',
                                            'modified_movement_name_path_out': 'next_movement_name_path'})

        smach.StateMachine.add('PRINT_DATA_1',
                                PrintUserData1('next_movement_name_path'),
                                transitions={
                                    succeeded: 'MODIF_MOV_SPEED_DUMMY_STATE_2',
                                    preempted: preempted,
                                    aborted: aborted},
                                remapping={'message1': 'next_movement_name_path'})

        smach.StateMachine.add('MODIF_MOV_SPEED_DUMMY_STATE_2',
                                ModifMovSpeedDummyState(),
                                transitions={succeeded: 'MODIFY_NEXT_MOVEMENT_SPEED_1',
                                                preempted: preempted,
                                                aborted: aborted},
                                remapping={'song_bpm': 'song_bpm',
                                            'selected_movement': 'selected_movement',
                                            'prev_current_position': 'prev_current_position'})

        smach.StateMachine.add('PRINT_DATA_2',
                                PrintUserData1('next_movement_name_path'),
                                transitions={
                                    succeeded: succeeded,
                                    preempted: preempted,
                                    aborted: aborted},
                                remapping={'message1': 'next_movement_name_path'})

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
