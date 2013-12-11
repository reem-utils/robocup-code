#! /usr/bin/env python
# -.- coding: utf-8 -.-
## sm_hear_voice_commands_and_pois ##

import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import math
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from sound_action import SpeakActionState
from pal_smach_utils.navigation.get_current_pos import GetPosition
from pal_smach_utils.utils.timeout_container import SleepState
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from geometry_msgs.msg import Pose, Quaternion
#from pal_supervisor_msgs.srv import lookupTransform, lookupTransformRequest, lookupTransformResponse
from pal_smach_utils.utils.colors import Colors

colors = Colors()


MEMORISE_WAIT_TIME = 0.5
RADIANS_TO_PERP = 1.57
LEFT_WORD = "left"
RIGHT_WORD = "right"
FRONT_WORD = "front"
BACK_WORD = "back"


def MakeValidAngle(init_angle):
    """
    It Avoids negative angles or bigger than 2pi
    """
    angle = init_angle

    while angle >= 2*math.pi or angle < 0:

        if angle >= 2*math.pi:
            fixed_angle = angle - 2*math.pi
            rospy.logwarn(colors.BACKGROUND_RED + "ANGLE TOO BIG" + colors.NATIVE_COLOR)
        elif angle < 0:
            fixed_angle = 2*math.pi + angle
            rospy.logwarn(colors.BACKGROUND_RED + "NEGATIVE ANGLE" + colors.NATIVE_COLOR)
        else:
            fixed_angle = angle
        angle = fixed_angle
    rospy.logwarn(colors.BACKGROUND_GREEN + "CORRECT ANGLE" + colors.NATIVE_COLOR)
    fixed_angle = angle
    return fixed_angle


def PerpendicularToTable(start_orientation, side_name):
    """
    Bare in mind that we suppose we leave the table always on the
    right hand side.
    """

    (r, p, theta) = euler_from_quaternion((start_orientation.x, start_orientation.y, start_orientation.z, start_orientation.w))
    print "@@@@@@@@@ THETA ==== " + str(theta)
    if side_name == LEFT_WORD:
        theta_new = theta + RADIANS_TO_PERP
    elif side_name == RIGHT_WORD:
        theta_new = theta - RADIANS_TO_PERP
    elif side_name == FRONT_WORD:
        theta_new = theta
    elif side_name == BACK_WORD:
        theta_new = theta - 2*RADIANS_TO_PERP

    theta_final = MakeValidAngle(theta_new)

    print "@@@@@@@@@NEW THETA ==== " + str(theta_final)
    #final_perp_table_orientation = Pose()
    #final_perp_table_orientation.orientation = Quaternion(*quaternion_from_euler(0, 0, theta_new))
    #print "@@@@@@@@@NEW QUATERNION ORIENTATION ==== " + str(final_perp_table_orientation.orientation)
    #return final_perp_table_orientation.orientation.z
    return theta_final


class MemorisePois(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             input_keys=['object_name', 'orient_side', 'memorised_poi_data'])

    def execute(self, userdata):
        rospy.loginfo("DATA OF MEMORISE %s" % str(userdata.memorised_poi_data))
        rospy.loginfo("OBJECT NAME %s" % str(userdata.object_name))
        rospy.loginfo("param will be: " + '/mmap/poi/submap_0/' + str(userdata.object_name))
        rospy.loginfo("The whole parameter: " + str(userdata.object_name) + " -=- " + str(userdata.memorised_poi_data))
        angle = PerpendicularToTable(userdata.memorised_poi_data.orientation, userdata.orient_side)

        tries = 0
        while tries < 10:
            try:
                rospy.set_param('/mmap/poi/submap_0/' + str(userdata.object_name), ['submap_0', str(userdata.object_name), userdata.memorised_poi_data.position.x, userdata.memorised_poi_data.position.y, angle])
                break
            except Exception as ex:
                rospy.loginfo(str(ex))
                rospy.logerr("There was an error while trying to set the parameter. Trying again...")
            finally:
                tries += 1

        new_orientation = Quaternion(*quaternion_from_euler(0, 0, angle))
        rospy.loginfo("THIS IS THE NEW ORIENTATION POI DATA\n %s" % str(new_orientation))

        return succeeded


class SM_MemorisePois(smach.StateMachine):

    '''
    This state Machine get Pois commands and memorises the POI's in the map that Reem is generating
    Used by : SM_Follow_Operator

    '''
    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=['FO_POI_name', 'FO_orientation_side'])
        with self:

            #Gives the position and orientation of Reem packed in a Pose type variable
            smach.StateMachine.add('GET_POI_POSITION',
                                   GetPosition(),
                                   transitions={succeeded: 'MEMORISE_POIS', aborted: 'SLEEP'},
                                   remapping={'memorised_poi_data': 'memorised_poi_data'})

            smach.StateMachine.add('SLEEP',
                                   SleepState(MEMORISE_WAIT_TIME),
                                   transitions={succeeded: 'GET_POI_POSITION', preempted: preempted})

            smach.StateMachine.add('MEMORISE_POIS',
                                   MemorisePois(),
                                   transitions={succeeded: 'SAY_MEMORISED_POI',
                                                aborted: 'MEMORISE_POIS',
                                                preempted: preempted},
                                   remapping={'object_name': 'FO_POI_name',
                                              'orient_side': 'FO_orientation_side',
                                              'memorised_poi_data': 'memorised_poi_data'})

            def say_text_cb(userdata):
                text_say = "Now I know where to find the " + userdata.FO_POI_name
                return text_say
            smach.StateMachine.add('SAY_MEMORISED_POI',
                                   SpeakActionState(text_cb=say_text_cb, input_keys=['FO_POI_name']),
                                   transitions={succeeded: succeeded})

# vim: expandtab ts=4 sw=4
