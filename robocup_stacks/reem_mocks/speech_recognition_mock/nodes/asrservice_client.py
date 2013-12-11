#!/usr/bin/env python

import roslib; roslib.load_manifest('speech_recognition_mock')

import rospy

from pal_interaction_msgs.srv import *
from pal_interaction_msgs.msg import *

def configuration_data():
	data = asrupdate()
	'''data.language = [] 
	data.language.append('Japanese')
	data.enable_grammar = [] 
	data.enable_grammar.append('Who_is_Who')
	data.disable_grammar = []
	data.disable_grammar.append('Supermarket')
	data.acousticenv = []
	data.acousticenv.append('Open_Spaces')
	data.active = []
	data.active.append(True)'''
	
	data.language = 'Japanese'
	data.enable_grammar = 'Who_is_Who'
	data.disable_grammar = 'Supermarket'
	data.acousticenv = 'Open_Spaces'
	data.active = True

	return data

def asrservice_client(data):
	rospy.wait_for_service('asrupdate')
	try:
        	asrservice = rospy.ServiceProxy('asrupdate', recognizerService)
		response = asrservice(data)
		return response#.asrOk
    	except rospy.ServiceException, e:
        	print "&&&&&Service call failed: %s"%e

if __name__== "__main__":
	data_config2 = configuration_data()
	print "--- Requesting--- \n%s \n%s \n%s \n%s \n%s \n" %(data_config2.language,data_config2.enable_grammar,data_config2.disable_grammar,data_config2.acousticenv,str(data_config2.active))
	#This is also useless now because the's no response.
	answer = asrservice_client(data_config2)
	'''print "--- Answer --- \n%s \n%s \n%s \n%s \n%s \n" %(answer.conf_language,answer.conf_enable_grammar,answer.conf_disable_grammar,answer.conf_acousticenv,answer.conf_active)'''


