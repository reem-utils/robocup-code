#!/usr/bin/python
import roslib; roslib.load_manifest('iri_common_smach')
import rospy
import smach
import smach_ros

from iri_common_smach.st_get_list_of_stamped_poses_from_csv_file import GetListOfPoseStampedFromCsvFile

import csv

class PrintOutData(smach.State):
    """
    PRINTS OUT THE INPUT DATA 
   
    @type  data: anything that can be printed 
    @param data: variable to be printed 

    """
    def __init__(self):
        smach.State.__init__(self,
                             outcomes = ['success'],
                             input_keys = ['data'],
                             output_keys = [ ])

    def execute(self, userdata):
        rospy.loginfo('Executing PrintOutData')
        
        print userdata.data
        return 'success'



def construct_main_sm():
    # MAIN STATE MACHINE
    sm = smach.StateMachine(outcomes = ['succeeded','aborted'])

    with sm:
            smach.StateMachine.add('GET_LIST_OF_POSE', GetListOfPoseStampedFromCsvFile('./list_of_stamped_poses.csv'),
                                   transitions = {'success' : 'PRINT_LIST_OF_POSES',
                                                  'fail'    : 'aborted',},
                                   remapping   = {'list_of_stpose' : 'list'})

            smach.StateMachine.add('PRINT_LIST_OF_POSES', PrintOutData(),
                                   transitions = {'success' : 'succeeded'},
                                   remapping   = {'data' : 'list'})

    return sm

def main():
    rospy.init_node("get_list_of_stamped_poses_from_csv_file")
    sm_main = construct_main_sm()

    # Run state machine introspection server for smach viewer
    sis = smach_ros.IntrospectionServer('get_list_of_stamped_poses_from_csv_file', sm_main,
                                        '/get_list_of_stamped_poses_from_csv_file')

    sis.start()

    outcome = sm_main.execute()

    rospy.spin()
    sis.stop()

if __name__ == "__main__":
    main()

