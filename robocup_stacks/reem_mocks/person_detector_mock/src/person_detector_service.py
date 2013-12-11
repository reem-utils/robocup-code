#! /usr/bin/env python
import roslib; roslib.load_manifest('person_detector_mock')
import rospy

from random import random, randint

from person_detector_mock.srv import DetectPeople, DetectPeopleResponse
from iri_perception_msgs.msg import peopleTracking as PeopleTracking
from iri_perception_msgs.msg import peopleTrackingArray as PeopleTrackingArray

personx = 1.5
persony = 0.0

def random_person():
	person = PeopleTracking()
	person.x = randint(0, 1000) / 10.0
	person.y = randint(0, 1000) / 10.0
	person.vx = randint(0, 100) / 10.0
	person.vy = randint(0, 100) / 10.0
	person.covariances = [random() for x in range(16)]
	return person
	
def fixed_person():
    global personx
    global persony
    person = PeopleTracking()
    person.x = personx
    person.y = persony
    person.vx = randint(0, 100) / 10.0
    person.vy = randint(0, 100) / 10.0
    person.covariances = [random() for x in range(16)]
    personx= personx + 0.1
    persony = persony + 0.0
    return person

def handle_detection(req):
	people = []
	for i in range(randint(0, 7)):
		person = random_person()
#		person = fixed_person()
		person.targetId = i
		people.append(person)
	people_tracking = PeopleTrackingArray(rospy.Header(), people)
	return DetectPeopleResponse(people_tracking)

def detector_service():
	rospy.init_node('person_detector_service')
	s = rospy.Service('detectPeople', DetectPeople, handle_detection)
	rospy.spin()

if __name__ == '__main__':
	detector_service()
