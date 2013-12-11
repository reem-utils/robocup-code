#!/usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import copy
import random
from global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from topic_reader import TopicReaderState
from pal_vision_msgs.msg import FaceDetections
from math_utils import vector_magnitude


FACE_READING_TIMEOUT = 10
DEFAULT_HOG = []
SAW_LOADS_OF_FACES_TXT = "There are some people around here."
NO_FACES_SEEN_TXT = "No one is to be seen."
FOUND_FACE_TXT = "I found the face I was looking for"
NOT_FOUND_FACE_TXT = "I couldn't find the face."

BIG_SMALL_DIVIDING_HIGHT = 1.7
FAR_NEAR_DIVIDING_DISTANCE = 2.0
CENTERED_DIVIDING_OFFSET = 0.5

CENTERED_WORD = "CENTERED"
RIGHT_WORD = "RIGHT"
LEFT_WORD = "LEFT"

FAR_WORD = "FAR"
NEAR_WORD = "NEAR"

BIG_WORD = "BIG"
SMALL_WORD = "SMALL"


def SayIfHogsAreSimilar(hog1, hog2):
    """
    This function isnt finished yet. TODO
    For the moment it looks how alike are the two lists
    and makes a percentage based on the maximum length of both lists.
    """
    return 100 * len(frozenset(hog1).intersection(hog2)) / max(len(hog1), len(hog2))


def DistanceFromFace(face_point):
    """
    Calculates the distance projected in the ground from a face.
    """
    vector = copy.deepcopy(face_point)
    vector.z = 0.0
    return vector_magnitude(vector)


def FaceBigSmall(big_small_word, hight):

    if big_small_word == BIG_WORD:
        if hight < BIG_SMALL_DIVIDING_HIGHT:
            return False
        else:
            return True
    elif big_small_word == SMALL_WORD:
        if hight > BIG_SMALL_DIVIDING_HIGHT:
            return False
        else:
            return True
    else:
        return True


def FaceFarNear(far_near_word, position):

    if far_near_word == FAR_WORD:
        if DistanceFromFace(position) < FAR_NEAR_DIVIDING_DISTANCE:
            return False
        else:
            return True
    elif far_near_word == NEAR_WORD:
        if DistanceFromFace(position) > FAR_NEAR_DIVIDING_DISTANCE:
            return False
        else:
            return True
    else:
        return True


def FaceCenterRightLeft(centred_right_left_word, offset):

    if centred_right_left_word == CENTERED_WORD:
        if abs(offset) > CENTERED_DIVIDING_OFFSET:
            return False
        else:
            return True
    elif centred_right_left_word == RIGHT_WORD:
        if offset > 0.0:
            return False
        else:
            return True
    elif centred_right_left_word == LEFT_WORD:
        if offset < 0.0:
            return False
        else:
            return True
    else:
        return True


def BigSmallFilter(big_small_word, original_list):

    rospy.loginfo("FILTERING BY BIG_SMALL")
    rospy.loginfo("ORIGINAL LIST BIG SMALL==> " + str(original_list))
    filtered_list = list(filter(lambda x: FaceBigSmall(big_small_word, x.position3D.z), original_list))
    rospy.loginfo("FILTERED LIST BIG SMALL==> " + str(filtered_list))
    return filtered_list


def FarNearFilter(far_near_word, original_list):

    rospy.loginfo("ORIGINAL LIST NEAR FAR==> " + str(original_list))
    filtered_list = list(filter(lambda x: FaceFarNear(far_near_word, x.position3D), original_list))
    rospy.loginfo("FILTERED LIST NEAR FAR==> " + str(filtered_list))

    return filtered_list


def CentredRightLeftFilter(centred_right_left_word, original_list):

    rospy.loginfo("ORIGINAL LIST CENTERED_RIGHT_LEFT==> " + str(original_list))
    filtered_list = list(filter(lambda x: FaceCenterRightLeft(centred_right_left_word, x.position3D.y), original_list))
    rospy.loginfo("FILTERED LIST CENTERED_RIGHT_LEFT==> " + str(filtered_list))

    return filtered_list


def HightDistanceCenterFaceFilters(big_small_word, far_near_word, centred_right_left_word, original_list):

    #Filter by big or small
    new_faces_list = BigSmallFilter(big_small_word, original_list)
    #Filter by Far or Near
    new_faces_list2 = FarNearFilter(far_near_word, new_faces_list)
    #Filter by Centered. Right or Left
    new_faces_list3 = CentredRightLeftFilter(centred_right_left_word, new_faces_list2)

    return new_faces_list3


class ProcessFaces(smach.State):

    """
    Filters all the faces detected based on the properties given.

    #. First it will see if a Hog identifier is given. If so, it will look for a face that matches.
    If no face is found it will return aborted.
    #. If no hog is given, it will use the properties given to filter the faces detected.

    @input_keys: The input is of type pal_vision_msgs/FaceDetection[] inside faces_data_in.
    @output_keys: The output is of type pal_vision_msgs/FaceDetection inside face_data_out.
    """

    def __init__(self, hog_descriptor=DEFAULT_HOG, prop_big_small="", prop_far_near="", prop_centered_right_left=""):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             input_keys=['faces_data_in'],
                             output_keys=['face_data_out'])
        self._hog_descriptor = hog_descriptor
        self._prop_big_small = prop_big_small
        self._prop_far_near = prop_far_near
        self._prop_centered_right_left = prop_centered_right_left

    def execute(self, userdata):

        faces_list = copy.deepcopy(userdata.faces_data_in)

        # If we want to search for a precise face.
        rospy.loginfo("FILTERING BY HOG")
        if len(self._hog_descriptor) > 0:
            for i in range(len(faces_list)):
                if SayIfHogsAreSimilar(faces_list[i].hog, self._hog_descriptor):
                    rospy.loginfo("SELECTED FACE WAS ==>" + str(faces_list[i]))
                    userdata.face_data_out = faces_list[i]
                    return succeeded
            rospy.loginfo("NO FACE WAS SELECTED")
            return aborted

        final_filtered_list = HightDistanceCenterFaceFilters(self._prop_big_small,
                                                             self._prop_far_near,
                                                             self._prop_centered_right_left,
                                                             faces_list)

        #Once all the filters have been applied, we select a random face from the ones that were left.
        if len(final_filtered_list) == 0:
            rospy.loginfo("NO FACE WAS SELECTED")
            return aborted

        selected_face = final_filtered_list[random.randint(0, len(final_filtered_list)-1)]
        rospy.loginfo("SELECTED FACE WAS ==>" + str(selected_face))
        userdata.face_data_out = selected_face

        return succeeded


class DetectFaces(smach.StateMachine):

    """
    The output is of type pal_vision_msgs/FaceDetection[] inside face_detections_out.
    """

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    [succeeded, preempted, aborted],
                                    output_keys=['face_detections_out'])
        with self:

            def face_detection_cb(userdata, message):

                rospy.loginfo("Faces that I see now ==> " + str(message.faces))

                if len(message.faces) == 0:
                    rospy.loginfo("There are no faces to be seen. ")
                    return aborted
                rospy.loginfo("I can see faces.")
                userdata.face_detections_out = message.faces
                return succeeded

            smach.StateMachine.add('READ_FACE_DETECTION_TOPIC',
                                   TopicReaderState(topic_name='/person/faceDetections',
                                                    msg_type=FaceDetections,
                                                    timeout=FACE_READING_TIMEOUT,
                                                    callback=face_detection_cb,
                                                    output_keys=['face_detections_out']),
                                   transitions={succeeded: 'SAW_LOADS_OF_FACES', aborted: 'NO_FACES_SEEN'},
                                   remapping={'face_detections_out': 'face_detections_out'})

            some_faces_text = SAW_LOADS_OF_FACES_TXT
            smach.StateMachine.add('SAW_LOADS_OF_FACES',
                                   SpeakActionState(some_faces_text),
                                   transitions={succeeded: succeeded})

            no_faces_text = NO_FACES_SEEN_TXT
            smach.StateMachine.add('NO_FACES_SEEN',
                                   SpeakActionState(no_faces_text),
                                   transitions={succeeded: aborted})


class DetectAFace(smach.StateMachine):

    def __init__(self, hog_descriptor=DEFAULT_HOG, prop_big_small="", prop_far_near="", prop_centered_right_left=""):
        smach.StateMachine.__init__(self,
                                    [succeeded, 'no_face_found', preempted, aborted],
                                    output_keys=['face_data_out'])

        self._hog_descriptor = hog_descriptor
        self._prop_big_small = prop_big_small
        self._prop_far_near = prop_far_near
        self._prop_centered_right_left = prop_centered_right_left

        with self:

            smach.StateMachine.add('DETECT_FACES',
                                   DetectFaces(),
                                   transitions={succeeded: 'PROCESS_FACES', preempted: preempted, aborted:  'no_face_found'},
                                   remapping={'face_detections_out': 'face_detections_out'})

            smach.StateMachine.add('PROCESS_FACES',
                                   ProcessFaces(self._hog_descriptor, self._prop_big_small, self._prop_far_near, self._prop_centered_right_left),
                                   transitions={succeeded: 'FOUND_FACE', preempted: preempted, aborted: 'NOT_FOUND_FACE'},
                                   remapping={'faces_data_in': 'face_detections_out',
                                              'face_data_out': 'face_data_out'})

            a_face_text = FOUND_FACE_TXT
            smach.StateMachine.add('FOUND_FACE',
                                   SpeakActionState(a_face_text),
                                   transitions={succeeded: succeeded})

            no_face_text = NOT_FOUND_FACE_TXT
            smach.StateMachine.add('NOT_FOUND_FACE',
                                   SpeakActionState(no_face_text),
                                   transitions={succeeded:  'no_face_found'})
