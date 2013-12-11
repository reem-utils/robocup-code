#! /usr/bin/env python
# -.- coding: utf-8 -.-
'''
READ_AND_PROCESS_OBJECT_DELIVERY_LIST.PY
'''


import roslib
roslib.load_manifest('pal_smach_utils')
import smach
import rospy

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from pal_smach_utils.speech.sound_action import SpeakActionState

WHAT_TO_DO_NEXT_FRASE = "Mmmm...Let me see what I have to do next."


class ExtractObjectAndLocationFromList(smach.State):

    '''
    The marker is initialised outside.
    '''

    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['continue',
                                       'finished',
                                       preempted,
                                       aborted],
                             input_keys=['in_list',
                                         'in_list_marker'],
                             output_keys=['object_name_out',
                                          'delivery_location_out',
                                          'list_marker_out'])

    def execute(self, userdata):

        if len(userdata.in_list) > userdata.in_list_marker:

            next_task = userdata.in_list[userdata.in_list_marker]
            rospy.loginfo('I have to fetch a %s and I have to deliver it to %s' % (next_task[0], next_task[1]))
            userdata.object_name_out = next_task[0]
            userdata.delivery_location_out = next_task[1]
            userdata.list_marker_out = userdata.in_list_marker + 1

            return 'continue'

        return 'finished'


class ReadAndPorcessObjectDeliveryList(smach.StateMachine):

    '''
    This SM That takes in a list of vectors, where for each object there is
    a location where to take that object.
    It basicaly take object 1 to location A, 2 to B and so on.
    Finishes when it has delivered all the objects in the list that are also in
    its POI memory banks. If a non memorised previously object is in the list
    it will just let you know that she doesnt have it memorised.

    @Input_keys: in_list-->  List of vector elements of two positions.
                                            Firstone is the object, secondone is the
                                            delivery location for that object.
    @Output_keys : out_list--> The object that is the next in the list that isnt alredy
                               marked as done.
                   delivery_location_out--> The delivery location that is the next in the list that 
                                            isnt already marked as done

    @In_Out_key: list_marker--> Counter that uses to know which is the next object-delivery.
    '''

    def __init__(self):
        smach.StateMachine.__init__(self,
                                    ['fetch_and_deliver', 'finished_list', preempted, aborted],
                                    input_keys=['in_list',
                                                'in_list_marker'],
                                    output_keys=['object_name_out',
                                                 'delivery_location_out',
                                                 'list_marker_out'])

        with self:

            smach.StateMachine.add('PREPARED_TO_TAKE_ORDERS',
                                   SpeakActionState(WHAT_TO_DO_NEXT_FRASE),
                                   transitions={succeeded: 'EXTRACTING_DATA_STATE',
                                                preempted: preempted,
                                                aborted: aborted})

            smach.StateMachine.add('EXTRACTING_DATA_STATE',
                                   ExtractObjectAndLocationFromList(),
                                   transitions={'continue': 'READ_OUTLOUD_OBJECT_AND_DELIVERY_LOCATION',
                                                'finished': 'READ_OUTLOUD_FINISHED',
                                                preempted: preempted,
                                                aborted: aborted},
                                   remapping={'in_list': 'in_list',
                                              'in_list_marker': 'in_list_marker',
                                              'object_name_out': 'object_name_out',
                                              'delivery_location_out': 'delivery_location_out',
                                              'list_marker_out': 'list_marker_out'})

            def say_text_cb(userdata):
                text_say = "Number " + str(userdata.list_marker_out) + " in the list is taking " + userdata.object_name_out + " to the delivery location " + userdata.delivery_location_out
                return text_say
            smach.StateMachine.add('READ_OUTLOUD_OBJECT_AND_DELIVERY_LOCATION',
                                   SpeakActionState(text_cb=say_text_cb,
                                                    input_keys=['object_name_out',
                                                                'delivery_location_out',
                                                                'list_marker_out']),
                                   transitions={succeeded: 'fetch_and_deliver'})

            def say_text_cb(userdata):
                text_say = "There are no more things to do in the list."
                return text_say
            smach.StateMachine.add('READ_OUTLOUD_FINISHED',
                                   SpeakActionState(text_cb=say_text_cb,
                                                    input_keys=['object_name_out',
                                                                'delivery_location_out',
                                                                'list_marker_out']),
                                   transitions={succeeded: 'finished_list'})
