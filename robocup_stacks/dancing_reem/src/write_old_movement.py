# -*- coding: utf-8 -*-
import roslib
roslib.load_manifest('dancing_reem')
import os
import rospy
import smach
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted


MOVEMENT_XML_TEMPORAL_FILE_PATH_OLD = "/tmp/tmp_mov_file_old.xml"


class WriteOldMovement(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=[succeeded, preempted, aborted],
                             input_keys=['in_file_name'],
                             output_keys=['old_file_name_out'])

    def execute(self, userdata):

        tmpFile = MOVEMENT_XML_TEMPORAL_FILE_PATH_OLD

        # We erase the previous file if it there was any.
        if os.path.isfile(tmpFile):
            os.remove(tmpFile)

        old_mov_tring = open(userdata.in_file_name, 'r').read()
        #rospy.loginfo("Movement Read ===> \n" + old_mov_tring)
        with open(tmpFile, "w") as text_file:
            text_file.write(old_mov_tring)
        userdata.old_file_name_out = tmpFile
        #rospy.loginfo("Old Movement Memorised in path ===> " + str(tmpFile))

        return succeeded
