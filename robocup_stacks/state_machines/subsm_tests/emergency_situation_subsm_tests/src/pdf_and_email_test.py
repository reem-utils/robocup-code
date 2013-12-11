#! /usr/bin/env python

import roslib
roslib.load_manifest('emergency_situation_subsm_tests')
import rospy
import smach
import smach_ros
from move_base_msgs.msg import *
from pal_smach_utils.navigation.get_current_pos import GetPosition
from pal_smach_utils.navigation.move_action import MoveActionState

from pdf_creator import create_pdf
from mail_sender import mail_sender

from smach_ros import SimpleActionState
import random
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler
from image_creator import ImageCreator


PKG_PATH = roslib.packages.get_pkg_dir('emergency_situation')
RESOLUTION=rospy.get_param("/emergency_situation/resolution")
IMAGE_NAME=rospy.get_param("/emergency_situation/image")
IMAGE_ORIGIN=rospy.get_param("/emergency_situation/origin")
IMAGE_PATH=roslib.packages.get_pkg_dir('robocup_worlds')+'/navigation/'

def move_around(userdata, goal):
    moveGoal = MoveBaseGoal()
    moveGoal.target_pose.header.stamp = rospy.Time.now()
    moveGoal.target_pose.header.frame_id = 'base_link'
    moveGoal.target_pose.pose.position.x = random.randint(-2, 2)
    moveGoal.target_pose.pose.position.y = random.randint(-2, 2)
    moveGoal.target_pose.pose.position.z = 0
    rotationAngle = random.random()
    moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, rotationAngle))

    print moveGoal

    return moveGoal


class RecordPosition(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded','aborted','preempted'], input_keys=['location_of_person'], output_keys=['location_list'])
        self.people_need_assistance=[]

    def execute(self, userdata):
        print "Location Saved................"
        self.people_need_assistance.append([userdata.location_of_person.position.x, userdata.location_of_person.position.y])
        print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        print str(userdata.location_of_person)
        print str(self.people_need_assistance)
        userdata.location_list = self.people_need_assistance
        return 'succeeded'


class CallFireDepartmentState(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded','aborted','preempted'], input_keys=['location_list'])

    def execute(self,userdata):
        print "Informing Fire Department..............."
        ImageCreator(location_list=userdata.location_list,origin=IMAGE_ORIGIN,scale=RESOLUTION,image_name=IMAGE_NAME,pkg_path=PKG_PATH,image_path=IMAGE_PATH)
        create_pdf(PKG_PATH+'/config/')
        print "PDF CREATED..............."
        mail_sender('reem.emergency@gmail.com', 'Emergency Situation', 'Location attached',PKG_PATH+'/config/'+'reem2.pdf')
        print "MAIL SENT................"
        return 'succeeded' 



def main():
    rospy.init_node('pdf_and_mail_subsm_test')

    sm = smach.StateMachine(outcomes=['succeeded', 'preempted', 'aborted'])

    with sm:

        smach.StateMachine.add(
            'MOVE_AROUND', 
            SimpleActionState('move_base', MoveBaseAction, goal_cb=move_around),
            transitions={'aborted': 'aborted','succeeded':'GET_POSITION'})

        smach.StateMachine.add(
            'GET_POSITION',
            GetPosition(),
            transitions={'succeeded':'RECORD_POSITION'},
            remapping={'memorised_poi_data':'location_of_person','location_list':'location_list'})                

        smach.StateMachine.add(
            'RECORD_POSITION',
            RecordPosition(),
            transitions={'succeeded':'CALL_FIRE'})

        smach.StateMachine.add(
            'CALL_FIRE',
            CallFireDepartmentState(),
            transitions = {'succeeded':'succeeded'})

    
    sis = smach_ros.IntrospectionServer('emergency_situation_mail_sender_subsm_test_introspection', sm, '/SM_ROOT')

    sis.start()

    sm.execute()

    rospy.spin()

    sis.stop()

if __name__ == '__main__':
    main()

# vim: expandtab ts=4 sw=4
