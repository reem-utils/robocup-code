import sys
import smach
from tf.transformations import quaternion_from_euler

from geometry_msgs.msg import Pose, Point, Quaternion
# from pal_vision_msgs.msg import FaceDetections
# Import face detection messages
from face_detector.msg import FaceDetectorAction
"""
try:
    from iri_people_tracking_rai.msg import peopleTrackingArray
except:
    from person_detector_mock.msg import peopleTrackingArray
"""
# from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_smach_utils.navigation.move_action import MoveActionState
from smach_ros import SimpleActionState
from rospy.rostime import Duration
from pal_smach_utils.utils.global_common import transform_pose

# import math


from pal_smach_utils.utils.global_common import DETECT_PEOPLE_TIMEOUT, succeeded, aborted, preempted
COUNTNUMBER = 4


class RotationCounter(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted])
        self.counter = 0

    def execute(self, userdata):
        if self.counter < COUNTNUMBER:
            self.counter = self.counter + 1
            print self.counter
            return succeeded
        else:
            self.counter = 1
            return aborted


class FindPersonStateMachine(smach.StateMachine):
    """
    Looks for a person, rotating in place if necessary, and return any
    information in `closest_person'.
    """

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=['location_list'], output_keys=['closest_person'])

        with self:

            # def detect_person_cb(userdata, message):
            #     LOCATION_LIST_DISTANCE = 1
            #     people = message.faces
            #     if userdata.location_list:
            #         for person in people:
            #             #for key, not_walking in userdata.location_list.items():
            #             for not_walking in userdata.location_list:
            #                 """
            #                 print "not_walking[0]: type %s, valor %s " % (type(not_walking[0]), str(not_walking[0]))
            #                 print "not_walking[1]: type %s, valor %s " % (type(not_walking[1]), str(not_walking[1]))
            #                 print "not_walking_list: type %s, valor %s " % (type(not_walking), str(not_walking))
            #                 print "Ahora los indexes y valores"
            #                 for test_test in not_walking:
            #                     print "\n", test_test

            #                 print "\n\n\n\n==============Ahora testando indices 0 y 1 tenemos: %s Y %s =======\n\n\n" % (not_walking[0], not_walking[1])
            #                 """
            #                 distance_from_list = math.sqrt((person.position3D.x - not_walking[0]) ** 2 + (person.position3D.y - not_walking[1]) ** 2)
            #                 if distance_from_list < LOCATION_LIST_DISTANCE:
            #                     people.pop(people.index(person))

            #     closestPerson = None
            #     closestPersonDistance = sys.maxint
            #     for person in people:
            #         dist = person.position3D.x ** 2 + person.position3D.y ** 2
            #         if dist < closestPersonDistance:
            #             closestPerson = person
            #             closestPersonDistance = dist
            #         # FIXME: blacklist already seen people
            #     userdata.closest_person = closestPerson
            #     return succeeded if closestPerson else aborted

            def detect_faces_cb_ros_pkg(userdata, status, result):

                '''This code detects faces using the ROS package and then checks the list of people who are not able to walk.
                If the distance of people who are not able to walk is close to the detected faces they are popped from the list.
                First perosn who is closer than ---closestPersonDistance--- are sent to userdata'''

                LOCATION_LIST_DISTANCE = 1
                print "CallBack is called"
                people = result.face_positions
                # pose_in_map = transform_pose(people.pos, people.header.frame_id, "/map")
                if userdata.location_list:
                    for person in people:
                        pose_in_stereo = Pose()
                        pose_in_stereo.position = person.pos

                        pose_in_map = transform_pose(pose_in_stereo, userdata.message.header.frame_id, "/map")

                        for not_walking in userdata.location_list:
                            distance_from_list = ((pose_in_map.position.x - not_walking[0])**2 + (pose_in_map.position.pos.y - not_walking[1])**2)
                            if distance_from_list < LOCATION_LIST_DISTANCE:
                                people.pop(people.index(person))

                closestPerson = None
                closestPersonDistance = sys.maxint
                for person in people:
                    dist = person.pos.z
                    if dist < closestPersonDistance:
                        closestPerson = person
                        closestPersonDistance = dist
                    # FIXME: blacklist already seen people
                userdata.closest_person = closestPerson
                print "Closest person (from find_person_with_visit_checker): ", closestPerson
                return succeeded if closestPerson else aborted

            # smach.StateMachine.add(
            #     'DETECT_PERSON',
            #     TopicReaderState(
            #         topic_name = 'face_detector/result',
            #         msg_type = PositionMeasurementArray,
            #         callback = detect_faces_cb_ros_pkg,
            #         output_keys = ['closest_person'],
            #         input_keys = ['location_list'],
            #         timeout = DETECT_PEOPLE_TIMEOUT),
            #     transitions = {aborted: 'ROTATION_CHECK', succeeded: succeeded})

            smach.StateMachine.add(
                'DETECT_PERSON',
                SimpleActionState(
                    '/face_detector',
                    FaceDetectorAction,
                    exec_timeout=Duration(DETECT_PEOPLE_TIMEOUT),
                    result_cb=detect_faces_cb_ros_pkg,
                    input_keys=['location_list'],
                    output_keys=['closest_person']),
                transitions={aborted: 'ROTATION_CHECK', succeeded: succeeded})

            # outputs: closest_person

            pose = Pose()
            pose.position = Point(0, 0, 0)
            pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 30))

            smach.StateMachine.add(
                'ROTATION_CHECK',
                RotationCounter(),
                transitions={'succeeded': 'ROTATE', aborted: aborted})

            smach.StateMachine.add(
                'ROTATE',
                MoveActionState("/base_link", pose=pose),
                transitions={succeeded: 'DETECT_PERSON'})

# vim: expandtab ts=4 sw=4
