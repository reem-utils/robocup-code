#! /usr/bin/env python

import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import smach_ros
import actionlib
#from actionlib_msgs.msg import GoalStatus
from smach_ros import SimpleActionState

from global_common import *
from pal_smach_utils.grasping.sm_search_obj_orig import *

# This is SM find known object

class V8_identify_objects(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys=['object_data'])

    def execute(self, userdata):
        rospy.sleep(0.5) # in seconds
        
        print userdata.keys()
        return succeeded
    
class V5_locate_object(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded])

    def execute(self, userdata):
        rospy.sleep(0.5) # in seconds
        return succeeded

class FindKnownObjectStateMachine(smach.StateMachine):
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
        output_keys=['pose_object'])

        with self:
            smach.StateMachine.add(
                'SM_search_object',
                SearchObjectStateMachine(),
                remapping = {'object_data' : 'pose_object'},
                transitions = {succeeded: 'V8_identify_objects'})

            smach.StateMachine.add(
                'V8_identify_objects',
                V8_identify_objects(),
                transitions = {succeeded: 'V5_locate_object', aborted: 'SM_search_object'})
                
            smach.StateMachine.add(
                'V5_locate_object',
                V5_locate_object()) 

# Call SM search object

# Add V8 Identify objects

# Add V5 Locate object

# vim: expandtab ts=4 sw=4
