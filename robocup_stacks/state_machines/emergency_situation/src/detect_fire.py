#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('emergency_situation')
import rospy
import smach

from pal_smach_utils.speech.sound_action import SpeakActionState
from geometry_msgs.msg import Quaternion
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from smach_ros import SimpleActionState
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler
from std_msgs.msg import Float64
from pal_smach_utils.utils.topic_reader import TopicReaderState
from pal_smach_utils.navigation.get_current_pos import GetPosition
from sensor_msgs.msg import Image
import cv
from cv_bridge import CvBridge
import numpy as np


COUNTNUMBER = 4
RESULTS_COUNT = 5


class MoveToNextLocationChecker(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted, 'go_self'], output_keys=['o_rotation_angle', 'o_position_in_kitchen'])
        self.index_loc = 0
        self.index_angle = 0
        self.pois = rospy.get_param("/mmap/fire_locations")
        self.position_in_kitchen = []
        self.rotationAngle = []

        for key, value in self.pois.iteritems():
                self.position_in_kitchen.append([value[2], value[3]])
                self.rotationAngle.append([value[4]])  # , value[4] + 3.14/2, value[4] + 3.14, value[4] + 3*3.14/2])

    def execute(self, userdata):
        print len(self.rotationAngle)
        print str(self.position_in_kitchen) + "x y list"
        print str(self.rotationAngle) + "orientation"
        if self.index_loc < len(self.position_in_kitchen):
            if self.index_angle < len(self.rotationAngle[self.index_loc]):
                print self.position_in_kitchen[self.index_loc]
                userdata.o_position_in_kitchen = self.position_in_kitchen[self.index_loc]

                userdata.o_rotation_angle = self.rotationAngle[self.index_loc][self.index_angle]
                print str(self.rotationAngle[self.index_loc][self.index_angle]) + "Rotation angle"
                self.index_angle += 1
                return succeeded
            else:
                self.index_angle = 0
                self.index_loc = self.index_loc + 1
                return 'go_self'
        else:
            return aborted


class RecordPosition(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded, aborted, preempted], input_keys=['fire_location_map'], output_keys=['location_of_fire'])

    def execute(self, userdata):
        print rospy.loginfo("Saving Fire Location ................")
        self.fire_location = [userdata.fire_location_map.x, userdata.fire_location_map.position.y]
        print rospy.loginfo("Location is saved successfully !!!!")
        userdata.location_list = self.fire_location
        return succeeded


# class CheckSmokeStateMachine(smach.State):
#     def __init__(self):
#         smach.State.__init__(self, outcomes=[succeeded, aborted])
#         self.count = 0

#     def execute(self, userdata):
#         if self.count == RESULTS_COUNT


#         self.smoke = random.randint(0,1)
#         if self.smoke == 1:
#             print "Fire detected ..................................."
#             return succeeded
#         else:
#             print "There is nothing going on ......................."
#             return aborted


class DetectFireOrSmokeStateMachine(smach.StateMachine):

    def __init__(self):
        smach.StateMachine.__init__(self, outcomes=[succeeded, aborted, preempted], output_keys=['location_of_fire'])

        with self:

            self.countSuceeded = 0
            self.countAborted = 0
            self.count = 0
            self.countIDontKnow = 0

            def move_around(userdata, goal):
                # position_list_x=[0,0,0.5,0]
                # position_list_y=[0,0,0.5,0]
                # rotationAngle_list=[0,90,180,270]
                index = 0
                moveGoal = MoveBaseGoal()
                moveGoal.target_pose.header.stamp = rospy.Time.now()
                moveGoal.target_pose.header.frame_id = '/map'
                moveGoal.target_pose.pose.position.x = userdata.i_position_in_kitchen[0]
                moveGoal.target_pose.pose.position.y = userdata.i_position_in_kitchen[1]
                moveGoal.target_pose.pose.position.z = 0
                rotationAngle = userdata.i_rotation_angle
                moveGoal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, rotationAngle))
                index = index + 1

                print moveGoal

                return moveGoal

            def image_record_cb(userdata):
                bridge = CvBridge()
                cvImage = np.asarray(bridge.imgmsg_to_cv(userdata.data, "bgr8"))
                cv.SaveImage('image_fire.png', cvImage)
                rospy.loginfo("Fire image saved")
                return succeeded

# CHANGE ORDER  WITH MOVE BASE
            self.userdata.fire_location = []  # To initialize we need this.

            smach.StateMachine.add(
                'MOVE_TO_NEXT_LOCATION_CHECKER',
                MoveToNextLocationChecker(),
                transitions={succeeded: 'MOVE_TO_NEXT_FIRE_LOCATION', aborted: 'NO_FIRE_DETECTED', 'go_self': 'MOVE_TO_NEXT_LOCATION_CHECKER'})

            smach.StateMachine.add(
                'MOVE_TO_NEXT_FIRE_LOCATION',
                SimpleActionState('move_base', MoveBaseAction, goal_cb=move_around, input_keys=['i_position_in_kitchen', 'i_rotation_angle']),
                transitions={succeeded: 'CHECK_SMOKE', aborted: 'MOVE_TO_NEXT_FIRE_LOCATION'},
                remapping={'i_position_in_kitchen': 'o_position_in_kitchen', 'i_rotation_angle': 'o_rotation_angle'})

            def IsThereSmoke_cb(userdata, percentage):
                rospy.loginfo("Callback is called.")
                self.count += 1

                rospy.loginfo("Count is increased to: %d" % self.count)

                rospy.loginfo("Percentage: %d" % percentage.data)

                if percentage.data > 3.0 and percentage.data < 15.0:
                    self.countSuceeded += 1
                    rospy.loginfo("Succeeded count is increased: %d" % self.countSuceeded)

                if percentage.data < 3.0:
                    self.countAborted += 1
                    rospy.loginfo("Aborted count is increased: %d" % self.countAborted)

                if self.count == 5:
                    rospy.loginfo("Count is: %d" % self.count)
                    rospy.loginfo("Aborted count is: %d at percent calculation" % self.countAborted)
                    rospy.loginfo("Succeeded count is: %d at percent calculation" % self.countSuceeded)
                    percentage_suceeded = float(self.countSuceeded * 100 / self.count)
                    print self.countSuceeded
                    # percentage_suceeded = float(percentage_suceeded / 100)
                    print"Percent succeeded: ", percentage_suceeded
                    percentage_aborted = float(self.countAborted * 100 / self.count)
                    print self.countAborted
                    # percentage_aborted = float(percentage_aborted / 100)
                    print "Percent aborted: ", percentage_aborted
                    self.count = 0
                    self.countSuceeded = 0
                    self.countAborted = 0
                    print "Count I dont know: ", self.countIDontKnow
                    if percentage_suceeded >= 80:
                        return succeeded

                    elif percentage_aborted >= 80 or self.countIDontKnow > 0:
                        self.countIDontKnow = 0
                        return aborted

                    else:
                        self.countIDontKnow += 1
                        return 'I_DONT_KNOW'
                else:
                    return 'I_DONT_KNOW'

            smach.StateMachine.add(
                'CHECK_SMOKE',
                TopicReaderState(
                topic_name='/smoke_detector/smoke_percentage',
                msg_type=Float64,
                callback=IsThereSmoke_cb,
                outcomes=[succeeded, aborted, preempted, 'I_DONT_KNOW']),
                transitions={succeeded: 'GET_POSITION', aborted: 'MOVE_TO_NEXT_LOCATION_CHECKER', 'I_DONT_KNOW': 'CHECK_SMOKE'})

            # smach.StateMachine.add(
            #     'CHECK_SMOKE',
            #     CheckSmokeStateMachine(),
            #     transitions={'there_is_fire': 'THERE_IS_FIRE', 'there_is_no_smoke': 'MOVE_TO_NEXT_LOCATION_CHECKER', 'doubtful': 'CHECK_SMOKE'})

            smach.StateMachine.add(
                'GET_POSITION',
                GetPosition(),
                transitions={succeeded: 'RECORD_POSITION'},
                remapping={'memorised_poi_data': 'fire_location_map'})

            smach.StateMachine.add(
                'RECORD_POSITION',
                RecordPosition(),
                transitions={succeeded: 'THERE_IS_FIRE'},
                remapping={'location_of_fire': 'location_of_fire'})

            smach.StateMachine.add(
                'THERE_IS_FIRE',
                SpeakActionState("Oh my god! If you can't cook then don't cook!"),
                transitions={succeeded: 'SAVE_IMAGE', aborted: 'THERE_IS_FIRE'})

            smach.StateMachine.add(
                'SAVE_IMAGE',
                TopicReaderState(
                topic_name='/stereo/left/image',
                msg_type=Image,
                callback=image_record_cb,
                outcomes=[succeeded, aborted, preempted]),
                transitions={succeeded: succeeded, aborted: succeeded})

            smach.StateMachine.add(
                'THERE_IS_NO_FIRE',
                SpeakActionState("I did not detect smoke here. Let me check the next location"),
                transitions={succeeded: 'MOVE_TO_NEXT_LOCATION_CHECKER', aborted: 'MOVE_TO_NEXT_LOCATION_CHECKER'})

            smach.StateMachine.add(
                'NO_FIRE_DETECTED',
                SpeakActionState("I could not detect any fire. I know there is a fire. I will save people."),
                transitions={succeeded: 'SAVE_IMAGE', aborted: 'SAVE_IMAGE'})
