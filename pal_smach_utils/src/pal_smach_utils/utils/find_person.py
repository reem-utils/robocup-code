import sys
import smach
from tf.transformations import quaternion_from_euler

from geometry_msgs.msg import Pose, Point, Quaternion
from iri_perception_msgs.msg import peopleTrackingArray
"""
try:
    from iri_people_tracking_rai.msg import peopleTrackingArray
except:
    from iri_perception_msgs.msg import peopleTrackingArray
"""
from topic_reader import TopicReaderState
from pal_smach_utils.navigation.move_action import MoveActionState


from global_common import DETECT_PEOPLE_TIMEOUT, succeeded, aborted, preempted
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
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
                output_keys=['closest_person'])

        with self:

            def detect_person_cb(userdata, message):
                people = message.peopleSet
                closestPerson = None
                closestPersonDistance = sys.maxint
                for person in people:
                    dist = person.x ** 2 + person.y ** 2
                    if dist < closestPersonDistance:
                        closestPerson = person
                        closestPersonDistance = dist
                    # FIXME: blacklist already seen people
                userdata.closest_person = closestPerson
                return succeeded if closestPerson else aborted

            smach.StateMachine.add(
                'DETECT_PERSON',
                TopicReaderState(
                    topic_name='/iri_people_tracking_rai/peopleSet',
                    msg_type=peopleTrackingArray,
                    callback=detect_person_cb,
                    output_keys=['closest_person'],
                    timeout=DETECT_PEOPLE_TIMEOUT),
                transitions={aborted: 'ROTATION_CHECK', preempted: "DETECT_PERSON", succeeded: succeeded})

            # outputs: closest_person

            pose = Pose()
            pose.position = Point(0, 0, 0)
            pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 30))  # I (Ruben) think that the rotation it's 1.57079632679 = 90g

            smach.StateMachine.add('ROTATION_CHECK',
                RotationCounter(),
                transitions={succeeded: 'ROTATE', aborted: aborted}
                )

            smach.StateMachine.add(
                'ROTATE',
                MoveActionState("/base_link", pose=pose),
                transitions={succeeded: 'DETECT_PERSON', aborted: "DETECT_PERSON", preempted: "DETECT_PERSON"})

# vim: expandtab ts=4 sw=4
