#!/usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach
from global_common import succeeded, preempted, aborted, o1, o2, o3, o4
from pal_smach_utils.speech.sound_action import SpeakActionState
from topic_reader import TopicReaderStateMultiOutcomes
from pal_vision_msgs.msg import Gesture

GESTURE_READING_TIMEOUT = 10
DETECTED_GESTURE_TXT = "Oh, there you are. "
WRONG_DETECTED_GESTURE_TXT = "I have seen a "
WRONG_DETECTED_GESTURE_TXT_2 = ", but it's not what I was looking for."
GESTURE_NOT_DETECTED_TXT = "I don't see anyone making gestures. "


class GestureRecognition(smach.StateMachine):

    """
    Returns succeeded when detected the gesture given in gesture_looking_for.
    By default it looks for a Wave gesture.
    """

    def __init__(self, gesture_looking_for="Wave"):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted],
                                    output_keys=['gesture_id_out', "out_person_position"])

        self._gesture_looking_for = gesture_looking_for

        with self:

            def gesture_cb(userdata, message):
                """
                If gesture_id is empty --> returns aborted
                if gesture_id is the one we are looking for --> o1
                and if its not empty but not the one we are searching --> o2
                """
                rospy.loginfo("GESTURE RECOGNIZED ==> " + str(message.gestureId))
                rospy.loginfo("\n======================\nMESSAGE: \n %s\n", str(message))

                userdata.out_person_position = None

                if message.gestureId == "":
                    return aborted

                if message.gestureId == self._gesture_looking_for:
                    rospy.loginfo("CORRECT GESTURE! ")
                    userdata.gesture_id_out = message.gestureId
                    userdata.out_person_position = message
                    return o1
                rospy.loginfo("WRONG GESTURE! ")
                userdata.gesture_id_out = message.gestureId
                return o2

            smach.StateMachine.add('READ_GESTURE_TOPIC',
                                   TopicReaderStateMultiOutcomes(topic_name='recognized_gestures',
                                                                 msg_type=Gesture,
                                                                 timeout=GESTURE_READING_TIMEOUT,
                                                                 callback=gesture_cb,
                                                                 output_keys=['gesture_id_out', "out_person_position"]),
                                   transitions={o1: 'DETECTED_GESTURE',
                                                o2: 'WRONG_GESTURE_DETECTED',
                                                o3: 'GESTURE_NOT_DETECTED',
                                                o4: 'GESTURE_NOT_DETECTED',
                                                aborted: 'GESTURE_NOT_DETECTED'},
                                   remapping={'gesture_id_out': 'gesture_id_out'})

            def detected_gesture_cb(userdata):
                gesture_word = userdata.gesture_id_in
                detected_text = DETECTED_GESTURE_TXT + "I detected, " + str(gesture_word) + " . "
                return detected_text

            smach.StateMachine.add('DETECTED_GESTURE',
                                   SpeakActionState(text_cb=detected_gesture_cb, input_keys=['gesture_id_in']),
                                   transitions={succeeded: succeeded},
                                   remapping={'gesture_id_in': 'gesture_id_out'})

            def wrong_detected_gesture_cb(userdata):
                gesture_word = userdata.gesture_id_in
                text = WRONG_DETECTED_GESTURE_TXT + str(gesture_word) + WRONG_DETECTED_GESTURE_TXT_2
                return text

            smach.StateMachine.add('WRONG_GESTURE_DETECTED',
                                   SpeakActionState(text_cb=wrong_detected_gesture_cb, input_keys=['gesture_id_in']),
                                   transitions={succeeded: aborted},
                                   remapping={'gesture_id_in': 'gesture_id_out'})

            not_detected_text = GESTURE_NOT_DETECTED_TXT
            smach.StateMachine.add('GESTURE_NOT_DETECTED',
                                   SpeakActionState(not_detected_text),
                                   transitions={succeeded: aborted})
