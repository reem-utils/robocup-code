#!/usr/bin/env python

import roslib; roslib.load_manifest('speech_recognition_mock')

import rospy

from pal_interaction_msgs.srv import *
from pal_interaction_msgs.msg import *


def confirmation(req):
	conf_data = asrconfigOk()
	conf_data.conf_language = []
	conf_data.conf_language.append('Language:')
	conf_data.conf_language.append(str(req.asrupdate.language))
	conf_data.conf_language.append('Enabled')
	''.join(conf_data.conf_language)

	conf_data.conf_enable_grammar = []
	conf_data.conf_enable_grammar.append('Grammar:')
	conf_data.conf_enable_grammar.append(str(req.asrupdate.enable_grammar))
	conf_data.conf_enable_grammar.append('Enabled')
	''.join(conf_data.conf_enable_grammar)
	
	conf_data.conf_disable_grammar = []
	conf_data.conf_disable_grammar.append('Grammar:')
	conf_data.conf_disable_grammar.append(str(req.asrupdate.disable_grammar))
        conf_data.conf_disable_grammar.append('Disabled')
        ''.join(conf_data.conf_disable_grammar)
	
	conf_data.conf_acousticenv = []
	conf_data.conf_acousticenv.append('Acousticenv:')
	conf_data.conf_acousticenv.append(str(req.asrupdate.acousticenv))
        conf_data.conf_acousticenv.append('Disabled')
        ''.join(conf_data.conf_acousticenv)
	
	conf_data.conf_active = []
	conf_data.conf_active.append('Speech Recognition:')
	conf_data.conf_active.append(str(req.asrupdate.active))
	''.join(conf_data.conf_active)
	return conf_data


def handle_asrservice(req):
	# The next lines were the previous content:
	#conf_data = confirmation(req)
	#rospy.loginfo('Returning the confirmation Data of : \n%s \n%s \n%s \n%s \n%s \n  All OK',conf_data.conf_language,conf_data.conf_enable_grammar,conf_data.conf_disable_grammar,conf_data.conf_acousticenv,str(conf_data.conf_active))
	# Not giving anything back as we are just enabling or desabling

	# new content
	#returning [] so we dont get:
	#Exception when calling service 'asrservice': service [/asrservice] responded with an error: service cannot process request: service handler returned None
	return []


def asrservice_server():
        rospy.init_node('asrservice_server')
        s = rospy.Service('asrservice' , recognizerService , handle_asrservice)
        print "--- Asrservice_Server Ready ---"
        rospy.spin()


if __name__ == '__main__':
        asrservice_server()

