#! /usr/bin/env python
# vim: expandtab ts=4 sw=4
### set_distance_new_location.py ###

import rospy
import smach
import math

from pal_smach_utils.utils.global_common import succeeded
from pal_smach_utils.utils.math_utils import normalize_vector, vector_magnitude, multiply_vector

from geometry_msgs.msg import Quaternion, PoseStamped
from tf.transformations import quaternion_from_euler

#Times that after losing a person and going 2m from the last known location
#we look for candidates again. We will prefferably put a number lower than
# the NUMBER_TIMES_BEFORE_LOST to avoid looking too much before considering again
#that we have lost the track of the person again.
#Its loads the value from a .yalm, and if it's empty, will load the second value
NUMBER_TIMES_AFTER_LOST_BEFORE_LOOSING_AGAIN = rospy.get_param('/params_follow_me/number_times_after_lost_before_loosing_again', 2)


class Set_L50_New_Location(smach.State):
        def __init__(self):
            smach.State.__init__(self,
                                 outcomes=[succeeded], input_keys=['FO_people_location'],
                                 output_keys=['l50_navgoal', 'l50_lost_person'])

        def execute(self, userdata):
            rospy.loginfo('Calculating Vectors for 50cm distance ;P')
            distance = 0.5
            pose = userdata.FO_people_location
            unit_vector = normalize_vector(pose.position)

            k = vector_magnitude(pose.position)
            distance_des = k - distance
            dist_vector = multiply_vector(unit_vector, distance_des)

            alfa = math.atan2(dist_vector.x, dist_vector.y)

            if alfa > math.pi:
                alfa = alfa - (2 * math.pi)

            alfa_degree = (alfa * 360) / (2 * math.pi)

            rospy.loginfo('$$$$$$$$$$$$$Real Distance:%s', str(k))
            rospy.loginfo('$$$$$$$$$$$$$Desired Distance:%s', str(distance_des))
            rospy.loginfo('$$$$$$$$$$$$$ALFA ==> :%s', str(alfa_degree))
            nav_goal = PoseStamped()
            nav_goal.header.stamp = rospy.Time.now()
            nav_goal.header.frame_id = "/base_link"
            nav_goal.pose.position = dist_vector
            nav_goal.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, alfa))
            userdata.l50_navgoal = nav_goal
            rospy.loginfo('This is the Nav Goal We send to REEM: %s', str(nav_goal))
            userdata.l50_lost_person = False
            return succeeded


class Set_L200_Old_location(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded], input_keys=['sm_FO_old_pos'],
                             output_keys=['l200_navgoal', 'l200_lost_person', 'l200_no_people_counter'])

    def execute(self, userdata):

        rospy.loginfo('Calculating Vectors for 200cm distance ;P')
        distance = 2.0
        pose = userdata.sm_FO_old_pos
        unit_vector = normalize_vector(pose.position)

        k = vector_magnitude(pose.position)
        distance_des = k + distance
        dist_vector = multiply_vector(unit_vector, distance_des)
        rospy.loginfo('$$$$$$$$$$$$$Real Distance:%s', str(k))
        rospy.loginfo('$$$$$$$$$$$$$Desired Distance:%s', str(distance_des))
        nav_goal = PoseStamped()
        nav_goal.header.stamp = rospy.Time.now()
        nav_goal.header.frame_id = "/base_link"
        nav_goal.pose.position = dist_vector
        nav_goal.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
        userdata.l200_navgoal = nav_goal
        rospy.loginfo('This is the Nav Goal We send to REEM: %s', str(nav_goal))
        userdata.l200_lost_person = True
        userdata.l200_no_people_counter = NUMBER_TIMES_AFTER_LOST_BEFORE_LOOSING_AGAIN
        return succeeded


class Set_L_New_Location(smach.State):

    '''
    This state does the following:
        inputs -->  distance: the distance you want the robots to keep between him and the person he has detected (S.I.:metres)
                    we_lost_person: Boolean.    If false, it will just calculate the l_navgoal and will put the l_lost_person key to False
                                                If true, it will calculate the l_navgoal and will put the l_lost_person key to True.
                                                It will also evaluate the l_no_people_counter to NUMBER_TIMES_AFTER_LOST_BEFORE_LOOSING_AGAIN.
                                                The new position will be L metres AWAY from the last know persons position, mainly because we
                                                decided  that if we lose a person we will move a distance AHEAD to alow a new search, and prehaps find.
        input_keys --> 'FO_people_location':Type pose(). Pose where we have detected the person.


        Notes:  l_no_people_counter we use it to keep track how many times we lost a person and will be used outside to select
                whether we use we_lost_person = true or false.
    '''

    def __init__(self, distance=0.5, we_lost_person=False):
        smach.State.__init__(self,
                             outcomes=[succeeded],
                             input_keys=['FO_people_location'],
                             output_keys=['l_navgoal', 'l_lost_person', 'l_no_people_counter'])
        self._distance = distance
        self._we_lost_person = we_lost_person

    def execute(self, userdata):
        rospy.loginfo(':: Calculating Vectors for %s m distance ::', str(self._distance))
        #self._distance
        pose = userdata.FO_people_location
        unit_vector = normalize_vector(pose.position)
        rospy.loginfo("pose.position is:\n" + str(pose.position))
        rospy.loginfo("unit_vector is:\n " + str(unit_vector))

        k = vector_magnitude(pose.position)
        rospy.loginfo("Magnitude of vector from Reem to person ==> " + str(k))

        if not self._we_lost_person:
            """
            If person is closer than the distance given, we wont move but we might rotate.
            We want that if the person comes closer, the robot stays in the place.
            Thats why we make desired distance zero if person too close.
            """
            if k >= self._distance:
                distance_des = k - self._distance
            else:
                distance_des = 0.0
        else:
            distance_des = k + self._distance

        dist_vector = multiply_vector(unit_vector, distance_des)

        alfa = 0.0
        """
        We only calculate the turning if there is no base movement
        """
        if distance_des == 0.0:
            alfa = math.atan2(pose.position.y, pose.position.x)
            rospy.loginfo("ALFA is: " + str(alfa) + " in degrees: " + str(math.degrees(alfa)))
            if alfa > math.pi:
                rospy.loginfo("PERSON DETECTED BEHIND REEM, IMPOSSIBLE: " + str(alfa) + " in degrees: " + str(math.degrees(alfa)))
        else:
            rospy.loginfo("We will move so we WONT TURN, DESIRED_DISTANCE is > 0  ==> " + str(distance_des))

        alfa_degree = math.degrees(alfa)

        print "/********************************************/"
        rospy.loginfo('Distance from PERSON:%s', str(k))
        rospy.loginfo('Person and REEM WANTED distance:%s', str(self._distance))
        rospy.loginfo('Distance that Reem will MOVE:%s', str(distance_des))
        rospy.loginfo('Degrees that Reem will TURN ==> :%s', str(alfa_degree))
        print "/********************************************/"

        nav_goal = PoseStamped()
        nav_goal.header.stamp = rospy.Time.now()
        nav_goal.header.frame_id = "/base_link"
        nav_goal.pose.position = dist_vector
        nav_goal.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, alfa))
        rospy.loginfo('ALFA AND ORIENTATION ==> :%s, %s', str(alfa_degree), str(nav_goal.pose.orientation))
        userdata.l_navgoal = nav_goal
        rospy.loginfo('This is the Nav Goal We send to REEM: %s', str(nav_goal))
        if not self._we_lost_person:
            userdata.l_lost_person = False
        else:
            userdata.l_lost_person = True
            userdata.l_no_people_counter = NUMBER_TIMES_AFTER_LOST_BEFORE_LOOSING_AGAIN

        return succeeded
