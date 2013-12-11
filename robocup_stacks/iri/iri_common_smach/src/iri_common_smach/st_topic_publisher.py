#!/usr/bin/env python

import roslib; roslib.load_manifest('iri_common_smach')
import rospy
import smach
import smach_ros

class TopicPublisher(smach.State):
    def __init__(self, topic, msg_type):
        smach.State.__init__(self, outcomes=['finish'],
                                   input_keys=['msg'])
        self.topic    = topic
        self.msg_type = msg_type

    def execute(self, userdata):
        # Log the PCL
        pub = rospy.Publisher(self.topic, self.msg_type,  None, False, True)
        pub.publish(userdata.msg)
        return 'finish'
