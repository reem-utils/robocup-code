#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib
roslib.load_manifest('robot_inspection')
import rospy
import smach
import smach_ros
import dynamic_reconfigure.client
from rospy.rostime import Duration

#from tibi_dabo_msgs.msg import sequenceAction, sequenceGoal
from smach_ros import SimpleActionState, ServiceState
from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine
from pal_smach_utils.speech.sound_action import SpeakActionState, SpeakActionFromPoolStateMachine
from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction
from pal_smach_utils.navigation.enter_room import EnterRoomStateMachine
from pal_smach_utils.speech.speak_and_motion_action import SpeakAndMotionActionConcurrentSM
from pal_smach_utils.speech.listen_general_command import RecogCommand
from pal_smach_utils.grasping.st_reem_hand import OpenReemHand2, CloseReemHand
from std_srvs.srv import Empty


# imports from PALs code
#from presentation.smach_presentation_utils import *
#from handshaking.smach_handshaking_utils import *
#  from pal_vision_msgs import *


MOTION_FOLDER_PATH = "/mnt_flash/etc/control/robot/reemh3/motion/"
LEAVING_DOOR_NAME = "exit"
PRE_EXIT_NAME = "pre_exit"
REGISTRATION_TABLE_NAME = "registration table"
DOOR_DISTANCE = 1.5


# main
def main():
    rospy.init_node('robot_inspection')

    # Create a SMACH state machine
    sm = smach.StateMachine(['succeeded', 'aborted', 'preempted'])

    with sm:  # FIXME Do all the speak actions and motion actions simultanously??

        smach.StateMachine.add('CLOSE_HAND', CloseReemHand(), transitions={'succeeded': 'STARTING_SPEECH', 'aborted': 'STARTING_SPEECH'})

        ## Indicate that we are starting
        smach.StateMachine.add('STARTING_SPEECH', SpeakActionState(text="I am ready to start the registration. I will now go to the registration desk.",
                                                                   wait_before_speaking=Duration(1.0)),
                               transitions={'succeeded': 'ENTER_ROOM',
                                            'aborted': 'ENTER_ROOM'})

        # Enters into the room through the door
        smach.StateMachine.add('ENTER_ROOM',
                               EnterRoomStateMachine(distance=DOOR_DISTANCE, orient_after_passing=0.0),
                               transitions={'succeeded': 'ENABLE_REEM_ALIVE'})

        smach.StateMachine.add('ENABLE_REEM_ALIVE',
                               ServiceState('/alive_engine/start', Empty),
                               transitions={'succeeded': 'MOVE_TO_REG_TABLE', 'aborted': 'MOVE_TO_REG_TABLE'})

        # Go to table
        sm.userdata.registration_table = REGISTRATION_TABLE_NAME
        smach.StateMachine.add('MOVE_TO_REG_TABLE',
                               MoveToRoomStateMachine(announcement=None),
                               transitions={'succeeded': 'DISABLE_REEM_ALIVE',
                                            'aborted': 'MOVE_TO_REG_TABLE'},
                               remapping={'room_name': 'registration_table'})

        smach.StateMachine.add('DISABLE_REEM_ALIVE',
                               ServiceState('/alive_engine/stop',
                                            Empty),
                               transitions={'succeeded': 'MOVE_TO_BOW', 'aborted': 'MOVE_TO_BOW'})

        # Bow to face
        filename = MOTION_FOLDER_PATH + "bow.xml"
        bow_motion_goal = MotionManagerGoal()
        bow_motion_goal.plan = False
        bow_motion_goal.filename = filename
        bow_motion_goal.checkSafety = False
        bow_motion_goal.repeat = False
        bow_motion_goal.priority = 0
        bow_action = SimpleActionState('/motion_manager', MotionManagerAction,
                                       goal=bow_motion_goal)
        smach.StateMachine.add('MOVE_TO_BOW', bow_action,
                               transitions={'succeeded': 'PRESENT_REEM',
                                            'aborted': 'PRESENT_REEM'})

        # Present the robot and the team
        present_text = 'Hi everybody! My name is REEM. I came here with my teammates from the REEM_@_EERI team!'
        smach.StateMachine.add('PRESENT_REEM', SpeakActionState(text=present_text,
                                                                wait_before_speaking=Duration(0.2)),
                               transitions={'succeeded': 'START_PRESENT',
                                            'aborted': 'PRESENT_REEM'})

        # Deliver the form and say something funny
        take_it_text = "Oh, you look really good today! This is my registration form. Please, take it."
        smach.StateMachine.add('SAY_HERE_CV', SpeakActionState(text=take_it_text, wait_before_speaking=Duration(0.10)),
                               transitions={'succeeded': 'OPEN_HAND', 'aborted': 'SAY_HERE_CV'})

        smach.StateMachine.add('START_PRESENT', SpeakAndMotionActionConcurrentSM(filename=MOTION_FOLDER_PATH + "robocup_start_presentation.xml", checksafety=False, plan=False,
                                                                                 text=take_it_text),
                               transitions={'succeeded': 'OPEN_HAND',
                                            'aborted': 'SAY_HERE_CV'})

        smach.StateMachine.add('OPEN_HAND', OpenReemHand2(), transitions={'succeeded': 'SAY_READ_AND_MID', 'aborted': 'SAY_READ_AND_MID'})

        read_this = "Please, can you read the form and tell my mates if there's anything wrong."
        smach.StateMachine.add('SAY_READ_AND_MID', SpeakAndMotionActionConcurrentSM(filename=MOTION_FOLDER_PATH + "robocup_middle_presentation.xml", checksafety=False, plan=False,
                                                                                    text=read_this, wait_before_speaking=Duration(1.0)),
                               transitions={'succeeded': 'END_PRESENTATION_AND_THANK',
                                            'aborted': 'SAY_HERE_CV'})

        thank_you = "Thank you. Tell me when I should leave the arena."
        smach.StateMachine.add('END_PRESENTATION_AND_THANK', SpeakAndMotionActionConcurrentSM(filename=MOTION_FOLDER_PATH + "robocup_end_presentation.xml", checksafety=False, plan=False,
                                                                                              text=thank_you, wait_before_speaking=Duration(0.8)),
                               transitions={'succeeded': 'RE_ENABLE_REEM_ALIVE',
                                            'aborted': 'SAY_HERE_CV'})

        smach.StateMachine.add('RE_ENABLE_REEM_ALIVE',
                               ServiceState('/alive_engine/start', Empty),
                               transitions={'succeeded': 'WAIT_LISTEN_ORDER', 'aborted': 'WAIT_LISTEN_ORDER'})

        smach.StateMachine.add('WAIT_LISTEN_ORDER', RecogCommand(GRAMMAR_NAME='robocup/room', 
                                                                 command_key='location', command_value=LEAVING_DOOR_NAME,
                                                                 ask_for_confirmation=False),
                               transitions={'succeeded': 'BABY_DONT_HURT_ME', 'aborted': 'ASK_TO_REPEAT'})

        repeat_pool = ["Pardon?", "Can you repeat the name, please?",
                       "I'm sorry I didn't understand you. Can you repeat that?",
                       "I didn't get it. Can you please repeat?"]
        smach.StateMachine.add('ASK_TO_REPEAT',
                               SpeakActionFromPoolStateMachine(repeat_pool),
                               transitions={'succeeded': 'WAIT_LISTEN_ORDER', 'aborted': 'WAIT_LISTEN_ORDER'})

        baby_dont_hurt_me = "Okay. Please, Don't hurt me when you hit the emergency button."
        smach.StateMachine.add('BABY_DONT_HURT_ME', SpeakActionState(text=baby_dont_hurt_me, wait_before_speaking=Duration(0.20)),
                               transitions={'succeeded': 'SAY_AND_DO_BYE',
                                            'aborted': 'SAY_HERE_CV'})

        # Say Bye bye and move the hand
        smach.StateMachine.add('SAY_AND_DO_BYE', SpeakAndMotionActionConcurrentSM(filename=MOTION_FOLDER_PATH + "wave.xml", checksafety=False, plan=True,
                                                                                  text="Bye Bye!", wait_before_speaking=Duration(2.1)),
                               transitions={'succeeded': 'INTERACT_POS', 'aborted': 'INTERACT_POS'})

        interact_goal = MotionManagerGoal()
        interact_goal.plan = True
        interact_goal.filename = filename
        interact_goal.checkSafety = False
        interact_goal.repeat = False
        interact_goal.priority = 0
        interact_goal.filename = MOTION_FOLDER_PATH + 'interact.xml'
        smach.StateMachine.add('INTERACT_POS',
                               SimpleActionState('/motion_manager', MotionManagerAction, goal=interact_goal),
                               transitions={'succeeded': 'SLOW_SPEED', 'aborted': 'INTERACT_POS'})

        def slow_speed(userdata):
            node_to_reconfigure = "/move_base/PalLocalPlanner"
            client = dynamic_reconfigure.client.Client(node_to_reconfigure)
            new_params = {'max_vel_x': 0.2}
            client.update_configuration(new_params)
            return 'succeeded'

        smach.StateMachine.add('SLOW_SPEED', smach.CBState(slow_speed, outcomes=['succeeded']),
                               transitions={'succeeded': 'GO_PRE_EXIT'})

        # Go to the leaving door
        sm.userdata.pre_exit_door = PRE_EXIT_NAME
        smach.StateMachine.add('GO_PRE_EXIT', MoveToRoomStateMachine(announcement=None),
                               transitions={'succeeded': 'STOP_REEM_ALIVE',
                                            'aborted': 'CANT_LEAVE'},
                               remapping={'room_name': 'pre_exit_door'})

        smach.StateMachine.add('STOP_REEM_ALIVE',
                               ServiceState('/alive_engine/stop',
                                            Empty),
                               transitions={'succeeded': 'CROSSING_DOOR_POS', 'aborted': 'CROSSING_DOOR_POS'})

        rest_goal = MotionManagerGoal()
        rest_goal.plan = True
        rest_goal.filename = filename
        rest_goal.checkSafety = False
        rest_goal.repeat = False
        rest_goal.priority = 0
        rest_goal.filename = MOTION_FOLDER_PATH + 'rest.xml'
        smach.StateMachine.add('CROSSING_DOOR_POS', SimpleActionState('/motion_manager', MotionManagerAction,
                                                                      goal=rest_goal),
                               transitions={'succeeded': 'LEAVE_ARENA', 'aborted': 'CROSSING_DOOR_POS'})

        sm.userdata.exit_door = LEAVING_DOOR_NAME
        smach.StateMachine.add('LEAVE_ARENA', MoveToRoomStateMachine(announcement=None),
                               transitions={'succeeded': 'succeeded',
                                            'aborted': 'LEAVE_ARENA'},
                               remapping={'room_name': 'exit_door'})

        cant_leave = "Emergency button was pressed, retrying to leave the arena."
        smach.StateMachine.add('CANT_LEAVE', SpeakActionState(text=cant_leave, wait_before_speaking=Duration(0.0)),
                               transitions={'succeeded': 'GO_PRE_EXIT', 'aborted': 'GO_PRE_EXIT'})

    # Create and start the introspection server
    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()


