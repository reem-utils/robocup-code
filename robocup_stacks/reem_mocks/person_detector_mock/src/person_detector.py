#! /usr/bin/env python
import roslib
roslib.load_manifest('person_detector_mock')
import rospy
#from random import random, randint
from iri_perception_msgs.msg import peopleTracking as PeopleTracking
from iri_perception_msgs.msg import peopleTrackingArray as PeopleTrackingArray

from random import randint, random

TO_BE_REMOVED_MASK = 0x01
OCCLUDDED_MASK = 0x02
CANDIDATE_MASK = 0x04
LEGGED_TARGET_MASK = 0x08
VISUALLY_CONFIRMED_MASK = 0x10
FRIEND_IN_SIGHT_MASK = 0x20
BACK_LEARNT_MASK = 0x40
FACE_LEARNT_MASK = 0x80

id_mock = 1


def random_person():
    person = PeopleTracking()
    person.targetStatus = 0
    isOccluded = randint(1, 2)
    if (isOccluded <= 1):
        person.targetStatus += OCCLUDDED_MASK
    isLegged = randint(1, 2)
    if (isLegged <= 1):
        person.targetStatus += LEGGED_TARGET_MASK
    isVisually = randint(1, 10)
    if (isVisually <= 1):
        person.targetStatus += VISUALLY_CONFIRMED_MASK
    global id_mock
    id_mock += 1
    person.targetId = id_mock#randint(1, 20)
    person.x = randint(5, 25) / 10.0
    person.y = randint(2, 7) / 10.0
    person.vx = randint(-17, 17) / 10.0
    person.vy = randint(-17, 17) / 10.0
    person.covariances = [random() for x in range(16)]
    return person


def detection_array():
    people = []
    for i in range(randint(1, 10)):
        person = random_person()
        people.append(person)
    people_tracking = PeopleTrackingArray(rospy.Header(), people)
    return people_tracking


def detector():
    pub = rospy.Publisher('closestPerson', PeopleTracking)
    pub2 = rospy.Publisher('/iri_people_tracking_rai/peopleSet', PeopleTrackingArray)
    rospy.init_node('person_detector')
    rate = rospy.Rate(2)  # Hz
    while not rospy.is_shutdown():
        message = random_person()
        pub.publish(message)
        message2 = detection_array()
        pub2.publish(message2)
        rate.sleep()

if __name__ == '__main__':
    try:
        detector()
    except rospy.ROSInterruptException:
        pass
