#! /usr/bin/env python
import roslib
roslib.load_manifest('person_detector_mock')
import rospy
#from random import random, randint
from iri_perception_msgs.msg import peopleTracking as PeopleTracking
from iri_perception_msgs.msg import peopleTrackingArray as PeopleTrackingArray

from random import randint, random

from pal_smach_utils.utils.publish_marker import PublishMarkerWithName
from geometry_msgs.msg import Pose

CONST_ID = 1


"""
     ^ X IN Base Link, AXIS of REEM
     |
Y    |
<----+

"""


def random_person():
    person = PeopleTracking()
    person.targetId = randint(0, 10)
    person.x = randint(10, 20) / 10.0
    person.y = randint(-10, 10) / 10.0
    person.vx = randint(-17, 17) / 10.0
    person.vy = randint(-17, 17) / 10.0
    person.covariances = [random() for x in range(16)]
    return person


def constant_id_person_turns_around():
    person = PeopleTracking()
    person.targetId = CONST_ID
    person.x = randint(10, 20) / 10.0
    person.y = 0.5
    person.vx = 0.0
    person.vy = 0.0
    person.covariances = [random() for x in range(16)]
    return person


class MarkerUserdata():
    """
    This is a class created to use a State od smach structure.
    """
    def __init__(self):
        self.setData()

    def setData(self):
        self.in_pose = Pose()


def PublishPeopleTrackingMarker(person):

    """
    Inputs data person is of type PeopleTRacking.
    It publishes a marker of the position of that person.
    """

    person_pose = MarkerUserdata()
    person_pose.in_pose.position.x = person.x
    person_pose.in_pose.position.y = person.y
    person_pose.in_pose.position.z = 0

    marker_state = PublishMarkerWithName(marker_name="/people_tracking_mock/person_position")
    marker_state.execute(person_pose)

    return person_pose


def detection_array():
    people = []
    #Here we simulate the fact that the person data is not always published.
    for i in range(randint(1, 1)):
            person = constant_id_person_turns_around()
            rospy.loginfo("PERSON CREATED =====>>>>> " + str(person))
            people.append(person)
            PublishPeopleTrackingMarker(person)
    people_tracking = PeopleTrackingArray(rospy.Header(), people)
    return people_tracking


def detector():
    pub = rospy.Publisher('/iri_people_tracking_rai/peopleSet', PeopleTrackingArray)
    rospy.init_node('person_detector_advanced')
    rate = rospy.Rate(10)  # Hz
    while not rospy.is_shutdown():
        message = detection_array()
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        detector()
    except rospy.ROSInterruptException:
        pass
