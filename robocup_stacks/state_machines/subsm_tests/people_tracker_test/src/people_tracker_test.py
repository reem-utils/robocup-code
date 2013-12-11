#! /usr/bin/env python

import roslib
roslib.load_manifest('people_tracker_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from smach import CBState

from pal_smach_utils.utils.topic_reader import TopicReaderState

from iri_perception_msgs.msg import peopleTrackingArray

from pal_smach_utils.utils.colors import Colors

from visualization_msgs.msg import Marker, MarkerArray

from geometry_msgs.msg import Point, Pose

from pal_smach_utils.utils.math_utils import vector_magnitude

colors = Colors()

i = 0
marker_array = MarkerArray()
MAX_NUMBER_PT_TEST_MARKERS = 100
PT_TEST_MARKERS_LIFETIME = 1.0

tracked_person_id = None

MAX_LEARN_DISTANCE = rospy.get_param('/params_follow_me/max_distance', 2.0)
MAX_LEARN_DISPLACEMENT = rospy.get_param('/params_follow_me/max_displace', 1.0)

tracked_marker_array = MarkerArray()


def findPersonByIdInPeopleSet(targetId=None, peopleSet=None):
    if (id is not None and peopleSet is not None):
        for person in peopleSet:
            if (person.targetId == targetId):
                return person

    return None


def main():
    rospy.init_node('sm_people_tracker_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        @smach.cb_interface(outcomes=[succeeded])
        def showStartMessage(userdata):
            rospy.loginfo(colors.YELLOW_BOLD + "Starting people tracker test..." + colors.NATIVE_COLOR)
            return succeeded

        smach.StateMachine.add('BEGIN_PEOPLE_TRACKER_TEST',
                               CBState(showStartMessage),
                               transitions={succeeded: 'GRAB_PEOPLE_TRACKER_DATA'})

        # When timeout is set to None, TopicReaderState will wait till it reads some data
        # We rely in the people tracker in this case because this state will always finish
        # since the people tracker will send at least an empty array of persons detected
        smach.StateMachine.add('GRAB_PEOPLE_TRACKER_DATA',
                               TopicReaderState(topic_name='/iri_people_tracking_rai/peopleSet', msg_type=peopleTrackingArray, timeout=None),
                               transitions={succeeded: 'PROCESS_PEOPLE_TRACKER_DATA',
                                            preempted: preempted,
                                            aborted: 'GRAB_PEOPLE_TRACKER_DATA'},
                               remapping={'message': 'out_persons_detected'})

        @smach.cb_interface(outcomes=[succeeded])
        def showPeopleTrackerData(userdata):
            rospy.loginfo(colors.YELLOW + "Showing people tracker data..." + colors.NATIVE_COLOR)

            global tracked_person_id
            if (tracked_person_id is None):

                pt_learning_zone_marker_pub = rospy.Publisher("/LEARNING_ZONE_people_tracker_test/", Marker)

                learning_zone_marker = Marker()
                learning_zone_marker.header.frame_id = "/base_link"
                learning_zone_marker.ns = "learning_zone_ns"
                learning_zone_marker.id = 0
                learning_zone_marker.type = learning_zone_marker.LINE_STRIP
                learning_zone_marker.action = learning_zone_marker.ADD
                learning_zone_marker.points = [Point(), Point(), Point(), Point()]
                learning_zone_marker.points[0].x = 0.0
                learning_zone_marker.points[0].y = 0.0
                learning_zone_marker.points[0].z = 0.0
                learning_zone_marker.points[1].x = MAX_LEARN_DISTANCE
                learning_zone_marker.points[1].y = MAX_LEARN_DISPLACEMENT
                learning_zone_marker.points[1].z = 0.0
                learning_zone_marker.points[2].x = MAX_LEARN_DISTANCE
                learning_zone_marker.points[2].y = -MAX_LEARN_DISPLACEMENT
                learning_zone_marker.points[2].z = 0.0
                learning_zone_marker.points[3].x = 0.0
                learning_zone_marker.points[3].y = 0.0
                learning_zone_marker.points[3].z = 0.0
                learning_zone_marker.pose.position.x = 0.0
                learning_zone_marker.pose.position.y = 0.0
                learning_zone_marker.pose.position.z = 0.0
                learning_zone_marker.scale.x = 0.05
                learning_zone_marker.color.a = 0.9
                learning_zone_marker.color.r = 1.0
                learning_zone_marker.color.g = 0.5
                learning_zone_marker.color.b = 0.4
                learning_zone_marker.lifetime = rospy.Duration(1.0)
                learning_zone_marker.header.stamp = rospy.Time.now()

                pt_learning_zone_marker_pub.publish(learning_zone_marker)

                min_distance = MAX_LEARN_DISTANCE
                for person in userdata.in_persons_detected.peopleSet:
                    displace = abs(person.y)
                    person_pose = Pose()
                    person_pose.position.x = person.x
                    person_pose.position.y = person.y
                    distance = vector_magnitude(person_pose.position)
                    if displace < MAX_LEARN_DISPLACEMENT and distance < min_distance:
                        min_distance = distance
                        tracked_person_id = person.targetId

                if (tracked_person_id is None):
                    rospy.loginfo(colors.YELLOW_BOLD + "    THERE ISN'T ANY CANDIDATE IN FRONT OF THE ROBOT" + colors.NATIVE_COLOR)
                else:
                    rospy.loginfo(colors.BACKGROUND_GREEN + "    Following person with id => " + str(tracked_person_id) + colors.NATIVE_COLOR)

            tracked_person = findPersonByIdInPeopleSet(tracked_person_id, userdata.in_persons_detected.peopleSet)
            if (tracked_person is not None):
                pt_tracked_marker_pub = rospy.Publisher("/LEARNING_ZONE_people_tracker_test/", Marker)

                marker = Marker()
                marker.header.frame_id = "/base_link"
                marker.ns = "person_tracked_ns"
                marker.id = 0
                marker.type = marker.CYLINDER
                marker.action = marker.ADD
                marker.pose.position.x = tracked_person.x
                marker.pose.position.y = tracked_person.y
                marker.pose.position.z = 0.5
                marker.scale.x = 0.1
                marker.scale.y = 0.1
                marker.scale.z = 1.0
                marker.color.a = 1.0
                marker.color.r = 0.2
                marker.color.g = 0.2
                marker.color.b = 0.2
                marker.lifetime = rospy.Duration(10.0)
                marker.header.stamp = rospy.Time.now()

                pt_tracked_marker_pub.publish(marker)
            elif (tracked_person_id is not None):
                rospy.loginfo(colors.RED_BOLD + "    LOST PERSON with id => " + str(tracked_person_id) + colors.NATIVE_COLOR)

            pt_test_marker_pub = rospy.Publisher("/people_tracker_test/", MarkerArray)

            global markers
            global i
            for person in userdata.in_persons_detected.peopleSet:

                marker = Marker()
                marker.header.frame_id = "/base_link"
                marker.ns = "people_tracked_ns"
                marker.id = i
                marker.type = marker.ARROW
                marker.action = marker.ADD
                marker.points = [Point(), Point()]
                marker.points[0].x = person.x
                marker.points[0].y = person.y
                marker.points[0].z = 0.0
                marker.points[1].x = person.x + person.vx
                marker.points[1].y = person.y + person.vy
                marker.points[1].z = 0.0
                marker.scale.x = 0.1  # arrow shaft diameter
                marker.scale.y = 0.1  # arrow head diameter
                marker.scale.z = 0.0  # arrow head length if is not zero
                marker.color.a = 0.4
                marker.color.r = 0.5
                marker.color.g = 0.0
                marker.color.b = 1.0
                marker.lifetime = rospy.Duration(PT_TEST_MARKERS_LIFETIME)
                marker.header.stamp = rospy.Time.now()

                marker_array.markers.append(marker)

                i += 1
                if (i >= MAX_NUMBER_PT_TEST_MARKERS):
                    marker_array.markers.pop(0)

            pt_test_marker_pub.publish(marker_array)

            return succeeded

        smach.StateMachine.add('PROCESS_PEOPLE_TRACKER_DATA',
                               CBState(showPeopleTrackerData, input_keys=['in_persons_detected']),
                               remapping={'in_persons_detected': 'out_persons_detected'},
                               transitions={succeeded: 'GRAB_PEOPLE_TRACKER_DATA'})

    sis = smach_ros.IntrospectionServer('people_tracker_test_sm', sm, '/PEOPLE_TRACKER_TEST')
    sis.start()
    sm.execute()

    rospy.spin()
    rospy.loginfo(colors.BACKGROUND_GREEN + "PEOPLE TRACKER TEST HAS BEEN STOPPED" + colors.NATIVE_COLOR)
    sis.stop()

if __name__ == '__main__':
    main()
