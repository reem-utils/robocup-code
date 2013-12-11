#!/usr/bin/env python

import roslib
roslib.load_manifest('speech_recognition_mock')

import rospy
import time

from pal_interaction_msgs.msg import *

DELIVERY_MESSAGE = {'action': 'goto', 'objectA': 'coke', 'objectB': 'juice', 'objectC': 'marmalade', 'location1': 'table 1', 'location2': 'table 3'}


def get_message(actions, message_text="Go to the kitchen, detect a drink and guide me to the exit", confidence=2):
    tstart = rospy.Time.now()
    time.sleep(1)
    tend = rospy.Time.now()

    message = asrresult()
    message.text = message_text
    message.confidence = confidence
    message.start = tstart
    message.end = tend

    for key, value in actions.iteritems():
        atag = actiontag()
        atag.key = key
        atag.value = value
        message.tags.append(atag)

    return message


def frase_detector():
    pub = rospy.Publisher('usersaid', asrresult, latch=True)
    rospy.init_node('usersaid_publisher')
    rate = rospy.Rate(0.5)
    default_messages = [
        [{'fifi': 'foo'}], [{'action': 'deliver', 'object': 'burrito_total', 'location': 'table_7'}],
        [{'action': 'deliver', 'objectA': 'apple', 'objectB': 'chewing_gum', 'objectC': 'mega_burrito_total', 'location1': 'table_1', 'location2': 'table_2'}],[{'action':'yes'}],
        [{'action': 'stopwait'}], [{'more': 'rubish'}],[{'action': 'follow'}], [{'action': 'no'}], [{'poi': 'food'}], [{'poi': 'drinks'}], [{'action': 'yes'}] ,[{'poi':'table_1'}],
        [{'action': 'yes'}], [{'action': 'bring', 'object': 'pringles'}], [{'poi': 'apple'}], [{'action': 'yes'}],[{'action': 'release'}], [{'action': 'POI1'}],
        [{'action': 'POI3'}], [{'fifi': 'foo'}], [{'fifi': 'foo'}], [{'poi': 'table_1'}],[{'action': 'yes'}]
    ]

    messages = rospy.get_param('mock_config/usersaid', default_messages)

    counter = 0
    while not rospy.is_shutdown():
        # FIXME: maybe insert junk randomly into the messages
        result = get_message(*messages[counter])
#        i = 1
#        orig = {}

#        n_e = raw_input("HOW MANY ELEMENTS (default = 1, 6 reserved for DELIVERY) ==> ")
#        if not n_e:
#            number_elements = 1
#        else:
#            if n_e.isdigit():
#                number_elements = int(float(n_e))
#            else:
#                print ("You should input numbers, set number of elements to 1")
#                number_elements = 1
#            print str(number_elements)

#        print str(i <= number_elements)
#
#        if number_elements != 6:
#            while i <= number_elements:
#                print "Number of elements ==> " + str(number_elements)
#                #key_value = raw_input("WRITE WHAT YOU WANNA SAY (default = action) ==> KEY: ")
#
#                if not key_value:
#                    key_value = "action"
#
#                val_value = raw_input("WRITE WHAT YOU WANNA SAY (default = yes) ==> VALUE: ")
#
#                if not val_value:
#                    val_value = "yes"
#
#                partial_result = {key_value: val_value}
#                orig.update(partial_result)
#                print "ELEMENT NUMBER ==> " + str(i)
#                i += 1
#        else:
#            orig = DELIVERY_MESSAGE
#
#        result = get_message(*[orig])
        print "Message Sent ==>" + str(result)
        #rospy.loginfo("YOU SAID ==> " + str(result))
        pub.publish(result)
        counter = (counter + 1) % len(messages)
        #rate.sleep()
        rospy.sleep(1)
if __name__ == '__main__':
    try:
        frase_detector()
    except rospy.ROSInterruptException:
        pass
