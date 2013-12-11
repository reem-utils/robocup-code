#! /usr/bin/env python
import smach
import rospy

from pal_smach_utils.utils.topic_reader import TopicReaderState

from object_recognition_mock.srv import enable
from pr_msgs.msg import ObjectPoseList
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from smach_ros import ServiceState


class RecognizeObjectsStateMachine(smach.StateMachine):
    '''Returns a list of all detected objects via the 'object_detected_list output' key.
    timeout indicates the timeout of the TopicReaderState that waits till it reads an object.
    The output_key is None when no object is recognized.'''

    def __init__(self, timeout=10):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=[], output_keys=['object_detected_list'])

        with self:

            def moped_enable_cb(userdata, response):
                if response.correct != None:
                    rospy.loginfo("ENABLE_CLOSE_OBJECT_SEARCH response: " + str(response.correct))
                    return succeeded
                else:
                    return aborted

            smach.StateMachine.add('ENABLE_CLOSE_OBJECT_SEARCH',
                             ServiceState('/iri_moped_handler/enable', enable,
                                          response_cb=moped_enable_cb,
                                          request=True),
                             transitions={succeeded: 'LOOK_FOR_OBJECTS', aborted: aborted})

            smach.StateMachine.add('LOOK_FOR_OBJECTS',
                             TopicReaderState(topic_name='/iri_moped_handler/outputOPL',
                                              msg_type=ObjectPoseList,
                                              timeout=timeout),
                              remapping={'message': 'object_detected_list'},
                              transitions={succeeded: 'DISABLE_CLOSE_OBJECT_SEARCH',
                                           aborted: 'NO_OBJECT_FOUND'})

            smach.StateMachine.add('NO_OBJECT_FOUND', EmptyMessageState(),
                                    remapping={'out_object_detected_list': 'object_detected_list'},
                                    transitions={succeeded: 'DISABLE_CLOSE_OBJECT_SEARCH'})

            def moped_disable_cb(userdata, response):
                if response.correct != None:
                    rospy.loginfo("DISABLE_CLOSE_OBJECT_SEARCH response: " + str(response.correct))
                    rospy.sleep(3.0)
                    return succeeded
                else:
                    return aborted

            smach.StateMachine.add('DISABLE_CLOSE_OBJECT_SEARCH',
                             ServiceState('/iri_moped_handler/enable', enable,
                                          response_cb=moped_disable_cb,
                                          request=False),
                             transitions={succeeded: succeeded, aborted: aborted})


class EmptyMessageState(smach.State):
    '''Simply forces the state machine to output a None message when no known objects are found.'''

    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys=['out_object_detected_list'])

    def execute(self, userdata):
        userdata.out_object_detected_list = None  # ObjectPoseList() with no objects is another posibility
        return succeeded
