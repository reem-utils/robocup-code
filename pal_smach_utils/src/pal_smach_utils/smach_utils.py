#!/usr/bin/env python
import roslib; roslib.load_manifest('pal_smach_utils')
import rospy
import time
import smach
from smach import StateMachine
from pal_vision_msgs import *
from pal_vision_msgs.msg import *
from geometry_msgs.msg import Pose, Point, TransformStamped
from pal_supervisor_msgs.srv import lookupTransform
import math
import tf


def make_tf(parent, child, trans, rot):
        m = TransformStamped()
        m.header.frame_id = parent
        m.child_frame_id = child
        m.transform.translation.x = trans[0]
        m.transform.translation.y = trans[1]
        m.transform.translation.z = trans[2]
        m.transform.rotation.x = rot[0]
        m.transform.rotation.y = rot[1]
        m.transform.rotation.z = rot[2]
        m.transform.rotation.w = rot[3]
        return m
    
## Helper functions
def distance(pos1, pos2):
    return math.sqrt(math.pow(pos2.x-pos1.x, 2) +
                     math.pow(pos2.y-pos1.y, 2) +
                     math.pow(pos2.z-pos1.z, 2))

def face_detected(person):
    faceBox = person.faceBox
    face_box_is_empty = (faceBox.x == 0 and faceBox.y == 0  and
                        faceBox.width == 0 and faceBox.height == 0)
    face_detected = not face_box_is_empty
    return face_detected


class TimeoutMonitor(smach.State):
    """ This state will monitor a topic with timeouts check and possibility to
    pass userdata. Parameter topic_name and msg_type define the topic to
    subscribe to.
    Parameter cb : function to call when a message has been received. If it returns None the state will not end and will 
		    wait for the next message or for a timeout, it can also return one of the outcomes of the state to exit the state immediately  
    Parameter global_timeout : if this parameter is different than None, if the execution of the
				 state lasts longer that global_timeout duration, the execution stops and the state returns 'failed'.
    Parameter last_msg_timeout : if this parameter is different than None, if no message has been received during timeout duration, the execution stops and the state returns 'failed'. The type of messages monitored must have a 'header' field TODO.
    Parameter provide_self_instance: If true, the callback needs to have 3 arguments, and the first one will be the self instance
    Parameter sleep_duration time to sleep in the execute method to avoid saturating the robot 
    If the function passed in the 'cb' parameter returns before the
    timeouts expire, the state will return the outcome of this function.
 """
    def __init__(self, cb, topic_name, msg_type,
                global_timeout=None, outcomes=['failed','preempted'],
                last_msg_timeout=None, input_keys=[],
                output_keys=[], io_keys=[], provide_self_instance=False, sleep_duration = 0.05):
        if 'failed' not in outcomes:
            outcomes.append('failed')
        smach.State.__init__(self, outcomes=outcomes, input_keys=input_keys,
                             output_keys=output_keys, io_keys=io_keys)
        # max time since beginning
        self._global_timeout = global_timeout
        # max time since last message : will not be needed when checking if the
        # person grasps the hand of the robot
        self._last_msg_timeout = last_msg_timeout
        self._received_msg = None
        self._beginning = None
        self._last_msg_stamp = None
        self._monitor_cb = cb
        self._provide_self_instance = provide_self_instance
        self._sleep_duration = sleep_duration
        rospy.Subscriber(topic_name, msg_type, self.internal_callback)

        # this is to be able to pass userdata to the internal_callback
        if cb and smach.has_smach_interface(cb):
            self.register_input_keys(cb.get_registered_input_keys())
            self.register_output_keys(cb.get_registered_output_keys())
            self.register_outcomes(cb.get_registered_outcomes())

    def internal_callback(self, msg):
        self._received_msg = msg
        if self._last_msg_timeout is not None:
            self._last_msg_stamp = msg.header.stamp

    def check_global_timeout(self):
        if self._global_timeout is None:
            return True
        return (rospy.Time.now() - self._beginning) < self._global_timeout

    def check_last_msg_timeout(self):
        if self._last_msg_timeout is None:
            return True

        if self._last_msg_stamp is None:
            return (rospy.Time.now() - self._beginning < self._last_msg_timeout)
        else:      
            return (rospy.Time.now() - self._last_msg_stamp < self._last_msg_timeout)

    def execute(self, ud):
        self._beginning = rospy.Time.now()
        outcome = 'failed'#None
        
        # this is needed to test if the person goes away (if not seen by
        # personServer) until it will be possible to check for hand grasping :
        while (self.check_global_timeout() and self.check_last_msg_timeout() and  not rospy.is_shutdown()):

            if self.preempt_requested():
                self.service_preempt()
                return 'preempted'
            if self._received_msg is not None: 
                if self._provide_self_instance:
                    out = self._monitor_cb(self, ud, self._received_msg)
                else:
                    out = self._monitor_cb(ud, self._received_msg)
                    
                self._received_msg = None
                if out is not None:
                    outcome = out
                    break
	    rospy.sleep(rospy.Duration(self._sleep_duration))

        if outcome == 'failed':
            if not self.check_global_timeout():
                print "Execution aborted because check_global_timeout() failed"
            else:
                print "Execution aborted because check_last_msg_timeout() failed"
        
        self._beginning = None
        return outcome


class PublisherState(smach.State):
    """
    State that publishes a message each time it is executed. 
    cb : function that should return the message to publish.
    topic_name : topic on which the messages should be published.
    msg_type : type of the messages to publish
    """
    def __init__(self, cb, topic_name, msg_type,
                outcomes=['done','failed','preempted'], input_keys=[],
                output_keys=[], io_keys=[]):

        smach.State.__init__(self, outcomes=outcomes, input_keys=input_keys,
                             output_keys=output_keys, io_keys=io_keys)
        self._publisher = rospy.Publisher(topic_name, msg_type)
        self._cb = cb

        if cb and smach.has_smach_interface(cb):
            self.register_input_keys(cb.get_registered_input_keys())
            self.register_output_keys(cb.get_registered_output_keys())
            self.register_outcomes(cb.get_registered_outcomes())

    def execute(self, ud):
        if self.preempt_requested():
            self.service_preempt()
            return 'preempted'        
        msg = self._cb(ud)
        if msg:
            self._publisher.publish(msg)
            return 'done'
        return 'failed'

class FindPositionState(smach.State):
    def __init__(self, distance, outcomes=['done','failed'], input_keys=[],
                output_keys=[], io_keys=[]):

        smach.State.__init__(self, outcomes=outcomes, input_keys=input_keys,
                             output_keys=output_keys, io_keys=io_keys)
        self._handshaking_distance = distance

    def execute(self, userdata):
        
        pos = userdata.pose.position
        orientation = userdata.pose.orientation
        dist = distance(Point(), Point(pos.x,pos.y,pos.z))
        # goal_base_link is the position the robot has to reach, in the
        # /base_link frame
        goal_base_link = Pose()
        print "Distance from robot to target position.", dist
        
        if dist <= self._handshaking_distance + 0.2: 
            # robot does not move back, stays at same position in this case
            return 'skip'
        else:
            alpha = (dist-self._handshaking_distance) / dist
            goal_base_link.position.x = (pos.x)*alpha
            goal_base_link.position.y = (pos.y)*alpha
            goal_base_link.position.z = (pos.z)*alpha
            goal_base_link.orientation = userdata.pose.orientation
            goal_base_link.orientation.w = 1.0

        lookupTrans = rospy.ServiceProxy('lookupTransform', lookupTransform)
        result = lookupTrans("base_link","map", rospy.Time())
        #print result.transform
        transformer = tf.Transformer(True)
        result.transform.header.stamp = rospy.Time()
        transformer.setTransform(result.transform)
        goal_base_link_trans = make_tf('base_link', 'goal', (goal_base_link.position.x,
                                                             goal_base_link.position.y,
                                                             goal_base_link.position.z),
                                                             (0.0,0.0,0.0,1.0))
        
        transformer.setTransform(goal_base_link_trans)
        #goal to base_link transform
        #print transformer.allFramesAsString()
        #print transformer.canTransform("map","goal",rospy.Time())
        #print transformer.waitForTransform("map","goal",rospy.Time(), rospy.Duration(1.0))
        (trans,rot) = transformer.lookupTransform("map","goal", rospy.Time())
        #print trans
        #print rot
        
        goal_map = Pose()
        goal_map.position.x = trans[0]
        goal_map.position.y = trans[1]
        goal_map.position.z = trans[2]
        goal_map.orientation.x = rot[0]
        goal_map.orientation.y = rot[1]
        goal_map.orientation.z = rot[2]
        goal_map.orientation.w = rot[3]
                   
  
        userdata.goal = goal_map
        return 'done'

class SelectPersonState(smach.State):
    """ State that selects a person. Needs to be passed at least the following
    output keys : 'position' and 'id'. This state will select the closest
    person.
    Parameter timeout : Persons whose DetectedPerson message has been published
    more than timeout seconds ago will not be considered. If successful,
    returns 'done' and puts position and objectId of the selected person in
    userdata. If not, returns 'failed'. """
    # TODO GRA-HAS-12 (translational and rotational distance)
    def __init__(self, timeout, input_keys=[], output_keys=[], io_keys=[]):
        smach.State.__init__(self, outcomes=['done','failed','preempted'],
                             input_keys=input_keys, output_keys=output_keys,
                             io_keys=io_keys)
        self._timeout = timeout
        self._received_msgs = {}
        rospy.Subscriber('detected_persons', DetectedPerson, self.callback)

        rospy.loginfo('SelectPersonState: init')

    def callback(self, msg):
        objId = msg.objectId
        self._received_msgs[objId]=msg

    def execute(self, ud):
        if self.preempt_requested():
            self.service_preempt()
            return 'preempted'
        rospy.sleep(rospy.Duration(0.6))
        outcome = 'failed'
        selected_person = None
        if len(self._received_msgs) == 0:
            rospy.loginfo('Person selection failed: no one has been detected')
            outcome = 'failed'
        else:
            # remove old detections
            objs_to_remove = []
            for key, value in self._received_msgs.iteritems():
                if ((rospy.Time.now() - value.header.stamp) >= self._timeout):
                    objs_to_remove.append(key)

            if len(objs_to_remove) > 0:
                for index in objs_to_remove:
                    del(self._received_msgs[index])

            # choose closest
            if len(self._received_msgs) != 0:
                # will choose the closest person
                closest = None
                for msg in self._received_msgs.itervalues():                 
                    if closest is None:
                        closest = msg
                    elif (distance(Point(), msg.position3D) <
                         distance(Point(), closest.position3D)):
                        closest = msg
                selected_person = closest
            else:
                rospy.loginfo('Nobody there.')

        if selected_person is not None:
            ud.pose.position = selected_person.position3D
            ud.id = selected_person.objectId
            outcome = 'done'
        else:
            outcome = 'failed'
        self._received_msgs = {}
        return outcome

class ThrottleState(smach.State):
    """ State that given a period of time in milliseconds, will return 'done' if more than the specified
        period has elapsed since the last time it returned done.
        (Returns 'done' every period milliseconds, otherwise returns 'false')
        first_call_success will determine if the first time this state is reached it must returned 'done' or it must wait until period ms have elapsed
    """
    def __init__(self, period_ms, first_call_success=True):
        smach.State.__init__(self, outcomes=['done','failed'])
        self._period = rospy.Duration(period_ms/1000,1000*period_ms%1000)
        if first_call_success:
            self._last_done = rospy.Time() #This is zero time
        else:
            self._last_done = rospy.Time.now()  

    
    def execute(self, ud):
        if (self._last_done + self._period) < rospy.Time.now() :
            self._last_done = rospy.Time.now()
            return 'done' 
        else:
            return 'failed'
        

class DummyState(smach.State):
    """ Dummy state that will always return 'done'
    """
    def __init__(self):
        smach.State.__init__(self, outcomes=['done'])
    
    def execute(self, ud):
        return 'done'
        
