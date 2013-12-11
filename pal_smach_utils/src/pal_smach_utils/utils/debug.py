
import os

DEBUG_ENV_VAR = 'ROBOCUP_DEBUG_UTILITIES_DEBUG_LEVEL'
MIN_BUG_LEVEL = 0
DEFAULT_DEBUG_LEVEL = 2

import rospy


def getDebugLevel():
    return int(os.getenv(DEBUG_ENV_VAR, DEFAULT_DEBUG_LEVEL))


def checkDebugLevel(debugLevel):
    if (type(debugLevel) is not int):
        raise Exception("The debug level must be an int !")
    if (debugLevel < MIN_BUG_LEVEL):
        raise Exception("The debug level must be equal or greater than 0 !")


def setDebugLevel(debugLevel):
    checkDebugLevel(debugLevel)
    os.environ[DEBUG_ENV_VAR] = str(debugLevel)


def debugPrint(message, debugLevel=DEFAULT_DEBUG_LEVEL):
    checkDebugLevel(debugLevel)
    if (debugLevel <= getDebugLevel()):
        rospy.loginfo(message)
