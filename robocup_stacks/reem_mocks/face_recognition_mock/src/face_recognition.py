#! /usr/bin/env python
import roslib
roslib.load_manifest('face_recognition_mock')
import rospy
import actionlib
import random

from face_recognition.msg import FaceRecognitionResult, FaceRecognitionAction
from pal_vision_msgs.msg import FaceDetections, FaceDetection, Rectangle
from geometry_msgs.msg import Point

MAX_FACES_TO_CREATE = 10
MIN_FACES_TO_CREATE = 0


class FaceRecognitionServer:

    #_names = ['Homer', 'Lisa', 'Bart']
    _names = rospy.get_param('mock_config/face_recognition', ["james", "john", "robert"])  # , "michael", "william", "david", "richard", "charles", "joseph", "thomas", "mary", "patricia", "linda", "barbara", "elizabeth", "jennifer", "maria", "susan", "margret", "dorothy"]

    def __init__(self, name):
        self._server = actionlib.SimpleActionServer(name,
                                                    FaceRecognitionAction,
                                                    self._execute,
                                                    auto_start=False)
        print "\033[00;32mThe face_recognition (mock) can recognize: " + str(self._names) + str('\033[m')
        self._server.start()

    def _execute(self, goal):
        result = FaceRecognitionResult()
        if goal.order_id == 0:
            # recognize once
            result.order_id = 0
            result.names = random.sample(self._names, random.randint(0, len(self._names)))
            result.confidence = sorted(
                [70 + 30 * random.random() for x in range(len(result.names))],
                reverse=True)
        elif goal.order_id == 3:
            # re(train)
            result.order_id = 3
            self._names.append(goal.order_argument)
            result.names = random.sample(self._names, 1)
            result.confidence = [100.0]
        else:
            raise ValueError

        self._server.set_succeeded(result)


class Point2():
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0


def createRandomFace():

    face_pos = Point2()
    face_pos.x = random.randint(3, 40) / 10.0
    face_pos.y = random.randint(-20, 20) / 10.0
    face_pos.z = random.randint(10, 20) / 10.0
    face_pos_bb = Rectangle()
    face_pos_hog = [random.random(), random.random()]
    return FaceDetection(face_pos, face_pos_bb, face_pos_hog)


def createFaces():

    faces_detected = FaceDetections()
    for i in range(0, random.randint(MIN_FACES_TO_CREATE, MAX_FACES_TO_CREATE)):
        faces_detected.faces.append(createRandomFace())

    return faces_detected


def detector_service():

    """
    TODO , which is the correct name for the topic of the publisher
    """

    rospy.init_node('face_recognition')
    server = FaceRecognitionServer(rospy.get_name())
    pub = rospy.Publisher('/person/faceDetection', FaceDetections)
    pub2 = rospy.Publisher('/person/faceDetections', FaceDetections)
    rate = rospy.Rate(2)  # Hz
    while not rospy.is_shutdown():
        message = FaceDetections()
        pos = Point
        pos.x = 1.0
        pos.y = 1.0
        pos.z = 1.0
        bb = Rectangle()
        hog = [1.0, 0.1]
        face = FaceDetection(pos, bb, hog)
        # face.position3D = pos
        message.faces.append(face)
        pub.publish(message)

        pub2.publish(createFaces())
        rate.sleep()

if __name__ == '__main__':
    detector_service()

# vim: expandtab ts=4 sw=4
