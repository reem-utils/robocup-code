#!/usr/bin/python
import roslib; roslib.load_manifest('iri_common_smach')
import rospy
import smach
import smach_ros
import geometry_msgs

from geometry_msgs.msg import * 

import csv

"""
Reads PoseStamped list from a csv file
format of the file:
# allowed comments using '#' at the beginning of the line
frame_id, pos_x, pos_y, pos_z, ori_x, ori_y, ori_z, ori_w
"""
def get_list_of_stamped_poses_from_csv_file(filename):
    list_of_poses = []
    
    with open(filename,'rb') as f:
        reader = csv.reader(f)

        try:
            for row in reader:
                if row:
                    if row[0][0] != '#':
                        tmp_pose = geometry_msgs.msg.PoseStamped()
                        tmp_pose.header.frame_id = row[0]
                        tmp_pose.header.stamp = rospy.Time.now()
                        tmp_pose.pose.position.x = row[1]
                        tmp_pose.pose.position.y = row[2]
                        tmp_pose.pose.position.z = row[3]
                        tmp_pose.pose.orientation.x = row[4]
                        tmp_pose.pose.orientation.y = row[5]
                        tmp_pose.pose.orientation.z = row[6]
                        tmp_pose.pose.orientation.w = row[7]
                        list_of_poses.append(tmp_pose)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

    return list_of_poses

# define state for reading a list of stamped poses from a csv file 
class GetListOfPoseStampedFromCsvFile(smach.State):
    """
    GET A LIST OF STAMPED POSES FROM A CSV FILE 
   
    @type  file_name: string
    @param file_name: URI of the csv file
    @type  list_of_stpose: PoseStamped[]
    @param list_of_stpose: List of PoseStamped

    """
    def __init__(self, file_name):
        smach.State.__init__(self,
                             outcomes = ['success','fail'],
                             input_keys = [],
                             output_keys = ['list_of_stpose'])

        self.file_name = file_name

    def execute(self, userdata):
        rospy.loginfo('Executing GetListOfPoseStampedFromCsvFile')
        
        try:
            list_of_stamped_poses = get_list_of_stamped_poses_from_csv_file(self.file_name)
            userdata.list_of_stpose = list_of_stamped_poses
            if list_of_stamped_poses == None:
                rospy.logerr('No list received from %s', self.file_name)
                return 'fail'

        except rospy.ServiceException, e:
            return 'fail'
        
        return 'success'

