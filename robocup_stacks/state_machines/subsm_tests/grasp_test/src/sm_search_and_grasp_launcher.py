#! /usr/bin/env python

import roslib; roslib.load_manifest('grasp_test')
import rospy
import smach
import actionlib

#from smach_ros import SimpleActionState, ServiceState
import smach_ros
from std_msgs import *
#from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
#from geometry_msgs.msg import Pose, Point, Quaternion
#from coord_translator.srv import *

#from common import *



from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.grasping.sm_search_and_grasp import *
from pal_smach_utils.grasping.arm_and_hand_goals import *



#from pal_smach_utils.navigation.enter_room import *
#from pal_smach_utils.navigation.move_to_object import *
#from pal_smach_utils.speech.sound_action import SpeakActionState


#from pal_smach_utils.utils.sm_fko import *
#from pal_smach_utils.grasping.sm_search_obj_orig import *
#from common.sm_grasp import *
#from pal_smach_utils.grasping.sm_give import *

#from pal_smach_utils.speech.get_category_and_announce import Get_category_and_announce_object





    
class DummyStateMachine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=[succeeded], output_keys = ['object_to_search_for'])

    def execute(self, userdata):
        print "Dummy state to go to SM_grasp (waiting 10s to initiate, as my pc is too slow to handle all the launch file in time)!"
        print "[                                             =D                                               ]"
        rospy.sleep(5) # in seconds
        userdata.object_to_search_for = ""
        return succeeded 

    
def main():
    rospy.init_node('sm_search_and_grasp_test_state_machine')
    
    sm = smach.StateMachine(outcomes=[succeeded, preempted, aborted])

    with sm:

        # Using this state to wait and to initialize object_to_search_for input_key (needed by SearchAndGraspStateMachine() )
        smach.StateMachine.add(
    		'dummy_state',
    		DummyStateMachine(),
    		transitions = {succeeded: 'SM_grasp'})
	
# 	    def N2_goal_cb(userdata, old_goal):
#             nav_goal = MoveBaseGoal()
#             nav_goal.target_pose.header.stamp = rospy.Time.now()
#             nav_goal.target_pose.header.frame_id = "/base_link" 
#             rospy.loginfo("userdata.keys(): " + str(userdata.keys()))
#             
#             
#             position = Point(userdata.pose_object.object_list[0].pose.position.x, userdata.pose_object.object_list[0].pose.position.y, 0)
#             distance_vector = multiply_vector(normalize_vector(position), 0.5) # 0.5m
#             position = substract_vector(position, distance_vector)
#             nav_goal.target_pose.pose.position = position
#             
#             nav_goal.target_pose.pose.orientation = Quaternion(*quaternion_from_euler(0, 0, 0))
#             # FIXME: calculate correct position
#             
#             return nav_goal
# 
# 
#             #TODO: Use the correct navigation way to do it. For now we go to the pose -0.5m
#         smach.StateMachine.add(
#             'Grasp_target_action',
#             SimpleActionState(
#                 'move_base',
#                 MoveBaseAction,
#                 goal_cb = N2_goal_cb,
#                 input_keys = ['pose_object']),
#             transitions = {succeeded: 'ENABLE_CLOSE_OBJECT_SEARCH'})  

        smach.StateMachine.add(
                     'SM_grasp',
                     SearchAndGraspStateMachine(),
                    transitions = {succeeded: succeeded, aborted: aborted})
        
                    
         # NOT USING ANYTHING  MORE

        
    sis = smach_ros.IntrospectionServer(
        'sm_search_and_grasp_introspection', sm, '/SM_ROOT')
    sis.start()

    sm.execute()

    rospy.spin()
    sis.stop()
    
    
if __name__ == '__main__':
    main()

