#! /usr/bin/env python

import roslib
roslib.load_manifest('clean_up')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.utils.check_dependences import CheckDependencesState
from pal_smach_utils.utils.robot_controllers_activation import StopRobotControllers
#from pal_smach_utils.utils.run_script_on_robot import RunScriptOnRobot
#from pal_smach_utils.utils.run_script_local import RunScriptLocal
from clean_up import CleanUp


def main():
    rospy.init_node('clean_up_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        TOPICS = ["/usersaid", "tf"]
        ACTIONS = ["/sound", "/move_base", "/move_by/move_base", "/move_right_arm_torso", "/right_hand_controller/follow_joint_trajectory",
                   "/left_hand_controller/follow_joint_trajectory"]
        SERVICES = ["/object_translator", "/object_translator_dataBase", "/get_next_probable_location", "/loc_translator"]
        MAP_LOC = ["kitchen", "exit"]
        cds = CheckDependencesState(topic_names=TOPICS, service_names=SERVICES, action_names=ACTIONS, map_locations=MAP_LOC)
        smach.StateMachine.add('CHECK_DEPENDENCES', cds,
                               #transitions={aborted: 'START_GRASPING',  # aborted,
                               #             succeeded: 'START_GRASPING'})
                               transitions={aborted: 'CLEAN_UP_TEST',  # aborted,
                                            succeeded: 'CLEAN_UP_TEST'})

        '''# We told grasping should be already running!
        smach.StateMachine.add('START_GRASPING',
                               #RunScriptOnRobot(script_name='graspingStart.sh'),
                               RunScriptLocal('graspingStart.sh'),
                               transitions={succeeded: 'CLEAN_UP_TEST', aborted: aborted})'''

        smach.StateMachine.add('CLEAN_UP_TEST',
                               CleanUp(),
                               #transitions={succeeded: 'STOP_GRASPING', preempted: 'STOP_GRASPING', aborted: 'STOP_GRASPING'})
                               transitions={succeeded: 'STOP_CONTROLLERS', preempted: 'STOP_CONTROLLERS', aborted: 'STOP_CONTROLLERS'})

        '''#If we don't start grasping, I suppose we shouldn't stop it, is it?
        smach.StateMachine.add('STOP_GRASPING',
                               # RunScriptOnRobot(script_name="graspingStop.sh"),
                               RunScriptLocal(script_name="graspingStop.sh"),
                               transitions={succeeded: 'STOP_CONTROLLERS', aborted: succeeded})'''

        smach.StateMachine.add('STOP_CONTROLLERS', StopRobotControllers(head=True, left=True, right=True),
                               transitions={succeeded: succeeded, preempted: preempted, aborted: aborted})

    sis = smach_ros.IntrospectionServer(
        'clean_up_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
