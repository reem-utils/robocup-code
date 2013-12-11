#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach

from smach_ros import ServiceState
from geometry_msgs.msg import Pose
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_supervisor_msgs.srv import lookupTransform, lookupTransformRequest

#Creates a Pose vaiable from a TransformedStamped variable
def poi_reem_basic(transstamped):
    print "#########################%s" % str(transstamped)
    poi = Pose()
    poi.position.x = transstamped.transform.translation.x
    poi.position.y = transstamped.transform.translation.y
    poi.orientation.z = transstamped.transform.rotation.z
    return poi


class GetPosition(smach.StateMachine):

    '''
    This SM just gets the position and orientation of the robot in Base_link and outputs this data
    in form of a Pose type variable.
    '''

    def __init__(self):
        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], output_keys=['memorised_poi_data'])

        with self:

            def poi_request_cb(userdata, request):
                poi_request = lookupTransformRequest()
                poi_request.target_frame = '/map'
                poi_request.source_frame = '/base_link'
                poi_request.transform_time = rospy.get_rostime()
                rospy.loginfo('POI REQUEST %s' % str(poi_request))
                return poi_request

            #Note that in theory decorators wouldnt be necessary, but its the only way
            # to get ServiceState to alow in and output_keys.
            #This should be the structure of the execute
            @smach.cb_interface(output_keys=['poi_output'])
            def poi_response_cb(userdata, response):
                #Here we get the response data
                poi_response = response.transform
                rospy.loginfo('POI RESPONSE TRANSFORMSTAMPED %s' % str(poi_response))
                #Here we process this data, because we only need translation x, y and rotation in z axis
                poi_position = poi_reem_basic(poi_response)
                rospy.loginfo(' POIS POSE %s' % str(poi_position))
                #Here we assign the processed data to the variable that will be the output key
                userdata.poi_output = poi_position
                return succeeded

            #TODO: change the lookup transform call to transform_pose function of utils
            smach.StateMachine.add('ACCESS_POIS',
                                   ServiceState('lookupTransform',
                                   lookupTransform,
                                   request_cb=poi_request_cb,
                                   response_cb=poi_response_cb,
                                   output_keys=['poi_output']),
                                   transitions={succeeded: succeeded, aborted: aborted, preempted: preempted},
                                   remapping={'poi_output': 'memorised_poi_data'})

# vim: expandtab ts=4 sw=4
