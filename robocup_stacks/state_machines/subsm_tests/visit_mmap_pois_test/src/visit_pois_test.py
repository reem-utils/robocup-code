#! /usr/bin/env python
import roslib
roslib.load_manifest('visit_mmap_pois_test')
import rospy
import smach
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler
from pal_smach_utils.navigation.move_action import MoveActionState

BANNED = ['exit', 'drinks_location', 'party_room', 'registration table']


def tuple_to_pose(tup):
    pose = Pose()
    print tup
    pose.position = Point(tup[0], tup[1], 0)
    pose.orientation = Quaternion(*quaternion_from_euler(0, 0, tup[2]))
    return pose

count_1 = 0
count_2 = 0


def main():
    rospy.init_node('visit_pois_mmap_test')

    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])
    pois = rospy.get_param('/mmap/poi/submap_0').iteritems()
    loc_prob = []
    for l in rospy.get_param('/mmap/locations_prob/').iteritems():
        loc_prob.append((l[0], l[1].iteritems()))

    with sm:
        def get_next_poi(userdata):
            global count_1, count_2
            for a in pois:  # userdata.poi = (1 2, name)
                if not a[1][1] in BANNED:
                    userdata.poi = (1, a[1][1])
                    userdata.poi_pose = tuple_to_pose((a[1][2], a[1][3], a[1][4]))
                    count_1 += 1
                    return succeeded
            for a in loc_prob:
                for b in a[1]:  # userdata.poi = (2, room name, poi name)
                    userdata.poi = (2, a[0], b[0])
                    userdata.poi_pose = tuple_to_pose((b[1][1], b[1][2], b[1][3]))
                    count_2 += 1
                    return succeeded
            print count_1, count_2
            return 'finished'

        smach.StateMachine.add('GET_NEXT_POI',
                               smach.CBState(get_next_poi,
                                             input_keys=[],
                                             output_keys=['poi', 'poi_pose'], outcomes=[succeeded, 'finished']),
                               transitions={succeeded: 'ANNOUNCE_NEXT_POI', 'finished': succeeded})

        def tell_next_poi(userdata):
            print userdata.poi
            if userdata.poi[0] == 1:
                return "Going to the %s" % userdata.poi[1]
            return "Going to the %s's %s" % (userdata.poi[1], userdata.poi[2])

        smach.StateMachine.add('ANNOUNCE_NEXT_POI', SpeakActionState(text_cb=tell_next_poi, input_keys=['poi']),
                               transitions={succeeded: 'GO_TO_POI'})

        smach.StateMachine.add('GO_TO_POI',
                               MoveActionState("/map", goal_key='poi_pose'),
                               transitions={succeeded: 'GET_NEXT_POI', aborted: 'ANNOUNCE_ABORTED'})

        def tell_next_poi(userdata):
            if userdata.poi[0] == 1:
                    return 'Moving to %s aborted' % userdata.poi[1]
            return "Moving to %s's %s aborted" % (userdata.poi[1], userdata.poi[2])

        smach.StateMachine.add('ANNOUNCE_ABORTED', SpeakActionState(text_cb=tell_next_poi, input_keys=['poi']),
                               transitions={succeeded: 'GET_NEXT_POI'})

    sis = smach_ros.IntrospectionServer('visit_pois_test', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
