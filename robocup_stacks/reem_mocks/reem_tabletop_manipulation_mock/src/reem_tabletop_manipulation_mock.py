#!/usr/bin/env python
import roslib
roslib.load_manifest('reem_tabletop_manipulation_mock')
import rospy
from actionlib import SimpleActionServer

import random
from reem_tabletop_manipulation_launch.msg import GraspTargetAction, GraspTargetResult
#from tabletop_object_detector.msg import TabletopDetectionResult
from household_objects_database_msgs.msg import DatabaseModelPoseList, DatabaseModelPose
from tabletop_object_detector.msg import TabletopDetectionResult


class ReemTabletopManipulationMock():
    def __init__(self):

        a_grasp_target_action = {'name': '/tabletop_grasping_node', 'ActionSpec': GraspTargetAction, 'execute_cb': self.grasp_target_action_cb, 'auto_start': False}

        self.s  = SimpleActionServer(**a_grasp_target_action)
        self.s.start()


    def grasp_target_action_cb(self, req):
        rospy.loginfo('Grasp Target Action \'%s\' /tabletop_grasping_node was called.' % req.appearanceID)
        res = GraspTargetResult()
        res.detectionResult = TabletopDetectionResult()
        res.detectionResult.models = [DatabaseModelPoseList()]
        res.detectionResult.models[0].model_list = [DatabaseModelPose()]# = [0].model_id = req.databaseID
        res.detectionResult.models[0].model_list[0].model_id = req.databaseID
        self.s.set_succeeded(res) if bool(random.randint(0, 1)) else self.s.set_aborted(res)



if __name__ == '__main__':

      rospy.init_node('reem_tabletop_manipulation_mock')

      ReemTabletopManipulationMock()

      rospy.spin()
