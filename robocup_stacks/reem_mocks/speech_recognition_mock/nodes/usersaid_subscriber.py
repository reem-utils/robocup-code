#!/usr/bin/env python

import roslib; roslib.load_manifest('speech_recognition_mock')

import rospy

from pal_interaction_msgs.msg import *

def call_back(data):
	print ("IN Callback")
	rospy.loginfo("I'm hearing :\nText:%s\nConfidence: %s\n TStart: %s\nTEnd: %s\nTag.Key: %s\nTag.Value: %s\n","".join(data.text),str(data.confidence),str(data.start), str(data.end),data.tags[0].key,data.tags[0].value)
	
def listener():
    rospy.init_node('usersaid_subscriber')
    rospy.Subscriber("usersaid", asrresult, call_back)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()



if __name__ == '__main__':
        try:
                listener()
        except rospy.ROSInterruptException:
                pass

