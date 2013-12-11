# -*- coding: utf-8 -*-
"""
@author: ricardo
"""

import roslib; roslib.load_manifest('dancing_reem')
import rospy

from std_msgs.msg import ColorRGBA
from pal_device_msgs.srv import TimedBlinkEffect, TimedColourEffect, TimedFadeEffect
from pal_device_msgs.msg import LedGroup

# THE EFECT WILL BE FOR EVER TILL REEM ENDS DANCING
BLINK_EFECT_DURATION_DANCING = 0

# The duration of each color, I just want the fisrt color to epear.
FIRST_COLOR_DURATION = 1.0
SECOND_COLOR_DURATION = 0.0


class LedManager():

    def __init__(self):
        # List of LED services
        # /ledManager/TimedBlinkEffect
        # /ledManager/TimedColourEffect
        # /ledManager/TimedFadeEffect

        self.startLedClients()

    def startLedClients(self):

        # Checks that services are up
        rospy.loginfo ("Waiting for TimedBlinkEffect service to start")
        rospy.wait_for_service('/ledManager/TimedBlinkEffect')
        rospy.loginfo ("Waiting for TimedColourEffect service to start")
        rospy.wait_for_service('/ledManager/TimedColourEffect')
        rospy.loginfo ("Waiting for TimedFadeEffect service to start")
        rospy.wait_for_service('/ledManager/TimedFadeEffect')
        
        # generate the persitent connection
        try:
            self.LEDS_BLINK = rospy.ServiceProxy('/ledManager/TimedBlinkEffect', TimedBlinkEffect)
            self.LEDS_COLOR = rospy.ServiceProxy('/ledManager/TimedColourEffect', TimedColourEffect)
            self.LEDS_FADE = rospy.ServiceProxy('/ledManager/TimedFadeEffect', TimedFadeEffect)
        except rospy.ServiceException, e:
            print "Service connection failed: %s" % e

    def callLeds(self, status):
        if status == 'LEFT' or status == 'RIGHT':
            self.callLedsForTurningMv(status)
        elif status == 'STRAIGTH' or status == 'BACKWARDS':
            self.callLedsForStraightMv(status)
        else:
            self.callLedsForCmplxMv()

    def callLedsForStraightMv(self, status):

        fColor = ColorRGBA()
        sColor = ColorRGBA()

        fColor.r = 0
        if status == 'STRAIGHT':
            fColor.g = 0
            fColor.b = 0.9
        else:
            fColor.g = 0.9
            fColor.b = 0
        sColor.r = 0
        sColor.g = 0.9
        sColor.b = 0

        ledGroup = LedGroup()
        ledGroup.ledMask = 3  # binary mask to decide which leds are active
        try:
            self.LEDS_FADE(ledGroup, fColor, sColor, rospy.Duration(0.5), True, rospy.Duration(2), 50)
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e

    def callLedsForCmplxMv(self):

        fColor = ColorRGBA()
        sColor = ColorRGBA()

        fColor.r = 1.0
        fColor.g = 1.0
        fColor.b = 1.0
        sColor.r = 0.0
        sColor.g = 0.0
        sColor.b = 0.0

        ledGroup = LedGroup()
        ledGroup.ledMask = 3  # binary mask to decide which leds are active
        try:
            self.LEDS_BLINK(ledGroup, fColor, sColor, rospy.Duration(0.75), rospy.Duration(0.25), rospy.Duration(5), 50)
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e

    def callLedsForTurningMv(self, side):

        fColor = ColorRGBA()
        sColor = ColorRGBA()

        fColor.r = 0.5
        fColor.g = 1.0
        fColor.b = 0.5
        sColor.r = 0.0
        sColor.g = 0.0
        sColor.b = 0.0

        ledGroup = LedGroup()
        if side == 'LEFT':
            ledGroup.ledMask = 1  # binary mask to decide which leds are active
        else:
            ledGroup.ledMask = 2

        try:
            self.LEDS_BLINK(ledGroup, fColor, sColor, rospy.Duration(0.75), rospy.Duration(0.25), rospy.Duration(5), 50)
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e


    # TODO 
    def callLedsForDancing(self, blinking_freq):

        """
        fColor : the first Color
        sColor : the second Color
        By defining LedGroup, we will have RGBA of color of each
        set of colours.
        I suppose that the last parameter of LEDS_BLINK is the frequency,
        although its not on the server definition that I have.
        """

        fColor = ColorRGBA()
        sColor = ColorRGBA()

        fColor.r = 0.5
        fColor.g = 1.0
        fColor.b = 0.5
        sColor.r = 0.0
        sColor.g = 0.0
        sColor.b = 0.0

        ledGroup = LedGroup()

        first_color_duration = rospy.Duration(FIRST_COLOR_DURATION)
        second_color_duration = rospy.Duration(SECOND_COLOR_DURATION)

        try:
            self.LEDS_BLINK(ledGroup, fColor, sColor, first_color_duration, second_color_duration, BLINK_EFECT_DURATION_DANCING, blinking_freq)
        except rospy.ServiceException, e:
            print "Service call To Blinking LEDs failed: %s" % e
