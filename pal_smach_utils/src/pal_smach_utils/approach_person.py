#!/usr/bin/env python
from __future__ import division
import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import actionlib
import smach
from smach import StateMachine, State, Concurrence, CBState
from smach_ros import MonitorState, SimpleActionState, IntrospectionServer
from pal_vision_msgs import *
from pal_vision_msgs.msg import *
from pal_smach_utils.smach_utils import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import math
from geometry_msgs.msg import *
from nav_msgs.msg import Path
import sys

HANDSHAKING_DISTANCE = rospy.get_param('/handshaking/handshakingDistance', 0.7)

## State machine callbacks
def approach_person_cb(userdata):
    """
    Callback for the state MOVE_TO_POSITION.
    This state creates a PoseStamped message based on the Pose message passed
    in userdata, and published.
    """
    goal = PoseStamped()
    goal.pose = userdata.goal
    goal.header.frame_id = '/map'
    goal.header.stamp = rospy.Time.now()
    return goal

@smach.cb_interface(input_keys=['pose'], output_keys=['pose'],
                    outcomes=['done','failed'])
def get_position_cb(userdata):
    """
    Callback for the state GET_POSITION.
    """
    rospy.sleep(rospy.Duration(0.1))
    print 'x=?'
    userdata.pose.position.x = float(sys.stdin.readline())
    print 'y=?'
    userdata.pose.position.y = float(sys.stdin.readline())
    userdata.pose.position.z = 0.0
    print userdata.pose.position
    userdata.pose.orientation.x = 0.0
    userdata.pose.orientation.y = 0.0
    userdata.pose.orientation.z = 0.0
    userdata.pose.orientation.w = 1.0
    return 'done'

def start_navigating_cb(userdata, received_msg):
    """
    Callback for the state START_NAVIGATING
    Waits until a message published on RosPathPlanner/Path contains a non-empty
    poses field.
    """
    path_poses = received_msg.poses
    if len(path_poses) is 0:
        outcome = None
    else:
        outcome = 'done'
    rospy.sleep(rospy.Duration(0.1))
    return outcome

def robot_is_moving_cb(userdata, received_msg):
    """
    Callback for the state ROBOT_IS_MOVING
    Wait until the robot has stopped navigating
    i.e. poses fields of RosPathPlanner/path messages are empty
    """
    path_poses = received_msg.poses
    if len(path_poses) is not 0:
        outcome = None
    else:
        outcome = 'done'
    rospy.sleep(rospy.Duration(0.3))
    return outcome

def goal_reached_cb(userdata, received_msg):
    """
    Callback for the state CHECK_GOAL_REACHED
    Check if the position reached by the robot is close enough to the goal
    to consider it has been reached.
    """
    position = received_msg.pose.position
    goal = userdata.goal.position
    goal_reached = (math.fabs(position.x-goal.x) < 0.3 and
                   math.fabs(position.y-goal.y) < 0.3)

    if goal_reached:
        return 'done'
    return 'failed'

class DummyNavigateToPerson(smach.State):
    def __init__(self, outcomes=['done','failed'], input_keys=[],
                output_keys=[], io_keys=[]):

        smach.State.__init__(self, outcomes=outcomes, input_keys=input_keys,
                             output_keys=output_keys, io_keys=io_keys)

    def execute(self, userdata):
      return 'done'

def create_approach_person_state(dummy_implementation=False):
    """
    Returns an APPROACH_STATE container. Calculates the goal position given the
    position of the target person, sends the goal to navigation services and
    waits until the robot has reached the goal.
    dummy_implementation : if True, the states that require
    navigation services to run will not be added to the state machine.
    """
    approach_person = StateMachine(outcomes=['done','failed','preempted'],
                                       input_keys=['pose'])
    approach_person.userdata.goal = Pose()
    approach_person.userdata.robot_position = Pose()
    
    ## APPROACH_PERSON
    with approach_person:
    
      ## CALCULATE_POSITION: compute map coordinates of the detected person
      calculate_goal_state = FindPositionState(distance = HANDSHAKING_DISTANCE, input_keys=['pose'],
                                               output_keys=['goal'], outcomes=['done','failed','skip','preempted'])

      smach.StateMachine.add('CALCULATE_POSITION', calculate_goal_state,
                             transitions={'done':'NAVIGATE_TO_PERSON',
                                          'failed':'CALCULATE_POSITION',
                                          'skip':'done',
                                          'preempted':'preempted'})

      if not dummy_implementation:    

        def create_move_base_goal(userdata, goal):
          nav_goal = MoveBaseGoal()
          nav_goal.target_pose.pose.position.x = userdata.goal.position.x;
          nav_goal.target_pose.pose.position.y = userdata.goal.position.y;      
          nav_goal.target_pose.pose.orientation.x = userdata.goal.orientation.x;
          nav_goal.target_pose.pose.orientation.y = userdata.goal.orientation.y;
          nav_goal.target_pose.pose.orientation.z = userdata.goal.orientation.z;
          nav_goal.target_pose.pose.orientation.w = userdata.goal.orientation.w;
          nav_goal.target_pose.header.frame_id = '/map';
          return nav_goal

        #NAVIGATE_TO_PERSON: use navigation action to move the robot in front of the person
        smach.StateMachine.add('NAVIGATE_TO_PERSON', 
                               SimpleActionState('move_base', 
                                                 MoveBaseAction, 
                                                 goal_cb=create_move_base_goal,
                                                 input_keys=['goal']),            #needed in order that create_move_base_goal can use userdata.goal
                               transitions={'succeeded':'done',    
                                            'aborted':'failed'})      
      else:

        smach.StateMachine.add('NAVIGATE_TO_PERSON', DummyNavigateToPerson(),
                               transitions={'done':'done','failed':'failed'}) 

    return approach_person

if __name__ == '__main__':
    rospy.init_node("handshaking")
    sm = StateMachine(outcomes = ['succeeded','aborted','preempted'])
    ## USERDATA of the state machine
    # objectId of the person selected :
    sm.userdata.id = -1
    # position of the person selected :
    sm.userdata.pose = Pose()
    with sm:

        ## GET_POSITION
        get_position_state = CBState(get_position_cb)
        StateMachine.add('GET_POSITION', get_position_state,
                transitions={'done':'APPROACH_PERSON',
                             'failed':'GET_POSITION'})

        ## APPROACH_PERSON container
        approach_person = create_approach_person_state()

        StateMachine.add('APPROACH_PERSON', approach_person,
                         transitions={'done':'GET_POSITION',
                                      'failed':'GET_POSITION'})

     # Run state machine introspection server for smach viewer
    intro_server = IntrospectionServer('navigation_sm',sm,'/NAV_STATE_MACHINE')

    intro_server.start()
    rospy.sleep(rospy.Duration(3.0))
    outcome = sm.execute()
    intro_server.stop()
    rospy.signal_shutdown('All done.')

