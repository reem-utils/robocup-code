#! /usr/bin/env python

import roslib
import rospy
import copy
import smach
#import smach_ros
import actionlib
import math
from subprocess import Popen
from smach_ros import SimpleActionState, ServiceState
from roslib import packages


from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pr_msgs.msg import ObjectPoseList

from geometry_msgs.msg import Pose, Point, Quaternion
from control_msgs.msg import *
from actionlib_msgs.msg import GoalStatus
#from blort_ros.msg import TrackerConfidences
#from blort_ros.srv import *
from iri_moped_handler.srv import enable

class Check_object_to_search_for(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted],input_keys=['object_to_search_for', 'object_found'])

    def execute(self, userdata):
        if userdata.object_to_search_for == userdata.object_found.object_list[0].name:
            return succeeded
        else:
            rospy.loginfo("Aborting: MOPED found the object: " + userdata.object_found.object_list[0].name + " but we were searching for " + userdata.object_to_search_for)
            return aborted







class CheckObject(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted],input_keys=['object_found'], output_keys =['checkcount'])

    def execute(self, userdata):
        rospy.loginfo("look_for_objects returned an structure of objects: ")
        if len(userdata.object_found.object_list) != 0:
            rospy.loginfo("Object is: " + userdata.object_found.object_list[0].name +
             "\nIn position: " +  str(userdata.object_found.object_list[0].pose.position) + 
             "\nWith orientation: " + str(userdata.object_found.object_list[0].pose.orientation))
            userdata.checkcount = 0
            return succeeded
        else:
            rospy.loginfo("The structure is empty, we'll search again.")
            return aborted





## We return success (and the object found data) only if we found an object with a confidence > 0.45
## We return aborted if we timeout reading from outputOPL 
class SearchObjectWithConfidenceStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
            input_keys = ['object_to_search_for'],
            output_keys = ['object_found'])


        with self:



            def moped_enable_cb(userdata, response):
                if response.correct != None:
                    return succeeded
                else:
                    return aborted

            smach.StateMachine.add(
                'ENABLE_CLOSE_OBJECT_SEARCH',
                ServiceState('/iri_moped_handler/enable', enable,
                    response_cb = moped_enable_cb,
                    request = True),
                transitions = {succeeded:'read_outputOPL'})


            smach.StateMachine.add(
                    'read_outputOPL',
                    TopicReaderState(
                                     topic_name='/iri_moped_handler/outputOPL',
                                     msg_type=ObjectPoseList,
                                     timeout=30),
                    remapping= {'message' : 'object_found'},
                    transitions = {succeeded: 'CHECK_IF_OBJECT_FOUND', aborted: aborted})

            smach.StateMachine.add(
                    'CHECK_IF_OBJECT_FOUND',
                    CheckObject(),
                    transitions = {succeeded: 'DISABLE_CLOSE_OBJECT_SEARCH', aborted: 'read_outputOPL'})




            # smach.StateMachine.add(
            #         'CHECK_IF_IS_THE_OBJECT_WE_ARE_SEARCHING_FOR',
            #         Check_object_to_search_for(),
            #         transitions = {succeeded: 'DISABLE_CLOSE_OBJECT_SEARCH', aborted: 'read_outputOPL'})


            smach.StateMachine.add(
                'DISABLE_CLOSE_OBJECT_SEARCH',
                ServiceState('/iri_moped_handler/enable', enable,
                    response_cb = moped_enable_cb,
                    request = False),
                transitions = {succeeded: succeeded})













