#!/usr/bin/env python

import roslib; roslib.load_manifest('estirabot_apps_base')
import rospy
import smach
import smach_ros

from sensor_msgs.msg import PointCloud2
from iri_deformable_analysis.srv import DoDeformableAnalysis, DoDeformableAnalysisRequest
from iri_common_smach.st_topic_publisher import TopicPublisher

class PerformAnalysis(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['success','fail','timeout'],
                                   input_keys=['pcl_RGB','deformable_config'],
                                   output_keys=['best_grasp_pose'])

    def execute(self, userdata):
        # Config and launch the deformable analysis
        handler = rospy.ServiceProxy(
                                '/estirabot/skills/deformable_analysis/do_deformable_analysis',
                                DoDeformableAnalysis)

        analysis_request                    = DoDeformableAnalysisRequest()
        analysis_request.pcl_to_analyze     = userdata.pcl_RGB
        analysis_request.fusion_criteria_id = userdata.deformable_config.best_pose_algorithm_id

        try:
            response = handler(analysis_request)

            if (not response):
                return 'fail'

        except rospy.ServiceException, e:
            return 'timeout'

        pose_st = response.deformable_analysis.graspability.best_grasp_pose
        userdata.best_grasp_pose = pose_st

        return 'success'

class SM_ESTIRABOT_DeformableAnalysis():
    """
    State machine to perform a deformable analysis

    Currently composed of logging state and service call
    """
    def __init__(self, pcl_log = True, log_topic = '/log/pcl_table_scene'):
       self.sm = smach.StateMachine(outcomes    = ['success','fail','timeout'],
                                    input_keys  = ['pcl_RGB','deformable_config'],
                                    output_keys = ['best_grasp_pose'])
       self.pcl_log   = pcl_log
       self.log_topic = log_topic

    def build_sm(self):
        with self.sm:
            if (self.pcl_log):
                smach.StateMachine.add('LOG_PCL_TO_ANALYSE', 
                                       TopicPublisher(self.log_topic, PointCloud2),
                        transitions = {'finish' : 'CALL_PERFORM_ANALYSIS'},
                        remapping   = {'msg'    : 'pcl_RGB'})

            smach.StateMachine.add('CALL_PERFORM_ANALYSIS', PerformAnalysis(),
                    transitions = {'success' : 'success',
                                   'fail'    : 'fail',
                                   'timeout' : 'timeout'},
                    remapping   = {'pcl_RGB' : 'pcl_RGB',
                                   'deformable_config' : 'deformable_config',
                                   'best_grasp_pose'   : 'best_grasp_pose'})
        return self.sm
