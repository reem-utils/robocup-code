#!/usr/bin/env python
import roslib; roslib.load_manifest('navigation_sm_mock')
import rospy


from std_msgs.msg import String
from pal_navigation_msgs.srv import *
from pal_navigation_msgs.msg import NavigationStatus

import threading
import thread

currentState = NavigationStatus()
currentState.status = String('LOC')
currentState.msg    = String('')

lock = threading.Lock()


def getCurrentState ():
    global lock
    lock.acquire()
    global currentState
    st = NavigationStatus()
    st.status = currentState.status
    st.msg    = currentState.msg
    lock.release()
    rospy.loginfo ('\n\n********************** Getting Current state with value %s'%st)
    return st

def setCurrentState(st):
    rospy.loginfo ('\n\n========1')
    global lock
    rospy.loginfo ('\n\n========2')
    lock.acquire()
    rospy.loginfo ('\n\n========3')
    global currentState
    rospy.loginfo ('\n\n========4')
    currentState.status = String(st)
    currentState.msg    = String('pepepe')
    lock.release()
    rospy.loginfo ('\n\n====================== Setting Current state to %s'%st)




def change_status_by_service (req):
  
    state = getCurrentState().status.data
    
    """ Check for a sound command """
    if req.input == 'LOC' and state == 'LOC' :
        return AcknowledgmentResponse (True,'Already on LOC state')
    if req.input == 'MAP' and state == 'MAP':
        return AcknowledgmentResponse (True,'Already on MAP state')
    if req.input == 'STOP' and state == 'STOP':
        return AcknowledgmentResponse (True,'Already on STOP state')
    if req.input != 'LOC' and req.input != 'MAP' and req.input != 'STOP'  and req.input != 'SAVE':
        error = 'Received unknown command %s'% req.input
        rospy.loginfo (error) 
        return AcknowledgmentResponse (False,error)
        
    """ Check that the sm is not already changing to another state 
        Requests for STOP are always allowed """
    if state == 'CHANGING' and req.input != 'STOP':
        return AcknowledgmentResponse (False,"The SM is still on a process of changing state. Status change to %s requested is not possible"% req.input)

    result = AcknowledgmentResponse ()
    
    rospy.loginfo (' Putting state to CHANGING')
    setCurrentState ('CHANGING')    
    rospy.sleep (3.0)
    
    rospy.loginfo (' Putting state to %s'%req.input)
    setCurrentState (req.input)    
    rospy.sleep (1.0)
    
    rospy.loginfo (' Done')
    return result



def main():

    rospy.init_node("navigation_sm_mock")

    """ Creates the service that receives state change """
    srv = rospy.Service('/pal_navigation_sm', Acknowledgment, change_status_by_service)
    """  Creates the publisher of the current state """ 
    pub = rospy.Publisher('/pal_navigation_sm/state', NavigationStatus)
    
    
    while True:
        #publish state 
        st = getCurrentState()
        pub.publish(st)
        rospy.sleep (1.0)


if __name__=="__main__":
    main()


