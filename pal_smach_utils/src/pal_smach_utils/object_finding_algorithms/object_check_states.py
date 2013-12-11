#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from pal_smach_utils.utils.global_common import succeeded, aborted, transform_pose


class CheckObjectAndRemoveFromList(smach.State):
    '''Checks if there is any object in the entering userdata. It removes the found object from the list and outputs the list.
    The target_frame parameter is the desired frame_id of the poses of the result.
    The leave_unknowns parameter specifies whether the objects tagged as unknown (not trained) should be used and left in the list
    or not.
    Outcomes:
        - succeeded: A object was found and is returned. Also it was removed from the list.
        - aborted: No object was found, or all the objects were unknown and leave_unknowns was set to False.
    Userdata:
        - in_objects_data: ObjectPoseList of objects found.
        - in_target_object: String containing the name of the object wanted to be found. It's the empty string ( '' ) if it's looking for any object.
        - out_object_found: The found object. It's the first on the list if in_target_object is the empty string ( '' ), or the target_object if found.
                            If no object is found, this output key has the value None (not a string).
        - out_objects_data: The list of objects exceptuating the object found. It's the same list if no object is found.
    '''
    def __init__(self, target_frame, leave_unknowns=False):
        smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys=['in_objects_data', 'in_target_object'],
                             output_keys=['out_object_found', 'out_objects_data'])
        self.target_frame = target_frame
        self.leave_unknowns = leave_unknowns

    def fill_print_object_information_and_remove_from_list(self, userdata, object_index):
        ''' Fills in the selected output object and removes it of the list '''
        frame_id = userdata.in_objects_data.header.frame_id
        print "---------------- Object recognition --------------------"
        print "Object found is: " + userdata.in_objects_data.object_list[object_index].name
        print "In position in the %s coordinate frame: " % frame_id
        print userdata.in_objects_data.object_list[object_index].pose.position
        print "With orientation:"
        print userdata.in_objects_data.object_list[object_index].pose.orientation
        print "--------------------------------------------------------"
        obj_data_copy = userdata.in_objects_data
        if frame_id != self.target_frame:
            obj_data_copy.object_list[object_index].pose = transform_pose(userdata.in_objects_data.object_list[object_index].pose, frame_id, '/map', timeout=3)
        # Remove the selected object:
        userdata.out_object_found = obj_data_copy.object_list.pop(object_index)
        userdata.out_objects_data = obj_data_copy

    def execute(self, userdata):
        if userdata.in_objects_data is not None:
            n_objects = len(userdata.in_objects_data.object_list)
            if userdata.in_target_object != '':  # There has been a target object specified (str(None) was once used)
                print "Target object specified! Looking for the", str(userdata.in_target_object) + '.'
                for i in range(0, n_objects):
                    if userdata.in_objects_data.object_list[i].name == userdata.in_target_object:
                        self.fill_print_object_information_and_remove_from_list(userdata, i)
                        return succeeded
                    elif not self.leave_unknowns:
                        obj_data_copy = userdata.in_objects_data
                        obj_data_copy.object_list.pop(i)
                        userdata.out_objects_data = obj_data_copy
            else:  # We need to have first the known objects
                for i in range(0, n_objects):
                    if userdata.in_objects_data.object_list[i].name != 'unknown':
                        self.fill_print_object_information_and_remove_from_list(userdata, i)
                        return succeeded
                # No known objects in the list
                if n_objects and self.leave_unknowns:
                    self.fill_print_object_information_and_remove_from_list(userdata, 0)
                    return succeeded
        print "\nNo object recognized!! Let's go to another place...\n"
        userdata.out_object_found = None
        userdata.out_objects_data = []  # userdata.in_objects_data
        return aborted


class CheckRemaining(smach.State):

    '''
    Checks if there are objects in a ObjectPoseList.
    Userdata:
        - in_obj_list: ObjectPoseList of objects. Can be None if there aren't objects yet.
    Outcomes:
        - remaining: Means that there are objects remaining.
        - empty: Means that the list is empty or that the ObjectPoseList equals None.
    '''

    def __init__(self):
        smach.State.__init__(self, outcomes=['remaining', 'empty'], input_keys=['in_obj_list'])

    def execute(self, userdata):
        if (userdata.in_obj_list is not None) and (len(userdata.in_obj_list.object_list) > 0):
            obj_name_list = []
            for obj in userdata.in_obj_list.object_list:
                obj_name_list.append(obj.name)
            print "Objects remaining in the location:", obj_name_list
            return 'remaining'
        return 'empty'
